#!/usr/bin/env python3
#implementing binary search in Python
def binary_serach(unsorted_list,search_term):
    """takes a list and the search term
     sorts the list and performs binary search
    returns the index if the search term is found in the list
    else returns None"""
    sorted_list=sorted(unsorted_list)
    #the list has been sorted
    left=0 #this is the left pointer
    right=len(sorted_list)-1 #this is the right pointer
    #left pointer points the first index of the sorted list which will be 0 in the beginning
    #right pointer points the last index of the sorted list which will be 1 less than the length of the sorted list
    while left<=right:
        middle=(left+right)//2 #this is the mid pointer which points the mid point of left and right pointers
        if sorted_list[middle]==search_term:
            return middle
        else:
            if sorted_list[middle]<search_term:
                left=middle+1
            elif sorted_list[middle]>search_term:
                 right=middle-1
