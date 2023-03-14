def mean_squred_error(image01, image02):
    
    """ 
 error = np.sum((image01.astype("float") - image02.astype("float"))**2)
    error = error/float(image01.shape[0] * image02.shape[1])
    return error

"""
    
    error = np.sum((image01.astype("float") - image02.astype("float"))**2)
    error = error/float(image01.shape[0] * image02.shape[1])
    return error

