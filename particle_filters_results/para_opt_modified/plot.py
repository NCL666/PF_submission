import numpy as np 
import matplotlib.pyplot as plt 

opt_redraw_0_EPN_threshold_25_rough_var_1 = np.genfromtxt('opt_redraw_0_EPN_threshold_25_rough_var_1.csv', delimiter = ',')
opt_redraw_0_EPN_threshold_50_rough_var_1 = np.genfromtxt('opt_redraw_0_EPN_threshold_50_rough_var_1.csv', delimiter = ',')
opt_redraw_0_EPN_threshold_75_rough_var_1 = np.genfromtxt('opt_redraw_0_EPN_threshold_75_rough_var_1.csv', delimiter = ',')


opt_redraw_3_EPN_threshold_75_rough_var_0 = np.genfromtxt('opt_redraw_3_EPN_threshold_75_rough_var_0.csv', delimiter = ',')
opt_redraw_3_EPN_threshold_75_rough_var_1 = np.genfromtxt('opt_redraw_3_EPN_threshold_75_rough_var_1.csv', delimiter = ',')

# get epn data from table when variance n change
rejection_redraw_0_EPN_threshold_25_rough_var_1_EPN = opt_redraw_0_EPN_threshold_25_rough_var_1[:, 0]
metropolis_redraw_0_EPN_threshold_25_rough_var_1_EPN = opt_redraw_0_EPN_threshold_25_rough_var_1[:, 3]
systematic_redraw_0_EPN_threshold_25_rough_var_1_EPN = opt_redraw_0_EPN_threshold_25_rough_var_1[:, 6]
stratified_redraw_0_EPN_threshold_25_rough_var_1_EPN = opt_redraw_0_EPN_threshold_25_rough_var_1[:, 9]

# get rmse data from table when variance n change
rejection_redraw_0_EPN_threshold_25_rough_var_1_RMSE = np.sqrt(opt_redraw_0_EPN_threshold_25_rough_var_1[:, 1])
metropolis_redraw_0_EPN_threshold_25_rough_var_1_RMSE = np.sqrt(opt_redraw_0_EPN_threshold_25_rough_var_1[:, 4])
systematic_redraw_0_EPN_threshold_25_rough_var_1_RMSE = np.sqrt(opt_redraw_0_EPN_threshold_25_rough_var_1[:, 7])
stratified_redraw_0_EPN_threshold_25_rough_var_1_RMSE = np.sqrt(opt_redraw_0_EPN_threshold_25_rough_var_1[:, 10])

# get time data from time table when variance n change
rejection_redraw_0_EPN_threshold_25_rough_var_1_time = opt_redraw_0_EPN_threshold_25_rough_var_1[:, 2]
metropolis_redraw_0_EPN_threshold_25_rough_var_1_time = opt_redraw_0_EPN_threshold_25_rough_var_1[:, 5]
systematic_redraw_0_EPN_threshold_25_rough_var_1_time = opt_redraw_0_EPN_threshold_25_rough_var_1[:, 8]
stratified_redraw_0_EPN_threshold_25_rough_var_1_time = opt_redraw_0_EPN_threshold_25_rough_var_1[:, 11]


# get epn data from table when variance n change
rejection_redraw_0_EPN_threshold_50_rough_var_1_EPN = opt_redraw_0_EPN_threshold_50_rough_var_1[:, 0]
metropolis_redraw_0_EPN_threshold_50_rough_var_1_EPN = opt_redraw_0_EPN_threshold_50_rough_var_1[:, 3]
systematic_redraw_0_EPN_threshold_50_rough_var_1_EPN = opt_redraw_0_EPN_threshold_50_rough_var_1[:, 6]
stratified_redraw_0_EPN_threshold_50_rough_var_1_EPN = opt_redraw_0_EPN_threshold_50_rough_var_1[:, 9]

