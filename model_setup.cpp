#include <iostream>
#include <vector>
#include <random>
#include <math.h>
#include <string>
#include <fstream>
#include <chrono>



double model(int T, int N, void (*resampling_func)(std::vector<double>&, std::vector<int>&), bool save, std::string file_name){
    /*
    T -- The total number of time step
    N -- The number of particles
    resampling_func -- The resampling method
    filename -- The filename which stores the results
    */
    // random number generator
    std::default_random_engine generator;
    std::normal_distribution<double> normal_dist(0.0, 1.0); //std normal distirbtion

    // initialise iterator
    int i, t;
    // initialise the weight sum, the reciprocal of weight_sum and particle_sum;
    double weight_sum, reciprocal_weight_sum, particle_sum;

    // parameters of process noise v_k
    double mean_v = 0;
    double std_dev_v = sqrt(10);

    // parameters of measurement noise n_k
    double mean_n = 0;
    double std_dev_n = sqrt(1);

    double x = 0.1; //initial actual state
    double y = pow(x,2)/20 + std_dev_n * normal_dist(generator); // initial measurement

    // initialise our initial, prior particle distribution
    // as a gaussain around the true initial value
    std::vector<double> x_P(N); //particle prior distribution
    double V = 2.0; //variance of initial prior distribution
    for (int i =  0;  i < N; i++) {
        x_P[i] = x + sqrt(V) * normal_dist(generator); 
    }
    // initialise updated particle states
    std::vector<double> x_P_update(N);
    // initialise particle estimate
    std::vector<double> y_P(N);
    // initialise particle weight vector
    std::vector<double> P_weight(N);
    // initialise sample index
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
    for ( t = 1; t < T ; t++){
        x = 0.5 * x + 25 * x/(1 + pow(x,2)) + 8 * cos(1.2*(t-1)) + std_dev_v * normal_dist(generator); // update the actual state for this time step
        y = pow(x,2)/20 + std_dev_n * normal_dist(generator); // update the acutual estimate for this time step
        
        
        weight_sum = 0; //set weight sum to 0
        // update the particle state and estimate
        for ( i = 0; i < N; i++){
            // update the actual state for this time step
            x_P_update[i] = 0.5 * x_P[i] + 25 * x_P[i]/(1 + pow(x_P[i],2)) + 8*cos(1.2*(t-1)) + std_dev_v * normal_dist(generator);
            // update the weight function given the particle state 
            P_weight[i] = (1 / sqrt(2* M_PI * pow(std_dev_n,2))) * exp(- pow(y - pow(x_P_update[i],2)/20, 2)/ (2 * pow(std_dev_n, 2)));
            // cummmulate the weight
            weight_sum += P_weight[i];
        }


        
        // Renormalization of the weight vector
        reciprocal_weight_sum = 1/weight_sum;  // calculate reciprocal of weight_sum since multiply is faster than divide
        for (i = 0; i < N; i++){
            P_weight[i] = P_weight[i] * reciprocal_weight_sum;
        }
        
        // Resampling step
        resampling_func(P_weight, sample_index);
        

        // accummulate the sum of the particles
        particle_sum = 0.0;
        // update x_P given sample_index
        for (i = 0; i < N; i++){
            x_P[i] = x_P_update[sample_index[i]];
            particle_sum += x_P[i];
        }
        
        // after the resampling, the weight of each particle is equal to 1/N
        x_est[t] = particle_sum / N;
        // store the actual state and estimate
        x_out[t] = x;
        y_out[t] = y;

    }
    auto end_time = std::chrono::high_resolution_clock::now();
    double duration = std::chrono::duration_cast<std::chrono::microseconds>( end_time - start_time ).count()*(1e-6);
    
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


    return duration;
}

