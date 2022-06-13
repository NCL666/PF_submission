import numpy as np
import matplotlib.pyplot as plt

# get time data from csv
para_time_table_thread1 = np.genfromtxt('para_time_thread1.csv', delimiter=',')
para_time_table_thread2 = np.genfromtxt('para_time_thread2.csv', delimiter=',')
para_time_table_thread4 = np.genfromtxt('para_time_thread4.csv', delimiter=',')
para_time_table_thread8 = np.genfromtxt('para_time_thread8.csv', delimiter=',')
para_time_table_thread16 = np.genfromtxt('para_time_thread16.csv', delimiter=',')
para_time_table_thread32 = np.genfromtxt('para_time_thread32.csv', delimiter=',')


# get time data from table_thread1
rejection_para_time_thread1 = para_time_table_thread1[:, 0]
metropolis_para_time_thread1 = para_time_table_thread1[:, 1]
systematic_para_time_thread1 = para_time_table_thread1[:, 2]
stratified_para_time_thread1 = para_time_table_thread1[:, 3]

# get time data from table_thread2
rejection_para_time_thread2 = para_time_table_thread2[:, 0]
metropolis_para_time_thread2 = para_time_table_thread2[:, 1]
systematic_para_time_thread2 = para_time_table_thread2[:, 2]
stratified_para_time_thread2 = para_time_table_thread2[:, 3]

# get time data from table_thread4
rejection_para_time_thread4 = para_time_table_thread4[:, 0]
metropolis_para_time_thread4 = para_time_table_thread4[:, 1]
systematic_para_time_thread4 = para_time_table_thread4[:, 2]
stratified_para_time_thread4 = para_time_table_thread4[:, 3]

# get time data from table_thread8
rejection_para_time_thread8 = para_time_table_thread8[:, 0]
metropolis_para_time_thread8 = para_time_table_thread8[:, 1]
systematic_para_time_thread8 = para_time_table_thread8[:, 2]
stratified_para_time_thread8 = para_time_table_thread8[:, 3]

# get time data from table_thread16
rejection_para_time_thread16 = para_time_table_thread16[:, 0]
metropolis_para_time_thread16 = para_time_table_thread16[:, 1]
systematic_para_time_thread16 = para_time_table_thread16[:, 2]
stratified_para_time_thread16 = para_time_table_thread16[:, 3]

# get time data from table_thread32
rejection_para_time_thread32 = para_time_table_thread32[:, 0]
metropolis_para_time_thread32 = para_time_table_thread32[:, 1]
systematic_para_time_thread32 = para_time_table_thread32[:, 2]
stratified_para_time_thread32 = para_time_table_thread32[:, 3]


# subplot setup
plt.figure()
plt.subplots(2, 2, figsize = (12, 12))
particle_num_vec = [6, 8, 10, 12, 14, 16, 18]

# plot run time required by rejection for different thread
plt.subplot(221)
plt.plot(particle_num_vec, rejection_para_time_thread1,  'x-', label = 'thread = 1')
plt.plot(particle_num_vec, rejection_para_time_thread2, 'x-', label = 'thread = 2')
plt.plot(particle_num_vec, rejection_para_time_thread4, 'x-', label = 'thread = 4')
plt.plot(particle_num_vec, rejection_para_time_thread8, 'x-', label = 'thread = 8')
plt.plot(particle_num_vec, rejection_para_time_thread16, 'x-', label = 'thread = 16')
plt.plot(particle_num_vec, rejection_para_time_thread32, 'x-', label = 'thread = 32')
plt.xlabel('$log_2(N)$')
plt.ylabel('Time')
plt.yscale('log')
plt.legend()
plt.title('Rejection Resampling on different number of threads')

# plot run time required by metropolis for different thread
plt.subplot(222)
plt.plot(particle_num_vec, metropolis_para_time_thread1,  'x-', label = 'thread = 1')
plt.plot(particle_num_vec, metropolis_para_time_thread2, 'x-', label = 'thread = 2')
plt.plot(particle_num_vec, metropolis_para_time_thread4, 'x-', label = 'thread = 4')
plt.plot(particle_num_vec, metropolis_para_time_thread8, 'x-', label = 'thread = 8')
plt.plot(particle_num_vec, metropolis_para_time_thread16, 'x-', label = 'thread = 16')
plt.plot(particle_num_vec, metropolis_para_time_thread32, 'x-', label = 'thread = 32')
plt.xlabel('$log_2(N)$')
plt.ylabel('Time')
plt.yscale('log')
plt.legend()
plt.title('Metropolis Resampling on different number of threads')

