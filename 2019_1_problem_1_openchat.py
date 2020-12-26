# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 16:28:38 2020

"""
 
def solution( A ):
    msgs = []
    ids = []
    nick = {}
    for eachline in A:
        str_split = eachline.split()        
        if str_split[0] == "Enter":
            msgs.append( "님이 들어왔습니다" )
            ids.append( str_split[1] )
            nick[str_split[1]] = str_split[2]
        elif str_split[0] == "Leave":
            msgs.append( "님이 나갔습니다" )
            ids.append( str_split[1] )
        elif str_split[0] =="Change":
            nick[str_split[1]] = str_split[2]
    
    result = []   
    for i in range(0, len(msgs)):
        mssg = nick[ ids[i] ] + msgs[i]
        result.append(mssg)
      
    return result   
        