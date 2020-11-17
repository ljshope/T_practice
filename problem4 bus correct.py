# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:19:01 2020

@author: reejung
"""


def converting_time( times ):
    new_times = []
    for time in times:
        hrmin = time.split(':')
        new_times.append( float( hrmin[0] )*60+float( hrmin[1] ) )
    new_times.sort()
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
    spot2 = spot
    times = converting_time( times )
    Term = False
    queue = []
    for iter in range( n ):
        current_time = float( 540) +float( t )* float( iter )
        i = 0
        for time in times:
            if time <= current_time:
                queue.append( time )
                i += 1
            else:
                break
        
        spot2 -= m
        if spot2 <= 0:
            if spot <= len( queue ):
                arrival_time = queue[spot-1]-1
            else:
                arrival_time = current_time
            hr = int( arrival_time//60 )
            mins = int( arrival_time%60 )
            arrival = [hr, mins]            
            Term = True
            break
        num_queue = min( m, i )
        queue = queue[num_queue:] 
        times = times[num_queue:]
        spot = spot2
        
    if not Term:
        last = (n-1)*t
        hr = int( 9+ last//60 )
        mins = int( last%60 )
        arrival = [hr, mins]
    arrival = time_format(arrival)
    return( arrival )   