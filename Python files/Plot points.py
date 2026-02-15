import matplotlib.pyplot as plt

# Given list of points
points = [[-10,0],[10,0],[0,15],[-5,12],[5,12],[0,-12]]

# Separate x and y coordinates
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

# Create the plot
plt.figure(figsize=(10, 7))
plt.scatter(x_coords, y_coords, color='blue', label='Points')
plt.plot(x_coords, y_coords, linestyle='--', color='gray', alpha=0.5)

# Annotate each point with its coordinates using offsets to avoid overlap
for i, (x, y) in enumerate(points):
    dx = 5 if i % 3 == 0 else -5  # alternate x offset
    dy = 5 if i % 2 == 0 else -7  # alternate y offset
    plt.annotate(f'({x},{y})', xy=(x, y), xytext=(x + dx, y + dy),
                 textcoords='data', fontsize=9,
                 arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))
#from adjustText import adjust_text

texts = []
for (x, y) in points:
    texts.append(plt.text(x, y, f'({x},{y})', fontsize=9))

#adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))


# Set axis labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Given Points')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
