# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19YwpJuMnUiv4y85k-U0U3g2KB-Xvg5UV
"""

!curl ipecho.net/plain

!pip install streamlit --quiet
!pip install pyngrok --quiet

import pandas as pd
yt = pd.read_csv('Youtuber.csv')

yt.describe()

yt.head()

yt.dropna()

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# yt = pd.read_csv('Youtuber.csv')
# 
# st.set_page_config(layout="wide")
# st.title("Youtubers Worldwide")
# 
# left_column, right_column = st.columns(2)
# 
# # Load and display the image in one of the columns
# with right_column:
#     st.image("yt.jpg", use_column_width=True)  # Adjust width to fit column
# 
# 
# # Create a sidebar header and a separator
# st.sidebar.header("Dashboard")
# st.sidebar.markdown("---")
# 
# st.sidebar.header("Data Visualizations")
# 
# # Create a dropdown menu to select the chart type
# chart_option = st.sidebar.selectbox("Select Chart", ["Grouped Bar Chart", "Histogram"])
# 
# # Display the selected chart
# if chart_option == "Grouped Bar Chart":
#     # Display the grouped bar chart
#     st.subheader("Grouped Bar Chart")
#     # Your code for displaying the grouped bar chart here
# 
# 
# elif chart_option == "Histogram":
#     # Count the number of YouTubers in each country
# 
#     yt['Country'] = yt['Country'].astype(str)
#     country_counts = yt['Country'].value_counts()
# 
#     # Plot a histogram
#     fig, ax = plt.subplots(figsize=(12, 6))
#     ax.hist(yt['Country'], bins=len(country_counts))
# 
#     # Add labels and title
#     ax.set_xlabel('Country')
#     ax.set_ylabel('Number of YouTubers')
#     ax.set_title('Distribution of YouTubers Across Countries')
# 
#     # Rotate x-axis labels for better visibility
#     plt.xticks(rotation=45)
# 
#     # Show plot
#     st.pyplot(fig)
# 
# list_variables = yt.columns
# 
# # Display a header for the Visualization section
# st.markdown("## Visualization")
# symbols = st.multiselect("Select two variables", list_variables, ["Content Type", "Rank"])
# 
# ## Description of Dataset
# 
# num = st.number_input('No of Rows',5,10)
# st.dataframe(yt.head(num))
# 
# ### Description of the dataset
# 
# st.dataframe(yt.describe())
# 
# ### Missing value
# 
# ytnull = yt.isnull().sum()/len(yt)*100
# totalmiss = ytnull.sum().round(2)
# st.write("Percentage of missing value in my dataset",totalmiss)
# 
# 
# # Function to convert 'K' and 'M' suffixed strings to numeric values
# def k_to_numeric(value):
#     if isinstance(value, str):
#         if 'K' in value:
#             return float(value.replace('K', '')) * 1000
#         elif 'M' in value:
#             return float(value.replace('M', '')) * 1000000
#         else:
#             return float(value)
#     elif isinstance(value, (int, float)):
#         return value
#     else:
#         raise ValueError("Unexpected value: {}".format(value))
# 
# 
# 
# # Convert 'K' suffixed strings to numeric values in the DataFrame
# yt['Subscribers'] = yt['Subscribers'].apply(k_to_numeric)
# yt['Average Views'] = yt['Average Views'].apply(k_to_numeric)
# 
# 
# 
# # Create a dropdown menu with different types of content
# content_type = st.selectbox('Select Content Type', yt['Content Type'].unique())
# 
# # Filter the dataset based on the selected content type
# filtered_yt = yt[yt['Content Type'] == content_type]
# 
# # Display the filtered list of YouTubers
# if not filtered_yt.empty:
#     st.write(f'YouTubers producing {content_type}:')
#     st.write(filtered_yt['Channel Name'].tolist())
# else:
#     st.write('No YouTubers found for the selected content type.')
# 
# # Calculate average number of subscribers and views for the selected content type
# avg_subscribers = np.mean(filtered_yt['Subscribers'])
# avg_views = np.mean(filtered_yt['Average Views'])
# 
# # Define content types and corresponding averages
# content_types = ['Subscribers', 'Average Views']
# averages = [avg_subscribers, avg_views]
# 
# # Define the x locations for the groups
# x = np.arange(len(content_types))
# 
# # Define width of the bars
# width = 0.35
# 
# # Create subplots for the grouped bar chart
# fig, ax = plt.subplots()
# 
# # Plot bars
# bar1 = ax.bar(x, averages, width, label='Content Type')
# 
# # Add labels, title, and legend
# ax.set_ylabel('Count')
# ax.set_title('Average Subscribers and Views by Content Type')
# ax.set_xticks(x)
# ax.set_xticklabels(content_types)
# ax.legend()
# 
# # Add text annotations
# for rect in bar1:
#     height = rect.get_height()
#     ax.annotate('{}'.format(height),
#                 xy=(rect.get_x() + rect.get_width() / 2, height),
#                 xytext=(0, 3),  # 3 points vertical offset
#                 textcoords="offset points",
#                 ha='center', va='bottom')
# 
# # Show plot
# st.pyplot(fig)
# 
# 
# 
# 
# 
#

pip install sweetviz

import sweetviz as sv
import pandas as pd

# Load your dataset
yt = pd.read_csv('Youtuber.csv')

# Generate the Sweetviz report
report = sv.analyze(yt)

# Save the report to an HTML file
report.show_html('report.html')

!streamlit run app.py & npx localtunnel --port 8501

pip freeze>requirements.txt

from google.colab import drive
drive.mount('/content/drive')