# get rmse data from table when variance n change
rejection_redraw_0_EPN_threshold_50_rough_var_1_RMSE = np.sqrt(opt_redraw_0_EPN_threshold_50_rough_var_1[:, 1])
metropolis_redraw_0_EPN_threshold_50_rough_var_1_RMSE = np.sqrt(opt_redraw_0_EPN_threshold_50_rough_var_1[:, 4])
systematic_redraw_0_EPN_threshold_50_rough_var_1_RMSE = np.sqrt(opt_redraw_0_EPN_threshold_50_rough_var_1[:, 7])
stratified_redraw_0_EPN_threshold_50_rough_var_1_RMSE = np.sqrt(opt_redraw_0_EPN_threshold_50_rough_var_1[:, 10])

# get time data from table when variance n change
rejection_redraw_0_EPN_threshold_50_rough_var_1_time = opt_redraw_0_EPN_threshold_50_rough_var_1[:, 2]
metropolis_redraw_0_EPN_threshold_50_rough_var_1_time = opt_redraw_0_EPN_threshold_50_rough_var_1[:, 5]
systematic_redraw_0_EPN_threshold_50_rough_var_1_time = opt_redraw_0_EPN_threshold_50_rough_var_1[:, 8]
stratified_redraw_0_EPN_threshold_50_rough_var_1_time = opt_redraw_0_EPN_threshold_50_rough_var_1[:, 11]

# get epn data from table when variance n change
rejection_redraw_0_EPN_threshold_75_rough_var_1_EPN = opt_redraw_0_EPN_threshold_75_rough_var_1[:, 0]
metropolis_redraw_0_EPN_threshold_75_rough_var_1_EPN = opt_redraw_0_EPN_threshold_75_rough_var_1[:, 3]
systematic_redraw_0_EPN_threshold_75_rough_var_1_EPN = opt_redraw_0_EPN_threshold_75_rough_var_1[:, 6]
stratified_redraw_0_EPN_threshold_75_rough_var_1_EPN = opt_redraw_0_EPN_threshold_75_rough_var_1[:, 9]

# get time data from table when variance n change
rejection_redraw_0_EPN_threshold_75_rough_var_1_RMSE = np.sqrt(opt_redraw_0_EPN_threshold_75_rough_var_1[:, 1])
metropolis_redraw_0_EPN_threshold_75_rough_var_1_RMSE = np.sqrt(opt_redraw_0_EPN_threshold_75_rough_var_1[:, 4])
systematic_redraw_0_EPN_threshold_75_rough_var_1_RMSE = np.sqrt(opt_redraw_0_EPN_threshold_75_rough_var_1[:, 7])
stratified_redraw_0_EPN_threshold_75_rough_var_1_RMSE = np.sqrt(opt_redraw_0_EPN_threshold_75_rough_var_1[:, 10])

# get time data from table when variance n change
rejection_redraw_0_EPN_threshold_75_rough_var_1_time = opt_redraw_0_EPN_threshold_75_rough_var_1[:, 2]
metropolis_redraw_0_EPN_threshold_75_rough_var_1_time = opt_redraw_0_EPN_threshold_75_rough_var_1[:, 5]
systematic_redraw_0_EPN_threshold_75_rough_var_1_time = opt_redraw_0_EPN_threshold_75_rough_var_1[:, 8]
stratified_redraw_0_EPN_threshold_75_rough_var_1_time = opt_redraw_0_EPN_threshold_75_rough_var_1[:, 11]

# get epn data from table when variance n change
rejection_redraw_3_EPN_threshold_75_rough_var_0_EPN = opt_redraw_3_EPN_threshold_75_rough_var_0[:, 0]
metropolis_redraw_3_EPN_threshold_75_rough_var_0_EPN = opt_redraw_3_EPN_threshold_75_rough_var_0[:, 3]
systematic_redraw_3_EPN_threshold_75_rough_var_0_EPN = opt_redraw_3_EPN_threshold_75_rough_var_0[:, 6]
stratified_redraw_3_EPN_threshold_75_rough_var_0_EPN = opt_redraw_3_EPN_threshold_75_rough_var_0[:, 9]

