import matplotlib.pyplot as plt

thickness = [2.5, 5, 10, 15]
principal_stress = [903.4, 435.3, 215.5, 153.9]

plt.figure(figsize=(8,5))
plt.plot(thickness, principal_stress, marker='o')

plt.xlabel('Wall Thickness (mm)')
plt.ylabel('Maximum Principal Stress (MPa)')
plt.title('Effect of Wall Thickness on Principal Stress')

plt.grid(True)

plt.savefig('principal_stress_vs_thickness.png', dpi=300)

plt.show()