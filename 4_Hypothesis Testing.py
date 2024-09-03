import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.title('Hypothesis Testing :material/code_blocks:')

st.logo("logo.png")

st.markdown('''
`What Is Hypothesis Testing?`
            
            A statistical method used to determine whether there is enough
    evidence to reject a null hypothesis in favor of an alternative hypothesis. 
    Its significance lies in making informed decisions and conclusions
    based on data analysis.
            
Null Hypothesis ($H_0$): The square footage/valve count/overall value `significantly` predicts the irrigation monetary value.

Alternate Hypothesis ($H_a$): The square footage/valve count/overall value `does not significantly` predict the irrigation monetary value.

Our significance level* is:
            ''')

st.latex(r'''\alpha = 0.05''')

st.markdown('''
*The probability of rejecting the null hypothesis when it is actually true. It means there is a 5% risk of concluding that an effect or difference exists when there is none.
            ''')

st.markdown('''
##### Correlation Plots
            ''')
df = pd.read_csv('dataset/new_acre_valve.csv')
def calculate_new_col(col):
    return col['spray_count']*252.1 + col['mp_count']*364.2 + col['drip_count']*475 + col['rotor_count']*188.8 

# Apply function to create new column
df['est_irrig_value'] = df.apply(calculate_new_col, axis=1)
fig = sns.pairplot(df, x_vars=['square_feet', 'valve_count', 'value_mill'], y_vars=['est_irrig_value'])
st.pyplot(fig)

with st.echo():
    # Define predictor variables and dependent variable
    X = df[['square_feet', 'valve_count', 'value_mill']]
    y = df['est_irrig_value']

    # Add a constant term for the intercept
    X = sm.add_constant(X)

    # Fit the model
    model = sm.OLS(y, X).fit()

    # Print the summary
    st.write(model.summary())

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Fit the model
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = lr.predict(X_test)

st.markdown('''
            ##### Summary:
        1. Square Footage
            - Mean Squared Error: 0.0184
            - R-Squared: 0.598
            - P-Value: 0.067
            - We reject the null hypothesis that square footage significantly predicts the irrigation monetary value at the significance level of 0.05.

        2. Valve Count
            - Mean Squared Error: 0.0048
            - R-Squared: 0.895
            - P-Value: 0.000
            - We fail to reject the null hypothesis that square footage significantly predicts the irrigation monetary value at the significance level of 0.05.

        3. Total Project Value
            - Mean Squared Error: 0.0454
            - R-Squared: 0.00526
            - P-Value: 0.682
            - We reject the null hypothesis that square footage significantly predicts the irrigation monetary value at the significance level of 0.05.

        As a result, we concluded that `valve count` is significantly correlated to the irrigation value of a project. 
            However, this conclusion is based on a small sample size, which limits the statistical significance of the results. 
            To better understand Hunter's market share, it is crucial to allocate additional resources for a more comprehensive 
            analysis of the specification market.
            ''')
st.divider()
st.text('Developed by Christine Law • Marketing Analyst Intern 2024 • Hunter Industries')