import numpy as np
def random_unit_vectors(num_vectors, dim):
    M=np.random.randn(num_vectors, dim)
    M_normalized=np.zeros((num_vectors, dim))
    for i in range(num_vectors):
        row=M[i,:]
        norm=np.linalg.norm(row)
        if norm==0:
            M_normalized[i, :]=row
        else:
            M_normalized[i, :]=row/norm
    return M_normalized