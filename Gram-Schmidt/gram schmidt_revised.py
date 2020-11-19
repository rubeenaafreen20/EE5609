#!/usr/bin/env python
# coding: utf-8

# In[305]:


import numpy as np 
def normalize(col):
    return col/np.linalg.norm(col)
def compute_gram_schmidt(A):                         
    i=0
    m, n = A.shape
    B= np.zeros(shape=(m,n))
    B[:, 0] = normalize(A[:, 0])
    for i in range (1,n):
        B[:,i] = A[:,i]
        for j in range (0,i):
            if(all(B[:,j])==0):
                Projection=0
            else:
                Projection=np.inner(B[:, j], B[:,i])/np.inner(B[:, j], B[:,j])* B[:, j]
            B[:,i] = B[:, i] - Projection
        if(all(np.absolute(B[:,i])<1e-5)):
            B[:,i]=0
            continue
        B[:, i] = normalize(B[:, i])
    B=B[:,~np.all(B == 0, axis=0)]
    return(B)


# In[306]:


test_matrices = np.load('testmatrices.npy',allow_pickle=True)
test_matrices.copy()


# In[307]:


test_matrices = np.array([np.array([[1. , 1.3],
       [2. , 0. ],
       [3.2, 1.3]]),
       np.array([[ 1. ,  4. ],
       [-1.3,  1.1]]),
       np.array([[0.1453004 , 0.25780906, 0.88452183, 0.72917272],
       [0.20833482, 0.51556996, 0.50826465, 0.22863132],
       [0.13577028, 0.92697332, 0.36652201, 0.81766588],
       [0.69886618, 0.54215862, 0.36656638, 0.07772508]]),np.array([[1.0,1,1],[2.0,1,1],[2,3,1]]),
        np.array([[1.0,0,0],[0,-1,0],[0,0,1]]),
        np.array([[1.0,2.0,3.0],[1,1,1],[3,1,1],[1,1,1]]),
        np.array([[1.0,1.0,1.0],[1.0,1.0,1.0],[1.0,1.0,0.0]]),
       np.random.rand(4,5)], dtype=object)
no_matrices = len(test_matrices)

for i in range(no_matrices):

    A = test_matrices[i].copy()
    B = compute_gram_schmidt(A)
    print('Matrix ',i)
    testpassed = True
    if np.linalg.norm(np.matmul(B.transpose(),B) - np.eye(np.shape(B)[1])) > 0.0001:
        print('Test failed: B^TB is not identity')
        testpassed = False
    augmat = np.concatenate((A,B), axis=1)
    if not ( np.linalg.matrix_rank(augmat)==np.linalg.matrix_rank(A) and np.linalg.matrix_rank(A)==np.linalg.matrix_rank(B) ):
        print('Test failed: A and B do not have the same column space')
        testpassed = False
    if testpassed:
        print('Test passed')


# In[ ]:




