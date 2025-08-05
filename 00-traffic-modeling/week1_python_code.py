# =============================================================================
# CE 311K Module 1: Austin Traffic Pandemic Story - Week 1 Code
# Students analyze real Austin traffic incident data to understand pandemic impact
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# =============================================================================
# SESSION 1 (50 min): "What Really Happened to Austin Traffic?"
# Topics: Variables, Data Types, CSV files, Basic Pandas
# =============================================================================
# Download data https://data.austintexas.gov/browse?Ownership_Department-name=Transportation+and+Public+Works&limitTo=datasets&sortBy=relevance&pageSize=20&page=1
# For API  https://data.austintexas.gov/resource/dx9v-zd7x.json
# Our API has a default limit of providing 1,000 rows. Learn more about how you can modify the default limit.
# https://support.socrata.com/hc/en-us/articles/202949268-How-to-query-more-than-1000-rows-of-a-dataset
print("=== SESSION 1: Loading and Exploring Austin Traffic Data ===")

# TOPIC: Variables and Data Types
# Students learn variables by storing traffic data information
print("\n--- Understanding Variables and Data Types ---")

# Basic variables to store information about our traffic data
data_source = "Austin Traffic Incident Reports"  # String variable
total_years_available = 7                         # Integer variable  
pandemic_start_year = 2020                       # Integer variable
pre_pandemic_year = 2019                         # Integer variable
data_file_size_mb = 45.6                        # Float variable

print(f"Data source: {data_source}")
print(f"Years of data available: {total_years_available}")
print(f"Pandemic started in: {pandemic_start_year}")
print(f"Pre-pandemic comparison year: {pre_pandemic_year}")
print(f"Data file size: {data_file_size_mb} MB")

# TOPIC: What is a CSV file?
# Students understand the structure of comma-separated values
print("\n--- Understanding CSV Files ---")
print("CSV = Comma Separated Values")
print("Each row is a traffic incident")
print("Each column is a piece of information about that incident")

# Show what a CSV row looks like conceptually
sample_csv_header = "Published_Date,Issue_Reported,Location,Incident_Status,Issue_Type"
sample_csv_row = "2020-03-15 14:30:00,Traffic Signal Malfunction,IH 35 @ MLK,Active,Signal"

print(f"CSV Header: {sample_csv_header}")
print(f"Sample Row: {sample_csv_row}")

# TOPIC: Loading Data with Pandas
# Students learn pandas naturally emerges from need to handle large traffic datasets
print("\n--- Loading Austin Traffic Data with Pandas ---")

# Note: In actual class, students would load from Austin Open Data
# For this example, we'll simulate the data structure
print("Loading Austin traffic incident data...")
print("(In class: students download from data.austintexas.gov)")

# Create sample data that matches Austin Open Data structure
# This simulates what students would get from the real CSV
sample_data = {
    'Published_Date': [
        '2019-03-15 08:30:00', '2019-03-15 17:45:00', '2019-06-20 12:15:00',
        '2020-03-15 08:30:00', '2020-03-15 17:45:00', '2020-06-20 12:15:00',
        '2020-04-01 10:00:00', '2020-04-01 14:30:00', '2020-04-15 09:15:00',
        '2021-03-15 08:30:00', '2021-03-15 17:45:00', '2021-06-20 12:15:00'
    ],
    'Issue_Reported': [
        'Vehicle Stalled', 'Traffic Collision', 'Signal Malfunction',
        'Vehicle Stalled', 'Traffic Collision', 'Signal Malfunction', 
        'Traffic Collision', 'Vehicle Stalled', 'Traffic Collision',
        'Vehicle Stalled', 'Traffic Collision', 'Signal Malfunction'
    ],
    'Location': [
        'IH 35 @ Riverside', 'Mopac @ Barton Springs', 'Lamar @ MLK',
        'IH 35 @ Riverside', 'Mopac @ Barton Springs', 'Lamar @ MLK',
        'IH 35 @ 6th St', 'Mopac @ Cesar Chavez', 'IH 35 @ MLK',
        'IH 35 @ Riverside', 'Mopac @ Barton Springs', 'Lamar @ MLK'
    ],
    'Incident_Status': [
        'Cleared', 'Cleared', 'Active',
        'Cleared', 'Cleared', 'Cleared',
        'Cleared', 'Cleared', 'Cleared', 
        'Cleared', 'Active', 'Cleared'
    ]
}

