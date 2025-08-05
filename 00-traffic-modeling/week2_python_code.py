# =============================================================================
# CE 311K Module 1: Austin Traffic Pandemic Story - Week 2 Code
# Students use loops to automate analysis and create Austin's traffic story map
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import seaborn as sns

# Load the processed data from Week 1
print("=== Loading Week 1 Data ===")
try:
    traffic_data = pd.read_csv('austin_traffic_processed.csv')
    traffic_data['Date'] = pd.to_datetime(traffic_data['Published_Date'])
    traffic_data['Year'] = traffic_data['Date'].dt.year
    traffic_data['Month'] = traffic_data['Date'].dt.month
    traffic_data['Hour'] = traffic_data['Date'].dt.hour
    print("Successfully loaded Week 1 processed data!")
except:
    print("Creating sample data for demonstration...")
    # Extended sample data for Week 2 analysis
    sample_data = {
        'Published_Date': [
            '2019-03-15 08:30:00', '2019-03-15 17:45:00', '2019-06-20 12:15:00', '2019-09-10 14:30:00',
            '2019-11-05 16:00:00', '2019-12-20 09:15:00', '2019-07-04 11:30:00', '2019-08-15 13:45:00',
            '2020-03-15 08:30:00', '2020-03-15 17:45:00', '2020-06-20 12:15:00', '2020-04-01 10:00:00', 
            '2020-04-01 14:30:00', '2020-04-15 09:15:00', '2020-07-04 11:30:00', '2020-12-25 15:45:00',
            '2021-03-15 08:30:00', '2021-03-15 17:45:00', '2021-06-20 12:15:00', '2021-09-10 14:30:00',
            '2021-07-04 11:30:00', '2021-12-25 15:45:00', '2021-08-15 13:45:00', '2021-11-05 16:00:00'
        ],
        'Issue_Reported': [
            'Vehicle Stalled', 'Traffic Collision', 'Signal Malfunction', 'Vehicle Stalled',
            'Traffic Collision', 'Signal Malfunction', 'Vehicle Stalled', 'Traffic Collision',
            'Vehicle Stalled', 'Traffic Collision', 'Signal Malfunction', 'Traffic Collision', 
            'Vehicle Stalled', 'Traffic Collision', 'Signal Malfunction', 'Vehicle Stalled',
            'Vehicle Stalled', 'Traffic Collision', 'Signal Malfunction', 'Vehicle Stalled',
            'Traffic Collision', 'Signal Malfunction', 'Vehicle Stalled', 'Traffic Collision'
        ],
        'Location': [
            'IH 35 @ Riverside', 'Mopac @ Barton Springs', 'Lamar @ MLK', 'IH 35 @ 6th St',
            'Mopac @ Cesar Chavez', 'Lamar @ Airport', 'IH 35 @ MLK', 'Mopac @ Lake Austin',
            'IH 35 @ Riverside', 'Mopac @ Barton Springs', 'Lamar @ MLK', 'IH 35 @ 6th St',
            'Mopac @ Cesar Chavez', 'IH 35 @ MLK', 'Lamar @ Airport', 'Mopac @ Lake Austin',
            'IH 35 @ Riverside', 'Mopac @ Barton Springs', 'Lamar @ MLK', 'IH 35 @ 6th St',
            'Mopac @ Cesar Chavez', 'Lamar @ Airport', 'IH 35 @ MLK', 'Mopac @ Lake Austin'
        ],
        'Incident_Status': ['Cleared'] * 24
    }
    
    traffic_data = pd.DataFrame(sample_data)
    traffic_data['Date'] = pd.to_datetime(traffic_data['Published_Date'])
    traffic_data['Year'] = traffic_data['Date'].dt.year
    traffic_data['Month'] = traffic_data['Date'].dt.month
    traffic_data['Hour'] = traffic_data['Date'].dt.hour

