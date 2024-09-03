import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.title('Specification Market :material/query_stats:')

st.logo("logo.png")

st.subheader('Domestic :material/home_pin:')

st.markdown('''Please note that these numbers were compiled with information 
            from `DodgeBI`, which is a small portion of the actual irrigation market.
            This is not an accurate representation, but a close estimate.
            ''')

st.markdown('''
##### Total Specification Rate   

| Region | Hunter Specified Projects | Total Projects | Hunter/Total(%) |
| ----------- | ----------- | ----------- | ----------- |
| `'Central States'` | 258 |  737  | 35 |
| `'Florida'`| 74 |  296  | 25 |
| `'Great Lakes'` | 171 |  558  | 30.65 |
| `'Northeast'` | 105 |  476  | 22.06 |
| `'Northern California'` | 162 |  424  | 38.21 |
| `'Northwest'` | 106 |  261  | 40.61 |
| `'Southeast'` | 159 |  512  | 31.05 |
| `'Southern California'` | 85 |  201  | 42.29 |
| `'Southwest'` | 152 |  434  | 35.02 |
| `'Domestic'` | 1,308 |  4,017  | 32.56 |
            ''')
st.caption('These numbers were directly taken from `DodgeBI`. Please note that 118 Canada projects were omitted.')

st.markdown('''
##### Estimate Domestic Irrigation Market
   
| Region | Irrigation Value per SF($) | Project Average($) | Hunter Specified Market($) | Total Specified Market($) | Hunter/Total(%)|
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| `'Central States'` | 0.25 | 6,699.14 |  1,728,378.12  | 4,937,266.18 | 35.01 |
| `'Florida'`| 0.17 | 5,028.20 |  372,086.80  | 1,488,347.20 | 25.00 |
| `'Great Lakes'` | 0.42 | 9,264.56 |  1,584,239.76  | 5,169,624.48 | 30.65 |
| `'Northeast'` |  0.30 | 4,288.17 |  450,257.85  | 2,041,168.92 | 22.06 |
| `'Northern California'` | 0.32 | 5,228.22 |  846,971.64  | 2,216,765.28 | 38.21 |
| `'Northwest'` | 0.57 | 6,624.34 |  702,180.04  | 1,728,952.74 | 40.61 |
| `'Southeast'` | 0.37 | 6,777.24 |  1,077,581.16  | 3,469,946.88 | 31.05 |
| `'Southern California'` | 0.52 | 6,676.41 |  567,494.85  | 1,341,958.41 | 42.29 |
| `'Southwest'` | 0.70 | 4,898.96 |  744,641.92  | 2,126,148.64 | 35.02 |
| `'Domestic'` | 0.40 | 6,165.03 |  8,063,859.24  | 24,764,925.51 | 32.56 |
            ''')

st.caption('''
For more details on where the '`Project Average`' values came from, check out the `Dataset` tab. 
           The remaining values were from multiplying the region's '`Project Average`' to its corresponding project numbers from the first table.
        ''')

st.markdown('''
            ##### Specification-Driven Sales

| Region | Hunter Spec Market($) | Hunter Total Sales($) | Spec/Sales (%) |
| ----------- | ----------- | ----------- | ----------- |
| `'Central States'` | 1,728,378.12 | 86,861,729.26 | 1.99 |
| `'Florida'` | 372,086.80 | 79,686,983.49 | 0.47 |
| `'Great Lakes'`| 1,584,239.76 | 39,048,791.55 | 4.06 |
| `'Northern California'` | 846,971.64 | 25,793,560.27 | 3.28 |
| `'Northeast'` | 450,257.85 | 48,945,176.18 | 0.92 |
| `'Northwest'` | 702,180.04 | 32,485,935.43 | 2.16 |
| `'Southern California'`| 567,494.85 | 29,951,923.33 | 1.89 |
| `'Southeast'` | 1,077,581.16	 | 40,662,662.20 | 2.65 |
| `'Southwest'` | 744,641.92 | 29,855,769.90 | 2.49 |
| `'Domestic'` | 8,063,859.24 | 413,292,531.61 | 1.95 |
            ''')

st.caption('''The percentage was significantly small when considering the limited amount of `DodgeBI` projects (4017).
            For a more accurate percentage of sales that were specification driven in 2023, 
            we looked at numbers from `Land F/X`.''')

st.subheader('International :material/public:')
st.markdown('''
##### Land F/X Numbers: A More Accurate Estimate
'`Land F/X`'  is a globally used software tool for irrigation designers that helps with project layout. 
            By selecting preferred manufacturers, it provides a more precise count of Hunter-specified projects, 
            leading to more accurate estimates of the irrigation market.


| 2023 Quarter | # of Projects |
| ----------- | ----------- |
| `'Quarter 1'` | 6,240 |
| `'Quarter 2'` | 6,621 |
| `'Quarter 3'`| 6,356 |
| `'Quarter 4'` | 6,040 |
| `'Total'` | 25,257 |
            ''')

st.markdown('''
            
Hunter's Land F/X Market Size: `$155,710,162.71`
            
Overall Land F/X Market Size: `$478,201,623.55`
            
Percent: `32.5616%`''')

st.markdown('''
##### Specification-Driven Sales Globally 
| Region | Hunter Total Sales($) |
| ----------- | ----------- |
| `'China'` | 2,499,797.26 |
| `'Latin America'` | 13,840,776.36 |
| `'Middle East'`| 32,420,131.37 |
| `'Northern Europe'` | 33,484,822.44 |
| `'Pacific Rim'` | 26,095,198.90 |
| `'Southern Europe'` | 30,216,969.54 |
| `'Domestic'`| 413,292,531.61 |
| `'Global'`| 551,850,227.48 |

These sales numbers were provided by Greg Lamson.
            
            Percent: 155710162.71/(551850227.48) = 28.22%
    (Hunter's Land F/X Market Size/ Global Total)
            
Therefore, we can conclude that `28.22%` of sales were driven by specification with more specification-driven sales happening internationally.
            ''')

st.divider()
st.text('Developed by Christine Law • Marketing Analyst Intern 2024 • Hunter Industries')