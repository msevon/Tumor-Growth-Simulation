import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tumor_model import TumorModel

# DEFINE SIMULATION PARAMETERS
grid_size = int(input("Enter simulation grid size.\n"))  # grid size (change this for finer/coarser resolution)
num_iterations = int(input("Enter number of iterations.\n"))  # number of simulation iterations

# INITIALIZE TUMOR MODEL:
# input the values for the variables used in creating the tumor model
initial_radius = float(input("What is the current radius of the tumor at the moment (centimeters)?\n"))
print("\nTumor spread is affected by multiple parameters linked to the health of an individual.\nPlease input values for the following parameters.\n\n0: protective factor , 1: risk factor.\n")
genetics = float(input("Genetics:\n"))
signaling = float(input("Signaling:\n"))
angiogenesis = float(input("Angiogenesis:\n"))
immune_response = float(input("Immune Response:\n"))
hormones = float(input("Hormones:\n"))
microenvironment = float(input("Microenvironment:\n"))
nutrition = float(input("Nutrition:\n"))
oxygen = float(input("Oxygen:\n"))
treatment_effectiveness = float(input("Treatment Effectiveness:\n"))
microbiome = float(input("Microbiome:\n"))
age_lifestyle = float(input("Age & Lifestyle:\n"))
inflammation = float(input("Inflammation:\n"))

# create an instance of the TumorModel class with the variable values
tumor_model = TumorModel(initial_radius, genetics, signaling, angiogenesis, immune_response, hormones,
                         microenvironment, nutrition, oxygen, treatment_effectiveness,
                         microbiome, age_lifestyle, inflammation)

# INITIALIZE THE GRID
grid = np.zeros((grid_size, grid_size, grid_size))
# create a 3D mesh grid for visualization
x, y, z = np.meshgrid(np.arange(grid_size), np.arange(grid_size), np.arange(grid_size))
# initialize tumor at the center of the grid
center = grid_size // 2
grid[(x - center) ** 2 + (y - center) ** 2 + (z - center) ** 2 <= tumor_model.initial_radius ** 2] = 1
# create a 3D figure for visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# SIMULATION LOOP
with open("simulation_data.txt", "w") as data_file:
    data_file.write("Iteration;New_Tumor_Cells\n")
    print("\nSimulation starts.")
    for i in range(num_iterations):
        # calculate tumor growth based on the growth rate
        tumor_mask = (grid == 1)
        neighbors = np.roll(tumor_mask, shift=(1, 0, 0), axis=(0, 1, 2)) + \
                    np.roll(tumor_mask, shift=(-1, 0, 0), axis=(0, 1, 2)) + \
                    np.roll(tumor_mask, shift=(0, 1, 0), axis=(0, 1, 2)) + \
                    np.roll(tumor_mask, shift=(0, -1, 0), axis=(0, 1, 2)) + \
                    np.roll(tumor_mask, shift=(0, 0, 1), axis=(0, 1, 2)) + \
                    np.roll(tumor_mask, shift=(0, 0, -1), axis=(0, 1, 2))
        # apply the tumor growth rate to control the spread
        new_tumor_cells = (neighbors >= 1) & (grid == 0) & (np.random.rand(*grid.shape) < tumor_model.growth_rate)
        grid[new_tumor_cells] = 1
        # write simulation data to the file
        num_new_tumor_cells = np.count_nonzero(new_tumor_cells)
        data_file.write(f"{i + 1};{num_new_tumor_cells}\n")
        # visualize tumor growth
        ax.cla()
        ax.scatter(x[tumor_mask], y[tumor_mask], z[tumor_mask], c='red', marker='o', s=5)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Tumor Growth\nIteration {i+1}/{num_iterations}\n(New Tumor Cells: {num_new_tumor_cells})')
        plt.pause(0.2)
# END SIMULATION
plt.show()
print("\nSimulation stops.")
