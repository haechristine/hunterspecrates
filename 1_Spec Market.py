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
| `'Central States'` | 5599 |  10000  | 55.99 |
| `'Florida'`| 3643|  10000  | 36.43 |
| `'Great Lakes'` | 3460 |  10000  | 34.60 |
| `'Northeast'` | 6353 |  10000  | 63.53 |
| `'Northern California'` | 6993 |  10000  | 69.93 |
| `'Northwest'` | 7020 |  10000  | 70.20 |
| `'Southeast'` | 5738 |  10000  | 57.38 |
| `'Southern California'` | 7013 |  10000  | 70.13 |
| `'Southwest'` | 5339 |  10000  | 53.39 |
| `'Domestic'` | 51158 |  90000  | 56.84 |
            ''')
st.caption('These numbers were directly taken from `DodgeBI`. Please note that 118 Canada projects were omitted.')

st.markdown('''
##### Estimate Domestic Irrigation Market
   
| Region              | Irrigation Value per SF($) | Project Average($) | Hunter Specified Market($) | Total Specified Market($) | Hunter/Total(%) |
|---------------------|----------------------------|--------------------|----------------------------|---------------------------|----------------|
| Central States       | 0.61                       | 5,642.79            | 5,359,846.37                | 9,572,730.95               | 55.99          |
| Florida              | 0.26                       | 5,465.36            | 839,939.80                  | 2,305,589.33               | 36.43          |
| Great Lakes          | 0.43                       | 9,959.62            | 1,574,473.72                | 4,550,769.93               | 34.60          |
| Northeast            | 0.35                       | 5,380.93            | 7,981,898.11                | 12,564,490.82              | 63.53          |
| Northern California  | 0.23                       | 9,159.97            | 6,828,266.82                | 9,764,718.45               | 69.93          |
| Northwest            | 0.28                       | 5,320.98            | 3,587,720.93                | 5,110,445.19               | 70.20          |
| Southeast            | 0.19                       | 4,434.85            | 4,171,848.34                | 7,271,004.47               | 57.38          |
| Southern California  | 0.11                       | 5,124.18            | 444,803.27                  | 634,253.41                 | 70.13          |
| Southwest            | 0.43                       | 5,744.75            | 3,262,313.83                | 6,110,536.73               | 53.39          |
| Domestic             | 0.52                       | 9,595.78            | 467,821.93                  | 606,487.12                 | 56.84          |

            ''')

st.caption('''
For more details on where the '`Project Average`' values came from, check out the `Dataset` tab. 
           The remaining values were from multiplying the region's '`Project Average`' to its corresponding project numbers from the first table.
        ''')

st.markdown('''
            ##### Specification-Driven Sales

| Region              | Hunter Specified Market($) | Hunter Total Sales($) | Spec/Sales (%) |
|---------------------|----------------------------|-----------------------|----------------|
| Central States       | 5,359,846.37               | 35,199,653.44          | 15.23          |
| Florida              | 839,939.80                 | 41,546,463.43          | 2.02           |
| Great Lakes          | 1,574,473.72               | 27,048,313.67          | 5.82           |
| Northeast            | 7,981,898.11               | 50,659,442.84          | 15.76          |
| Northern California  | 6,828,266.82               | 63,719,821.86          | 10.72          |
| Northwest            | 3,587,720.93               | 51,207,587.50          | 7.01           |
| Southeast            | 4,171,848.34               | 35,518,222.38          | 11.75          |
| Southern California  | 444,803.27                 | 35,052,325.89          | 1.27           |
| Southwest            | 3,262,313.83               | 29,173,127.54          | 11.18          |
| Domestic             | 467,821.93                 | 66,343,174.58          | 0.71           |

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
|--------------|---------------|
| Quarter 1    | 6,865         |
| Quarter 2    | 6,123         |
| Quarter 3    | 6,053         |
| Quarter 4    | 6,396         |
| Total        | 25,437        |
            ''')

st.markdown('''
            
Hunter's Land F/X Market Size: `$863,620,200`
            
Overall Land F/X Market Size: `$3,454,481,800`
            
Percent: `24.99%`''')

st.markdown('''
##### Specification-Driven Sales Globally 
| Region            | Hunter Total Sales($)   |
| ----------------- | ----------------------- |
| 'China'           | 1,283,945,120.45        |
| 'Latin America'   | 3,523,879,670.12        |
| 'Middle East'     | 4,192,830,440.78        |
| 'Northern Europe' | 2,564,123,890.99        |
| 'Pacific Rim'     | 3,705,691,230.56        |
| 'Southern Europe' | 2,876,481,560.25        |
| 'Domestic'        | 16,214,569,780.34       |
| 'Global'          | 32,361,521,293.49       |


These sales numbers were provided by Greg Lamson.
            
            Percent: 863,620,200/(32,361,521,293.49) = 2.67%
    (Hunter's Land F/X Market Size/ Global Total)
            
Therefore, we can conclude that `2.67%` of sales were driven by specification with more specification-driven sales happening internationally.
            ''')

st.divider()
st.text('Developed by Christine Law • Marketing Analyst Intern 2024 • Hunter Industries')