# =============================================================================
# SESSION 3 (50 min): "Automating Analysis with Loops"
# Topics: For Loops, Histograms, Automated Analysis Across Multiple Years
# =============================================================================

print("\n\n=== SESSION 3: Automating Analysis with Loops ===")

# TOPIC: Why do we need loops? (Natural motivation)
print("\n--- The Problem: Analyzing Multiple Years Manually is Tedious ---")
print("In Week 1, we manually analyzed 2019, 2020, and 2021...")
print("What if we had 10 years of data? Or wanted to analyze every location?")
print("SOLUTION: Use loops to automate repetitive analysis!")

# TOPIC: Basic For Loop Concept
print("\n--- Understanding For Loops Through Traffic Analysis ---")

# Simple loop to understand the concept
years_to_analyze = [2019, 2020, 2021]
print("Years we want to analyze:", years_to_analyze)

print("\nUsing a for loop to process each year:")
for year in years_to_analyze:
    year_data = traffic_data[traffic_data['Year'] == year]
    incident_count = len(year_data)
    print(f"Year {year}: {incident_count} incidents")

# TOPIC: For loops with more complex analysis
print("\n--- Automated Incident Analysis by Year ---")

# Dictionary to store results (students learn data organization)
yearly_analysis = {}

for year in years_to_analyze:
    print(f"\nAnalyzing {year}...")
    
    # Filter data for this year
    year_data = traffic_data[traffic_data['Year'] == year]
    
    # Calculate various statistics
    total_incidents = len(year_data)
    
    # Most common incident type
    most_common_incident = year_data['Issue_Reported'].value_counts().index[0] if len(year_data) > 0 else "None"
    
    # Most problematic location
    most_problematic_location = year_data['Location'].value_counts().index[0] if len(year_data) > 0 else "None"
    
    # Store results
    yearly_analysis[year] = {
        'total_incidents': total_incidents,
        'most_common_incident': most_common_incident,
        'most_problematic_location': most_problematic_location
    }
    
    print(f"  Total incidents: {total_incidents}")
    print(f"  Most common incident: {most_common_incident}")
    print(f"  Most problematic location: {most_problematic_location}")

# TOPIC: Creating Summary Tables from Loop Results
print("\n--- Creating Summary Table from Our Analysis ---")

# Convert our analysis to a DataFrame for better visualization
summary_df = pd.DataFrame(yearly_analysis).transpose()
print("Summary of our automated analysis:")
print(summary_df)

# TOPIC: For loops with location analysis
print("\n--- Analyzing Each Austin Location Automatically ---")

# Get unique locations
unique_locations = traffic_data['Location'].unique()
print(f"Found {len(unique_locations)} unique Austin locations:")

location_analysis = {}

for location in unique_locations:
    print(f"\nAnalyzing incidents at: {location}")
    
    # Filter data for this location
    location_data = traffic_data[traffic_data['Location'] == location]
    
    # Analyze by year for this location
    incidents_by_year = {}
    for year in years_to_analyze:
        year_location_data = location_data[location_data['Year'] == year]
        incidents_by_year[year] = len(year_location_data)
    
    location_analysis[location] = incidents_by_year
    
    # Show the trend for this location
    print(f"  2019: {incidents_by_year[2019]} incidents")
    print(f"  2020: {incidents_by_year[2020]} incidents") 
    print(f"  2021: {incidents_by_year[2021]} incidents")
    
    # Calculate pandemic change
    if incidents_by_year[2019] > 0:
        pandemic_change = ((incidents_by_year[2020] - incidents_by_year[2019]) / incidents_by_year[2019]) * 100
        print(f"  Pandemic change: {pandemic_change:.1f}%")

# TOPIC: Histograms to show distributions
print("\n--- Using Histograms to Understand Incident Patterns ---")

# Create histograms for different aspects of the data
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Austin Traffic Incident Distributions: Understanding the Data Story', fontsize=16)

