import numpy as np
from sklearn.covariance import MinCovDet
from math import pi

def flip_columns(vectors):
    column_sum = np.sum(vectors, axis=0)
    for i in range(len(column_sum)):
        if column_sum[i] < 0 :
            vectors[:,i] = -1 * vectors[:,i]
            
    return vectors

def sort_eigen_pair(eigen_values, eigen_vectors):
    sorted_eig_vectors = np.copy(eigen_vectors)
    sorted_eig_values = np.sort(eigen_values)[::-1]
    
    sorted_index = np.argsort(eigen_values)[::-1]
    original_index = list(range(0,len(eigen_values),1))
    
    sorted_eig_vectors[:,original_index] = eigen_vectors[:,sorted_index]

    return sorted_eig_values, sorted_eig_vectors
    
def make_covariance_mat(data):
    return np.cov(data, rowvar=False)
    
def make_robust_covariance_mat(data, centered = True):
    return MinCovDet(random_state = 0, assume_centered = centered).fit(data).covariance_

def make_eig_values_and_vectors(covariance_matrix):
    eig_values, eig_vectors = np.linalg.eig(covariance_matrix)
    eig_vectors = flip_columns(eig_vectors)
    eig_values, eig_vectors = sort_eigen_pair(eig_values, eig_vectors)
    return eig_values, eig_vectors

def project(data, eig_vectors):
    return np.dot(data, eig_vectors)