# Module 1: Telling Austin's Pandemic Traffic Story Through Data

## Module Overview
**Duration:** 2 weeks (4 x 50-minute sessions)
**Story + System + Concepts + Data Formula**

### Story Setup
Austin experienced one of the most dramatic traffic changes in its history during the 2020 pandemic - but not in the way you might expect. While most assumed traffic simply disappeared during lockdowns, the data reveals a more complex story: certain types of incidents actually increased, traffic patterns shifted to different times of day, and some areas became more dangerous while others became safer. Students will investigate this counterintuitive phenomenon using real traffic incident data.

### Observable System  
Students can validate findings by observing current Austin traffic patterns at different times/locations and comparing to historical norms. They can check if pandemic-era changes persist in 2025.

### Python Concepts (Natural Integration)
- **Variables**: Store incident counts, dates, locations (emerge from need to track different data points)
- **Data Types**: Strings for incident types, integers for counts, datetime for temporal analysis
- **Conditionals**: Filter data by year (2019 vs 2020 vs 2021) to isolate pandemic effects
- **Pandas DataFrames**: Handle large CSV traffic dataset (natural need for structured data analysis)
- **Loops**: Process multiple years of data, calculate statistics across time periods
- **Plotting**: Visualize incident patterns to reveal the story in the data

### Real Data Source
Austin Open Data: Real-Time Traffic Incident Reports
- **URL**: https://data.austintexas.gov/Transportation-and-Mobility/Real-Time-Traffic-Incident-Reports/dx9v-zd7x
- **Format**: CSV with columns for date, time, location, incident type, status
- **Size**: 500K+ records from 2018-present
- **API Access**: Available through Socrata Open Data API

### Assessment Focus
Students explain their hypothesis about pandemic traffic, validate findings against observable Austin traffic patterns, and articulate what the data story reveals about urban transportation resilience.

---

## Week 1 Sessions

### Session 1 (50 min): "What Really Happened to Austin Traffic?"
**Learning Objectives:**
- Load and explore real Austin traffic data
- Understand variables and data types through traffic metrics
- Use basic pandas operations to examine data structure

**Pre-Session Videos (Students Watch):**
- "Python Variables and Data Types" (10 min) - *Charlie Dey, TACC*
- "Introduction to Pandas" (15 min) - *Charlie Dey, TACC*
- "What is a CSV file?" (5 min) - *Charlie Dey, TACC*

### Session 2 (50 min): "Filtering the Pandemic Signal"  
**Learning Objectives:**
- Use conditional statements to filter data by year
- Compare pre-pandemic vs pandemic traffic patterns
- Create basic visualizations to see trends

**Pre-Session Videos:**
- "Python Conditionals and Filtering" (12 min) - *Charlie Dey, TACC*
- "Basic Plotting with Matplotlib" (10 min) - *Charlie Dey, TACC*

---

## Week 2 Sessions

### Session 3 (50 min): "Automating Analysis with Loops"
**Learning Objectives:**
- Use for loops to analyze multiple years of data
- Create histograms to show incident distributions
- Identify patterns across different time periods

### Session 4 (50 min): "Mapping Austin's Traffic Story"
**Learning Objectives:**
- Plot incident locations to reveal geographic patterns
- Synthesize findings into a coherent traffic story
- Validate results against observable Austin traffic

---

## Validation Strategy
Students will:
1. Compare their findings to published Austin DOT traffic reports
2. Observe current traffic patterns at identified high-incident locations
3. Interview Austin residents about their pandemic traffic experiences
4. Present findings to local transportation professionals for feedback

## Assessment Rubric
**Does this make engineering sense?** (Not "does the code work?")
- Can students explain why certain areas/times showed different pandemic effects?
- Do their conclusions align with observable traffic patterns?
- Can they articulate limitations of incident data vs. actual traffic volume?
- Do they propose engineering solutions based on their findings?