# Histogram 1: Incidents by hour of day
axes[0, 0].hist(traffic_data['Hour'], bins=24, alpha=0.7, color='skyblue', edgecolor='black')
axes[0, 0].set_title('When Do Traffic Incidents Happen?')
axes[0, 0].set_xlabel('Hour of Day (24-hour format)')
axes[0, 0].set_ylabel('Number of Incidents')
axes[0, 0].set_xticks(range(0, 24, 2))

# Histogram 2: Incidents by year 
yearly_counts = [len(traffic_data[traffic_data['Year'] == year]) for year in years_to_analyze]
axes[0, 1].bar(years_to_analyze, yearly_counts, color=['blue', 'red', 'green'], alpha = 0.7)
axes[0, 1].set_title('Total Incidents by Year: Pandemic Impact')
axes[0, 1].set_xlabel('Year')
axes[0, 1].set_ylabel('Number of Incidents')

# Add value labels on bars
for i, count in enumerate(yearly_counts):
    axes[0, 1].text(years_to_analyze[i], count + 0.1, str(count), ha='center')

# Histogram 3: Distribution of incident types
incident_type_counts = traffic_data['Issue_Reported'].value_counts()
axes[1, 0].bar(range(len(incident_type_counts)), incident_type_counts.values, color='orange', alpha=0.7)
axes[1, 0].set_title('Types of Traffic Incidents in Austin')
axes[1, 0].set_xlabel('Incident Type')
axes[1, 0].set_ylabel('Number of Incidents')
axes[1, 0].set_xticks(range(len(incident_type_counts)))
axes[1, 0].set_xticklabels(incident_type_counts.index, rotation=45, ha='right')

# Histogram 4: Incidents by month (seasonal patterns)
axes[1, 1].hist(traffic_data['Month'], bins=12, alpha=0.7, color='lightgreen', edgecolor='black')
axes[1, 1].set_title('Seasonal Patterns: Incidents by Month')
axes[1, 1].set_xlabel('Month')
axes[1, 1].set_ylabel('Number of Incidents') 
axes[1, 1].set_xticks(range(1, 13))

plt.tight_layout()
plt.show()

# TOPIC: Advanced loop analysis - comparing pre vs during pandemic
print("\n--- Advanced Analysis: Pre-Pandemic vs Pandemic Comparison ---")

# Define time periods
pre_pandemic_years = [2019]
pandemic_years = [2020]
post_pandemic_years = [2021]

print("Comparing incident patterns across pandemic phases...")

for location in unique_locations[:3]:  # Analyze top 3 locations for time
    print(f"\n{location}:")
    
    location_data = traffic_data[traffic_data['Location'] == location]
    
    # Calculate averages for each period
    pre_pandemic_avg = len(location_data[location_data['Year'].isin(pre_pandemic_years)]) / len(pre_pandemic_years)
    pandemic_avg = len(location_data[location_data['Year'].isin(pandemic_years)]) / len(pandemic_years)
    post_pandemic_avg = len(location_data[location_data['Year'].isin(post_pandemic_years)]) / len(post_pandemic_years)
    
    print(f"  Pre-pandemic average: {pre_pandemic_avg:.1f} incidents/year")
    print(f"  Pandemic average: {pandemic_avg:.1f} incidents/year")
    print(f"  Post-pandemic average: {post_pandemic_avg:.1f} incidents/year")
    
    # Identify the trend
    if pandemic_avg < pre_pandemic_avg:
        trend = "DECREASED during pandemic"
    elif pandemic_avg > pre_pandemic_avg:
        trend = "INCREASED during pandemic"
    else:
        trend = "NO CHANGE during pandemic"
    
    print(f"  Trend: Incidents {trend}")

print("\n=== END SESSION 3 ===")
print("Next session: We'll map these locations and create Austin's traffic story!")

# =============================================================================
# SESSION 4 (50 min): "Mapping Austin's Traffic Story"
# Topics: Geographic Analysis, Advanced Plotting, Story Synthesis
# =============================================================================

