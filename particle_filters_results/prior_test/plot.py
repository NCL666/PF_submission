import numpy as np 
import matplotlib.pyplot as plt 

""" Read No Redraw Data"""
test_file = np.genfromtxt('para_EPN_MSE_redraw_0.csv', delimiter=',')

para_rejection_redraw_0_EPN = test_file[:,0]
para_rejection_redraw_0_MSE = np.sqrt(test_file[:,1])
para_rejection_redraw_0_time = test_file[:,2]

para_metropolis_redraw_0_EPN = test_file[:,3]
para_metropolis_redraw_0_MSE = np.sqrt(test_file[:,4])
para_metropolis_redraw_0_time = test_file[:,5]

para_systematic_redraw_0_EPN = test_file[:,6]
para_systematic_redraw_0_MSE = np.sqrt(test_file[:,7])
para_systematic_redraw_0_time = test_file[:,8]

para_stratified_redraw_0_EPN = test_file[:,9]
para_stratified_redraw_0_MSE = np.sqrt(test_file[:,10])
para_stratified_redraw_0_time = test_file[:,11]

""" Read 1 Redraw Data"""
test_file = np.genfromtxt('para_EPN_MSE_redraw_1.csv', delimiter=',')

para_rejection_redraw_1_EPN = test_file[:,0]
para_rejection_redraw_1_MSE = np.sqrt(test_file[:,1])
para_rejection_redraw_1_time = test_file[:,2]

para_metropolis_redraw_1_EPN = test_file[:,3]
para_metropolis_redraw_1_MSE = np.sqrt(test_file[:,4])
para_metropolis_redraw_1_time = test_file[:,5]

para_systematic_redraw_1_EPN = test_file[:,6]
para_systematic_redraw_1_MSE = np.sqrt(test_file[:,7])
para_systematic_redraw_1_time = test_file[:,8]

para_stratified_redraw_1_EPN = test_file[:,9]
para_stratified_redraw_1_MSE = np.sqrt(test_file[:,10])
para_stratified_redraw_1_time = test_file[:,11]

""" Read 2 Redraw Data"""
test_file = np.genfromtxt('para_EPN_MSE_redraw_2.csv', delimiter=',')

para_rejection_redraw_2_EPN = test_file[:,0]
para_rejection_redraw_2_MSE = np.sqrt(test_file[:,1])
para_rejection_redraw_2_time = test_file[:,2]

para_metropolis_redraw_2_EPN = test_file[:,3]
para_metropolis_redraw_2_MSE = np.sqrt(test_file[:,4])
para_metropolis_redraw_2_time = test_file[:,5]

para_systematic_redraw_2_EPN = test_file[:,6]
para_systematic_redraw_2_MSE = np.sqrt(test_file[:,7])
para_systematic_redraw_2_time = test_file[:,8]

para_stratified_redraw_2_EPN = test_file[:,9]
para_stratified_redraw_2_MSE = np.sqrt(test_file[:,10])
para_stratified_redraw_2_time = test_file[:,11]

""" Read 3 Redraw Data"""
test_file = np.genfromtxt('para_EPN_MSE_redraw_3.csv', delimiter=',')

para_rejection_redraw_3_EPN = test_file[:,0]
para_rejection_redraw_3_MSE = np.sqrt(test_file[:,1])
para_rejection_redraw_3_time = test_file[:,2]

para_metropolis_redraw_3_EPN = test_file[:,3]
para_metropolis_redraw_3_MSE = np.sqrt(test_file[:,4])
para_metropolis_redraw_3_time = test_file[:,5]

para_systematic_redraw_3_EPN = test_file[:,6]
para_systematic_redraw_3_MSE = np.sqrt(test_file[:,7])
para_systematic_redraw_3_time = test_file[:,8]

para_stratified_redraw_3_EPN = test_file[:,9]
para_stratified_redraw_3_MSE = np.sqrt(test_file[:,10])
para_stratified_redraw_3_time = test_file[:,11]

