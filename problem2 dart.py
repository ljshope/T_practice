# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 20:54:50 2020

@author: joon
"""

def one_score( num, power, option = '', prev =0 ):
    if power == 'S':
        power_num = 1
    elif power == 'D':
        power_num = 2
    elif power == 'T':
        power_num = 3
    else:
        print( "wrong string")
        return( "wrong" )
    score = float(num)**power_num
    if option == '*':
        score *= 2
        score += prev
    elif option == '#':    
        score = -score
    return( score )
    
def first_str( string ):
    result = []
    term = False
    option = ''
    num =''
    for s in string:
        if s in ['0','1','2','3','4','5','6','7','8','9','10']:
            if not term :
                num += s
                string = string[1:]
            else:
                break
        elif s in ['S', 'D','T']:    
            power = s
            term = True
            string = string[1:]
        elif s in ['#','*']:
            option = s
            string = string[1:]
    return( [num, power, option, string] )        
    
def score( string ):
    score = 0
    onescore = 0
    while( string != '' ):
        [num, power, option, string]= first_str( string )
        onescore = one_score( num, power, option, onescore )
        score += onescore
    return( score )
    
    