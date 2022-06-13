import numpy as np 
import matplotlib.pyplot as plt 


B_vec = np.array([3,4,5,6,7,8,9,10])
rmse = np.zeros(8)

for i in range(8):
    B = B_vec[i]
    mse = 0
    for j in range(50):
        name = 'para_metropolis_B_' + str(B) + '_repeat_' + str(j) + '.csv'
        data = np.genfromtxt(name ,delimiter=',')
        mse += np.sum(np.square(data[2:,0] - data[2:,1]))
    
    rmse[i] = np.sqrt(mse / 50 / 75)


plt.subplots(1,2, figsize=(12,6))

plt.subplot(121)
m, c = np.polyfit(B_vec, rmse, 1)
plt.plot(B_vec, B_vec *m+c)
plt.plot(B_vec, rmse, 'x')
plt.xlabel('B Iterations')
plt.ylabel('RMSE')











""" Time for Metropolis """
time_vec = np.array([0.255645, 0.301663, 0.356935, 0.401612, 0.439868, 0.492368, 0.522225, 0.575134])
m, c = np.polyfit(B_vec, time_vec, 1)

plt.subplot(122)
plt.plot(B_vec, B_vec *m+c)
plt.plot(B_vec, time_vec, 'x')
plt.xlabel('B Iterations')
plt.ylabel('Execution Time')

plt.savefig('Metropolis_Test')