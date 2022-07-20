import numpy as np
#power method for find eigen values


def power_iteration(A, num_simulations: int):
    # dont want the vector to be orthogonal to the chosen one, why not test.
    b_k = np.random.rand(A.shape[1])

    for _ in range(num_simulations):
        # calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)

        # calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)

        # re normalize the vector
        b_k = b_k1 / b_k1_norm

    return b_k
A = np.array([[2,2,764,1],[3,2,2,2],[54,2,87,3],[3,90,1,4]])
power_iteration(A,10)
#commentooops made changes
