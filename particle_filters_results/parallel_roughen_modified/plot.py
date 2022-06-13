import numpy as np 
import matplotlib.pyplot as plt 

""" Read No Redraw Data"""
test_file = np.genfromtxt('rough.csv', delimiter=',')

rejection_EPN = test_file[:,0]
rejection_RMSE = np.sqrt(test_file[:,1])
rejection_time = test_file[:,2]

metropolis_EPN = test_file[:,3]
metropolis_RMSE = np.sqrt(test_file[:,4])
metropolis_time = test_file[:,5]

systematic_EPN = test_file[:,6]
systematic_RMSE = np.sqrt(test_file[:,7])
systematic_time = test_file[:,8]

stratified_EPN = test_file[:,9]
stratified_RMSE = np.sqrt(test_file[:,10])
stratified_time = test_file[:,11]


# set up the var_vec
N_num = len(rejection_EPN)
var_vec = np.zeros(N_num)
for i in range(N_num):
    var_vec[i] =  (i+1)/4



rejection_EPN_ratio = np.divide(rejection_EPN,100)
metropolis_EPN_ratio = np.divide(metropolis_EPN,100)
systematic_EPN_ratio = np.divide(systematic_EPN,100)
stratified_EPN_ratio = np.divide(stratified_EPN,100)


m, c = np.polyfit(var_vec, rejection_EPN_ratio, 1)
plt.plot(var_vec, rejection_EPN_ratio, 'x', c = '#A7226E')
plt.plot(var_vec, var_vec * m+c, label = 'rejection', c = '#A7226E')

m, c = np.polyfit(var_vec, metropolis_EPN_ratio, 1)
plt.plot(var_vec, metropolis_EPN_ratio, 'x', c = '#EC2049')
plt.plot(var_vec, var_vec * m+c, label = 'metropolis', c = '#EC2049')

m, c = np.polyfit(var_vec, systematic_EPN_ratio, 1)
plt.plot(var_vec, systematic_EPN_ratio, 'x', c = '#2F9599')
plt.plot(var_vec, var_vec * m+c, label = 'systematic', c = '#2F9599')

m, c = np.polyfit(var_vec, stratified_EPN_ratio, 1)
plt.plot(var_vec, stratified_EPN_ratio, 'x', c = '#F7DB4F')
plt.plot(var_vec, var_vec * m+c, label = 'stratified', c = '#A7226E')


plt.legend()
plt.xlabel('Roughening Variance')
plt.ylabel('Effective Particle Ratio')
plt.savefig('rough_EPN')
plt.close()


m, c = np.polyfit(var_vec, rejection_RMSE, 1)
plt.plot(var_vec, rejection_RMSE, 'x-', label = 'rejection', c = '#A7226E')
#plt.plot(var_vec, var_vec * m+c, label = 'rejection', c = '#A7226E')

m, c = np.polyfit(var_vec, metropolis_RMSE, 1)
plt.plot(var_vec, metropolis_RMSE, 'x-', label = 'metropolis', c = '#EC2049')
#plt.plot(var_vec, var_vec * m+c, label = 'metropolis', c = '#EC2049')

m, c = np.polyfit(var_vec, systematic_RMSE, 1)
plt.plot(var_vec, systematic_RMSE, 'x-', label = 'systematics', c = '#2F9599')
#plt.plot(var_vec, var_vec * m+c, label = 'systematic', c = '#2F9599')

m, c = np.polyfit(var_vec, stratified_RMSE, 1)
plt.plot(var_vec, stratified_RMSE, 'x-', label = 'stratified', c = '#F7DB4F')
#plt.plot(var_vec, var_vec * m+c, label = 'stratified', c = '#A7226E')


plt.legend()
plt.xlabel('Roughening Variance')
plt.ylabel('RMSE')
plt.savefig('rough_MSE')
plt.close()



m, c = np.polyfit(var_vec, rejection_time, 1)
plt.plot(var_vec, rejection_time, 'x', c = '#A7226E')
plt.plot(var_vec, var_vec * m+c, label = 'rejection', c = '#A7226E')

m, c = np.polyfit(var_vec, metropolis_time, 1)
plt.plot(var_vec, metropolis_time, 'x', c = '#EC2049')
plt.plot(var_vec, var_vec * m+c, label = 'metropolis', c = '#EC2049')

m, c = np.polyfit(var_vec, systematic_time, 1)
plt.plot(var_vec, systematic_time, 'x', c = '#2F9599')
plt.plot(var_vec, var_vec * m+c, label = 'systematic', c = '#2F9599')

m, c = np.polyfit(var_vec, stratified_time, 1)
plt.plot(var_vec, stratified_time, 'x', c = '#F7DB4F')
plt.plot(var_vec, var_vec * m+c, label = 'stratified', c = '#A7226E')


plt.legend()
plt.xlabel('Roughening Variance')
plt.ylabel('Time')
plt.savefig('rough_time')
plt.close()

