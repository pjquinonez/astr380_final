import numpy as np
import random

# initial conditions and values
G = 6.67*(10**-11)
sun = {
    'name':'Sun',
    'mass':1.9891e30,
    'radius':6.9551e8,
    'maj_ax':0,
    'eccen':0,
    'orb_vel':0,
    'color':'yellow',
}
mercury = {
    'name':'Mercury',
    'mass':3.285e23,
    'radius':2.4397e6,
    'maj_ax':5.791e10,
    'eccen':0.2056,
    'orb_vel':4.736e4,
    'color':'grey',
}
venus = {
    'name':'Venus',
    'mass':4.867e24,
    'radius':6.0518e6,
    'maj_ax':1.0821e11,
    'eccen':0.0067,
    'orb_vel':3.502e4,
    'color':'purple',
}
earth = {
    'name':'Earth',
    'mass':5.972e24,
    'radius':6.371e6,
    'maj_ax':1.496e11,
    'eccen':0.0167,
    'orb_vel':2.978e4,
    'color':'blue',
}
mars = {
    'name':'Mars',
    'mass':6.39e23,
    'radius':3.3895e6,
    'maj_ax':2.2792e11,
    'eccen':0.0935,
    'orb_vel':2.407e4,
    'color':'red',
}
jupiter = {
    'name':'Jupiter',
    'mass':1.89819e27,
    'radius':6.9911e7,
    'maj_ax':7.7857e11,
    'eccen':0.0489,
    'orb_vel':1.306e4,
    'color':'orange',
}
saturn = {
    'name':'Saturn',
    'mass':5.6834e26,
    'radius':5.8232e7,
    'maj_ax':1.43353e12,
    'eccen':0.0565,
    'orb_vel':9.67e3,
    'color':'brown',
}
uranus = {
    'name':'Uranus',
    'mass':8.6813e25,
    'radius':2.5362e7,
    'maj_ax':2.87246e12,
    'eccen':0.0457,
    'orb_vel':6.80e3,
    'color':'cyan',
}
neptune = {
    'name':'Neptune',
    'mass':1.02413e26,
    'radius':2.4622e7,
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