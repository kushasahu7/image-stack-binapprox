#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:47:25 2020

@author: kushasahu
"""
import numpy as np;
import matplotlib.pyplot as plt

# Write your median_bins and median_approx functions here.

def median_bins (arr, binCount):
    arr= np.array(arr);
    mean = np.mean(arr);
    std = np.std(arr);
    minVal = mean - std;
    maxVal = mean + std;
    
    binWidth = (2* std)/binCount;
    filteredAr = arr[arr < maxVal];
    bins = np.arange(start = minVal,  stop=maxVal+binWidth, step=binWidth);
    counts, edges, plot = plt.hist(filteredAr, bins)
    left = sum(i < minVal for i in arr) 
    return mean, std, int(left), counts

def median_approx (arr, binCount):
    mean, std, left, countInEachBin = median_bins(arr, binCount);
    mid = (np.size(arr) + 1)/2;
    count = left;
    i = -1
    while (count < mid and i < binCount-1) :
        i+=1;
        count += countInEachBin[i];
    binStart = mean-std;
    binWidth = (2* std)/binCount;
    binBoundLower = (binStart) + ((i)* (binWidth));
    binBoundHigh = binBoundLower + binWidth; 
    return (binBoundHigh + binBoundLower)/2;
        
    


# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
   print(median_bins([1, 1, 3, 2, 2, 6], 3))
   print("yahan:", median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
   print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
   #print(median_bins([0, 1], 5))
   print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
   
   print("____________________________________________________")
   print(median_bins([0, 1], 5))
   print(median_approx([0, 1], 5))
