import streamlit as st
import plotly.express as px
import pandas as pd

# Load dataset (Make sure to upload or link your dataset)
data = pd.read_csv('path_to_your_dataset.csv')

# Ensure only numeric columns are included for correlation calculation
numeric_data = data.select_dtypes(include=['number'])

# Clean the data by handling missing values if necessary
# You can either drop missing data or fill it with a value (e.g., mean, median, etc.)
numeric_data = numeric_data.fillna(numeric_data.mean())  # Fill NaN values with column means

# Create a correlation heatmap
corr = numeric_data.corr()
fig2 = px.imshow(corr, color_continuous_scale='Viridis', title="Correlation Heatmap")

# Example plot: Create a scatter plot for 'Healthcare Spending vs Life Expectancy'
fig1 = px.scatter(data, x='Healthcare_Spending_Percent_GDP', y='Life_Expectancy_2023', 
                  hover_data=['Country'], title="Healthcare Spending vs Life Expectancy")

# Streamlit app layout
st.title("Interactive Dashboard: Life Expectancy and Healthcare Spending")

# Scatter Plot
st.subheader("Healthcare Spending vs Life Expectancy")
st.plotly_chart(fig1)

# Correlation Heatmap
st.subheader("Correlation Heatmap of Health Indicators")
st.plotly_chart(fig2)

# Optional: Add filters or sliders for interaction
region = st.selectbox('Select Region', data['Region'].unique())
st.write(f"Showing data for: {region}")

filtered_data = data[data['Region'] == region]
fig3 = px.scatter(filtered_data, x='Healthcare_Spending_Percent_GDP', y='Life_Expectancy_2023', 
                  hover_data=['Country'], title=f"Healthcare Spending vs Life Expectancy in {region}")
st.plotly_chart(fig3)
