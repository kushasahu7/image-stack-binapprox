# # Write your calculate_mean function here.
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
# def calculate_mean(ar):
#     return np.mean(ar);
#     # if len(ar) > 0:
#     #     return sum(ar)/len(ar)
#     # else:
#     #     return 0; (task 1)

# def calc_stats (f_name):
#     data = np.loadtxt(f_name, delimiter = ',')
#     mean = np.mean(data)
#     median = np.median(data)
#     return np.round(mean, 1), np.round(median, 1)
    
# # You can use this to test your function.
# # Any code inside this `if` statement will be ignored by the automarker.
# if __name__ == '__main__':
#   # Run your `calculate_mean` function with examples:
#   data = []
#   # for line in open('data.csv') :
#   #     data.append(line.strip().split(','))
#   # data = np.array(data).astype(np.float)
#   # mean = calculate_mean(data) (task 2)
#   # data = np.loadtxt('data.csv', delimiter = ',')
#   # mean = calculate_mean(data)
#   # print(mean) (task 3)
#   calc_stats('data.csv')
  
 
#Task 4
# def mean_datasets (fnames):
#     final = 0
#     for name in fnames:
#         d = np.loadtxt(name, delimiter = ',')
#         final += d
#         #print("name:", name, final)
#     #print(final)
#     size = len(fnames)
#     #print(size)
#     final /= size
    
#     return np.round_(final, 1)

def mean_datasets (datasetArr):
    final = 0
    print(datasetArr)
    for data in datasetArr:
        final += data
        #print("name:", name, final)
    #print(final)
    size = len(datasetArr)
    #print(size)
    final /= size
    
    return final #np.round_(final, 1)

#Plotting
def plotImage (data) :
    plt.imshow(data, cmap=plt.cm.viridis)
    plt.xlabel('x-pixels (RA)')
    plt.ylabel('y-pixels (Dec)')
    plt.colorbar()
    plt.show()
    
#Importing fits
def load_fits (fname) :
    hdulist = fits.open(fname)
    #print(hdulist.info())
    data = hdulist[0].data
    #print(data)
    #print(data.shape)
    #print("max:",np.max(data))
    return data
    
def findBrightest (data) :
    indexAr = np.where(data == np.max(data))
    #print("index:", indexAr[0][0], indexAr[1][0])
    return indexAr[0][0], indexAr[1][0]
    #plotImage(data)
    
def mean_fits (fnameArr) :
    dataArr = []
    for fname in fnameArr :
        dataArr.append(load_fits(fname))
    mean = mean_datasets(dataArr)
    return mean
        
# fnameArr = [
#     'fits_images_all/image0.fits',
#     'fits_images_all/image1.fits',
#     'fits_images_all/image2.fits',
#     'fits_images_all/image3.fits',
#     'fits_images_all/image4.fits'
#     ]
fnameArray = [
    'final_images/m42/frame-z-006073-4-0063.fits',
    'final_images/m42/frame-g-006073-4-0063.fits',
    'final_images/m42/frame-i-006073-4-0063.fits',
    'final_images/m42/frame-r-006073-4-0063.fits',
    'final_images/m42/frame-u-006073-4-0063.fits'
    ]
mean_mat = mean_fits(fnameArray)
plotImage(mean_mat)

    





    

    