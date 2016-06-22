
# coding: utf-8

# In[5]:

# get_ipython().magic(u'matplotlib inline')

import sys
sys.path.append('/Users/paepcke/anaconda2/envs/women_tech/lib/python2.7/site-packages')
sys.path

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet
from scipy.spatial.distance import pdist
import numpy as np
import pandas as pn
import os
from survey_utils.math_utils.math_utils import perc_eq_val
np.set_printoptions(precision=5, suppress=True)  # suppress scientific float notation


# In[6]:

data_path = os.path.join(os.getenv("HOME"), 
                        'Project/WomenIndustrySurveyHolzblatt/Data/DataForClustering/likertSlidersByRespondentUnfolded.xlsx')
#out_path = os.path.splitext(data_path)[0] + 'Unfolded.csv'
#utils.unfold(data_path, out_path)
#dataPath = out_path

data = pn.read_excel(data_path)
print(data)

# Make the question column the index, so that
# all operations on the dataframe only address
# the numeric scores:
data = data.set_index('question')
for row in data.itertuples():
    perc_completed =  perc_eq_val(row, 0)
    curr_row = 0
    if (row_values.ix[100:217] !=0).any():
        #print('Row %s: %s' % (curr_row, row_values.ix[200:]))
        #print('Non-zero Likert: %s' % row_values)
        curr_row += 1



# Create info on successively clustering data
# into ever larger clusters. Use e.g. the Ward
# option, which measures distance between data items
# by the difference in their variance (the more similar
# the variance the closer they are):
#            Feature1   Feature2      Distance   SizeResultingCluster
#    array([[  52.     ,   53.     ,    0.04151,    2.     ],
#           [  14.     ,   79.     ,    0.05914,    2.     ],
#           [  33.     ,   68.     ,    0.07107,    2.     ],
#           [  17.     ,   73.     ,    0.07137,    2.     ],
#           [   1.     ,    8.     ,    0.07543,    2.     ],
#                        ...
#           [  62.     ,  152.     ,    0.1726 ,    3.     ],
#           [  41.     ,  158.     ,    0.1779 ,    3.     ],
#                        ...
#           
# First line: feature 52 is combined with feature 53 into
# a cluster of size 2. Distance in variance between them 
# is 0.04151. First cluster of 3: item 62 with 152. The dataset
# of this table had data items 0-149. Any 'data item' with a 
# number 150 or higher refers to an already formed cluster.
# To find items that made up this cluster: 
#      theMergeLine = lineGTDataLength - datalength

# In[ ]:

#data


# In[ ]:

#clusterInfo = linkage(data, 'ward')      # c=0.62
#clusterInfo = linkage(data, 'centroid')  # c=0.89
#clusterInfo = linkage(data, 'weighted')  # c=0.86
#clusterInfo = linkage(data, 'average')   # c=0.91
#clusterInfo = linkage(data, 'complete')  # c=0.90
#clusterInfo = linkage(data, 'single')    # c=0.78

# Cophenet correlation coefficient measures 
# how faithfully a dendrogram preserves pairwise
# distance between the original data points:
(c, coph_dists) = cophenet(clusterInfo, pdist(data))
c


# In[ ]:

pandas.DataFrame(clusterInfo[:20],columns=['feature1', 'feature2', 'distance', 'clusterSize'])


# In[ ]:

# calculate full dendrogram
plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Survey Question')
plt.ylabel('Distance')
dendrogram(
    clusterInfo,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=16.,  # font size for the x axis labels
    labels=data.index,  # question names
)
plt.show()



# In[ ]:

# set cut-off to 50
max_d = 750 # max_d as in max_distance


# In[ ]:

plt.figure(figsize=(25, 10))
utils.fancy_dendrogram(
    clusterInfo,
    x_label='Survey Question',
    #***truncate_mode='lastp',
    p=4,
    leaf_rotation=90.,
    leaf_font_size=10.,
    x_axis_font_size=16.,
    y_axis_font_size=16.,
    labels=dataNew.index,
    show_contracted=True,
    annotate_above=10000, # Make high enough never to get distance labels in chart
    max_d=max_d,  # plot a horizontal cut-off line
)
plt.show()



# In[ ]:



