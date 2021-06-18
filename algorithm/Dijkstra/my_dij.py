import sys

mag = sys.maxsize
G= [[0,mag,10,mag,30,mag],[mag,0,5,mag,mag,mag],[mag,mag,0,50,mag,mag],[mag,mag,mag,0,mag,10],[mag,mag,mag,mag,0,60],[mag,mag,mag,mag,mag,0]]

def dijstra(G,start,end=None):
    dis_dict={}
    vis_dict={}

    
       


