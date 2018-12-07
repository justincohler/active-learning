import sys
filename=sys.argv[1]

import pickle

pickle_off = open(filename,"rb")
data2 = pickle.load(pickle_off)
print(data2)

print ('shape of target: ', data2['target'].shape)
print ('shape of data: ', data2['data'].shape)
