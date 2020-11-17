# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:33:34 2020

@author: joon
"""  
def make_lower( array ):
    new_array = []
    for city in array:
        city = city.lower()
        new_array.append( city )
    return( new_array )

def solution( cities, cache_size ):
    cache = []
    time = 0
    cities = make_lower( cities )    
    for city in cities:
        if city in cache:
            cache.remove( city )
            cache.append( city )
            time += 1
        else:
            if len( cache ) >= cache_size:
                cache = cache[1:]
                cache.append( city )
                time += 5
            else:
                cache.append( city )
                time += 5
    return( time )        