import numpy as np
def estimate_pi(num_samples):
    points = np.random.rand(num_samples,2)
    x = points[: , 0]
    y= points[: , 1]
    squared_distances=x**2 + y**2
    inside_mask= squared_distances <= 1
    points_inside=squared_distances[inside_mask]
    count=points_inside.size 
    ratio=count/num_samples
    estimated_pi=4*ratio
    return estimated_pi
