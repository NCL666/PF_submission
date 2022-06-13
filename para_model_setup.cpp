#include <iostream>
#include <vector>
#include <random>
#include <math.h>
#include <string>
#include <fstream>
#include "omp.h"
#include <algorithm>
#include <chrono>


double model(int T, int N, void (*resampling_func)(std::vector<double>&, std::vector<int>&, int, std::vector<std::default_random_engine>&), bool save, std::string file_name, int nthreads){
    /*
    T -- The total number of time step
    N -- The number of particles
    resampling_func -- The resampling method
    filename -- The filename which stores the results
    */

    // parallel setup
    omp_set_num_threads(nthreads); //set the number of threads
    int ithread, num_particle_per_thread; 
    if (N % nthreads == 0){
        num_particle_per_thread = N/nthreads;//number of particles per thread
    } else{
        num_particle_per_thread = N/nthreads + 1; //number of particles per thread
    }

    // random number generator
    std::random_device r;
    std::vector<std::default_random_engine> generator_vec(omp_get_max_threads());
    std::normal_distribution<double> normal_dist(0.0, 1.0); //std normal distirbtion
    for (int i = 0; i < omp_get_max_threads(); i++){
        generator_vec[i] =  std::default_random_engine(r());
    }
    std::default_random_engine& single_generator = generator_vec[0];

    // initialise iterator
    int i, t;
    // initialise MSE between the real one and the estimated one
    double MSE_sum = 0;
    // initialise the weight sum, the reciprocal of weight_sum and particle_sum;
    double weight_sum, reciprocal_weight_sum, particle_sum;

    // parameters of process noise v_k
    double mean_v = 0;
    double std_dev_v = sqrt(1);

    // parameters of measurement noise n_k
    double mean_n = 0;
    double std_dev_n = sqrt(1);

    // initial setup
    double x = 0.1; //initial actual state
    double y = pow(x,2)/20 + std_dev_n * normal_dist(single_generator); // initial measurement

    // initialise our initial, prior particle distribution
    // as a gaussain around the true initial value
    std::vector<double> x_P(N); //particle prior distribution
    double V = 2.0; //variance of initial prior distribution
    for (int i =  0;  i < N; i++) {
        x_P[i] = x + sqrt(V) * normal_dist(single_generator); 
    }
    
    // initialise updated particle states
    std::vector<double> x_P_update(N);
    // initialise particle estimate
    std::vector<double> y_P(N);
    // initialise particle weight vector
    std::vector<double> P_weight(N);
    // initialise particle index
    std::vector<int> sample_index(N);

    // initialise vectors to store results
    std::vector<double> x_out(T); // actual system state at each time step
    x_out[0] = x;
    std::vector<double> y_out(T); // actual measurement at each time step
    y_out[0] = y;
    std::vector<double> x_est(T); // the estimated measurement using particles at each time step
    x_est[0] = x;
    
    // time the process
    auto start_time = std::chrono::high_resolution_clock::now();
    // For each time step
    for(t = 1; t < T ; t++){
        x = 0.5 * x + 25 * x/(1 + pow(x,2)) + 8 * cos(1.2*(t-1)) + std_dev_v * normal_dist(single_generator); // update the actual state for this time step
        y = pow(x,2)/20 + std_dev_n * normal_dist(single_generator); // update the acutual estimate for this time step
        
        
        weight_sum = 0; //set weight sum to 0
        #pragma omp parallel reduction(+:weight_sum) shared(num_particle_per_thread, generator_vec, x_P_update, P_weight, x_P, std_dev_v, std_dev_n) private(ithread, i)
        {   
            ithread = omp_get_thread_num();
            std::default_random_engine& generator = generator_vec[ithread]; // Get the generator based on thread id
            for (i = num_particle_per_thread * ithread; i < num_particle_per_thread * (ithread + 1) && i < N; i++){
                x_P_update[i] = 0.5 * x_P[i] + 25 * x_P[i]/(1 + pow(x_P[i],2)) + 8*cos(1.2*(t-1)) + std_dev_v * normal_dist(generator);
                // update the weight function given the particle state 
                P_weight[i] = (1 / sqrt(2* M_PI * pow(std_dev_n, 2))) * exp(- pow(y - pow(x_P_update[i],2)/20, 2)/ (2 * pow(std_dev_n, 2)));
                weight_sum += P_weight[i];
            }
        }
        #pragma omp barrier
        
        // Renormalization of the weight vector
        reciprocal_weight_sum = 1/weight_sum;  // calculate reciprocal of weight_sum since multiply is faster than divide
        #pragma omp parallel shared(P_weight, reciprocal_weight_sum, N) private(i, ithread)
        {
            ithread = omp_get_thread_num();
            for (i = num_particle_per_thread * ithread; i < num_particle_per_thread * (ithread + 1) && i < N; i++){
                P_weight[i] = P_weight[i] * reciprocal_weight_sum;
            }
        }
        #pragma omp barrier

        // Resampling step
        resampling_func(P_weight, sample_index, nthreads, generator_vec);
        
        // accummulate the sum of the particles
        particle_sum = 0.0;
        // update x_P given sample_index
        #pragma omp parallel reduction(+:particle_sum) shared(x_P, x_P_update, sample_index, num_particle_per_thread, N) private(i, ithread)
        {   
            ithread = omp_get_thread_num();
            for (i = num_particle_per_thread * ithread; i < num_particle_per_thread * (ithread + 1) && i < N; i++){
                x_P[i] = x_P_update[sample_index[i]];
                particle_sum += x_P[i];
            }
        }
        #pragma omp barrier
        
        
        // after the resampling, the weight of each particle is equal to 1/N
        x_est[t] = particle_sum / N;
        // store the actual state and estimate
        x_out[t] = x;
        y_out[t] = y;

        // sum up the position error
        MSE_sum += pow((x_out[t] - x_est[t]), 2);
    }
    auto end_time = std::chrono::high_resolution_clock::now();
    double duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count()*(1e-6);
    

    if (save == true){
        // export the reult into a csv
        std::ofstream csv_writer;
        // file name
        std::string filename = file_name + ".csv";

        csv_writer.open(filename);

        for (t = 0; t < T ; t++){
            csv_writer << x_out[t] << ',' << x_est[t] << '\n';
        }

        csv_writer.close();
    }

    return MSE_sum/T;
}