# set up the N_vec
N_num = len(para_rejection_redraw_0_EPN)
N_vec = np.zeros(N_num)
for i in range(N_num):
    N_vec[i] =  2**(2*i+6)

# Calculate the EPN ratio
# redraw 0
para_rejection_redraw_0_EPN_ratio = np.divide(para_rejection_redraw_0_EPN,N_vec)
para_metropolis_redraw_0_EPN_ratio = np.divide(para_metropolis_redraw_0_EPN,N_vec)
para_systematic_redraw_0_EPN_ratio = np.divide(para_systematic_redraw_0_EPN,N_vec)
para_stratified_redraw_0_EPN_ratio = np.divide(para_stratified_redraw_0_EPN,N_vec)
# redraw 1
para_rejection_redraw_1_EPN_ratio = np.divide(para_rejection_redraw_1_EPN,N_vec)
para_metropolis_redraw_1_EPN_ratio = np.divide(para_metropolis_redraw_1_EPN,N_vec)
para_systematic_redraw_1_EPN_ratio = np.divide(para_systematic_redraw_1_EPN,N_vec)
para_stratified_redraw_1_EPN_ratio = np.divide(para_stratified_redraw_1_EPN,N_vec)
# redraw 2
para_rejection_redraw_2_EPN_ratio = np.divide(para_rejection_redraw_2_EPN,N_vec)
para_metropolis_redraw_2_EPN_ratio = np.divide(para_metropolis_redraw_2_EPN,N_vec)
para_systematic_redraw_2_EPN_ratio = np.divide(para_systematic_redraw_2_EPN,N_vec)
para_stratified_redraw_2_EPN_ratio = np.divide(para_stratified_redraw_2_EPN,N_vec)
# redraw 3
para_rejection_redraw_3_EPN_ratio = np.divide(para_rejection_redraw_3_EPN,N_vec)
para_metropolis_redraw_3_EPN_ratio = np.divide(para_metropolis_redraw_3_EPN,N_vec)
para_systematic_redraw_3_EPN_ratio = np.divide(para_systematic_redraw_3_EPN,N_vec)
para_stratified_redraw_3_EPN_ratio = np.divide(para_stratified_redraw_3_EPN,N_vec)


# subplots for EPN set up
plt.figure()
plt.subplots(2, 2, figsize = (16,16))

# para rejection EPN Ratio plot
plt.subplot(221)
plt.plot(N_vec, para_rejection_redraw_0_EPN_ratio, 'x-', label = "redraw = 0")
plt.plot(N_vec, para_rejection_redraw_1_EPN_ratio, 'x-', label = "redraw = 1")
plt.plot(N_vec, para_rejection_redraw_2_EPN_ratio, 'x-', label = "redraw = 2")
plt.plot(N_vec, para_rejection_redraw_3_EPN_ratio, 'x-', label = "redraw = 3")
plt.xscale('log', base = 2 )
plt.xlabel('N -- Number of Particles')
plt.ylabel('Effective Particles Number Ratio')
plt.legend()
plt.title('Parallel Rejection')

# para metropolis EPN Ratio plot
plt.subplot(222)
plt.plot(N_vec, para_metropolis_redraw_0_EPN_ratio, 'x-', label = "redraw = 0")
plt.plot(N_vec, para_metropolis_redraw_1_EPN_ratio, 'x-', label = "redraw = 1")
plt.plot(N_vec, para_metropolis_redraw_2_EPN_ratio, 'x-', label = "redraw = 2")
plt.plot(N_vec, para_metropolis_redraw_3_EPN_ratio, 'x-', label = "redraw = 3")
plt.xscale('log', base = 2 )
plt.xlabel('N -- Number of Particles')
plt.ylabel('Effective Particles Number Ratio')
plt.legend()
plt.title('Parallel Metropolis')

