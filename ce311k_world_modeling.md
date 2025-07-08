# CE 311K: World Modeling with Computational Methods
*Redesigned for the LLM Era*

## Course Philosophy

Students learn to **think computationally about real-world systems** by building models they can observe, test, and validate. Each 2-week module focuses on a different type of system behavior, naturally introducing the algorithms and numerical methods needed to model that behavior.

## The Modeling Pipeline (Applied to Each System)

**Week 1**: Observe → Abstract → Model  
**Week 2**: Simulate → Validate → Iterate

---

## Module 1: Austin Traffic Data Analysis (Weeks 1-2)
**System Type**: Data Processing and Statistical Analysis

**Observable Behavior**: Students analyze real Austin traffic count data
- Hourly traffic volume patterns
- Peak hour identification and duration
- Day-of-week and seasonal variations
- Speed vs. volume relationships

**Natural Algorithms/Methods**:
- **Variables and data types** (storing traffic counts, times, speeds)
- **Lists and arrays** (organizing time series data)
- **Control statements** (if/else for peak detection, loops for data processing)
- **Basic statistics** (mean, median, standard deviation of traffic volumes)

**Week 1**: Load and explore traffic data, identify patterns with basic statistics
**Week 2**: Create traffic classification system (peak/off-peak) and visualize trends

**Validation**: Compare findings to published Austin traffic studies and DOT reports

---

## Module 2: Parking Lot with Traffic Control (Weeks 3-4)
**System Type**: Discrete Event System with Control Logic

**Observable Behavior**: Students observe campus parking lots with entrance signals
- Car arrival patterns and entrance queuing
- Traffic light control of parking lot access
- Search behavior for available spots inside lot
- Peak vs. off-peak utilization and control strategies

**Natural Algorithms/Methods**:
- **Queue data structures** (entrance lines, internal circulation)
- **Finite state machines** (traffic light states and parking lot status)
- **Random number generation** (simulating arrival times)
- **Control logic** (adaptive signal timing based on lot occupancy)

**Week 3**: Build parking lot simulator with traffic light controlling entrance
**Week 4**: Add adaptive control (signal changes based on lot capacity), multiple entrances

**Validation**: Compare simulation results to actual parking lot observations and signal timing

---

## Module 3: Building Energy Systems (Weeks 5-6)
**System Type**: Continuous Dynamic System with Control

**Observable Behavior**: Students monitor campus building energy usage
- Temperature variations throughout day and seasons
- HVAC system cycling and energy consumption
- Occupancy effects on heating/cooling demand
- Weather impact on energy use patterns

**Natural Algorithms/Methods**:
- **Differential equations** (heat transfer and thermal dynamics)
- **Numerical integration** (energy consumption over time)
- **Curve fitting** (temperature response curves)
- **Time series analysis** (daily/seasonal patterns)

**Week 5**: Model heat flow and temperature dynamics in buildings
**Week 6**: Add HVAC control systems, occupancy effects, and optimization

**Validation**: Compare model predictions to actual building energy data

---

## Module 4: Creek Flow Dynamics (Weeks 7-8)
**System Type**: Open Channel Hydraulics System

**Observable Behavior**: Students measure Waller Creek flow near campus
- Water velocity at different depths and widths
- Flow rate changes with rainfall
- Sediment transport during high flow events
- Channel geometry effects on flow patterns

**Natural Algorithms/Methods**:
- **Manning's equation** (flow velocity calculations)
- **Numerical integration** (flow rate from velocity profiles)
- **Regression analysis** (stage-discharge relationships)
- **Interpolation** (flow between measurement points)

**Week 7**: Model basic open channel flow with Manning's equation
**Week 8**: Add variable geometry, rainfall effects, and sediment transport

**Validation**: Compare model predictions to actual flow measurements and USGS gauge data

---

## Module 5: Structural Analysis - Beams and Bridges (Weeks 9-10)
**System Type**: Static and Dynamic Structural Response

**Observable Behavior**: Students analyze campus pedestrian bridges and building beams
- Deflection under different load conditions (static analysis)
- Vibration response to walking loads (dynamic analysis)
- Stress distribution in structural members
- Load transfer through connections and supports

**Natural Algorithms/Methods**:
- **Matrix operations** (stiffness method for structures)
- **Linear algebra** (solving equilibrium equations)
- **Numerical integration** (moment and deflection calculations)
- **Eigenvalue analysis** (natural frequency and vibration modes)

**Week 9**: Model basic beam deflection and truss analysis with static loads
**Week 10**: Add dynamic loading, vibration analysis, and multi-span structures

**Validation**: Compare to structural design calculations and actual deflection measurements

---

## Module 6: Water Distribution Network (Weeks 11-12)
**System Type**: Flow Network with Pressure Constraints

**Observable Behavior**: Students examine campus water distribution system
- Water pressure at different locations and elevations
- Flow rates through pipes of various sizes
- Peak demand periods and system response
- System behavior during maintenance or outages

**Natural Algorithms/Methods**:
- **Network flow algorithms** (Hardy Cross method, Newton-Raphson)
- **Graph theory** (pipe networks as graphs)
- **Numerical methods** (solving nonlinear pressure equations)
- **Constraint satisfaction** (pressure and flow limits)

