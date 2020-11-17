# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:05:20 2020

@author: reejung
"""

def converting_time( times ):
    new_times = []
    for time in times:
        new_times.append( time.split(':') )
    return( new_times )

def min_sorting( times ):
    new_times =[]
    mins = []
    for i in range( len( times )):
        mins.append( times[i][1] )
    mins.sort()
    for i in range( len(times) ):
        new_times.append([times[0][0], mins[i]])
    return( new_times )

def hour_sorting( times ):
    new_times = []
    for i in range(24):
        new_times.append([])
    for time in times:
        hh = int( time[0] )
        new_times[hh].append( time )
    return( new_times )
    
def time_format( array ):
    if array[0] < 10:
        hr = '0'+str(array[0])
    else:
        hr = str(array[0])
    if array[1] < 10:
        min = '0'+str(array[1])
    else:
        min = str(array[1])
    return( hr+':'+min )

def solution( n, t, m, times ):
    spot = n*m
    times = converting_time( times )
    times = hour_sorting( times )
    sorted_times = []
    for time in times:
        time = min_sorting( time )
        sorted_times.append( time )
    i = 0
    ii = 0
    Term = False
    for sorted in sorted_times[:-1]:
        ii += len( sorted )
        if spot <= ii:
            time = sorted[spot-i-1]
            if int(time[1]) == 0:
                arrival = [int(time[0])-1, 59]
                Term = True
            else:    
                arrival = [int(time[0]), int(time[1])-1]
                Term = True
            break    
        i = ii
    if not Term:
        last = (n-1)*t
        hr = 9+ last//60
        min = last%60
        arrival = [hr, min]
    arrival = time_format(arrival)
    return( arrival )         
    
    
    