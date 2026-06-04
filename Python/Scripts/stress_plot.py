import matplotlib.pyplot as plt

thickness = [2.5, 5, 10, 15]
stress = [825.4, 411.7, 211.5, 145.4]

plt.figure(figsize=(8,5))
plt.plot(thickness, stress, marker='o')

plt.xlabel('Wall Thickness (mm)')
plt.ylabel('Von Mises Stress (MPa)')
plt.title('Effect of Wall Thickness on Stress')

plt.grid(True)

plt.savefig('stress_vs_thickness.png', dpi=300)

plt.show()