**Week 11**: Model basic pipe network with flow and pressure calculations
**Week 12**: Add demand variations, pump operations, and failure scenarios

**Validation**: Test model against campus facilities water system data

---

## Module 7: Groundwater Seepage Flow (Weeks 13-14)
**System Type**: Steady-State Flow Through Porous Media

**Observable Behavior**: Students examine seepage around campus retaining walls/basements
- Water table levels at different locations
- Seepage rates through soil and rock
- Flow patterns around underground structures
- Pore water pressure distributions

**Natural Algorithms/Methods**:
- **Finite difference methods** (Laplace equation for flow nets)
- **Partial differential equations** (Darcy's law in 2D)
- **Iterative solvers** (Gauss-Seidel, successive over-relaxation)
- **Boundary conditions** (specified head vs. flow boundaries)

**Week 13**: Model basic 2D seepage using finite difference grid
**Week 14**: Add complex boundaries, layered soils, and anisotropic permeability

**Validation**: Compare flow patterns to hand-drawn flow nets and piezometer data

---

## Module 8: Machine Learning for Infrastructure Assessment (Weeks 15-16)
**System Type**: Pattern Recognition and Predictive Modeling

**Observable Behavior**: Students analyze patterns in infrastructure data
- Building maintenance records and failure patterns
- Traffic flow prediction from historical data
- Energy consumption forecasting
- Structural health monitoring sensor data

**Natural Algorithms/Methods**:
- **Machine learning basics** (supervised vs. unsupervised learning)
- **Regression analysis** (predicting continuous outcomes)
- **Classification algorithms** (decision trees, logistic regression)
- **Feature engineering** (selecting relevant data characteristics)

**Week 15**: Build basic prediction models for infrastructure performance
**Week 16**: Add classification for maintenance prioritization and anomaly detection

**Validation**: Test predictions against actual infrastructure performance data

---

## Module 9: Computer Vision for Structural Damage Assessment (Weeks 17-18)
**System Type**: Image Analysis and Automated Inspection

**Observable Behavior**: Students photograph and analyze campus infrastructure
- Crack patterns in concrete walls and pavements
- Corrosion on metal structures and railings
- Surface deterioration on building facades
- Deformation in structural members

**Natural Algorithms/Methods**:
- **Convolutional Neural Networks (CNNs)** (image feature detection)
- **Image preprocessing** (filtering, enhancement, segmentation)
- **Computer vision pipelines** (detection → classification → measurement)
- **Transfer learning** (using pre-trained models for damage detection)

**Week 17**: Build basic image classification for damage vs. no-damage
**Week 18**: Add crack measurement, severity assessment, and automated reporting

**Validation**: Compare AI assessments to professional structural inspection reports

---

## Assessment Strategy

### Weekly Deliverables
- **Week 1**: Problem analysis and initial model design
- **Week 2**: Refined model with validation and iteration report

### Skills Progression Matrix
Each module builds computational sophistication:

| Module | Focus | Data Structures | Key Algorithms | Mathematical Methods |
|--------|-------|----------------|----------------|---------------------|
| 1 | Traffic Data | Arrays, Lists | Statistical Analysis | Basic Statistics |
| 2 | Parking + Signals | Queues, State Machines | Discrete Simulation + Control | Probability + Logic |
| 3 | Building Energy | Time Series | Numerical Integration | Differential Equations |
| 4 | Creek Flow | Spatial Data | Interpolation | Manning's Equation |
| 5 | Structures | Matrices | Linear Algebra | Matrix Methods |
| 6 | Water Networks | Graphs | Network Flow | Nonlinear Equations |
| 7 | Seepage | 2D Grids | Finite Differences | Partial Differential Equations |
| 8 | ML Infrastructure | Feature Vectors | Classification/Regression | Statistical Learning |
| 9 | Computer Vision | Image Arrays | Convolutional Neural Networks | Deep Learning |

### Portfolio Assessment
Students maintain a **modeling portfolio** showing:
- Evolution of their computational thinking
- Increasing sophistication in model validation
- Cross-connections between different systems
- Reflection on modeling choices and limitations

### Final Project
Students choose a **new real-world system** and apply the full modeling pipeline, demonstrating mastery of:
- System observation and abstraction
- Appropriate algorithm/method selection
- Implementation with AI assistance
- Rigorous validation methodology
- Clear communication of results and limitations

## Course Outcomes

By the end of this course, students will be able to:
1. **Observe** real-world systems and identify modelable components
2. **Abstract** complex problems into computational representations
3. **Implement** models using appropriate tools and AI assistance
4. **Validate** models against real-world data and observations
5. **Iterate** and improve models based on feedback and new information
6. **Apply** both traditional numerical methods and modern AI techniques to engineering problems
7. **Communicate** modeling decisions and limitations to stakeholders

This progression ensures students encounter the full spectrum of computational thinking - from classical numerical methods to cutting-edge AI applications - while always grounding learning in observable, testable civil engineering phenomena.