# para systematic EPN Ratio plot
plt.subplot(223)
plt.plot(N_vec, para_systematic_redraw_0_EPN_ratio, 'x-', label = "redraw = 0")
plt.plot(N_vec, para_systematic_redraw_1_EPN_ratio, 'x-', label = "redraw = 1")
plt.plot(N_vec, para_systematic_redraw_2_EPN_ratio, 'x-', label = "redraw = 2")
plt.plot(N_vec, para_systematic_redraw_3_EPN_ratio, 'x-', label = "redraw = 3")
plt.xscale('log', base = 2 )
plt.xlabel('N -- Number of Particles')
plt.ylabel('Effective Particles Number Ratio')
plt.legend()
plt.title('Parallel Systematic')

# para stratified EPN Ratio plot
plt.subplot(224)
plt.plot(N_vec, para_stratified_redraw_0_EPN_ratio, 'x-', label = "redraw = 0")
plt.plot(N_vec, para_stratified_redraw_1_EPN_ratio, 'x-', label = "redraw = 1")
plt.plot(N_vec, para_stratified_redraw_2_EPN_ratio, 'x-', label = "redraw = 2")
plt.plot(N_vec, para_stratified_redraw_3_EPN_ratio, 'x-', label = "redraw = 3")
plt.xscale('log', base = 2 )
plt.xlabel('N -- Number of Particles')
plt.ylabel('Effective Particles Number Ratio')
plt.legend()
plt.title('Parallel Stratified')

plt.savefig('prior_EPN')
plt.close()



# subplots for MSE set up
plt.figure()
plt.subplots(2, 2, figsize = (16,16))

# para rejection MSE plot
plt.subplot(221)
plt.plot(N_vec, para_rejection_redraw_0_MSE, 'x-', label = "redraw = 0")
plt.plot(N_vec, para_rejection_redraw_1_MSE, 'x-', label = "redraw = 1")
plt.plot(N_vec, para_rejection_redraw_2_MSE, 'x-', label = "redraw = 2")
plt.plot(N_vec, para_rejection_redraw_3_MSE, 'x-', label = "redraw = 3")
plt.xscale('log', base = 2)
plt.yscale('log', base = 2)
plt.xlabel('N -- Number of Particles')
plt.ylabel('RMSE')
plt.legend()
plt.title('Parallel Rejection')

# para metropolis MSE plot
plt.subplot(222)
plt.plot(N_vec, para_metropolis_redraw_0_MSE, 'x-', label = "redraw = 0")
plt.plot(N_vec, para_metropolis_redraw_1_MSE, 'x-', label = "redraw = 1")
plt.plot(N_vec, para_metropolis_redraw_2_MSE, 'x-', label = "redraw = 2")
plt.plot(N_vec, para_metropolis_redraw_3_MSE, 'x-', label = "redraw = 3")
plt.xscale('log', base = 2)
plt.yscale('log', base = 2)
plt.xlabel('N -- Number of Particles')
plt.ylabel('RMSE')
plt.legend()
plt.title('Parallel Metropolis')

# para systematic MSE plot
plt.subplot(223)
plt.plot(N_vec, para_systematic_redraw_0_MSE, 'x-', label = "redraw = 0")
plt.plot(N_vec, para_systematic_redraw_1_MSE, 'x-', label = "redraw = 1")
plt.plot(N_vec, para_systematic_redraw_2_MSE, 'x-', label = "redraw = 2")
plt.plot(N_vec, para_systematic_redraw_3_MSE, 'x-', label = "redraw = 3")
plt.xscale('log', base = 2)
plt.yscale('log', base = 2)
plt.xlabel('N -- Number of Particles')
plt.ylabel('RMSE')
plt.legend()
plt.title('Parallel Systematic')

