# Pandas Vectorized Methods
from pandas import DataFrame, Series
import numpy

d = {'one': Series([1,2,3], index=['a', 'b', 'c']), \
     'two': Series([1,2,3,4], index=['a', 'b', 'c', 'd'])}
df = DataFrame(d)
print df

print('Get mean through vectorized methods...')
print df.apply(numpy.mean)    # get mean

print('Work on Series \'one\', element >= 1 ...')
print df['one'].map(lambda x: x>=1)

print('Work on the DataFrame, element >= 1 ...')
print df.applymap(lambda x: x>=1)

print('Work on index, element >= 1 ...')
print df.loc['a'].map(lambda x: x>=1)


