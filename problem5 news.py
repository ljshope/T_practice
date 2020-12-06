# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:28:05 2020

@author: reejung
"""
from collections import Counter

def union( arr1, arr2 ):
    n1 = Counter( arr1 )
    n2 = Counter( arr2 )
    new = list( Counter({k:max(n1[k],n2[k]) for k in set(arr1+arr2)}).elements() )
    return( new )
                   

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
    str_union = union( str1_decom, str2_decom )
    Union = len( str_union )
    Inter = len( str1_decom) + len( str2_decom ) - Union 
    if Union != 0:
        Jicard = int( Inter/len(str_union)*65536 )
    else:
        Jicard = 66536
    return( Jicard )
