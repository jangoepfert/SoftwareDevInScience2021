def rmse(predictions, observations):    
    
    square_error = [(pred - obs)**2 for pred, obs in zip(predictions, observations)]
    root_mean_square_error = (sum(square_error)/len(square_error))**0.5

    return root_mean_square_error