# plot run time required by systematic for different thread
plt.subplot(223)
plt.plot(particle_num_vec, systematic_para_time_thread1,  'x-', label = 'thread = 1')
plt.plot(particle_num_vec, systematic_para_time_thread2, 'x-', label = 'thread = 2')
plt.plot(particle_num_vec, systematic_para_time_thread4, 'x-', label = 'thread = 4')
plt.plot(particle_num_vec, systematic_para_time_thread8, 'x-', label = 'thread = 8')
plt.plot(particle_num_vec, systematic_para_time_thread16, 'x-', label = 'thread = 16')
plt.plot(particle_num_vec, systematic_para_time_thread32, 'x-', label = 'thread = 32')
plt.xlabel('$log_2(N)$')
plt.ylabel('Time')
plt.yscale('log')
plt.legend()
plt.title('Systematic Resampling on different number of threads')

# plot run time required by stratified for different thread
plt.subplot(224)
plt.plot(particle_num_vec, stratified_para_time_thread1,  'x-', label = 'thread = 1')
plt.plot(particle_num_vec, stratified_para_time_thread2, 'x-', label = 'thread = 2')
plt.plot(particle_num_vec, stratified_para_time_thread4, 'x-', label = 'thread = 4')
plt.plot(particle_num_vec, stratified_para_time_thread8, 'x-', label = 'thread = 8')
plt.plot(particle_num_vec, stratified_para_time_thread16, 'x-', label = 'thread = 16')
plt.plot(particle_num_vec, stratified_para_time_thread32, 'x-', label = 'thread = 32')
plt.xlabel('$log_2(N)$')
plt.ylabel('Time')
plt.yscale('log')
plt.legend()
plt.title('Stratified Resampling on different number of threads')
plt.savefig('Parallel Time Test.jpg')
plt.close()

# speed up plot
# calculate the speedup for different resampling methods
# initial setup
N_num = len(rejection_para_time_thread1)
# rejection speedup
rejection_speedup_thread1 = np.ones(N_num)
rejection_speedup_thread2 = np.zeros(N_num)
rejection_speedup_thread4 = np.zeros(N_num)
rejection_speedup_thread8 = np.zeros(N_num)
rejection_speedup_thread16 = np.zeros(N_num)
rejection_speedup_thread32 = np.zeros(N_num)
for i in range(N_num):
    rejection_speedup_thread2[i] = rejection_para_time_thread1[i]/rejection_para_time_thread2[i]
    rejection_speedup_thread4[i] = rejection_para_time_thread1[i]/rejection_para_time_thread4[i]
    rejection_speedup_thread8[i] = rejection_para_time_thread1[i]/rejection_para_time_thread8[i]
    rejection_speedup_thread16[i] = rejection_para_time_thread1[i]/rejection_para_time_thread16[i]
    rejection_speedup_thread32[i] = rejection_para_time_thread1[i]/rejection_para_time_thread32[i]

# metropolis speedup
metropolis_speedup_thread1 = np.ones(N_num)
metropolis_speedup_thread2 = np.zeros(N_num)
metropolis_speedup_thread4 = np.zeros(N_num)
metropolis_speedup_thread8 = np.zeros(N_num)
metropolis_speedup_thread16 = np.zeros(N_num)
metropolis_speedup_thread32 = np.zeros(N_num)
for i in range(N_num):
    metropolis_speedup_thread2[i] = metropolis_para_time_thread1[i]/metropolis_para_time_thread2[i]
    metropolis_speedup_thread4[i] = metropolis_para_time_thread1[i]/metropolis_para_time_thread4[i]
    metropolis_speedup_thread8[i] = metropolis_para_time_thread1[i]/metropolis_para_time_thread8[i]
    metropolis_speedup_thread16[i] = metropolis_para_time_thread1[i]/metropolis_para_time_thread16[i]
    metropolis_speedup_thread32[i] = metropolis_para_time_thread1[i]/metropolis_para_time_thread32[i]

# systematic speedup
systematic_speedup_thread1 = np.ones(N_num)
systematic_speedup_thread2 = np.zeros(N_num)
systematic_speedup_thread4 = np.zeros(N_num)
systematic_speedup_thread8 = np.zeros(N_num)
systematic_speedup_thread16 = np.zeros(N_num)
systematic_speedup_thread32 = np.zeros(N_num)
for i in range(N_num):
    systematic_speedup_thread2[i] = systematic_para_time_thread1[i]/systematic_para_time_thread2[i]
    systematic_speedup_thread4[i] = systematic_para_time_thread1[i]/systematic_para_time_thread4[i]
    systematic_speedup_thread8[i] = systematic_para_time_thread1[i]/systematic_para_time_thread8[i]
    systematic_speedup_thread16[i] = systematic_para_time_thread1[i]/systematic_para_time_thread16[i]
    systematic_speedup_thread32[i] = systematic_para_time_thread1[i]/systematic_para_time_thread32[i]