# get time data from table when variance n change
rejection_redraw_3_EPN_threshold_75_rough_var_0_RMSE = np.sqrt(opt_redraw_3_EPN_threshold_75_rough_var_0[:, 1])
metropolis_redraw_3_EPN_threshold_75_rough_var_0_RMSE = np.sqrt(opt_redraw_3_EPN_threshold_75_rough_var_0[:, 4])
systematic_redraw_3_EPN_threshold_75_rough_var_0_RMSE = np.sqrt(opt_redraw_3_EPN_threshold_75_rough_var_0[:, 7])
stratified_redraw_3_EPN_threshold_75_rough_var_0_RMSE = np.sqrt(opt_redraw_3_EPN_threshold_75_rough_var_0[:, 10])

# get time data from table when variance n change
rejection_redraw_3_EPN_threshold_75_rough_var_0_time = opt_redraw_3_EPN_threshold_75_rough_var_0[:, 2]
metropolis_redraw_3_EPN_threshold_75_rough_var_0_time = opt_redraw_3_EPN_threshold_75_rough_var_0[:, 5]
systematic_redraw_3_EPN_threshold_75_rough_var_0_time = opt_redraw_3_EPN_threshold_75_rough_var_0[:, 8]
stratified_redraw_3_EPN_threshold_75_rough_var_0_time = opt_redraw_3_EPN_threshold_75_rough_var_0[:, 11]

# get epn data from table when variance n change
rejection_redraw_3_EPN_threshold_75_rough_var_1_EPN = opt_redraw_3_EPN_threshold_75_rough_var_1[:, 0]
metropolis_redraw_3_EPN_threshold_75_rough_var_1_EPN = opt_redraw_3_EPN_threshold_75_rough_var_1[:, 3]
systematic_redraw_3_EPN_threshold_75_rough_var_1_EPN = opt_redraw_3_EPN_threshold_75_rough_var_1[:, 6]
stratified_redraw_3_EPN_threshold_75_rough_var_1_EPN = opt_redraw_3_EPN_threshold_75_rough_var_1[:, 9]

# get time data from table when variance n change
rejection_redraw_3_EPN_threshold_75_rough_var_1_RMSE = np.sqrt(opt_redraw_3_EPN_threshold_75_rough_var_1[:, 1])
metropolis_redraw_3_EPN_threshold_75_rough_var_1_RMSE = np.sqrt(opt_redraw_3_EPN_threshold_75_rough_var_1[:, 4])
systematic_redraw_3_EPN_threshold_75_rough_var_1_RMSE = np.sqrt(opt_redraw_3_EPN_threshold_75_rough_var_1[:, 7])
stratified_redraw_3_EPN_threshold_75_rough_var_1_RMSE = np.sqrt(opt_redraw_3_EPN_threshold_75_rough_var_1[:, 10])

# get time data from table when variance n change
rejection_redraw_3_EPN_threshold_75_rough_var_1_time = opt_redraw_3_EPN_threshold_75_rough_var_1[:, 2]
metropolis_redraw_3_EPN_threshold_75_rough_var_1_time = opt_redraw_3_EPN_threshold_75_rough_var_1[:, 5]
systematic_redraw_3_EPN_threshold_75_rough_var_1_time = opt_redraw_3_EPN_threshold_75_rough_var_1[:, 8]
stratified_redraw_3_EPN_threshold_75_rough_var_1_time = opt_redraw_3_EPN_threshold_75_rough_var_1[:, 11]

# N_vec setup
N_num = 6
N_vec = np.zeros(N_num)
for i in range(N_num):
    N_vec[i] = 2**(2*i+6)
    print(N_vec[i] * 0.35)

# EPN Ratio Calculation
rejection_redraw_0_EPN_threshold_25_rough_var_1_EPN_ratio = np.divide(rejection_redraw_0_EPN_threshold_25_rough_var_1_EPN, N_vec)
metropolis_redraw_0_EPN_threshold_25_rough_var_1_EPN_ratio = np.divide(metropolis_redraw_0_EPN_threshold_25_rough_var_1_EPN, N_vec)
systematic_redraw_0_EPN_threshold_25_rough_var_1_EPN_ratio = np.divide(systematic_redraw_0_EPN_threshold_25_rough_var_1_EPN, N_vec)
stratified_redraw_0_EPN_threshold_25_rough_var_1_EPN_ratio = np.divide(stratified_redraw_0_EPN_threshold_25_rough_var_1_EPN, N_vec)

