import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('Graphs :material/insert_chart:')

st.logo("logo.png")

st.markdown('''Please note that these graphs depict 90 datapoints. They are not completely accurate depictions, but close estimates.''')

option = st.selectbox(
    "Select the visualization you would like to see!",
    ("Distribution of Building Type",
      "Distribution of Mix Manufacturers",
      "Distribution of Emission Types Domestically",
      "Distribution of Emission Types Regionally",
      "Relationship Between Cost of Project and Region",
      "Relationship Between Square Footage and Number of Valves",
      "Relationship Between Square Footage and Total Price of Project",
      "Trends Amongst Hunter's 9 Regions' Square Footage Average",
      "Trends Amongst Hunter's 9 Regions' Valve Count Average",
      "Trends Amongst Hunter's 9 Regions' Irrigation Monetary Value",
      "Trends Amongst Hunter's 9 Regions' Cost per Square Footage",
      "Correlation Matrix"),
    index=None,
    placeholder="Select graph...",
)

add_region = None
if option == 'Distribution of Building Type':
    with st.sidebar:
        add_region = st.radio(
            "Choose a region",
            ("Domestic",
            "Central States",
            "Florida",
            "Great Lakes",
            "Northeast",
            "Northern California",
            "Northwest",
            "Southeast",
            "Southern California",
            "Southwest")
        )
# Generate Graphs
df = pd.read_csv('dataset/new_acre_valve.csv')

string_cols = df.select_dtypes(include='object').columns

# Trim whitespace from all string columns
df[string_cols] = df[string_cols].apply(lambda x: x.str.strip())

def calculate_new_col(col):
    return col['spray_count']*252.1 + col['mp_count']*364.2 + col['drip_count']*475 + col['rotor_count']*188.8 

# Apply function to create new column
df['est_irrig_value'] = df.apply(calculate_new_col, axis=1)

def calculate_sf(col):
    return col['est_irrig_value']/col['square_feet']

# Apply function to create new column
df['cost_per_sf'] = df.apply(calculate_sf, axis=1)


def gen_building_type():
    building_count = df.groupby('building_type').size().reset_index(name='count')
    
    # Create a figure and axis object
    fig, ax = plt.subplots(figsize=(15, 12))  # Adjusted size for better fit in Streamlit
    
    # Plot the data
    ax.bar(building_count['building_type'], building_count['count'], color='#00658A')

    # Set labels and title with larger font sizes
    ax.set_xlabel('Building Type', fontsize=18)
    ax.set_ylabel('Count', fontsize=18)
    ax.set_title('Distribution of Building Type Domestically', fontsize=20)
    ax.tick_params(axis='x', labelsize=18)  # Font size for x-axis labels
    ax.tick_params(axis='y', labelsize=18)  # Font size for y-axis labels
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90)
    
    plt.tight_layout()
    return fig

def mix_man():
    mix_count = df.groupby('mix_manufacturers').size().reset_index(name='count')
    
    colors = ['#C14729','#61A60E']

    # Create a figure and axis object
    fig, ax = plt.subplots(figsize=(8, 8))  # Adjusted size for a pie chart
    
    # Plot the pie chart
    wedges, texts, autotexts = ax.pie(
        mix_count['count'], 
        labels=mix_count['mix_manufacturers'].astype(str), 
        autopct='%1.1f%%',  # Display percentage
        colors=colors[:len(mix_count)],  # Color map for different slices
        startangle=140,  # Start angle for the pie chart
        wedgeprops={'edgecolor': 'black'}  # Add edge color for slices
    )
    
    # Set labels and title
    ax.set_title('Distribution of Mix Manufacturers', fontsize=16)
    
    # Improve the appearance of the pie chart labels
    for text in texts:
        text.set_fontsize(12)  # Font size for labels
    for autotext in autotexts:
        autotext.set_fontsize(12)  # Font size for percentages

    plt.tight_layout()  # Adjust layout to make room for labels

    return fig

def emission_type_domestic():
    emission_sum = np.array(df.iloc[:, 4:8].sum(axis=0))
    emission_name = np.array((df.iloc[:, 4:8]).columns)

    plt.figure(figsize=(8, 5)) 

    plt.bar(emission_name, emission_sum, color='#00658A')

    plt.xlabel('Emission Type')
    plt.ylabel('Count')
    plt.title('Distribution of Emission Type Domestically')

    plt.tight_layout()
    return plt

