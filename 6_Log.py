import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('Log Entries :material/lab_profile:')

st.logo("logo.png")

st.markdown('''
           > Week 1 (6/17-6/21)

- Getting settled and learning more about the project
- Setting up meetings with Marketing Strategy Team members (3 meetings)

> Week 2 (6/24-6/28)

- Meeting with Dodge representatives
    - Learned about the software
    - Answered questions about finding total specification rate, trends of projects overtime, etc.
- More meetings with Marketing Strategy Team (7 meetings)
- Meeting with Sales and Analyst representative to gain insight on outside opinions on project (2 meetings)
- Solidifying what variables to include in datasheet

> Week 3 and 4 (7/1-7/12)

- Last Marketing Strategy Team meeting
    - Found out average net distributor net cost for relevant valves
- Had discussion with Sales and Product Management to determie best ways to find the gross estimate of valve values
- More discussion on how to calculate the monetary irrigation value
- Deep diving into DodgeBI and looking into relevant 2023 projects to fill out datasheet

> Week 5 (7/15-7/29)

- Check-in meetings with Bryce Carnehl
- Continuing deep dive into DodgeBI and cultivating the datasheet

> Week 6 (7/22-7/26)
- Finished datasheet (refer to dataset tab)
- Began reaching out and having meetings with Sales/Specification Managers in all 9 regions
    - Gaining insight on our numbers as well as any specifics about their region
    - Taking note of considerations to take dependent per region
- Started creating a Jupyter Notebook and data cleaning/wrangling

> Week 7 (7/29-8/2)
- Reading up on variational autoencoding in order to expand dataset
- Working closely with Mandla Sibanda and Vince Carpino to help with importing necessary packages 
- Normalizing and one-hot encoding categorial variables in the dataset
- Creating more visualizations

> Week 8 (8/5-8/9)
- Redirecting final product to use Streamlit --> simple usability
- Implementing variational autoencoding into dataset
- Working closely with Mandla and Vince when persistent bugs occur
- Creating more visualizations
- Finishing up Sales meetings with Specification Managers
- Follow-up meeting with Dodge to share feedback with using their SpecShare tool

> Week 9 (8/12-8/16)
- Finalizing variational autoencoding to expand dataset
- Working on Streamlit report/website
- Drafting final presentation

> Week 10 (8/19-8/22)
- Finalizing final presentation
- Present to Specification Managers and at Intern All-Hands Meeting
''')

st.caption('''Special thanks to Bryce Carnehl for his exemplary guidance, to Mandla Sibanda and Vince Carpino for their invaluable coding assistance, and to Kris Guy for her help with editing the website content.:material/sentiment_very_satisfied:''')
            
st.divider()
st.text('Developed by Christine Law • Marketing Analyst Intern 2024 • Hunter Industries')