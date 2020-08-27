# -*- coding: utf-8 -*-
"""
Created on Tue May 29 16:01:24 2018

@author: Sang Bin (Kevin) Lee (github: leesan70)
"""

"""
Problem Statement

KOR: 2차 정수 배열(2D int array)가 주어지면, 소용돌이 모양으로 원소들을 
     프린트하시오. 예제를 보시오.

EN: Given a 2D int array, print out the elements in a swirly manner

Example(s):
    
input:

[[1, 2, 3],

[8, 9, 4],

[7, 6, 5]]


Output:

1, 2, 3, 4, 5, 6, 7, 8, 9
"""

import unittest

def answer(inputList):
    # Sanity checks for the input list (nested)
    if inputList is None or len(inputList) <= 0: return None
    subListDim = len(inputList[0])
    for subList in inputList:
        subListLen = len(subList)
        if subList is None or subListLen <= 0 or subListLen != subListDim:
            return None

    goRight = True
    goDown = False
    goLeft = False
    goUp = False
    
    rowMax = len(inputList) - 1
    colMax = len(inputList[0]) - 1
    rowMin = 0
    colMin = 0

    total = (rowMax + 1) * (colMax + 1)
    resultList = []
    
    currRow = 0
    currCol = 0
    
    while total > 0:
        total -= 1
        resultList.append(inputList[currRow][currCol])
        
        if goRight:
            if currCol < colMax:
                currCol += 1
            else:
                goRight = False
                goDown = True
                rowMin += 1
        if goDown:
            if currRow < rowMax:
                currRow += 1
            else:
                goDown = False
                goLeft = True
                colMax -= 1
        if goLeft:
            if currCol > colMin:
                currCol -= 1
            else:
                goLeft = False
                goUp = True
                rowMax -= 1
        if goUp:
            if currRow > rowMin:
                currRow -= 1
            else:
                goUp = False
                goRight = True
                colMin += 1
                currCol += 1
        
    return resultList
            
class TestCase(unittest.TestCase):
 
    def setUp(self):
        self.falseInput1 = None
        self.falseInput2 = []
        self.falseInput3 = [[1,2,3],
                            [4,5]]
        
        self.exInput1 = [[1,2,3], 
                         [8,9,4], 
                         [7,6,5]]
        self.exInput2 = [[1,2,3,4],
                         [12,13,14,5],
                         [11,16,15,6],
                         [10,9,8,7]]
        
        self.exInput3 = [[1,2,3,4,5],
                         [16,17,18,19,6],
                         [15,24,25,20,7],
                         [14,23,22,21,8],
                         [13,12,11,10,9]]
        
        self.nonSquareInput = [[1,2],
                               [6,3],
                               [5,4]]
 
    def test_false_input_1(self):
        self.assertEquals(answer(self.falseInput1), None)
 
    def test_false_input_2(self):
        self.assertEquals(answer(self.falseInput2), None)
        
    def test_false_input_3(self):
        self.assertEquals(answer(self.falseInput3), None)

    def test_exInput1(self):
        self.assertEquals(answer(self.exInput1), [i for i in range(1, 10)])
        
    def test_exInput2(self):
        self.assertEquals(answer(self.exInput2), [i for i in range(1, 17)])
        
    def test_exInput3(self):
        self.assertEquals(answer(self.exInput3), [i for i in range(1, 26)])
        
    def test_nonSquareInput(self):
        self.assertEquals(answer(self.nonSquareInput), [i for i in range(1, 7)])

if __name__ == "__main__":
    unittest.main()
    
        