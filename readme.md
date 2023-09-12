Tumor Growth Simulation



Overview


This Python program simulates tumor growth in a 3D environment. The simulation takes into account various parameters that affect tumor spread and growth. It provides insights into how the tumor evolves over time based on these parameters.



Parameters


Tumor spread is affected by multiple parameters linked to the health of an individual. These parameters include:
    
    -Genetics: Genetic factors that influence susceptibility to tumor growth.
    
    -Signaling: Signaling pathways that affect tumor cell proliferation.
    
    -Angiogenesis: The formation of new blood vessels to supply nutrients to the tumor.
   
    -Immune Response: The body's immune system's ability to recognize and combat the tumor.
   
    -Hormones: Hormonal factors that can promote or inhibit tumor growth.
    
    -Microenvironment: The local tissue environment that can support or hinder tumor development.
    
    -Nutrition: The availability of nutrients necessary for tumor cell survival.
   
    -Oxygen: The oxygen supply, which can impact the tumor's ability to grow.
   
    -Treatment Effectiveness: The effectiveness of medical treatments on the tumor.
    
    -Microbiome: The composition of the body's microbiome and its impact on tumor growth.
    
    -Age & Lifestyle: Factors related to an individual's age and lifestyle choices.
    
    -Inflammation: The level of inflammation in the body, which can influence tumor progression.


Usage


    1. Run the program by executing the main.py file.
   
    2. Input the simulation parameters, including the grid size, initial tumor radius, and values for the parameters listed above.
    
    3. The program will perform the simulation and visualize tumor growth in a 3D environment.
   
    4. Simulation data, including the iteration, current tumor radius (in centimeters), and the number of new tumor cells, will be saved to a file named simulation_data.txt.


Bash example


~python main.py


Dependencies


This program uses NumPy and Matplotlib for numerical computations and visualization.

The tumor_model.py file contains the TumorModel class, which includes the tumor growth logic.