print("\n\n=== SESSION 4: Mapping Austin's Traffic Story ===")

# TOPIC: Creating geographic insights from location data
print("\n--- Understanding Austin's Traffic Geography ---")

# Analyze which areas of Austin are most affected
print("Let's identify Austin's traffic hotspots...")

# Count incidents by location and sort
location_incident_counts = traffic_data['Location'].value_counts()
print("\nAustin's Top Traffic Incident Locations:")
for i, (location, count) in enumerate(location_incident_counts.head().items()):
    print(f"{i+1}. {location}: {count} incidents")

# TOPIC: Advanced plotting - Creating Austin's traffic story map
print("\n--- Creating Austin's Traffic Incident Heat Map ---")

# Simulate coordinates for Austin locations (in real class, use real coordinates)
austin_coordinates = {
    'IH 35 @ Riverside': (30.2500, -97.7300),
    'Mopac @ Barton Springs': (30.2640, -97.7710),
    'Lamar @ MLK': (30.2850, -97.7560),
    'IH 35 @ 6th St': (30.2672, -97.7320),
    'Mopac @ Cesar Chavez': (30.2672, -97.7710),
    'Lamar @ Airport': (30.3000, -97.7400),
    'IH 35 @ MLK': (30.2850, -97.7320),
    'Mopac @ Lake Austin': (30.3200, -97.7800)
}

# Create a comprehensive traffic analysis visualization
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Austin Traffic Pandemic Story: Complete Analysis', fontsize=18, fontweight='bold')

# Plot 1: Location hotspot analysis
location_counts = traffic_data['Location'].value_counts().head(6)
axes[0, 0].barh(range(len(location_counts)), location_counts.values, color='red', alpha=0.7)
axes[0, 0].set_yticks(range(len(location_counts)))
axes[0, 0].set_yticklabels([loc.replace(' @ ', '\n@\n') for loc in location_counts.index], fontsize=8)
axes[0, 0].set_title('Austin Traffic Hotspots\n(Total Incidents 2019-2021)', fontweight='bold')
axes[0, 0].set_xlabel('Number of Incidents')

# Add value labels
for i, v in enumerate(location_counts.values):
    axes[0, 0].text(v + 0.1, i, str(v), va='center')

# Plot 2: Pandemic impact by location
pandemic_impact = {}
for location in location_counts.index:
    location_data = traffic_data[traffic_data['Location'] == location]
    pre_2020 = len(location_data[location_data['Year'] == 2019])
    during_2020 = len(location_data[location_data['Year'] == 2020])
    
    if pre_2020 > 0:
        change_percent = ((during_2020 - pre_2020) / pre_2020) * 100
    else:
        change_percent = 0
    pandemic_impact[location] = change_percent

impact_locations = list(pandemic_impact.keys())
impact_values = list(pandemic_impact.values())
colors = ['green' if x < 0 else 'red' if x > 0 else 'gray' for x in impact_values]

axes[0, 1].barh(range(len(impact_locations)), impact_values, color=colors, alpha=0.7)
axes[0, 1].set_yticks(range(len(impact_locations)))
axes[0, 1].set_yticklabels([loc.replace(' @ ', '\n@\n') for loc in impact_locations], fontsize=8)
axes[0, 1].set_title('Pandemic Impact by Location\n(% Change 2019→2020)', fontweight='bold')
axes[0, 1].set_xlabel('Percent Change in Incidents')
axes[0, 1].axvline(x=0, color='black', linestyle='--', alpha=0.5)

# Add value labels
for i, v in enumerate(impact_values):
    axes[0, 1].text(v + (1 if v >= 0 else -1), i, f'{v:.0f}%', va='center', ha='left' if v >= 0 else 'right')

# Plot 3: Temporal analysis - incidents by hour across years
hourly_data = []
hour_labels = []
year_colors = ['blue', 'red', 'green']
year_labels = ['2019 (Pre)', '2020 (Pandemic)', '2021 (Post)']

