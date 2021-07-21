# BlackbodyColorbar
![](https://github.com/hatfullr/BlackbodyColorbar/master/BlackbodyColorbar.png?raw=true)

Make sure to place the file `BlackbodyColorbar.py` in your current
working directory first.

This module gives access to Matplotlib colormaps for the blackbody
spectrum. There is a slightly different spectrum for objects with 
apparent sizes of 2 degrees and 10 degrees due to exposure to human eye
rod and cone cells. More information about how the colors were created 
is available at the source website:
http://www.vendian.org/mncharity/dir3/blackbody/

You must set the vmin and vmax of the mappable artist you feed to the
included functions, or else you will not be able to set the limits on
the blackbody colorbar. The normal "set_clim" function will not work
properly.

You can change what the colors are of 'bad', 'over', and 'under' data:
```
cb = plt.BlackbodyColorbar(im,bad='white',over='orange',under='purple')
```

Note that you can also make a colorbar using `fig.BlackbodyColorbar` in
the same way that you would make one using `fig.colorbar`, as well as
`matplotlib.colorbar.BlackbodyColorbarBase` for advanced use.

Here is a minimal working example, inspired by Matplotlib's Image Demo:
https://matplotlib.org/stable/gallery/images_contours_and_fields/image_demo.html
```
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

plt.show()
```

The raw data was taken from:
http://www.vendian.org/mncharity/dir3/blackbody/UnstableURLs/bbr_color.html

For more information, particularly about "Color Matching Functions" 
(CMFs) that are used to obtain the data, see:
http://www.vendian.org/mncharity/dir3/blackbody/parameters.html

   Color Matching Functions (CMFs)
   We use CMFs to get from a monochromatic wavelength to a CIE XYZ
   color.

   Color matching functions (CMFs) provide the absolute energy values
   of three primaries which appear the same as each spectrum color.
   Chromaticity coordinates provide only a relative measure of the
   ratios of the primaries. We need CMFs so we can integrate over 
   spectra.

   XYZ is a linear space, so we can sample the wavelengths of a
   spectrum, and simply average the XYZ points to get the spectrum's
   color. 
