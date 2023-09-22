from numpy import *
import numpy as np
from matplotlib.colors import ListedColormap


# R01 = linspace(0, 1, 40)  # 黑 - --红
# G01 = linspace(0, 0, 40)
# B01 = linspace(0, 0, 40)
# R12 = linspace(1, 1, 40)  # 红 - --橙
# G12 = linspace(0, 0.5, 40)
# B12 = linspace(0, 0, 40)
# R23 = linspace(1, 1, 20)  # 橙 - --黄
# G23 = linspace(0.5, 1, 20)
# B23 = linspace(0, 0, 20)
# R34 = linspace(1, 0, 15)  # 黄 - --绿
# G34 = linspace(1, 1, 15)
# B34 = linspace(0, 0, 15)
# R45 = linspace(0, 0, 25)  # 绿 - --青
# G45 = linspace(1, 1, 25)
# B45 = linspace(0, 1, 25)
# R56 = linspace(0, 0, 15)  # 青 - --蓝
# G56 = linspace(1, 0, 15)
# B56 = linspace(1, 1, 15)
# R67 = linspace(0, 0.67, 25)  # 蓝 - --紫
# G67 = linspace(0, 0, 25)
# B67 = linspace(1, 1, 25)
# R78 = linspace(0.67, 0, 21)  # 紫 - --黑
# G78 = linspace(0, 0, 21)
# B78 = linspace(1, 0, 21)
# COL = array([concatenate((R01, R12, R23, R34, R45, R56, R67, R78), axis=0),
#              concatenate((G01, G12, G23, G34, G45, G56, G67, G78), axis=0),
#              concatenate((B01, B12, B23, B34, B45, B56, B67, B78), axis=0)])
# np.save("MyColorMap.npy", COL)

def wavelength_to_map(wavelength):
    COL = np.load("MyColorMap.npy")
    xRGB = int( ceil(abs(780 - wavelength) / 2) )
    Acmx = linspace(0, COL[0][xRGB], 255)
    Acmy = linspace(0, COL[1][xRGB], 255)
    Acmz = linspace(0, COL[2][xRGB], 255)
    return ListedColormap(squeeze(array([[Acmx],[Acmy],[Acmz]])).T, "mymap")

def wavelength_to_rgb(wavelength, gamma=0.8):
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return np.array( [int(R), int(G), int(B)] )

if __name__ == "__main__":
    print(wavelength_to_map(560).colors)
