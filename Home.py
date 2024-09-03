import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# import menu
# from menu import menu

st.title('Specification Analysis Report :material/analytics:')

st.logo("logo.png")

st.markdown('''

Hello! :material/sentiment_satisfied:

My name is Christine Law, and welcome to my data analysis on Hunter's specification rate within the irrigation market. 

> Project Information :material/task:

In order to better understand Hunter's market share, we needed to find out more about its specification rate. 
            Since we lacked crucial information about the overall size of the specification market, 
            **my role was to develop a method for more accurately estimating the monetary value of Hunter's specification rate within the irrigation sector.**
Specifically, I focused on projects from 2023 valued at $1 million or more
             as this was the first full year of "normal" data post-pandemic.
> Outline :material/grading:

- Phase 1: Extrapolating data from `DodgeBI` 
- Phase 2: Manipulating data to figure out market share 
- Phase 3: Working with sales to gain alignment and feedback 
 
> Goals :material/rocket_launch:
1. Use a machine learning algorithm (variational autoencoding) to expand dataset from 90 to 1,000.
2. Generate relevant data visualizations to better understand the dataset.
3. Find the estimated irrigation value domestically and for each of the nine regions.
4. Perform hypothesis testing to evaluate statistical significance of the analysis.
''')

st.divider()
st.text('Developed by Christine Law • Marketing Analyst Intern 2024 • Hunter Industries')