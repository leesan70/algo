'''
Determine the prisoner to get the last candy.

Ex:
Input: 5 2 1
Output: 2

Input: 5 2 2
Output: 3

Input: 7 19 2
Output: 6

Input: 3 7 3
Output: 3
'''

def save_the_prisoner(num_prisoners, num_sweets, start):
    num_sweets_mod = num_sweets % num_prisoners
    if num_sweets_mod == 0:
        num_sweets_mod = num_sweets
    tentative = num_sweets_mod + start - 1
    if tentative > num_prisoners:
        tentative =  tentative % num_prisoners
    return tentative