# TOPIC: Creating a DataFrame (natural need for structured data)
traffic_data = pd.DataFrame(sample_data)

print("Data loaded successfully!")
print(f"Data type: {type(traffic_data)}")
print(f"This is called a 'DataFrame' - perfect for traffic data analysis")

# TOPIC: Basic DataFrame exploration
print("\n--- Exploring Our Traffic Data ---")

# Show the shape of our data
rows, columns = traffic_data.shape
print(f"Our dataset has {rows} traffic incidents and {columns} pieces of information per incident")

# Show the first few incidents
print("\nFirst 5 traffic incidents:")
print(traffic_data.head())

# Show column names (what information we have about each incident)
print(f"\nInformation available for each incident: {list(traffic_data.columns)}")

# Show data types (students see why different data types matter)
print("\nData types for each column:")
print(traffic_data.dtypes)

# TOPIC: Basic data exploration (counting incidents)
print("\n--- Basic Traffic Incident Counting ---")

# Count total incidents
total_incidents = len(traffic_data)
print(f"Total traffic incidents in our data: {total_incidents}")

# Count by incident type
incident_counts = traffic_data['Issue_Reported'].value_counts()
print(f"\nIncident types and their counts:")
print(incident_counts)

# Most common incident type
most_common_incident = incident_counts.index[0]
most_common_count = incident_counts.iloc[0]
print(f"\nMost common incident type: {most_common_incident} ({most_common_count} incidents)")

print("\n=== END SESSION 1 ===")
print("Next session: We'll filter this data by year to see pandemic effects!")

# =============================================================================
# SESSION 2 (50 min): "Filtering the Pandemic Signal"
# Topics: Conditional Statements, Filtering Data, Basic Plotting
# =============================================================================

print("\n\n=== SESSION 2: Finding the Pandemic Traffic Signal ===")

# TOPIC: Working with dates (natural need for time-based analysis)
print("\n--- Preparing Data for Time Analysis ---")

# Convert date strings to datetime objects (students learn this is needed for filtering)
traffic_data['Date'] = pd.to_datetime(traffic_data['Published_Date'])
traffic_data['Year'] = traffic_data['Date'].dt.year
traffic_data['Month'] = traffic_data['Date'].dt.month
traffic_data['Hour'] = traffic_data['Date'].dt.hour

print("Added time information to help analyze pandemic effects:")
print(traffic_data[['Published_Date', 'Year', 'Month', 'Hour']].head())

# TOPIC: Conditional Statements for Data Filtering
print("\n--- Using Conditional Statements to Filter by Year ---")

# Create filters for different time periods (students learn conditionals naturally)
pre_pandemic_filter = traffic_data['Year'] == 2019
pandemic_year_filter = traffic_data['Year'] == 2020
post_pandemic_filter = traffic_data['Year'] == 2021

# Apply filters to get subsets of data
pre_pandemic_data = traffic_data[pre_pandemic_filter]
pandemic_data = traffic_data[pandemic_year_filter] 
post_pandemic_data = traffic_data[post_pandemic_filter]

print(f"Pre-pandemic (2019) incidents: {len(pre_pandemic_data)}")
print(f"Pandemic year (2020) incidents: {len(pandemic_data)}")
print(f"Post-pandemic (2021) incidents: {len(post_pandemic_data)}")

# TOPIC: Conditional logic for multiple conditions
print("\n--- More Complex Filtering: Pandemic March vs Pre-Pandemic March ---")

# Compare same month across years (students learn complex conditions)
march_2019 = traffic_data[(traffic_data['Year'] == 2019) & (traffic_data['Month'] == 3)]
march_2020 = traffic_data[(traffic_data['Year'] == 2020) & (traffic_data['Month'] == 3)]

