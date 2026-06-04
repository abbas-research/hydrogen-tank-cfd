# Hydrogen Tank Thickness Optimization Using ANSYS and Python



## Project Overview



This project investigates the effect of wall thickness on the structural performance of a simplified hydrogen storage vessel subjected to an internal pressure of 35 MPa.



The study was conducted using ANSYS Static Structural analysis and Python-based data visualization.



## Software Used



- ANSYS Workbench

- ANSYS DesignModeler

- ANSYS Mechanical

- Python 3.14

- Matplotlib

- Microsoft Excel



## Geometry



- Cylindrical pressure vessel with domed end cap

- Outer diameter: 125 mm

- Length: 450 mm



## Thickness Cases Studied



- 2.5 mm

- 5 mm

- 10 mm

- 15 mm



## Results



| Thickness (mm) | Stress (MPa) | Deformation (mm) | Factor of Safety |

| -------------- | ------------ | ---------------- | ---------------- |

| 2.5            | 825.4        | 0.5780           | 0.303            |

| 5              | 411.7        | 0.2730           | 0.607            |

| 10             | 211.5        | 0.1219           | 1.182            |

| 15             | 145.4        | 0.0725           | 1.719            |



## Key Findings



- Increasing wall thickness reduced stress levels.

- Increasing wall thickness reduced total deformation.

- Factor of safety increased significantly with thickness.

- The 10 mm configuration was the thinnest design achieving a factor of safety greater than 1.



## Python Analysis



Python scripts were developed to generate:



- Stress vs Thickness

- Deformation vs Thickness

- Factor of Safety vs Thickness



## Conclusion



The study demonstrated that increasing wall thickness reduced stress and deformation while increasing factor of safety. A wall thickness of approximately 10 mm was identified as the minimum acceptable configuration for the selected material under 35 MPa internal pressure.


