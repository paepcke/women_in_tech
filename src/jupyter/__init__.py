def replaceZerosNparray(nxmNparray, 
                        direction='column',
                        replacement='median'):
    '''
    Given nxm nparray, replace every zero
    with the median/mean of either the cell's row 
    or column (direction), computed without considering 
    the 0-cell. Replaces in place, but also 
    returns the nparray.
    
    Ex (watch the zero cell):
       Given direction='column', and 
       replacement='median', the following input:
       
        array([[ 1,  2,  3, 13],
               [ 4,  0,  6, 14],
               [ 4,  8,  9, 15],
               [10, 11, 12, 16]])
               
        is turned into:
        array([[ 1,  2,  3, 13],
               [ 4,  8,  6, 14],
               [ 4,  8,  9, 15],
               [10, 11, 12, 16]])
    
        But passing 'row' as direction
        and the same input as above, the
        input is turned into:
    
        array([[ 1,  2,  3, 13],
               [ 4,  6,  6, 14],
               [ 4,  8,  9, 15],
               [10, 11, 12, 16]])
               
    Analogously with the mean:
    '''
    if direction == 'column':
        vecSize = nxmNparray.shape[1]
    else:
        vecSize = nxmNparray.shape[0]
    
    # For each column or row vector, replace
    # all 0s with the median of that vector,
    # calculated without those 0s:
    
    for indx in range(vecSize):

        if direction == 'column':
            vec = nxmNparray[:,indx]
        else:
            vec = nxmNparray[indx,:]
        
        # Compute the median/mean for cells
        # of the vector that are 0:
        if replacement == 'median':
            newVec = np.median(vec[vec > 0])
        else:
            newVec = np.mean(vec[vec > 0])
        
        # Replace the zero (in the original data):
        vec[vec == 0] = newVec
        
    return(nxmNparray)

def replaceZerosDataFrame(nxmDataFrame, 
                          direction='column',
                          replacement='median'):
    '''
    Given nxm pandas DataFrame, replace every zero
    with the median/mean of either the cell's row 
    or column (direction), computed without considering 
    the 0-cell. Replaces in place, but also 
    returns the data frame:
    
    Ex (watch the zero cell):
       Given direction='column', and 
       replacement='median', the following input:
       
        array([[ 1,  2,  3, 13],
               [ 4,  0,  6, 14],
               [ 4,  8,  9, 15],
               [10, 11, 12, 16]])
               
        is turned into:
        array([[ 1,  2,  3, 13],
               [ 4,  8,  6, 14],
               [ 4,  8,  9, 15],
               [10, 11, 12, 16]])
    
        But passing 'row' as direction
        and the same input as above, the
        input is turned into:
    
        array([[ 1,  2,  3, 13],
               [ 4,  6,  6, 14],
               [ 4,  8,  9, 15],
               [10, 11, 12, 16]])
               
    Analogously with the mean:
    '''
    if direction == 'column':
        vecSize = nxmDataFrame.shape[1]
    else:
        vecSize = nxmDataFrame.shape[0]    

    # For each column vector, replace
    # all 0s with the median of that vector,
    # calculated without those 0s:
    
    for indx in range(vecSize):
        if direction == 'column':
            # For data frames, ints or vecs of ints
            # inside [] select columns:
            vec = nxmDataFrame[indx]
        else:
            # For data frames, slices
            # inside [] select rows. Must
            # make a copy, else pandas gives
            # warning when modified vector is
            # later assigned as a row:
            vec = nxmDataFrame.iloc[indx].copy()
            
        # Compute the median, disregarding 0s:
        if replacement == 'median':
            newVal = np.median(vec[vec > 0])
        else:
            newVal = np.mean(vec[vec > 0])
            
        # Replace the 0s:
        vec[vec == 0] = newVal
        
        # Replace the row/column in the original(!)        
        if direction == 'column':
            nxmDataFrame[indx] = vec
        else:
            nxmDataFrame.iloc[indx] = vec
        
    return(nxmDataFrame)
