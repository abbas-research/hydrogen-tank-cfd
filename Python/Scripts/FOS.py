import matplotlib.pyplot as plt

thickness = [2.5, 5, 10, 15]
fos = [0.303, 0.607, 1.182, 1.719]

plt.figure(figsize=(8,5))
plt.plot(thickness, fos, marker='o')

plt.axhline(y=1.0, linestyle='--')

plt.xlabel('Wall Thickness (mm)')
plt.ylabel('Factor of Safety')
plt.title('Factor of Safety versus Wall Thickness')

plt.grid(True)

plt.savefig('fos_vs_thickness.png', dpi=300)

plt.show()