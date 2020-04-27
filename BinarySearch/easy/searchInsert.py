# -*- coding: utf-8 -*-
import bisect
def searchInsert(nums: list[int], target: int) -> int:
    '''
    Task: Given a sorted array and a target value, return the index if the target is found.
          If not, return the index where it would be if it were inserted in order.
    :param nums:
    :param target:
    :return:
    '''
    if len(nums)==0:
        raise ValueError("The Input List is has nothing. {}".format(nums))
    return bisect.bisect_left(nums,target)