def emission_type_region():
    valve_sum = df.groupby('region').sum()
    valve_sum = valve_sum.iloc[:,3:7]
    valve_sum = valve_sum.reset_index()

    colors = ['#00658A', '#47ABD1', '#A777A6', '#61A60E']

    fig, ax = plt.subplots(figsize=(14, 10))

    num_regions = len(valve_sum['region'])
    num_categories = len(valve_sum.columns) - 1 

    bar_width = 0.8 / num_categories
    index = np.arange(num_regions)  

    for i, (category, color) in enumerate(zip(valve_sum.columns[1:], colors)):
        offset = (i - num_categories / 2 + 0.5) * bar_width
        ax.bar(index + offset, valve_sum[category], bar_width, label=category, color=color)

    ax.set_xlabel('Regions', fontsize = 18)
    ax.set_ylabel('Counts',fontsize = 18)
    ax.set_title('Valve Counts by Region and Emission Device',fontsize = 20)
    ax.tick_params(axis='x', labelsize=14)  # Font size for x-axis labels
    ax.tick_params(axis='y', labelsize=14)  # Font size for y-axis labels
    ax.set_xticks(index)
    ax.set_xticklabels(valve_sum['region'], rotation=45, ha='right')

    ax.legend(title='Categories')

    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    return fig

def gen_cost_region():
    total_region = df.groupby('region')['value_mill'].mean()
    total_region = total_region.reset_index()

    plt.figure(figsize=(8, 6)) 

    plt.bar(total_region['region'], total_region['value_mill'], color='#00658A')

    plt.xlabel('Region')
    plt.ylabel('Average Total Project Value (M)')
    plt.title('Trend Between the Region\'s Total Project Value')

    plt.xticks(rotation=90)

    return plt

def gen_sf_valve():
    plt.figure(figsize=(10, 5)) 

    plt.scatter(df['valve_count'], df['square_feet'], color='#00658A')

    plt.xlabel('Number of Valves')
    plt.ylabel('Landscape Area (SF)')
    plt.title('Square Footage vs. Number of Valves')

    return plt

def gen_sf_price():
    plt.figure(figsize=(10, 5)) 

    plt.scatter(df['value_mill'], df['square_feet'], color='#00658A')

    plt.xlabel('Total Project Value (millions)')
    plt.ylabel('Landscape Area (SF)')
    plt.title('Landscape Area vs. Total Project Value (M)')

    plt.xticks(rotation=45)

    return plt

def gen_region_sf():
    sf_region = df.groupby('region')['square_feet'].mean()
    sf_region = sf_region.reset_index()

    plt.figure(figsize=(8, 5)) 

    plt.bar(sf_region['region'], sf_region['square_feet'], color='#00658A')

    plt.xlabel('Region')
    plt.ylabel('Average Square Feet of Landscape Area')
    plt.title('Trend Between the Region\'s Landscape Area')

    plt.xticks(rotation=45)

    return plt

def gen_region_valve():
    valve_region = df.groupby('region')['valve_count'].mean()
    valve_region = valve_region.reset_index()

    plt.figure(figsize=(8, 6)) 

    plt.bar(valve_region['region'], valve_region['valve_count'], color='#00658A')

    plt.xlabel('Region')
    plt.ylabel('Average Valve Count')
    plt.title('Trend Between the Region\'s Valve Count')

    plt.xticks(rotation=45)
    return plt

def gen_region_value():
    money_region = df.groupby('region')['est_irrig_value'].mean()
    money_region = money_region.reset_index()

    plt.figure(figsize=(8, 6)) 

    plt.bar(money_region['region'], money_region['est_irrig_value'], color='#00658A')

    plt.xlabel('Region')
    plt.ylabel('Average Irrigation Value')
    plt.title('Trend Between the Region\'s Irrigation Value')

    plt.xticks(rotation=45)
    return plt

