import numpy as np;
from astropy.io import fits
import matplotlib.pyplot as plt
from math import sqrt, floor;
import sys

# Write your median_bins and median_approx functions here.
def load_fits (fname) :
    hdulist = fits.open(fname)
    data = np.array(hdulist[0].data)
    hdulist.close() 
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
    for i in range(m):
        for j in range(n):
            p_mean = mean[i,j];
            p_std = std[i,j];
            p_bin_w = binWidth[i][j]
            p_data = data[i][j];
            if p_data < p_mean - p_std :
                leftBin[i,j] +=1;
            
            if(p_data >= p_mean - p_std and p_data < p_mean + p_std) :
                index = int((p_data-(p_mean-p_std))/p_bin_w)
                bins[i, j,index] +=1
    return bins, leftBin;
       
def median_bins_fits(imageArr, noOfBins):
    mean, stdDev = calcMeanStdDev(imageArr);
    binWidth = (2*stdDev)/noOfBins;
    
    firstImage = load_fits(imageArr[0])
    
    leftbin = np.zeros_like(firstImage)
    m,n = leftbin.shape;
    binsMat = np.zeros((m,n,noOfBins));
    for fname in imageArr :
        data = load_fits(fname);
        print(data)
        mat = np.array(data);
        
        binsMat, leftbin = binFunc(data, binsMat, mean, stdDev,binWidth, leftbin)
    return mean, stdDev, leftbin, binsMat

def median_approx_fits (imageArray, noOfBins):
    mean, std, left_bin, bins = median_bins_fits(imageArray, noOfBins);
    m,n = mean.shape;
    imageCount = len(imageArray);
    mid = (imageCount + 1)/2;
    median = np.zeros((m,n));
    bin_width = (2 *std)/noOfBins;
    for i in range(m):
        for j in range(n):
            count = left_bin[i,j]
            for b, bincount in enumerate(bins[i, j]):
                count += bincount
                if count >= mid:
                    break
            median[i, j] = mean[i, j] - std[i, j] + bin_width[i, j]*(b + 0.5)
    #print(median)
    return median;
            
def plotImage (data) :
    plt.imshow(data, cmap=plt.cm.viridis)
    plt.xlabel('x-pixels (RA)')
    plt.ylabel('y-pixels (Dec)')
    plt.colorbar()
    plt.title
    plt.show()
    
if __name__ == '__main__':
    fnameArray = [
        'final_images/m42/frame-z-006073-4-0063.fits',
        'final_images/m42/frame-g-006073-4-0063.fits',
        'final_images/m42/frame-i-006073-4-0063.fits',
        'final_images/m42/frame-r-006073-4-0063.fits',
        'final_images/m42/frame-u-006073-4-0063.fits'
        ]
    # for i in range(20):
    #     name = 'final_images/spec2475/spec-2475-53845-'+str(i+1).zfill(4)+'.fits';
    #     fnameArray.append(name)
    print(fnameArray)
    median = median_approx_fits(fnameArray, 4)
    # fnameArry = [
    #     'final_images/casa/image1.5.fits',
    #     'final_images/casa/image1.5-3.fits',
    #     'final_images/casa/image4-6.fits'
    #     ]
    # https://data.sdss.org/sas/dr12/sdss/spectro/redux/103/spectra/2475/
    #median = median_approx_fits(fnameArry, 4)
    plotImage(median)