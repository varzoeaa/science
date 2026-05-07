# Kinetic Gas Theory Visualizations

This project contains interactive and animated Python simulations that illustrate the core concepts of kinetic gas theory and statistical mechanics. Each script in the `src` folder demonstrates a different physical phenomenon related to the microscopic behavior of gases.

## Contents

- **boltzmann.py**  
  Animates the Boltzmann energy distribution, showing how particle energy distribution changes with temperature.

- **maxwell-boltzmann.py**  
  Animates the Maxwell–Boltzmann speed distribution for gas molecules at different temperatures.

- **kinetic_gas.py**  
  Simulates a 3D box of gas molecules, visualizing their random motion and kinetic energy in real time.

- **collusion.py**  
  Shows a single particle bouncing in a 3D box, counting wall collisions and estimating pressure from momentum transfer.

- **ideal_gas_law.py**  
  Interactive simulation of the ideal gas law (`pV = nRT`), where you can adjust temperature and volume with sliders and observe the effect on pressure and particle motion.

## How to Run

1. **Install dependencies**  
   Make sure you have Python 3 and the following packages:
   - numpy
   - matplotlib

   You can install them with:

    pip install numpy matplotlib

2. **Run a simulation**  
    Open a terminal in the `src` folder and run, for example:

    python boltzmann.py


## Scientific Background

These simulations help visualize how the macroscopic properties of gases (pressure, temperature, volume) arise from the microscopic motion and collisions of molecules.  
- The **Boltzmann** and **Maxwell–Boltzmann** distributions describe how energy and speed are distributed among particles at a given temperature.
- The **kinetic theory** explains pressure as the result of countless collisions of molecules with the walls of a container.
- The **ideal gas law** (`pV = nRT`) connects these microscopic behaviors to the familiar macroscopic gas laws.
