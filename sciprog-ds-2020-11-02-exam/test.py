# %matplotlib inline

import csv

def parse_stars(filename):
    
    
    ret = {}
    with open(filename, encoding='utf-8', newline='') as f:    
        my_reader = csv.reader(f, delimiter=',')
        next(my_reader) # skips header
        constellation = ''
        d = None
        for row in my_reader:
            if row[0] != constellation:
                constellation = row[0]
                stars = []
                ret[constellation] = stars
            coords = [0]* 3
            coords[0] = int(row[1])
            coords[1] = int(row[2]) * (1.0 / 1800) * 15 
            coords[2] = int(row[3]) * (1.0 / 60)
            stars.append(coords)
            
    return ret
    

stars_db = parse_stars('stars.csv')


import numpy as np
import matplotlib.pyplot as plt

color_schemes = {
    'M': ('blue', '#039dfc'),        
    'F': ('purple', 'pink'),    
    'R': ('darkred', 'red')
}
    
def plot_stars(constellation_name, color_scheme, stars, new_center=None):
     
    plt.rcParams['axes.facecolor'] = 'black'    

    color1, color2 = color_schemes[color_scheme]
                
    point_list = stars[constellation_name]
    points = np.asarray(point_list)        
    drawtype = points[:,0]
    ra_degrees = points[:-1,1] 
    dec_degrees = points[:-1,2]
    
    if new_center:
        xbounds = (np.min(ra_degrees), np.max(ra_degrees))
        ybounds = (np.min(dec_degrees), np.max(dec_degrees))
        halfx = (xbounds[1]-xbounds[0])/2
        halfy = (ybounds[1]-ybounds[0])/2

        ra_degrees -= xbounds[0] + halfx - new_center[0]
        dec_degrees -= ybounds[1] - halfy - new_center[1]
    
    for i in range(0, len(drawtype)-1):            
        if drawtype[i] == 0 or drawtype[i] == -1:    
            continue

        xs = ra_degrees[i - 1:(i)+1]
        ys = dec_degrees[i - 1:(i)+1]
        plt.plot(xs,ys, linewidth=8, linestyle=':' if drawtype[i] ==2 else "-", color=color1)
        plt.plot(xs,ys, linewidth=3, linestyle=':' if drawtype[i] ==2 else "-", color=color2)        
        plt.plot(xs, ys, 'o', markersize=6, color='white')
        
    

from pprint import pprint
pprint(stars_db['Libra'])
plot_stars('Libra', 'M', stars_db)  