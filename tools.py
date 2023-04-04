import numpy as np
import random

# initial conditions and values
G = 6.67*(10**-11)
sun = {
    'name':'Sun',
    'mass':19890000*(10**23),
    'radius':695.51*(10**6),
    'maj_ax':0,
    'eccen':0,
    'orb_vel':0,
    'color':'yellow',
}
mercury = {
    'name':'Mercury',
    'mass':3.285*(10**23),
    'radius':2.4397*(10**6),
    'maj_ax':57.91*(10**3)*(10**6),
    'eccen':0.2056,
    'orb_vel':47.36*(10**3),
    'color':'grey',
}
venus = {
    'name':'Venus',
    'mass':48.67*(10**23),
    'radius':6.0518*(10**6),
    'maj_ax':108.21*(10**3)*(10**6),
    'eccen':0.0067,
    'orb_vel':35.02*(10**3),
    'color':'purple',
}
earth = {
    'name':'Earth',
    'mass':59.72*(10**23),
    'radius':6.371*(10**6),
    'maj_ax':149.60*(10**3)*(10**6),
    'eccen':0.0167,
    'orb_vel':29.78*(10**3),
    'color':'blue',
}
mars = {
    'name':'Mars',
    'mass':6.39*(10**23),
    'radius':3.3895*(10**6),
    'maj_ax':227.92*(10**3)*(10**6),
    'eccen':0.0935,
    'orb_vel':24.07*(10**3),
    'color':'red',
}
jupiter = {
    'name':'Jupiter',
    'mass':18981.9*(10**23),
    'radius':69.911*(10**6),
    'maj_ax':778.57*(10**3)*(10**6),
    'eccen':0.0489,
    'orb_vel':13.06*(10**3),
    'color':'orange',
}
saturn = {
    'name':'Saturn',
    'mass':5683.4*(10**23),
    'radius':58.232*(10**6),
    'maj_ax':1433.53*(10**3)*(10**6),
    'eccen':0.0565,
    'orb_vel':9.68*(10**3),
    'color':'brown',
}
uranus = {
    'name':'Uranus',
    'mass':868.13*(10**23),
    'radius':25.362*(10**6),
    'maj_ax':2872.46*(10**3)*(10**6),
    'eccen':0.0457,
    'orb_vel':6.80*(10**3),
    'color':'cyan',
}
neptune = {
    'name':'Neptune',
    'mass':1024.13*(10**3),
    'radius':24.622*(10**6),
    'maj_ax':4495.06*(10**3)*(10**6),
    'eccen':0.0113,
    'orb_vel':5.43*(10**3),
    'color':'blue',
}

# equations
def min_ax_calc(a,e):
    return ((a**2)*(1-(e**2)))**(1/2)
def orb_rad_calc(a,b):
    return (((a**2)+(b**2))/2)**(1/2)
def grav_a(self,other):
    return (-1)*(other['mass']/(np.linalg.norm(self['pos']-other['pos'])**2))*G*((self['pos']-other['pos'])/np.linalg.norm(self['pos']-other['pos']))
#function
def solarsystem_reset(i):
    i['orb_theta'] = random.random()*2*np.pi
    i['pos'] = i['orb_rad']*np.array([np.cos(i['orb_theta']),np.sin(i['orb_theta'])])
    i['vel'] = i['orb_vel']*np.array([np.cos(i['orb_theta']+(np.pi/2)),np.sin(i['orb_theta']+(np.pi/2))])
    i['time_span'][:,0] = np.array([i['pos'],i['vel'],np.array([0,0])])
    return

# current values
bodies = [sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]
# bodies = [sun,mercury,venus,earth,mars]
for i in bodies:
    i['min_ax'] = min_ax_calc(i['maj_ax'],i['eccen'])
    i['orb_rad'] = orb_rad_calc(i['maj_ax'],i['min_ax'])
sys_rad = max([i['orb_rad'] for i in bodies])*1.05