def gen_per_sf():
    per_region = df.groupby('region')['cost_per_sf'].mean()
    per_region = per_region.reset_index()

    plt.figure(figsize=(8, 6)) 

    plt.bar(per_region['region'], per_region['cost_per_sf'], color='#00658A')

    plt.xlabel('Region')
    plt.ylabel('Average Cost per Square Foot')
    plt.title('Trend Between the Region\'s Square Footage Value')

    plt.xticks(rotation=45)
    return plt

building_plot = gen_building_type
mix_plot = mix_man
emission_plot = emission_type_domestic
emission_region = emission_type_region
cost_region = gen_cost_region
sf_value = gen_sf_valve
sf_price = gen_sf_price
region_sf = gen_region_sf
region_valve = gen_region_valve
region_value = gen_region_value
per_sf = gen_per_sf

# Display the corresponding plot based on the selected fruit
if option == "Correlation Matrix":
    st.image('corr_matrix.png')
    st.caption('''Displays pairwise correlations between variables in the dataset

Examples:
1. 'est_irrig_value' and 'valve_count' have a strong positive correlation (0.95), revealing that a higher estimated value tend to have a higher valve count
2. 'drip_count' and 'mp_count' have a very weak negative correlation (-0.18), revealing that a lower drip count tend to have a higher drip count and vice versa''')
elif option == "Distribution of Building Type":
    st.pyplot(building_plot())
elif option == "Distribution of Mix Manufacturers":
    st.pyplot(mix_plot())
elif option == "Distribution of Emission Types Domestically":
    st.pyplot(emission_plot())
elif option == "Distribution of Emission Types Regionally":
    st.pyplot(emission_region())
elif option == "Relationship Between Cost of Project and Region":
    st.pyplot(cost_region())
elif option == "Relationship Between Square Footage and Number of Valves":
    st.pyplot(sf_value())
elif option == "Relationship Between Square Footage and Total Price of Project":
    st.pyplot(sf_price())
elif option == "Trends Amongst Hunter's 9 Regions' Square Footage Average":
    st.pyplot(region_sf())
elif option == "Trends Amongst Hunter's 9 Regions' Valve Count Average":
    st.pyplot(region_valve())
elif option == "Trends Amongst Hunter's 9 Regions' Irrigation Monetary Value":
    st.pyplot(region_value())
elif option == "Trends Amongst Hunter's 9 Regions' Cost per Square Footage":
    st.pyplot(per_sf())
    st.caption('''To find out the specific numbers, checkout the `Spec Market` tab under the 'Estimate Domestic Irrigation Market' Table.''')

def region_building(region):
    # region_data = df[df['region'].str.contains(region)]
    region_data = df[df['region'] == region]

    # Count frequencies of building types
    grouped = region_data['building_type'].value_counts().reset_index()

    plt.figure(figsize=(8, 5))
    plt.xticks(rotation=45)
    plt.bar(grouped['building_type'], grouped['count'], color='#47ABD1')

    plt.xlabel('Building Types')
    plt.ylabel('Frequency')
    plt.title(f'Building Type Distribution in {region}')
    
    return plt

# region_fl = region_building
# st.write(df)

if add_region =='Central States' and option == 'Distribution of Building Type':
    st.pyplot(region_building('Central States'))
elif add_region == 'Florida' and option == 'Distribution of Building Type':
    st.pyplot(region_building('Florida'))
elif add_region =='Great Lakes' and option == 'Distribution of Building Type':
    st.pyplot(region_building('Great Lakes'))
elif add_region =='Northeast' and option == 'Distribution of Building Type':
    st.pyplot(region_building('Northeast'))
elif add_region =='Northern California' and option == 'Distribution of Building Type':
    st.pyplot(region_building('Northern California'))
elif add_region =='Northwest' and option == 'Distribution of Building Type':
    st.pyplot(region_building('Northwest'))
elif add_region =='Southeast' and option == 'Distribution of Building Type':
    st.pyplot(region_building('Southeast'))
elif add_region =='Southern California' and option == 'Distribution of Building Type':
    st.pyplot(region_building('Southern California'))
elif add_region =='Southwest' and option == 'Distribution of Building Type':
    st.pyplot(region_building('Southwest'))

st.divider()
st.text('Developed by Christine Law • Marketing Analyst Intern 2024 • Hunter Industries')