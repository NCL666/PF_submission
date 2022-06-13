#include <iostream>
#include <vector>
#include <random>
#include <math.h>
#include <algorithm>
#include <chrono>


/*Single Thread Cummulative/Prefix Sum*/
void prefix_sum(const std::vector<double>& input, std::vector<double>& result) {
	result[0] = input[0];
    double sum = input[0];
	for (int i = 1; i < input.size(); i++) {
        sum = sum + input[i];
		result[i] = sum;
	}
} 

/*Rejection Resampling*/
void rejection_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index){
    int N = weight_vec.size(); // get the length of weight vector
    int i, j; // initialise the integer needed
    double u;
    std::default_random_engine generator;
    std::uniform_real_distribution<double> uniform_distribution(0.0,1.0);
    std::uniform_int_distribution<int> uniformn_int_distribution(0, N-1);

    // Find the max weight from the weight_vec
    double w_max = 0;
    for (i = 0;  i < N; i++){
        w_max = (w_max >=  weight_vec[i] ? w_max : weight_vec[i]);
    }

    // resampling step
    for (i = 0; i < N; i++){
        j = 1* i; //make a deep copy of i
        u = uniform_distribution(generator);
        while (u > (weight_vec[j] / w_max)){
            j = uniformn_int_distribution(generator);
            u = uniform_distribution(generator);
        }
        sample_index[i] = j;
    }
    
}

/*Metropolis Resampling*/
void metropolis_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index){
    /*
    B -- the number of iterations to be performed before
    */
    double u;
    int i, j, k, n;

    // random number generator setup
    std::default_random_engine generator;
    std::uniform_real_distribution<double> uniform_distribution(0.0,1.0);
    int N = weight_vec.size();
    std::uniform_int_distribution<int> uniformn_int_distribution(0, N-1);
    int B = 5;

    for (i = 0; i < N; i++){
        k = 1 * i; // make a deep copy of i
        for (n = 0; n < B; n++){
            u = uniform_distribution(generator);
            j = uniformn_int_distribution(generator);
            if (u <= (weight_vec[j]/weight_vec[k])){
                k = 1 * j; // make a deep copy
            }
        }
        sample_index[i] = k;
    }
}

/*Systematic Resampling*/
void systematic_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index){
    int N = weight_vec.size();
    int i, j;
    std::default_random_engine generator;
    std::uniform_real_distribution<double> uniform_distribution(0.0,1.0);

    // get cummulative sum
    std::vector<double> cum_sum(N);
    prefix_sum(weight_vec, cum_sum);
    

    // calculate division_position
    double rand = uniform_distribution(generator);
    std::vector<double> division_positions(N);
    for (i = 0; i < N; i++){
        division_positions[i] = (rand + i)/N;
    }

    // resampling
    i = 0;
    j = 0; 
    while (i < N){
        if (division_positions[i] < cum_sum[j]){
            sample_index[i] = j;
            i += 1;
        }
        else {
            j += 1;
        }
    }
}

/*Stratified Resampling*/
void stratified_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index){
    std::default_random_engine generator;
    std::uniform_real_distribution<double> uniform_distribution(0.0,1.0);

    int N = weight_vec.size();
    int i, j;

    // get cummulative sum
    std::vector<double> cum_sum(N);
    prefix_sum(weight_vec, cum_sum);

    // calculate division_position
    std::vector<double> division_positions(N);
    for (int i = 0; i < N; i++){
        division_positions[i] = (uniform_distribution(generator) + i)/N;
    }

    // resampling
    i = 0;
    j = 0; 
    while (i < N){
        if (division_positions[i] < cum_sum[j]){
            sample_index[i] = j;
            i += 1;
        }
        else {
            j += 1;
        }
    }
}
