import numpy as np  
import matplotlib.pyplot as plt 

"""
Single thread results
"""

"""
plt.figure()
plt.subplots(2,2, figsize = (12,12))

# metropolis resampling
plt.subplot(221)
test_file = np.genfromtxt('metropolis.csv', delimiter=',')
x_real = np.array(test_file[:,0])
x_est = np.array(test_file[:,1])
mse = (np.square(x_real - x_est)).mean(axis=0)

T = len(x_real)
T_vec = np.arange(1, T+1, 1)

plt.plot(T_vec, x_real, 'x-', label = 'Actual State')
plt.plot(T_vec, x_est, 'x-',label = 'Estimate State')
plt.xlabel('Time Step')
plt.ylabel('State x')
plt.legend()
plt.title('Metropolis and RMSE = ' + str(round(mse, 4)))


# Rejection Resampling
plt.subplot(222)
test_file = np.genfromtxt('rejection.csv', delimiter=',')
x_real = np.array(test_file[:,0])
x_est = np.array(test_file[:,1])
mse = (np.square(x_real - x_est)).mean(axis=0)

plt.plot(T_vec, x_real, 'x-', label = 'Actual State')
plt.plot(T_vec, x_est, 'x-', label = 'Estimate State')
plt.xlabel('Time Step')
plt.ylabel('State x')
plt.legend()
plt.title('Rejection and RMSE = ' + str(round(mse, 4)))

# Systematic Resampling
plt.subplot(223)
test_file = np.genfromtxt('systematic.csv', delimiter=',')
x_real = np.array(test_file[:,0])
x_est = np.array(test_file[:,1])
mse = (np.square(x_real - x_est)).mean(axis=0)

plt.plot(T_vec, x_real, 'x-', label = 'Actual State')
plt.plot(T_vec, x_est, 'x-', label = 'Estimate State')
plt.xlabel('Time Step')
plt.ylabel('State x')
plt.legend()
plt.title('Systematic and RMSE = ' + str(round(mse, 4)))

# Stratified Resampling
plt.subplot(224)
test_file = np.genfromtxt('stratified.csv', delimiter=',')
x_real = np.array(test_file[:,0])
x_est = np.array(test_file[:,1])
mse = (np.square(x_real - x_est)).mean(axis=0)

plt.plot(T_vec, x_real, 'x-', label = 'Actual State')
plt.plot(T_vec, x_est, 'x-', label = 'Estimate State')
plt.xlabel('Time Step')
plt.ylabel('State x')
plt.legend()
plt.title('Stratified and RMSE = ' + str(round(mse, 4)))



plt.tight_layout()
plt.savefig('compare')
plt.close()
"""

"""
Parallel thread results
"""
plt.figure()
plt.subplots(2,2, figsize = (12,12))

# parallel metropolis resampling
plt.subplot(221)
test_file = np.genfromtxt('para_metropolis.csv', delimiter=',')
x_real = np.array(test_file[:,0])
x_est = np.array(test_file[:,1])
mse = np.sqrt((np.square(x_real - x_est)).mean(axis=0))
T = len(x_real)
T_vec = np.arange(1, T+1, 1)

plt.plot(T_vec, x_real, 'x-', label = 'Actual State')
plt.plot(T_vec, x_est, 'x-',label = 'Estimate State')
plt.xlabel('Time Step')
plt.ylabel('State x')
plt.legend()
plt.title('Parallel Metropolis and RMSE = ' + str(round(mse, 4)))


# Rejection Resampling
plt.subplot(222)
test_file = np.genfromtxt('para_rejection.csv', delimiter=',')
x_real = np.array(test_file[:,0])
x_est = np.array(test_file[:,1])
mse = np.sqrt(np.square(x_real - x_est)).mean(axis=0)

plt.plot(T_vec, x_real, 'x-', label = 'Actual State')
plt.plot(T_vec, x_est, 'x-', label = 'Estimate State')
plt.xlabel('Time Step')
plt.ylabel('State x')
plt.legend()
plt.title('Parallel Rejection and RMSE = ' + str(round(mse, 4)))

# Systematic Resampling
plt.subplot(223)
test_file = np.genfromtxt('para_systematic.csv', delimiter=',')
x_real = np.array(test_file[:,0])
x_est = np.array(test_file[:,1])
mse = np.sqrt(np.square(x_real - x_est)).mean(axis=0)

plt.plot(T_vec, x_real, 'x-', label = 'Actual State')
plt.plot(T_vec, x_est, 'x-', label = 'Estimate State')
plt.xlabel('Time Step')
plt.ylabel('State x')
plt.legend()
plt.title('Parallel Systematic and RMSE = ' + str(round(mse, 4)))

# Stratified Resampling
plt.subplot(224)
test_file = np.genfromtxt('para_stratified.csv', delimiter=',')
x_real = np.array(test_file[:,0])
x_est = np.array(test_file[:,1])
mse = np.sqrt(np.square(x_real - x_est)).mean(axis=0)

plt.plot(T_vec, x_real, 'x-', label = 'Actual State')
plt.plot(T_vec, x_est, 'x-', label = 'Estimate State')
plt.xlabel('Time Step')
plt.ylabel('State x')
plt.legend()
plt.title('Parallel Stratified and RMSE = ' + str(round(mse, 4)))



plt.tight_layout()
plt.savefig('para_compare')
plt.close()