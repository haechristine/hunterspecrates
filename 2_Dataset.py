import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('Dataset Information :material/dataset:')

st.logo("logo.png")

st.markdown(''' 

- Gathered data from `DodgeBI` by filtering plans from 2023 and valued at $1 million or higher
- Went into each project's irrigation plan and counted the number of valves connected to specific emission devices
- There were 10 projects per region, adding up to a total of 90 projects
''')

st.markdown('''##### Column Details''')
st.markdown('''
            | Column             | Description                                                                                                                                                                                       |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `'id'`           | Project ID                                                                                                                                                        |
| `'region'`             | Project Region                                                                                                                                         |
| `'building_type'`        | Type of Building                                                                                                                                                |
| `'square_feet'` | Total Landscape Area                                                                                                                                                  |
| `'spray_count'`      | Number of Spray/Valve Connection                                                                                                                                                         |
| `'mp_count'`           | Number of MP/Valve Connection                                                                                                                                                      |
| `'drip_count'`      | Number of Drip/Valve Connection |
| `'rotor_count'`        | Number of Rotor/Valve Connection                                                                                                                                        |
| `'valve_count'`          | Total Number of Valves on Project                                                                                                                                          |
| `'mix_manufacturers'`    | Project Contains Various Maufacturers (T/F)                                                                                                                                                     |
| `'value_mill'`    | Project's Total Value                                                                                                                                                           |
| `'general_contractor'`  | General Contractor in Charge of Project            
| `'est_irrig_value'`           | Estimated Irrigation Value                                                                                                                            |
| `'cost_per_sf'`           | Irrigation Value per Square Foot                                                                                                                            |
            ''')
st.subheader('Original Specification Rate Dataset (90 datapoints)')
# Reading DataFrame
df = pd.read_csv('dataset/new_acre_valve.csv')

def calculate_new_col(col):
    return col['spray_count']*252.1 + col['mp_count']*364.2 + col['drip_count']*475 + col['rotor_count']*188.8 

# Apply function to create new column
df['est_irrig_value'] = df.apply(calculate_new_col, axis=1)

def calculate_sf(col):
    return col['est_irrig_value']/col['square_feet']

# Apply function to create new column
df['cost_per_sf'] = df.apply(calculate_sf, axis=1)

st.dataframe(df)
st.markdown('''
#### Valve Prices
            
Below is the breakdown of how we got to the estimated irrigation value for each project. The values in the following tables came from discussions with sales and product managers.
            
| Name | Avg Domestic Cost |
| ----------- | ----------- |
| `'Valve'` | $81.30 |
| `'MP'` | $12.30 |
| `'Rotor'` | $21.50 |
| `'Spray Nozzle'` | $8.54 |
| `'Drip'` | $0.17 |
| `'Swing Arm (MP/Spray)'` | $1.29 |
| `'Spray Nozzle'` | $6.75 |

- These numbers are all gross estimates and don’t include variables such as controllers and additional material needed to install the irrigation system. We are just considering the price for the valve and sprinkler heads. 
    - Example: the $81.30 valve price was reached by dividing total sales of valves in 2023 by total valve quantity sold in 2023.

| Name | Valve | Application Device QTY | Total Application Device Distributor Net | Valve Total by Emission Type (Multiplier) |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| `'Rotor Valve'` | $81.30 |  5  | $107.50 | $188.80 |
| `'MP Valve'` | $81.30 |  23  | $282.90 | $364.20 |
|`'Spray Valve'`| $81.30 |  20  | $170.80 | $252.10 |
| `'Drip Valve'` | $81.30 |  2,000  | $340.00 | $475.00 |

- The multiplier value was then used to obtain the estimated irrigation value of the project.
    - Example: Looking at our 1st project entry, there are 14 sprays and 5 drips.
            ''')

st.latex(r'''14*252.10+5*475.00 = $5,904.40''')

st.markdown('''
- '`Application Device QTY`' was reached by assuming 20 GPM as the domestic average.
    - Example: Typically there are 5 rotors attached to a valve flowing at 20 GPM.

Note: Keep in mind we are only including the rotor and emission device price in our irrigation market estimates.

            ''')

st.subheader('Synthetic Dataset (1,000 datapoints)')
st.markdown('''
            Below is the resulting dataset after variational autoencoding to expand our original one. 
            ''')
final_df = pd.read_csv('dataset/final_synthetic_df.csv')
st.dataframe(final_df)
st.caption('''Variational Autoencoding is a machine learning model that generates new data in the form of variations of the input data they're trained on.''')
st.markdown('''The graphs below depict the original and synthetic dataset side by side.''')

st.image("syntheticvsog.png")
st.image("output.png")
st.image("output1.png")
st.image("output2.png")
st.image("output3.png")
st.image("output4.png")
st.image("output5.png")
st.image("output6.png")

st.divider()
st.text('Developed by Christine Law • Marketing Analyst Intern 2024 • Hunter Industries')