print(f"March 2019 incidents: {len(march_2019)}")
print(f"March 2020 incidents: {len(march_2020)}")

# Calculate the change
incident_change = len(march_2020) - len(march_2019)
percent_change = (incident_change / len(march_2019)) * 100 if len(march_2019) > 0 else 0

print(f"Change in incidents: {incident_change}")
print(f"Percent change: {percent_change:.1f}%")

# TOPIC: Basic Plotting to Visualize the Story
print("\n--- Plotting Traffic Incidents to See the Pandemic Story ---")

# Count incidents by year
yearly_counts = traffic_data['Year'].value_counts().sort_index()

# Create our first plot
plt.figure(figsize=(10, 6))

# TOPIC: Basic bar plot
plt.subplot(1, 2, 1)
plt.bar(yearly_counts.index, yearly_counts.values, color=['blue', 'red', 'green'])
plt.title('Austin Traffic Incidents by Year')
plt.xlabel('Year')
plt.ylabel('Number of Incidents')
plt.xticks(yearly_counts.index)

# Add value labels on bars
for i, v in enumerate(yearly_counts.values):
    plt.text(yearly_counts.index[i], v + 0.1, str(v), ha='center')

# TOPIC: Plotting incident types to see what changed
plt.subplot(1, 2, 2)
incident_type_counts = traffic_data['Issue_Reported'].value_counts()
plt.pie(incident_type_counts.values, labels=incident_type_counts.index, autopct='%1.1f%%')
plt.title('Types of Traffic Incidents')

plt.tight_layout()
plt.show()

# TOPIC: Time-based plotting (when do incidents happen?)
print("\n--- When Do Traffic Incidents Happen? ---")

# Group by hour to see daily patterns
hourly_incidents = traffic_data.groupby(['Year', 'Hour']).size().unstack(level=0, fill_value=0)

plt.figure(figsize=(12, 6))
plt.plot(hourly_incidents.index, hourly_incidents[2019], 'b-o', label='2019 (Pre-pandemic)', linewidth=2)
plt.plot(hourly_incidents.index, hourly_incidents[2020], 'r-o', label='2020 (Pandemic)', linewidth=2)
plt.plot(hourly_incidents.index, hourly_incidents[2021], 'g-o', label='2021 (Post-pandemic)', linewidth=2)

plt.title('Traffic Incidents by Hour of Day: Pandemic Impact')
plt.xlabel('Hour of Day (24-hour format)')
plt.ylabel('Number of Incidents')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(range(0, 24, 2))
plt.show()

# TOPIC: Creating meaningful insights from data
print("\n--- What Does This Data Tell Us? ---")

# Find peak incident hours for each year
peak_2019 = hourly_incidents[2019].idxmax()
peak_2020 = hourly_incidents[2020].idxmax()
peak_2021 = hourly_incidents[2021].idxmax()

print(f"Peak incident hour in 2019: {peak_2019}:00")
print(f"Peak incident hour in 2020: {peak_2020}:00") 
print(f"Peak incident hour in 2021: {peak_2021}:00")

# Calculate average incidents per day
days_per_year = 365
avg_incidents_2019 = len(pre_pandemic_data) / days_per_year
avg_incidents_2020 = len(pandemic_data) / days_per_year
avg_incidents_2021 = len(post_pandemic_data) / days_per_year

print(f"\nAverage incidents per day:")
print(f"2019: {avg_incidents_2019:.1f}")
print(f"2020: {avg_incidents_2020:.1f}")
print(f"2021: {avg_incidents_2021:.1f}")

# TOPIC: Preparing for next week's analysis
print("\n--- Questions for Next Week ---")
print("1. Which specific Austin locations saw the biggest changes?")
print("2. Did different types of incidents change differently?")
print("3. How can we automate this analysis for all locations?")
print("4. What do these patterns tell us about Austin's transportation resilience?")

print("\n=== END SESSION 2 ===")
print("Next week: We'll use loops to analyze all locations and create Austin's traffic map!")

# Save data for next session (students learn data persistence)
traffic_data.to_csv('austin_traffic_processed.csv', index=False)
print("\nData saved for next week's analysis!")