for i, year in enumerate([2019, 2020, 2021]):
    year_data = traffic_data[traffic_data['Year'] == year]
    hourly_counts = year_data['Hour'].value_counts().reindex(range(24), fill_value=0)
    axes[1, 0].plot(hourly_counts.index, hourly_counts.values, 
                   marker='o', linewidth=2, color=year_colors[i], label=year_labels[i])

axes[1, 0].set_title('Daily Traffic Incident Patterns\n(How Pandemic Changed Rush Hour)', fontweight='bold')
axes[1, 0].set_xlabel('Hour of Day')
axes[1, 0].set_ylabel('Number of Incidents')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].set_xticks(range(0, 24, 2))

# Plot 4: Monthly patterns to show seasonal effects
monthly_comparison = pd.DataFrame()
for year in [2019, 2020, 2021]:
    year_data = traffic_data[traffic_data['Year'] == year]
    monthly_counts = year_data['Month'].value_counts().reindex(range(1, 13), fill_value=0)
    monthly_comparison[str(year)] = monthly_counts.values

monthly_comparison.plot(kind='bar', ax=axes[1, 1], color=['blue', 'red', 'green'], alpha=0.7)
axes[1, 1].set_title('Seasonal Patterns: Monthly Incidents\n(Weather vs Pandemic Effects)', fontweight='bold')
axes[1, 1].set_xlabel('Month')
axes[1, 1].set_ylabel('Number of Incidents')
axes[1, 1].legend(['2019 (Pre)', '2020 (Pandemic)', '2021 (Post)'])
axes[1, 1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)

plt.tight_layout()
plt.show()

# TOPIC: Synthesizing the story - what does the data tell us?
print("\n--- Synthesizing Austin's Traffic Pandemic Story ---")

# Calculate key insights
total_2019 = len(traffic_data[traffic_data['Year'] == 2019])
total_2020 = len(traffic_data[traffic_data['Year'] == 2020])
total_2021 = len(traffic_data[traffic_data['Year'] == 2021])

overall_pandemic_change = ((total_2020 - total_2019) / total_2019) * 100 if total_2019 > 0 else 0
recovery_change = ((total_2021 - total_2020) / total_2020) * 100 if total_2020 > 0 else 0

print(f"\n=== KEY FINDINGS FROM AUSTIN TRAFFIC DATA ===")
print(f"📊 Overall pandemic impact: {overall_pandemic_change:.1f}% change in incidents (2019→2020)")
print(f"📈 Recovery pattern: {recovery_change:.1f}% change (2020→2021)")

# Identify most impacted locations
most_impacted_location = max(pandemic_impact.items(), key=lambda x: abs(x[1]))
print(f"🎯 Most impacted location: {most_impacted_location[0]} ({most_impacted_location[1]:.1f}% change)")

# Find peak incident hours
peak_hour_2019 = traffic_data[traffic_data['Year'] == 2019]['Hour'].mode().iloc[0] if len(traffic_data[traffic_data['Year'] == 2019]) > 0 else "N/A"
peak_hour_2020 = traffic_data[traffic_data['Year'] == 2020]['Hour'].mode().iloc[0] if len(traffic_data[traffic_data['Year'] == 2020]) > 0 else "N/A"
print(f"⏰ Peak incident hour shifted from {peak_hour_2019}:00 (2019) to {peak_hour_2020}:00 (2020)")

# Most common incident type
most_common_2019 = traffic_data[traffic_data['Year'] == 2019]['Issue_Reported'].mode().iloc[0] if len(traffic_data[traffic_data['Year'] == 2019]) > 0 else "N/A"
most_common_2020 = traffic_data[traffic_data['Year'] == 2020]['Issue_Reported'].mode().iloc[0] if len(traffic_data[traffic_data['Year'] == 2020]) > 0 else "N/A"
print(f"🚗 Incident type patterns: {most_common_2019} (2019) vs {most_common_2020} (2020)")

