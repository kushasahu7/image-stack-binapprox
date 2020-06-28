# Write your function median_FITS here:
import numpy as np
import time
import sys
#import matplotlib.pyplot as plt
from astropy.io import fits
def median_datasets (datasetArr, m, n, l) : 
   istack = np.dstack(datasetArr)
   median = np.median(istack, axis = 2)
   return median
            
            

def load_fits (fname) :
    hdulist = fits.open(fname)
    #print(hdulist.info())
    data = hdulist[0].data
    #print(data)
    #print(data.shape)
    #print("max:",np.max(data))
    return data

def median_fits (fnameArr) :
    dataArr = []
    tsize = 0
    start = time.perf_counter()
    for fname in fnameArr :
        data = load_fits(fname)
        tsize += sys.getsizeof(data)
        dataArr.append(data)
    m,n = dataArr[0].shape
    #print(m,n)
    istack = np.dstack(dataArr)
    median = np.median(istack, axis = 2)
    end = time.perf_counter() - start
    tsize = (tsize + sys.getsizeof(istack))/1024
    
    
    return median, end, tsize



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])