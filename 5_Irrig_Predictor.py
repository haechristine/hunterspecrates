import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

# Load your trained model
model = ...  # Load your model here, e.g., joblib.load('model.pkl')

# Streamlit interface
st.title('Irrigation Value Predictor')

valve_count = st.number_input('Valve Count', min_value=0)
square_footage = st.number_input('Square Footage', min_value=0)
region_name = st.selectbox('Region Name', options=['north', 'south', 'east'])

input_data = pd.DataFrame({
    'valve_count': [valve_count],
    'square_footage': [square_footage],
    'region_name': [region_name]
})

# Preprocess input data
X_input = preprocessor.transform(input_data)

# Predict
prediction = model.predict(X_input)

st.write(f'Estimated Irrigation Value: ${prediction[0]:.2f}')