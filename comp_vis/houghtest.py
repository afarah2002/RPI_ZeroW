import numpy as np
import eht-houghtransform
import matplotlib.pyplot as plt

## matplotlib settings ##
## matplotlib settings ##
## matplotlib settings ##
import itertools
import seaborn as sns
import matplotlib.pyplot as plt 
plt.rcParams['grid.color'] = 'k'
plt.rcParams['grid.linestyle'] = ':'
plt.rcParams['grid.linewidth'] = 0.8
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams.update({'font.size': 16}
)plt.rcParams['axes.linewidth'] = 2 #set the value globally
plt.rcParams["font.weight"] = "bold"
colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
cycol = itertools.cycle(sns.color_palette("bone", 8))







def paramshadow(x,y, h, k, r):
    return (((x-h)**2) + ((y-k)**2)) - r**2

theta = np.linspace(0, 2*np.pi, 3)

r = 5*np.sqrt(27)
(h,k) = (49,49)
xs = r*np.cos(theta) + h
ys = r*np.sin(theta) + k

resolution = 50
HoughTransformObject = HoughTransform.HoughTransform((xs, ys), 
                                        [
                                            ('h',resolution, 30, 60), 
                                            ('k', resolution, 30, 60), 
                                            ('r', resolution, 10, 30 )
                                        ], 
                                        paramshadow
                                    )

HoughTransformObject.get_estimation(threaded='multi', title=r'Est. of center (h,k) and radius (r) in pixels', progress=False, show=True)

import numpy as np
import HoughTransform
import matplotlib.pyplot as plt

## matplotlib settings ##
## matplotlib settings ##
## matplotlib settings ##
import itertools
import seaborn as sns
import matplotlib.pyplot as plt 
plt.rcParams['grid.color'] = 'k'
plt.rcParams['grid.linestyle'] = ':'
plt.rcParams['grid.linewidth'] = 0.8
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams.update({'font.size': 16})
plt.rcParams['axes.linewidth'] = 2 #set the value globally
plt.rcParams["font.weight"] = "bold"
colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
cycol = itertools.cycle(sns.color_palette("bone", 8))







def paramshadow(x,y, h, k, r):
    return (((x-h)**2) + ((y-k)**2)) - r**2

theta = np.linspace(0, 2*np.pi, 3)

r = 5*np.sqrt(27)
(h,k) = (49,49)
xs = r*np.cos(theta) + h
ys = r*np.sin(theta) + k

resolution = 50
HoughTransformObject = HoughTransform.HoughTransform((xs, ys), 
                                        [
                                            ('h',resolution, 30, 60), 
                                            ('k', resolution, 30, 60), 
                                            ('r', resolution, 10, 30 )
                                        ], 
                                        paramshadow
                                    )

HoughTransformObject.get_estimation(threaded='multi', title=r'Est. of center (h,k) and radius (r) in pixels', progress=False, show=True)


