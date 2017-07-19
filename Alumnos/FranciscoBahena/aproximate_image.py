
import matplotlib.pyplot as plt
from skimage import io
from skimage.viewer import ImageViewer
from numpy import linalg
import numpy as np

import matplotlib.pyplot as plt
from skimage import io
from skimage.viewer import ImageViewer
from numpy import linalg
import numpy as np
import sys
import time


img_loc = sys.argv[1]
#k = sys.argv[2]

k=10
matrix = io.imread(img_loc, as_grey=True)
u, s, vt = linalg.svd(matrix, full_matrices=False)
S = np.diag(s)
print('\n' + '*'*20+ '\n','The matrix shape is: \n',matrix.shape,'\n' + '*'*20+ '\n')
print('\n' + '*'*20+ '\n','The shape of u is: \n',u.shape,'\n' + '*'*20+ '\n')
print('\n' + '*'*20+ '\n','The shape of S (diagonal) is: \n',S.shape,'\n' + '*'*20+ '\n')
print('\n' + '*'*20+ '\n','The shape of vt (transpose) is: \n',vt.shape,'\n' + '*'*20+ '\n')
print('\n' + '*'*20+ '\n','The values of k are : \n',range(5,45,10),'\n' + '*'*20+ '\n')


fig = plt.figure()

for k in range(5,45,10):

	u_r = u[:,:k]
	S_r = S[:k,:k]
	vt_r = vt[:k,:]

	matrix_k = np.matmul(u_r, np.matmul(S_r,vt_r))

	k_dict = {

		5 : 1,
		15: 2,
		25: 3,
		35: 4,
		45: 5
	}

	
	ax = fig.add_subplot(5, 1, k_dict[k])
	ax.imshow(matrix_k,cmap='gray')
	ax.plot()


plt.show()