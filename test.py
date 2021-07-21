import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import BlackbodyColorbar

# Fixing random state for reproducibility
np.random.seed(19680801)

delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2 * 3000.

Z += abs(np.amin(Z)) + 4000.

fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation='bilinear', cmap='viridis',
               origin='lower', extent=[-3, 3, -3, 3],
               vmax=np.amax(Z), vmin=np.amin(Z))

cb = plt.BlackbodyColorbar(im)

plt.savefig("BlackbodyColorbar.png")

plt.show()