rejection_redraw_0_EPN_threshold_50_rough_var_1_EPN_ratio = np.divide(rejection_redraw_0_EPN_threshold_50_rough_var_1_EPN, N_vec)
metropolis_redraw_0_EPN_threshold_50_rough_var_1_EPN_ratio = np.divide(metropolis_redraw_0_EPN_threshold_50_rough_var_1_EPN, N_vec)
systematic_redraw_0_EPN_threshold_50_rough_var_1_EPN_ratio = np.divide(systematic_redraw_0_EPN_threshold_50_rough_var_1_EPN, N_vec)
stratified_redraw_0_EPN_threshold_50_rough_var_1_EPN_ratio = np.divide(stratified_redraw_0_EPN_threshold_50_rough_var_1_EPN, N_vec)

rejection_redraw_0_EPN_threshold_75_rough_var_1_EPN_ratio = np.divide(rejection_redraw_0_EPN_threshold_75_rough_var_1_EPN, N_vec)
metropolis_redraw_0_EPN_threshold_75_rough_var_1_EPN_ratio = np.divide(metropolis_redraw_0_EPN_threshold_75_rough_var_1_EPN, N_vec)
systematic_redraw_0_EPN_threshold_75_rough_var_1_EPN_ratio = np.divide(systematic_redraw_0_EPN_threshold_75_rough_var_1_EPN, N_vec)
stratified_redraw_0_EPN_threshold_75_rough_var_1_EPN_ratio = np.divide(stratified_redraw_0_EPN_threshold_75_rough_var_1_EPN, N_vec)


# subplot setup -- EPN
plt.subplots(2, 2, figsize = (16,16))

plt.subplot(221)
plt.title('Rejection Resampling')

