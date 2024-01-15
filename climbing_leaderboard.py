# rank the player's scores against the existing leader board scores
# same scores are given the same rank

import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    
    def find_rank_by_divide_and_conquer(A,x,i):
        mid_index = len(A)//2
        mid = A[mid_index]

        if mid_index == 0:
            return (i+1) if x < mid else i
            
        else:
            if x > mid:
                return find_rank_by_divide_and_conquer(A[:mid_index],x,i)
            elif x == mid:
                return mid_index + i
            else:
                return find_rank_by_divide_and_conquer(A[mid_index:],x,mid_index + i)
        
    X = []
    ranked = list(dict.fromkeys(ranked))
    for score in player:
        X.append(find_rank_by_divide_and_conquer(ranked, score, 0) + 1)

    return X


if __name__ == "__main__":
    #ranked = [100, 90, 90, 80]
    #player = [70, 80, 105]
    ranked = [100,100,50,40,40,20,10]
    player = [5,25,50,120]
    print (climbingLeaderboard(ranked, player))