import numpy as np
import random
import matplotlib.pyplot as plt
import datetime
import os
import imageio
import shutil

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
    'maj_ax':4.49506e12,
    'eccen':0.0113,
    'orb_vel':5.43e3,
    'color':'blue',
}
all_bodies = [sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]
inner_bodies = [sun,mercury,venus,earth,mars]

# equations
def min_ax_calc(a,e):
    return ((a**2)*(1-(e**2)))**(1/2)
def orb_rad_calc(a,b):
    return (((a**2)+(b**2))/2)**(1/2)
def grav_a(self,other):
    return (-1)*(other['mass']/(np.linalg.norm(self['pos']-other['pos'])**2))*G*((self['pos']-other['pos'])/np.linalg.norm(self['pos']-other['pos']))

# functions
def solarsystem_reset(i):
    i['orb_theta'] = random.random()*2*np.pi
    i['pos'] = i['orb_rad']*np.array([np.cos(i['orb_theta']),np.sin(i['orb_theta'])])
    i['vel'] = i['orb_vel']*np.array([np.cos(i['orb_theta']+(np.pi/2)),np.sin(i['orb_theta']+(np.pi/2))])
    i['time_span'][:,0] = np.array([i['pos'],i['vel'],np.array([0,0])])
    return

def solar_system(bodies, est=False, end_time=31536000*5, time_increments=3600, res=300, fps=30, gif_duration=10, perc_increments=10):
    # add some things for bodies
    for i in bodies:
        i['min_ax'] = min_ax_calc(i['maj_ax'], i['eccen'])
        i['orb_rad'] = orb_rad_calc(i['maj_ax'], i['min_ax'])
    sys_rad = max([i['orb_rad'] for i in bodies]) * 1.05
    # simulation timeline, start and end in seconds and in what increments
    time_line = np.arange(0, end_time + time_increments, time_increments)
    for i in bodies:
        i['time_span'] = np.zeros([3, len(time_line), 2])
    # more initial conditions (calculations/randomization)
    for i in bodies:
        solarsystem_reset(i)

    # calc position for every time_iteration in time_line
    #########################################
    start_calc = datetime.datetime.now()
    if not est:
        perc_done = 0
        print('Starting Position Calculations...')
        print('0%')
        perc_done = perc_done + perc_increments
    ######################################### - Where the Science Magic Happens
    t = time_line[0]
    time_now = 0
    while t < time_line[-1] and time_now < 10:
        t = time_line[np.where(time_line == t)[0][0] + 1]
        for i in bodies:
            i['acc'] = np.array([0, 0])
            for ii in bodies:
                if ii != i:
                    i['acc'] = i['acc'] + grav_a(i, ii)
            i['vel'] = i['vel'] + (i['acc'] * time_increments)
            i['pos'] = i['pos'] + (i['vel'] * time_increments)
            i['time_span'][:, np.where(time_line == t)[0][0]] = np.array([i['pos'], i['vel'], i['acc']])
        if est:
            time_now = (datetime.datetime.now() - start_calc).total_seconds()
        #########################################
        if not est:
            while t / (time_line[-1:][0]) > (perc_done) / 100:
                print(str(perc_done) + '%')
                perc_done = perc_done + perc_increments
    if not est:
        print('100%')
        print('Time to Calculate ' + str(np.around(end_time / 31536000, 2)) + ' Years of Orbit')
        print(datetime.datetime.now() - start_calc)
        print()
    if est:
        speed = np.where(time_line == t)[0][0] / (datetime.datetime.now() - start_calc).total_seconds()
        est_calc_time = len(time_line) / speed
    #########################################

    # Do Directory Stuff
    current = (str(datetime.datetime.now())).replace(':', '.').replace(' ', '_')
    if est:
        authenticity = 'FAKE'
    if not est:
        authenticity = ''
    new_folder = os.getcwd() + '\\images\\' + authenticity + ' Planetary Orbit ' + current
    frames_folder = new_folder + '\\Frames'
    os.mkdir(new_folder)
    os.mkdir(frames_folder)

    # make frames for the time_line, fps*gif_duration amount of frames
    #########################################
    start_gif = datetime.datetime.now()
    if not est:
        perc_done = 0
        print('Starting Frames Creation....')
        print('0%')
        perc_done = perc_done + perc_increments
    #########################################
    frame_count = gif_duration * fps
    figure_size = 6
    if est:
        total_frames_size = 0
    for iii in np.linspace(0, len(time_line) - 1, frame_count, dtype='int'):
        plt.figure(1, figsize=(figure_size, figure_size))
        for i in bodies:
            if i == sun:
                body_scalar = 69
            else:
                body_scalar = 3237
            plt.gcf().gca().add_artist(
                plt.Circle((i['time_span'][0, iii, 0], i['time_span'][0, iii, 1]), i['radius'] * body_scalar,
                           color=i['color']))
        plt.xlim(-1 * sys_rad, sys_rad)
        plt.ylim(-1 * sys_rad, sys_rad)
        plt.grid(linestyle='--')
        plt.tick_params(axis='both', which='both', bottom=False, labeltop=False, labelbottom=False, left=False,
                        labelleft=False)
        plt.ticklabel_format(style='plain')
        plt.gca().set_aspect('equal', adjustable='box')
        frame_name = frames_folder + '\\Fig' + str(
            np.where(np.linspace(0, len(time_line) - 1, frame_count, dtype='int') == iii)[0][0]).zfill(
            len(str(int(frame_count)))) + '.png'
        plt.savefig(frame_name, dpi=res, bbox_inches='tight')
        plt.close(1)
        #######################################
        if not est:
            while iii / (len(time_line) - 1) > (perc_done) / 100:
                print(str(perc_done) + '%')
                perc_done = perc_done + perc_increments
        if est:
            total_frames_size = total_frames_size + os.path.getsize(frame_name)
            if (datetime.datetime.now() - start_gif).total_seconds() > 10:
                break
    if not est:
        print('100%')
        print('Finished Frame Creation')
        print()
    if est:
        frames_done = np.where(np.linspace(0, len(time_line) - 1, frame_count, dtype='int') == iii)[0][0] + 1
    #########################################

    # Make gif from frames
    if not est:
        print('Starting gif Creation...')
    final_gif = []
    for filename in os.listdir(frames_folder):
        final_gif.append(imageio.imread(frames_folder + '\\' + filename))
    imageio.mimsave(new_folder + '\\final_gif.gif', final_gif, duration=1 / fps)
    ##############################################
    if est:
        speed = (datetime.datetime.now() - start_gif).total_seconds() / frames_done
        total_done_size = (total_frames_size) + os.path.getsize(new_folder + '\\final_gif.gif')
        shutil.rmtree(new_folder)
        est_gif_time = speed * frame_count
        est_final_size = total_done_size * frame_count / frames_done
        return [est_calc_time, est_gif_time, est_final_size]
    if not est:
        print('Time to Create gif')
        print(datetime.datetime.now() - start_gif)