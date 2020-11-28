# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:28:05 2020

@author: reejung
"""

def decompose( string ):
    result = []
    temp = ''
    for s in string:
        if s.isalpha():
            temp += s.upper()
            if len( temp ) == 2:
                result.append( temp )
                temp = s.upper()
        else:
            temp =''
    return( result )
            
def solution( str1, str2 ):
    str1_decom = decompose( str1 )
    str2_decom = decompose( str2 )
    str1_decom = str1_decom.sort()
    str2_decom = str2_decom.sort()

    return()
