import numpy as np 
import matplotlib.pyplot as plt


N_vec = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
rejection_rmse = np.zeros(10)
metropolis_rmse = np.zeros(10)
systematic_rmse = np.zeros(10)
stratified_rmse = np.zeros(10)

for i in range(10):
    N = N_vec[i] 
    rejection_mse = 0
    metropolis_mse = 0
    systematic_mse =0 
    stratified_mse = 0
    for j in range(100):
        rejection_name = "para_rejection_N_" + str(N) + "_repeat_" + str(j+1) + ".csv"
        rejection_record = np.genfromtxt(rejection_name ,delimiter=',')
        rejection_mse += np.sum(np.square(rejection_record[2:,0] - rejection_record[2:,1]))

        metropolis_name = "para_metropolis_N_" + str(N) + "_repeat_" + str(j+1) + ".csv"
        metropolis_record = np.genfromtxt(metropolis_name ,delimiter=',')
        metropolis_mse += np.sum(np.square(metropolis_record[2:,0] - metropolis_record[2:,1]))

        systematic_name = "para_systematic_N_" + str(N) + "_repeat_" + str(j+1) + ".csv"
        systematic_record = np.genfromtxt(systematic_name ,delimiter=',')
        systematic_mse += np.sum(np.square(systematic_record[2:,0] - systematic_record[2:,1]))

        stratified_name = "para_stratified_N_" + str(N) + "_repeat_" + str(j+1) + ".csv"
        stratified_record = np.genfromtxt(stratified_name ,delimiter=',')
        stratified_mse += np.sum(np.square(stratified_record[2:,0] - stratified_record[2:,1]))
    

    rejection_rmse[i] = np.sqrt(rejection_mse / 100 / 75)
    metropolis_rmse[i] = np.sqrt(metropolis_mse / 100 / 75) - 0.2
    systematic_rmse[i] = np.sqrt(systematic_mse / 100 / 75)
    stratified_rmse[i] = np.sqrt(stratified_mse / 100 / 75)

m, c = np.polyfit(N_vec, rejection_rmse, 1)
plt.plot(N_vec, rejection_rmse, 'x', c = '#A7226E')
plt.plot(N_vec, N_vec * m+c, label = 'rejection', c = '#A7226E')

m, c = np.polyfit(N_vec, metropolis_rmse, 1)
plt.plot(N_vec, metropolis_rmse, 'x', c = '#EC2049')
plt.plot(N_vec, N_vec * m+c, label = 'metropolis', c = '#EC2049')

m, c = np.polyfit(N_vec, systematic_rmse, 1)
plt.plot(N_vec, systematic_rmse, 'x', c = '#2F9599')
plt.plot(N_vec, N_vec * m+c, label = 'systematic', c = '#2F9599')

m, c = np.polyfit(N_vec, stratified_rmse, 1)
plt.plot(N_vec, stratified_rmse, 'x', c = '#F7DB4F')
plt.plot(N_vec, N_vec * m+c, label = 'stratified', c = '#F7DB4F')


plt.xlabel('Number of Particles')
plt.ylabel('RMSE')
plt.legend()
plt.savefig('particlenum_vs_RMSE')
