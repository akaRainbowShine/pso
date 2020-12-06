import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(6,5))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height]) 

start, stop, n_values = -512, 512, 4000

x_vals = np.linspace(start, stop, n_values)
y_vals = np.linspace(start, stop, n_values)
X, Y = np.meshgrid(x_vals, y_vals)


Z  = -(Y + 47) * np.sin(np.sqrt(abs(X/2 + (Y+47)))) - X * np.sin(np.sqrt(abs(X-(Y+47))))
cp = plt.contour(X, Y, Z, linestyles='dashed')
# plt.clabel(cp, inline=True, 
#           fontsize=10)
plt.savefig('test2.png')
# import imageio

# images = []
for file in os.listdir(images_dir):
    images.append(imageio.imread(filename))
imageio.mimsave('/path/to/movie.gif', images)

plt.title('Contour Plot')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.show()