# para stratified MSE plot
plt.subplot(224)
plt.plot(N_vec, para_stratified_redraw_0_MSE, 'x-', label = "redraw = 0")
plt.plot(N_vec, para_stratified_redraw_1_MSE, 'x-', label = "redraw = 1")
plt.plot(N_vec, para_stratified_redraw_2_MSE, 'x-', label = "redraw = 2")
plt.plot(N_vec, para_stratified_redraw_3_MSE, 'x-', label = "redraw = 3")
plt.xscale('log', base = 2)
plt.yscale('log', base = 2)
plt.xlabel('N -- Number of Particles')
plt.ylabel('RMSE')
plt.legend()
plt.title('Parallel stratified')

plt.savefig('prior_MSE')
plt.close()


# subplots for time set up
plt.figure()
plt.subplots(2, 2, figsize = (16,16))

# para rejection time plot
plt.subplot(221)
plt.plot(N_vec, np.divide(para_rejection_redraw_0_time, para_rejection_redraw_0_time), 'x-', label = "redraw = 0")
plt.plot(N_vec, np.divide(para_rejection_redraw_1_time, para_rejection_redraw_0_time), 'x-', label = "redraw = 1")
plt.plot(N_vec, np.divide(para_rejection_redraw_2_time, para_rejection_redraw_0_time), 'x-', label = "redraw = 2")
plt.plot(N_vec, np.divide(para_rejection_redraw_3_time, para_rejection_redraw_0_time), 'x-', label = "redraw = 3")
plt.xscale('log', base = 2)
plt.xlabel('N -- Number of Particles')
plt.ylabel('Time Ratio')
plt.legend()
plt.title('Parallel Rejection')

# para metropolis time plot
plt.subplot(222)
plt.plot(N_vec, np.divide(para_metropolis_redraw_0_time, para_metropolis_redraw_0_time), 'x-', label = "redraw = 0")
plt.plot(N_vec, np.divide(para_metropolis_redraw_1_time, para_metropolis_redraw_0_time), 'x-', label = "redraw = 1")
plt.plot(N_vec, np.divide(para_metropolis_redraw_2_time, para_metropolis_redraw_0_time), 'x-', label = "redraw = 2")
plt.plot(N_vec, np.divide(para_metropolis_redraw_3_time, para_metropolis_redraw_0_time), 'x-', label = "redraw = 3")
plt.xscale('log', base = 2)
plt.xlabel('N -- Number of Particles')
plt.ylabel('Time Ratio')
plt.legend()
plt.title('Parallel Metropolis')

# para systematic MSE plot
plt.subplot(223)
plt.plot(N_vec, np.divide(para_systematic_redraw_0_time, para_systematic_redraw_0_time), 'x-', label = "redraw = 0")
plt.plot(N_vec, np.divide(para_systematic_redraw_1_time, para_systematic_redraw_0_time), 'x-', label = "redraw = 1")
plt.plot(N_vec, np.divide(para_systematic_redraw_2_time, para_systematic_redraw_0_time), 'x-', label = "redraw = 2")
plt.plot(N_vec, np.divide(para_systematic_redraw_3_time, para_systematic_redraw_0_time), 'x-', label = "redraw = 3")
plt.xscale('log', base = 2)
plt.xlabel('N -- Number of Particles')
plt.ylabel('Time Ratio')
plt.legend()
plt.title('Parallel Systematic')

# para stratified time plot
plt.subplot(224)
plt.plot(N_vec, np.divide(para_stratified_redraw_0_time, para_stratified_redraw_0_time), 'x-', label = "redraw = 0")
plt.plot(N_vec, np.divide(para_stratified_redraw_1_time, para_stratified_redraw_0_time), 'x-', label = "redraw = 1")
plt.plot(N_vec, np.divide(para_stratified_redraw_2_time, para_stratified_redraw_0_time), 'x-', label = "redraw = 2")
plt.plot(N_vec, np.divide(para_stratified_redraw_3_time, para_stratified_redraw_0_time), 'x-', label = "redraw = 3")
plt.xscale('log', base = 2)
plt.xlabel('N -- Number of Particles')
plt.ylabel('Time Ratio')
plt.legend()
plt.title('Parallel stratified')

plt.savefig('prior_time')
plt.close()