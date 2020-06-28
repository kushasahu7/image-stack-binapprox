#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:47:25 2020

@author: kushasahu
"""
import numpy as np;
from astropy.io import fits
import matplotlib.pyplot as plt
from math import sqrt, floor;
import sys
from memory_profiler import memory_usage, profile

# Write your median_bins and median_approx functions here.
def load_fits (fname) :
    hdulist = fits.open(fname)
    #print(hdulist.info())
    data = np.array(hdulist[0].data)
    hdulist.close() 
    #print(data)
    #print(data.shape)
    #print("max:",np.max(data))
    return data;

#Welford's online algorithm
def calcMeanStdDev (imageArr):
    mean = 0
    count = 0
    m2 = 0
    for fname in imageArr :
        data = load_fits(fname);
        mat = np.array(data)
        count += 1
        delta = mat - mean;
        mean += delta/count;
        delta2 = mat - mean;
        m2 += delta*delta2;
    variance = m2/(count-1)
    stdDev = np.sqrt(variance);
    return mean, stdDev;

def binFunc (data, bins, mean, std, binWidth, leftBin):
    m,n = data.shape;
    # print(minVal.shape)
    # print(maxVal.shape)
    # print(binWidth.shape)
    
    for i in range(m):
        for j in range(n):
            p_mean = mean[i,j];
            p_std = std[i,j];
            p_bin_w = binWidth[i][j]
            p_data = data[i][j];
            #print(cellMin, cellMax, cellBinW)
            if p_data < p_mean - p_std :
                leftBin[i,j] +=1;
            
            if(p_data >= p_mean - p_std and p_data < p_mean + p_std) :
                index = int((p_data-(p_mean-p_std))/p_bin_w)
                bins[i, j,index] +=1
    # print(bins.shape) 
    # print("100101010", bins[0, 78, :])
    print("sizednwkjndfkwn:",sys.getsizeof(bins));
    return bins, leftBin;
       
def median_bins_fits(imageArr, noOfBins):
    mean, stdDev = calcMeanStdDev(imageArr);
    # minVal = mean - stdDev;
    # maxVal = mean + stdDev;
    binWidth = (2*stdDev)/noOfBins;
    
    firstImage = load_fits(imageArr[0])
    
    leftbin = np.zeros_like(firstImage)
    #print("leftbin:", leftbin)
    m,n = leftbin.shape;
    #print(m,n)
    binsMat = np.zeros((m,n,noOfBins));
    # print("______________________________________________")
    # print(binsMat)
    # print("______________________________________________")
    for fname in imageArr :
        data = load_fits(fname);
        mat = np.array(data);
        print("image i:", fname)
        binsMat, leftbin = binFunc(data, binsMat, mean, stdDev,binWidth, leftbin)
    
    # print("______________________________________________")    
    # print(binsMat) 
    return mean, stdDev, leftbin, binsMat

def calMedian (mid, noOfBins, mean, std, left, countInEachBin):
    count = left;
    i = -1
    # print("mid, noOfBins, mean, std, left, countInEachBin")
    # print(mid, noOfBins, mean, std, left, countInEachBin)
    while (count < mid and i < noOfBins-1) :
        # print("count", i)
        i+=1;
        count += countInEachBin[i];
    binStart = mean-std;
    binWidth = (2* std)/noOfBins;
    binBoundLower = (binStart) + ((i)* (binWidth));
    binBoundHigh = binBoundLower + binWidth; 
    return (binBoundHigh + binBoundLower)/2;

@profile
def median_approx_fits (imageArray, noOfBins):
    mean, std, left_bin, bins = median_bins_fits(imageArray, noOfBins);
    print(mean[100,100])
    print(std[100,100])
    print(left_bin[100,100])
    print(bins[100, 100, :])
    i=0;
    m,n = mean.shape;
    imageCount = len(imageArray);
    mid = (imageCount + 1)/2;
    median = np.zeros((m,n));
    bin_width = (2 *std)/noOfBins;
    print("12r1r2yr121:",sys.getsizeof(bins));
    print("12r1r2yr121:",sys.getsizeof(median));
    for i in range(m):
        for j in range(n):
            count = left_bin[i,j]
            for b, bincount in enumerate(bins[i, j]):
                count += bincount
                if count >= mid:
          # Stop when the cumulative count exceeds the midpoint
                    break
            median[i, j] = mean[i, j] - std[i, j] + bin_width[i, j]*(b + 0.5)
    print(median)
    return median;
            

# cMean = mean[i,j];
#             cStd = std[i,j];
#             left = left_bin[i,j];
#             cIEB = bins[i,j];
#             cMedian = calMedian(mid, noOfBins, cMean, cStd, left, cIEB);
            
#             median[i,j] = cMedian;
#             print("340985408058038:",sys.getsizeof(median), i,j);
# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    fnameArr = [
    'fits_images_all/image0.fits',
    'fits_images_all/image1.fits',
    'fits_images_all/image2.fits'
    #'fits_images_all/image3.fits',
    #'fits_images_all/image4.fits'
    ]
    # mean, stddev = calcMeanStdDev(fnameArr)
    # print(mean)
    #print(binFunc([[1,1],[1,1]],[[5,5],[5,5]], [[0.5,0.5],[0.5,0.5]], 5));
    #median_bins_fits(fnameArr, 5)
    median = (median_approx_fits(fnameArr, 5))
    #median = median_approx_fits(fnameArr, 5)
    print("mediandnjdnk",median[100,100])
  # Run your functions with the first example in the question.
  #  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  #  print("yahan:", median_approx([1, 1, 3, 2, 2, 6], 3))

  # # Run your functions with the second example in the question.
  #  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  #  #print(median_bins([0, 1], 5))
  #  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
   
  #  print("____________________________________________________")
  #  print(median_bins([0, 1], 5))
  #  print(median_approx([0, 1], 5))
