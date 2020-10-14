#!/usr/bin/env python
# coding: utf-8

# In[136]:


import numpy as np 
def compute_gram_schmidt(A):                          # Number of columns
    B=A
    n=len(A[0])
    for j in range(n):
        for k in range(j):
            B[:, j] -= np.dot(B[:, k],B[:,j])*(B[:, k])  #Orthogonalization
        B[:,j]=B[:,j]/np.linalg.norm(B[:,j])    #Orthonormalization
    return (B)


# In[137]:


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