# stratified speedup
stratified_speedup_thread1 = np.ones(N_num)
stratified_speedup_thread2 = np.zeros(N_num)
stratified_speedup_thread4 = np.zeros(N_num)
stratified_speedup_thread8 = np.zeros(N_num)
stratified_speedup_thread16 = np.zeros(N_num)
stratified_speedup_thread32 = np.zeros(N_num)
for i in range(N_num):
    stratified_speedup_thread2[i] = stratified_para_time_thread1[i]/stratified_para_time_thread2[i]
    stratified_speedup_thread4[i] = stratified_para_time_thread1[i]/stratified_para_time_thread4[i]
    stratified_speedup_thread8[i] = stratified_para_time_thread1[i]/stratified_para_time_thread8[i]
    stratified_speedup_thread16[i] = stratified_para_time_thread1[i]/stratified_para_time_thread16[i]
    stratified_speedup_thread32[i] = stratified_para_time_thread1[i]/stratified_para_time_thread32[i]

# plot setup
plt.figure()
plt.subplots(2, 2, figsize = (12, 12))

# plot run time required by rejection for different thread
plt.subplot(221)
plt.plot(particle_num_vec, rejection_speedup_thread1,  'x-', label = 'thread = 1')
plt.plot(particle_num_vec, rejection_speedup_thread2, 'x-', label = 'thread = 2')
plt.plot(particle_num_vec, rejection_speedup_thread4, 'x-', label = 'thread = 4')
plt.plot(particle_num_vec, rejection_speedup_thread8, 'x-', label = 'thread = 8')
plt.plot(particle_num_vec, rejection_speedup_thread16, 'x-', label = 'thread = 16')
plt.plot(particle_num_vec, rejection_speedup_thread32, 'x-', label = 'thread = 32')
plt.xlabel('$log_2(N)$')
plt.ylabel('Speed up Ratio')
plt.yscale('log',base =2)
plt.legend()
plt.title('Rejection Resampling on different number of threads')

# plot run time required by metropolis for different thread
plt.subplot(222)
plt.plot(particle_num_vec, metropolis_speedup_thread1,  'x-', label = 'thread = 1')
plt.plot(particle_num_vec, metropolis_speedup_thread2, 'x-', label = 'thread = 2')
plt.plot(particle_num_vec, metropolis_speedup_thread4, 'x-', label = 'thread = 4')
plt.plot(particle_num_vec, metropolis_speedup_thread8, 'x-', label = 'thread = 8')
plt.plot(particle_num_vec, metropolis_speedup_thread16, 'x-', label = 'thread = 16')
plt.plot(particle_num_vec, metropolis_speedup_thread32, 'x-', label = 'thread = 32')
plt.xlabel('$log_2(N)$')
plt.ylabel('Speed up Ratio')
plt.yscale('log',base =2)
plt.legend()
plt.title('Metropolis Resampling on different number of threads')

# plot run time required by systematic for different thread
plt.subplot(223)
plt.plot(particle_num_vec, systematic_speedup_thread1,  'x-', label = 'thread = 1')
plt.plot(particle_num_vec, systematic_speedup_thread2, 'x-', label = 'thread = 2')
plt.plot(particle_num_vec, systematic_speedup_thread4, 'x-', label = 'thread = 4')
plt.plot(particle_num_vec, systematic_speedup_thread8, 'x-', label = 'thread = 8')
plt.plot(particle_num_vec, systematic_speedup_thread16, 'x-', label = 'thread = 16')
plt.plot(particle_num_vec, systematic_speedup_thread32, 'x-', label = 'thread = 32')
plt.xlabel('$log_2(N)$')
plt.ylabel('Speed up Ratio')
plt.yscale('log',base =2)
plt.legend()
plt.title('Systematic Resampling on different number of threads')

# plot run time required by stratified for different thread
plt.subplot(224)
plt.plot(particle_num_vec, stratified_speedup_thread1,  'x-', label = 'thread = 1')
plt.plot(particle_num_vec, stratified_speedup_thread2, 'x-', label = 'thread = 2')
plt.plot(particle_num_vec, stratified_speedup_thread4, 'x-', label = 'thread = 4')
plt.plot(particle_num_vec, stratified_speedup_thread8, 'x-', label = 'thread = 8')
plt.plot(particle_num_vec, stratified_speedup_thread16, 'x-', label = 'thread = 16')
plt.plot(particle_num_vec, stratified_speedup_thread32, 'x-', label = 'thread = 32')
plt.xlabel('$log_2(N)$')
plt.ylabel('Speed up Ratio')
plt.yscale('log',base =2)
plt.legend()
plt.title('Stratified Resampling on different number of threads')

plt.savefig('speed_up')