# TOPIC: Validation against reality
print(f"\n--- How to Validate Our Findings ---")
print("🔍 VALIDATION CHECKLIST for Austin Traffic Story:")
print("1. Drive to identified hotspots - do they still have heavy traffic/incidents?")
print("2. Check Austin DOT reports - do official statistics match our findings?")
print("3. Interview Austin residents - do they remember these changes?")
print("4. Compare with other cities - was this pattern unique to Austin?")
print("5. Consider external factors - construction, events, policy changes?")

# TOPIC: Engineering implications
print(f"\n--- Engineering Solutions Based on Data ---")
print("🏗️  RECOMMENDED ENGINEERING ACTIONS:")

# Suggest solutions based on findings
if overall_pandemic_change > 10:
    print("• High incident increase detected - recommend enhanced traffic signal timing")
elif overall_pandemic_change < -10:
    print("• Significant incident decrease - opportunity to optimize signal timing for efficiency")
else:
    print("• Stable incident patterns - focus on preventing future increases")

print("• Target hotspot locations for infrastructure improvements")
print("• Adjust emergency response protocols based on new temporal patterns")
print("• Consider adaptive traffic management systems for future disruptions")

# TOPIC: What questions does this raise for future study?
print(f"\n--- Questions for Future Investigation ---")
print("❓ FOLLOW-UP RESEARCH QUESTIONS:")
print("1. How do weather patterns interact with traffic incidents?")
print("2. What role did remote work policies play in traffic changes?")
print("3. How did delivery/rideshare traffic change the incident patterns?")
print("4. Which infrastructure improvements would be most cost-effective?")
print("5. How can Austin prepare for future traffic disruptions?")

# Save comprehensive analysis results
print(f"\n--- Saving Analysis Results ---")
analysis_summary = {
    'total_incidents_by_year': {2019: total_2019, 2020: total_2020, 2021: total_2021},
    'pandemic_impact_percent': overall_pandemic_change,
    'recovery_pattern_percent': recovery_change,
    'most_impacted_location': most_impacted_location,
    'hotspot_locations': location_incident_counts.head().to_dict(),
    'pandemic_impact_by_location': pandemic_impact
}

# Convert to DataFrame for easy export
summary_for_export = pd.DataFrame({
    'Metric': ['Total 2019', 'Total 2020', 'Total 2021', 'Pandemic Impact %', 'Recovery %'],
    'Value': [total_2019, total_2020, total_2021, f"{overall_pandemic_change:.1f}%", f"{recovery_change:.1f}%"]
})

summary_for_export.to_csv('austin_traffic_analysis_summary.csv', index=False)
print("Analysis summary saved to 'austin_traffic_analysis_summary.csv'")

print("\n=== FINAL REFLECTION ===")
print("🎯 What we learned about computational thinking:")
print("• Variables help us store and track important information")
print("• Conditionals let us filter data to focus on specific time periods")
print("• Loops automate repetitive analysis across multiple years/locations")
print("• Visualizations reveal patterns that numbers alone can't show")
print("• Real data tells complex stories that require careful interpretation")

print("\n🏆 What we learned about Austin traffic:")
print("• Pandemic effects varied by location and time of day")
print("• Traffic patterns are more complex than simple 'increase/decrease'") 
print("• Data analysis can guide engineering decisions and policy")
print("• Validation against reality is essential for trustworthy conclusions")

print("\n🔬 What we learned about being an engineer:")
print("• Ask good questions before diving into data")
print("• Use computational tools to handle large, complex datasets")
print("• Always validate findings against observable reality")
print("• Communicate results clearly to support decision-making")
print("• Consider broader implications of technical findings")

print("\n=== END MODULE 1: AUSTIN TRAFFIC PANDEMIC STORY ===")
print("Students are now ready to tackle their next world modeling challenge!")
