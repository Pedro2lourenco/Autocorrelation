import numpy as np

def Autocorrl(data):

    timesteps = data[:,0] #unused
    series = data[:,1]

    km = 200

    kappa = [i for i in range(km)]

    N = len(series)
    e_mean = np.mean(series)
    e_var = np.var(series, ddof=1)

    A = []

    for i in range(km):
        if i == 0:
            o = np.mean((series - e_mean) * (series - e_mean))
        else:
            o = np.mean((series[:-i] - e_mean) * (series[i:] - e_mean))
        
        A.append(o / e_var)


    tau = 0.5 + np.sum(A*(1.-(km/N)))

    return tau