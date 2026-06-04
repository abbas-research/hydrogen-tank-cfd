import matplotlib.pyplot as plt

thickness = [2.5, 5, 10, 15]
deformation = [0.578, 0.273, 0.1219, 0.0725]

plt.figure(figsize=(8,5))
plt.plot(thickness, deformation, marker='o')

plt.xlabel('Wall Thickness (mm)')
plt.ylabel('Maximum Deformation (mm)')
plt.title('Effect of Wall Thickness on Deformation')

plt.grid(True)

plt.savefig('deformation_vs_thickness.png', dpi=300)

plt.show()