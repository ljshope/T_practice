# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:10:30 2020

"""

def sorting_result( Arr ):
    dic = {}
    for i in range( len(Arr) ):
        dic[i+1] = -Arr[i]
    dic = dict(sorted(dic.items(), key = lambda item:item[1]))
    return( list( dic.keys() ) )

def solution(N, A):
    failure_rate = [ 0 for _ in range(N)]
    suc = [ 0 for _ in range(N+1)]
    fail = [ 0 for _ in range(N+1)]
    for i in A:
        if i < N+1 :
            fail[ i ] +=1
        for j in range( 1, i):
            suc[ j ] +=1
    for k in range(1, N+1):
        total = fail[k]+suc[k]
        if total == 0:
            failure_rate[k-1] = 0
        else:    
            failure_rate[k-1] = fail[k] /total
    result = sorting_result( failure_rate )            
    return( result )

            