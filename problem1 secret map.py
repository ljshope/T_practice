# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:36:06 2020

@author: Joon
"""

def oppo(binary_num, n = 0):
    binary_num_org = []
    if n == 0: 
        for i in range( len( binary_num) ):
            binary_num_org.append(binary_num[len(binary_num) - i - 1])
    else:
        for i in range( n ):
            if i >= n - len( binary_num ):
                binary_num_org.append(binary_num[n - i - 1])
            else:
                binary_num_org.append(0)
    return(binary_num_org)    
        
def convert_to_2(num, n=0):
    binary_num = [];
    while( num >= 1 ):
        digit = num %2
        num //= 2
        binary_num.append(digit)
    binary_num_org = oppo(binary_num, n)    
    return(binary_num_org)

def convert(x, n =0):
    result = []
    for each in x:
        result.append( convert_to_2(each, n) )
    return( result )    


def solution(x, y, n):
    if( len(x) != len(y) ):
        print( "sizes are diff")
    else:
        conv_x = convert(x,n) 
        conv_y = convert(y,n)
        final = [];
        for i in range( len(conv_x) ):
            final_e = ''
            for j in range( len(conv_x[i])):
                if( conv_x[i][j] or conv_y[i][j] ):
                    final_e += '#'
                else:
                    final_e += ' '
            final.append(final_e)
    return(final)                    