plt.plot(N_vec, rejection_redraw_0_EPN_threshold_25_rough_var_1_EPN_ratio, 'x-', label = 'Threshold = 0.25', c = '#2F9599')
plt.plot(N_vec, rejection_redraw_0_EPN_threshold_50_rough_var_1_EPN_ratio, 'x-', label = 'Threshold = 0.50', c = '#A7226E')
plt.plot(N_vec, rejection_redraw_0_EPN_threshold_75_rough_var_1_EPN_ratio, 'x-', label = 'Threshold = 0.75', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('Effective Particle Ratio')
plt.legend()


plt.subplot(222)
plt.title('Metropolis Resampling')

plt.plot(N_vec, metropolis_redraw_0_EPN_threshold_25_rough_var_1_EPN_ratio, 'x-', label = 'Threshold = 0.25', c = '#2F9599')
plt.plot(N_vec, metropolis_redraw_0_EPN_threshold_50_rough_var_1_EPN_ratio, 'x-', label = 'Threshold = 0.50', c = '#A7226E')
plt.plot(N_vec, metropolis_redraw_0_EPN_threshold_75_rough_var_1_EPN_ratio, 'x-', label = 'Threshold = 0.75', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('Effective Particle Ratio')
plt.legend()


plt.subplot(223)
plt.title('Systematic Resampling')

plt.plot(N_vec, systematic_redraw_0_EPN_threshold_25_rough_var_1_EPN_ratio, 'x-', label = 'Threshold = 0.25', c = '#2F9599')
plt.plot(N_vec, systematic_redraw_0_EPN_threshold_50_rough_var_1_EPN_ratio, 'x-', label = 'Threshold = 0.50', c = '#A7226E')
plt.plot(N_vec, systematic_redraw_0_EPN_threshold_75_rough_var_1_EPN_ratio, 'x-', label = 'Threshold = 0.75', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('Effective Particle Ratio')
plt.legend()

plt.subplot(224)
plt.title('Stratified Resampling')

plt.plot(N_vec, stratified_redraw_0_EPN_threshold_25_rough_var_1_EPN_ratio, 'x-', label = 'Threshold = 0.25', c = '#2F9599')
plt.plot(N_vec, stratified_redraw_0_EPN_threshold_50_rough_var_1_EPN_ratio, 'x-', label = 'Threshold = 0.50', c = '#A7226E')
plt.plot(N_vec, stratified_redraw_0_EPN_threshold_75_rough_var_1_EPN_ratio, 'x-', label = 'Threshold = 0.75', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('Effective Particle Ratio')
plt.legend()

plt.savefig('opt_EPN')
plt.close()

# subplot setup -- rmse
plt.subplots(2, 2, figsize = (16,16))

plt.subplot(221)
plt.title('Rejection Resampling')

plt.plot(N_vec, rejection_redraw_0_EPN_threshold_25_rough_var_1_RMSE, 'x-', label = 'Threshold = 0.25', c = '#2F9599')
plt.plot(N_vec, rejection_redraw_0_EPN_threshold_50_rough_var_1_RMSE, 'x-', label = 'Threshold = 0.50', c = '#A7226E')
plt.plot(N_vec, rejection_redraw_0_EPN_threshold_75_rough_var_1_RMSE, 'x-', label = 'Threshold = 0.75', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('RMSE')
plt.legend()


plt.subplot(222)
plt.title('Metropolis Resampling')

plt.plot(N_vec, metropolis_redraw_0_EPN_threshold_25_rough_var_1_RMSE, 'x-', label = 'Threshold = 0.25', c = '#2F9599')
plt.plot(N_vec, metropolis_redraw_0_EPN_threshold_50_rough_var_1_RMSE, 'x-', label = 'Threshold = 0.50', c = '#A7226E')
plt.plot(N_vec, metropolis_redraw_0_EPN_threshold_75_rough_var_1_RMSE, 'x-', label = 'Threshold = 0.75', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('RMSE')
plt.legend()


plt.subplot(223)
plt.title('Systematic Resampling')

plt.plot(N_vec, systematic_redraw_0_EPN_threshold_25_rough_var_1_RMSE, 'x-', label = 'Threshold = 0.25', c = '#2F9599')
plt.plot(N_vec, systematic_redraw_0_EPN_threshold_50_rough_var_1_RMSE, 'x-', label = 'Threshold = 0.50', c = '#A7226E')
plt.plot(N_vec, systematic_redraw_0_EPN_threshold_75_rough_var_1_RMSE, 'x-', label = 'Threshold = 0.75', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('RMSE')
plt.legend()

plt.subplot(224)
plt.title('Stratified Resampling')

plt.plot(N_vec, stratified_redraw_0_EPN_threshold_25_rough_var_1_RMSE, 'x-', label = 'Threshold = 0.25', c = '#2F9599')
plt.plot(N_vec, stratified_redraw_0_EPN_threshold_50_rough_var_1_RMSE, 'x-', label = 'Threshold = 0.50', c = '#A7226E')
plt.plot(N_vec, stratified_redraw_0_EPN_threshold_75_rough_var_1_RMSE, 'x-', label = 'Threshold = 0.75', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('RMSE')
plt.legend()

plt.savefig('opt_rmse')



# subplot setup -- time
plt.subplots(2, 2, figsize = (16,16))

plt.subplot(221)
plt.title('Rejection Resampling')

plt.plot(N_vec, np.divide(rejection_redraw_0_EPN_threshold_25_rough_var_1_time, rejection_redraw_0_EPN_threshold_25_rough_var_1_time), 'x-', label = 'Threshold = 0.25', c = '#2F9599')
plt.plot(N_vec, np.divide(rejection_redraw_0_EPN_threshold_50_rough_var_1_time, rejection_redraw_0_EPN_threshold_25_rough_var_1_time), 'x-', label = 'Threshold = 0.50', c = '#A7226E')
plt.plot(N_vec, np.divide(rejection_redraw_0_EPN_threshold_75_rough_var_1_time, rejection_redraw_0_EPN_threshold_25_rough_var_1_time), 'x-', label = 'Threshold = 0.75', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('Time Ratio')
plt.ylim(0.95,1.2)
plt.legend()


plt.subplot(222)
plt.title('Metropolis Resampling')

plt.plot(N_vec, np.divide(metropolis_redraw_0_EPN_threshold_25_rough_var_1_time, metropolis_redraw_0_EPN_threshold_25_rough_var_1_time), 'x-', label = 'Threshold = 0.25', c = '#2F9599')
plt.plot(N_vec, np.divide(metropolis_redraw_0_EPN_threshold_50_rough_var_1_time, metropolis_redraw_0_EPN_threshold_25_rough_var_1_time), 'x-', label = 'Threshold = 0.50', c = '#A7226E')
plt.plot(N_vec, np.divide(metropolis_redraw_0_EPN_threshold_75_rough_var_1_time, metropolis_redraw_0_EPN_threshold_25_rough_var_1_time), 'x-', label = 'Threshold = 0.75', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('Time Ratio')
plt.ylim(0.95,1.2)
plt.legend()


plt.subplot(223)
plt.title('Systematic Resampling')

plt.plot(N_vec, np.divide(systematic_redraw_0_EPN_threshold_25_rough_var_1_time, systematic_redraw_0_EPN_threshold_25_rough_var_1_time), 'x-', label = 'Threshold = 0.25', c = '#2F9599')
plt.plot(N_vec, np.divide(systematic_redraw_0_EPN_threshold_50_rough_var_1_time, systematic_redraw_0_EPN_threshold_25_rough_var_1_time), 'x-', label = 'Threshold = 0.50', c = '#A7226E')
plt.plot(N_vec, np.divide(systematic_redraw_0_EPN_threshold_75_rough_var_1_time, systematic_redraw_0_EPN_threshold_25_rough_var_1_time), 'x-', label = 'Threshold = 0.75', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('Time Ratio')
plt.ylim(0.95,1.2)
plt.legend()

plt.subplot(224)
plt.title('Stratified Resampling')

plt.plot(N_vec, np.divide(stratified_redraw_0_EPN_threshold_25_rough_var_1_time, stratified_redraw_0_EPN_threshold_25_rough_var_1_time), 'x-', label = 'Threshold = 0.25', c = '#2F9599')
plt.plot(N_vec, np.divide(stratified_redraw_0_EPN_threshold_50_rough_var_1_time, stratified_redraw_0_EPN_threshold_25_rough_var_1_time), 'x-', label = 'Threshold = 0.50', c = '#A7226E')
plt.plot(N_vec, np.divide(stratified_redraw_0_EPN_threshold_75_rough_var_1_time, stratified_redraw_0_EPN_threshold_25_rough_var_1_time), 'x-', label = 'Threshold = 0.75', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('Time Ratio')
plt.ylim(0.95,1.2)
plt.legend()

plt.savefig('opt_time')


# subplot setup -- redraw 3 EPN ratio
plt.subplots(2, 2, figsize = (16,16))
plt.subplot(221)
plt.title('Rejection Resampling')
plt.plot(N_vec, np.divide(rejection_redraw_0_EPN_threshold_75_rough_var_1_EPN, N_vec), 'x-', label = 'T=0.75,R=0,V=0', c = '#2F9599')
plt.plot(N_vec, np.divide(rejection_redraw_3_EPN_threshold_75_rough_var_0_EPN, N_vec), 'x-', label = 'T=0.75,R=3,V=0', c = '#A7226E')
plt.plot(N_vec, np.divide(rejection_redraw_3_EPN_threshold_75_rough_var_1_EPN, N_vec), 'x-', label = 'T=0.75,R=3,V=1', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('Effective Particle Ratio')
plt.legend()


plt.subplot(222)
plt.title('Metropolis Resampling')

plt.plot(N_vec, np.divide(metropolis_redraw_0_EPN_threshold_75_rough_var_1_EPN, N_vec), 'x-', label = 'T=0.75,R=0,V=0', c = '#2F9599')
plt.plot(N_vec, np.divide(metropolis_redraw_3_EPN_threshold_75_rough_var_0_EPN, N_vec), 'x-', label = 'T=0.75,R=3,V=0', c = '#A7226E')
plt.plot(N_vec, np.divide(metropolis_redraw_3_EPN_threshold_75_rough_var_1_EPN, N_vec), 'x-', label = 'T=0.75,R=3,V=1', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('Effective Particle Ratio')
plt.legend()


plt.subplot(223)
plt.title('Systematic Resampling')

plt.plot(N_vec, np.divide(systematic_redraw_0_EPN_threshold_75_rough_var_1_EPN, N_vec), 'x-', label = 'T=0.75,R=0,V=0', c = '#2F9599')
plt.plot(N_vec, np.divide(systematic_redraw_3_EPN_threshold_75_rough_var_0_EPN, N_vec), 'x-', label = 'T=0.75,R=3,V=0', c = '#A7226E')
plt.plot(N_vec, np.divide(systematic_redraw_3_EPN_threshold_75_rough_var_1_EPN, N_vec), 'x-', label = 'T=0.75,R=3,V=1', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('Effective Particle Ratio')
plt.legend()

plt.subplot(224)
plt.title('Stratified Resampling')

plt.plot(N_vec, np.divide(stratified_redraw_0_EPN_threshold_75_rough_var_1_EPN, N_vec), 'x-', label = 'T=0.75,R=0,V=0', c = '#2F9599')
plt.plot(N_vec, np.divide(stratified_redraw_3_EPN_threshold_75_rough_var_0_EPN, N_vec), 'x-', label = 'T=0.75,R=3,V=0', c = '#A7226E')
plt.plot(N_vec, np.divide(stratified_redraw_3_EPN_threshold_75_rough_var_1_EPN, N_vec), 'x-', label = 'T=0.75,R=3,V=1', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('Effective Particle Ratio')
plt.legend()

plt.savefig('opt_redraw_3_EPN')

# subplot setup -- redraw 3 RMSE
plt.subplots(2, 2, figsize = (16,16))
plt.subplot(221)
plt.title('Rejection Resampling')
plt.plot(N_vec, rejection_redraw_0_EPN_threshold_75_rough_var_1_RMSE, 'x-', label = 'T=0.75,R=0,V=0', c = '#2F9599')
plt.plot(N_vec, rejection_redraw_3_EPN_threshold_75_rough_var_0_RMSE, 'x-', label = 'T=0.75,R=3,V=0', c = '#A7226E')
plt.plot(N_vec, rejection_redraw_3_EPN_threshold_75_rough_var_1_RMSE, 'x-', label = 'T=0.75,R=3,V=1', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('RMSE')
plt.legend()


plt.subplot(222)
plt.title('Metropolis Resampling')
plt.plot(N_vec, metropolis_redraw_0_EPN_threshold_75_rough_var_1_RMSE, 'x-', label = 'T=0.75,R=0,V=0', c = '#2F9599')
plt.plot(N_vec, metropolis_redraw_3_EPN_threshold_75_rough_var_0_RMSE, 'x-', label = 'T=0.75,R=3,V=0', c = '#A7226E')
plt.plot(N_vec, metropolis_redraw_3_EPN_threshold_75_rough_var_1_RMSE, 'x-', label = 'T=0.75,R=3,V=1', c = '#EC2049')


plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('RMSE')
plt.legend()


plt.subplot(223)
plt.title('Systematic Resampling')
plt.plot(N_vec, systematic_redraw_0_EPN_threshold_75_rough_var_1_RMSE, 'x-', label = 'T=0.75,R=0,V=0', c = '#2F9599')
plt.plot(N_vec, systematic_redraw_3_EPN_threshold_75_rough_var_0_RMSE, 'x-', label = 'T=0.75,R=3,V=0', c = '#A7226E')
plt.plot(N_vec, systematic_redraw_3_EPN_threshold_75_rough_var_1_RMSE, 'x-', label = 'T=0.75,R=3,V=1', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('RMSE')
plt.legend()

plt.subplot(224)
plt.title('Stratified Resampling')
plt.plot(N_vec, stratified_redraw_0_EPN_threshold_75_rough_var_1_RMSE, 'x-', label = 'T=0.75,R=0,V=0', c = '#2F9599')
plt.plot(N_vec, stratified_redraw_3_EPN_threshold_75_rough_var_0_RMSE, 'x-', label = 'T=0.75,R=3,V=0', c = '#A7226E')
plt.plot(N_vec, stratified_redraw_3_EPN_threshold_75_rough_var_1_RMSE, 'x-', label = 'T=0.75,R=3,V=1', c = '#EC2049')
plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('RMSE')
plt.legend()

plt.savefig('opt_redraw_3_rmse')

# subplot setup -- time
plt.subplots(2, 2, figsize = (16,16))

plt.subplot(221)
plt.title('Rejection Resampling')

plt.plot(N_vec, np.divide(rejection_redraw_0_EPN_threshold_75_rough_var_1_time, rejection_redraw_0_EPN_threshold_75_rough_var_1_time), 'x-', label = 'T=0.75,R=0,V=0', c = '#2F9599')
plt.plot(N_vec, np.divide(rejection_redraw_3_EPN_threshold_75_rough_var_0_time, rejection_redraw_0_EPN_threshold_75_rough_var_1_time), 'x-', label = 'T=0.75,R=3,V=0', c = '#A7226E')
plt.plot(N_vec, np.divide(rejection_redraw_3_EPN_threshold_75_rough_var_1_time, rejection_redraw_0_EPN_threshold_75_rough_var_1_time), 'x-', label = 'T=0.75,R=3,V=1', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylim(0.95,1.2)
plt.ylabel('Time Ratio')
plt.legend()


plt.subplot(222)
plt.title('Metropolis Resampling')

plt.plot(N_vec, np.divide(metropolis_redraw_0_EPN_threshold_75_rough_var_1_time, metropolis_redraw_0_EPN_threshold_75_rough_var_1_time), 'x-', label = 'T=0.75,R=0,V=0', c = '#2F9599')
plt.plot(N_vec, np.divide(metropolis_redraw_3_EPN_threshold_75_rough_var_0_time, metropolis_redraw_0_EPN_threshold_75_rough_var_1_time), 'x-', label = 'T=0.75,R=3,V=0', c = '#A7226E')
plt.plot(N_vec, np.divide(metropolis_redraw_3_EPN_threshold_75_rough_var_1_time, metropolis_redraw_0_EPN_threshold_75_rough_var_1_time), 'x-', label = 'T=0.75,R=3,V=01', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylim(0.95,1.2)
plt.ylabel('Time Ratio')
plt.legend()


plt.subplot(223)
plt.title('Systematic Resampling')

plt.plot(N_vec, np.divide(systematic_redraw_0_EPN_threshold_75_rough_var_1_time, systematic_redraw_0_EPN_threshold_75_rough_var_1_time), 'x-', label = 'T=0.75,R=0,V=0', c = '#2F9599')
plt.plot(N_vec, np.divide(systematic_redraw_3_EPN_threshold_75_rough_var_0_time, systematic_redraw_0_EPN_threshold_75_rough_var_1_time), 'x-', label = 'T=0.75,R=3,V=0', c = '#A7226E')
plt.plot(N_vec, np.divide(systematic_redraw_3_EPN_threshold_75_rough_var_1_time, systematic_redraw_0_EPN_threshold_75_rough_var_1_time), 'x-', label = 'T=0.75,R=3,V=1', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylim(0.95,1.2)
plt.ylabel('Time Ratio')
plt.legend()

plt.subplot(224)
plt.title('Stratified Resampling')

plt.plot(N_vec, np.divide(stratified_redraw_0_EPN_threshold_75_rough_var_1_time, stratified_redraw_0_EPN_threshold_75_rough_var_1_time), 'x-', label = 'T=0.75,R=0,V=0', c = '#2F9599')
plt.plot(N_vec, np.divide(stratified_redraw_3_EPN_threshold_75_rough_var_0_time, stratified_redraw_0_EPN_threshold_75_rough_var_1_time), 'x-', label = 'T=0.75,R=3,V=0', c = '#A7226E')
plt.plot(N_vec, np.divide(stratified_redraw_3_EPN_threshold_75_rough_var_1_time, stratified_redraw_0_EPN_threshold_75_rough_var_1_time), 'x-', label = 'T=0.75,R=3,V=1', c = '#EC2049')

plt.xlabel('Number of Particles')
plt.xscale('log', base = 2 )
plt.ylabel('Time Ratio')
plt.ylim(0.95,1.2)
plt.legend()

plt.savefig('opt_redraw_3_time')