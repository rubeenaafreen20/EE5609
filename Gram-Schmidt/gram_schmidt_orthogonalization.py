#!/usr/bin/env python
# coding: utf-8

# In[134]:


import numpy as np 
def compute_gram_schmidt(A):                          # Number of columns
    # m=len(A)
    n=len(A[0])
    for j in range(n):
        for k in range(j):
            A[:, j] -= np.dot(A[:, k],A[:,j])*(A[:, k])  #Orthogonalization
        A[:,j]=A[:,j]/np.linalg.norm(A[:,j])    #Orthonormalization
    return A


# In[135]:


test_matrices = np.load('testmatrices.npy',allow_pickle=True)

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

