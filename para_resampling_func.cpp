#include <iostream>
#include "omp.h"
#include <vector>
#include <random>
#include <math.h>
#include <algorithm>
#include <chrono>

/*Parallel Cummulative/Prefix Sum*/
void para_prefix_sum(std::vector<double>& input, std::vector<double>& result, int nthreads){
    int N = input.size(); // get the length of input vector
    int i; //initialise iterator
     
    // parallel setup
    int ithread, sub_vec_size;
    double sum, sub_sum;
    if (N % nthreads == 0){
        sub_vec_size = N/nthreads;//number of particles per thread
    } else{
        sub_vec_size = N/nthreads + 1; //number of particles per thread
    }
    std::vector<double> sub_sum_vec(nthreads + 1);
    sub_sum_vec[0] = 0;
    
    #pragma omp parallel private(i, ithread, sum, sub_sum) shared(input, sub_vec_size, nthreads, sub_sum_vec)
    {
        ithread = omp_get_thread_num();
        /*calculate prefix-sum for each subarray*/
        sum = 0;
        for(i = sub_vec_size * ithread; i < sub_vec_size * (ithread + 1) && i < N; i++){
            sum += input[i];
            result[i] = sum;
        }
        sub_sum_vec[ithread+1] = sum; // store the sum of each subarray

        #pragma omp barrier //waits every thread to stop
        
        //each thread sums all sub_sum from all previous thread
        sub_sum = 0;
        for(int i=0; i<(ithread+1); i++){
            sub_sum += sub_sum_vec[i];
        }

        // corrects output array
        for(i = sub_vec_size * ithread; i < sub_vec_size * ithread + sub_vec_size && i < N; i++){
            result[i] += sub_sum;
        }

    }
}

/*Prallel Max element*/
double para_max_element(std::vector<double> &weight_vec, int nthreads){
    int N = weight_vec.size();
    double max_val = 0.0;
    int i;

    // parallel setup
    int ithread, num_particle_per_thread; 
    if (N % nthreads == 0){
        num_particle_per_thread = N/nthreads;//number of particles per thread
    } else{
        num_particle_per_thread = N/nthreads + 1; //number of particles per thread
    }

    #pragma omp parallel reduction(max: max_val) private(i, ithread) shared(num_particle_per_thread, weight_vec)
    {
        
        for (i = num_particle_per_thread * ithread; i < num_particle_per_thread * (ithread + 1) && i < N; i++){
            ithread = omp_get_thread_num();
            max_val = (max_val >= weight_vec[i] ? max_val : weight_vec[i]);
        }
    }
    return max_val;
}

/*Parallel Rejection Resampling*/
void para_rejection_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec){
    int N = weight_vec.size(); // get the length of weight vector
    int i, j; // initialise the integer needed
    double u;

    // random number generator
    std::uniform_real_distribution<double> uniform_distribution(0.0,1.0);
    std::uniform_int_distribution<int> uniformn_int_distribution(0, N-1);


    // parallel setup
    int ithread, num_particle_per_thread; 
    if (N % nthreads == 0){
        num_particle_per_thread = N/nthreads;//number of particles per thread
    } else{
        num_particle_per_thread = N/nthreads + 1; //number of particles per thread
    }

    // Find the max weight from the weight_vec
    double w_max = para_max_element(weight_vec, nthreads);
    #pragma omp parallel private(i, j, u, ithread) shared(N, weight_vec, num_particle_per_thread, w_max, sample_index, generator_vec)
    {
        ithread = omp_get_thread_num();
        std::default_random_engine& generator = generator_vec[ithread]; // Get the generator based on thread id
        for (i = num_particle_per_thread * ithread; i < num_particle_per_thread * (ithread + 1) && i < N; i++){
            j = 1* i; //make a deep copy of i
            u = uniform_distribution(generator);
            while (u > (weight_vec[j] / w_max)){
                j = uniformn_int_distribution(generator);
                u = uniform_distribution(generator);
            }
            sample_index[i] = j;
        }
    }
    #pragma omp barrier
}

/*Parallel Metropolis Resampling*/
void para_metropolis_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec){
    /*
    B -- the number of iterations to be performed before
    */
    int B = 10;
    int N = weight_vec.size();
    int i, j, k, n;
    double u;

    // random number generator setup
    std::default_random_engine generator;
    std::uniform_real_distribution<double> uniform_distribution(0.0,1.0);
    std::uniform_int_distribution<int> uniformn_int_distribution(0, N-1);
    
    // parallel setup
    int ithread, num_particle_per_thread; 
    if (N % nthreads == 0){
        num_particle_per_thread = N/nthreads;//number of particles per thread
    } else{
        num_particle_per_thread = N/nthreads + 1; //number of particles per thread
    }

    #pragma omp parallel private(i, j, k, generator, n, ithread) shared(num_particle_per_thread, weight_vec)
    {
        ithread = omp_get_thread_num();//get thread id
        generator = generator_vec[ithread]; // set up the random generator for each thread
        for(i = num_particle_per_thread * ithread; i < num_particle_per_thread * (ithread + 1) && i < N; i++){
            k = 1 * i;
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
}

/*Systematic Resampling*/
void para_systematic_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec){
    int N = weight_vec.size();
    int i, j;
    
    std::default_random_engine generator = generator_vec[0];
    std::uniform_real_distribution<double> uniform_distribution(0.0,1.0);

    // get cummulative sum
    std::vector<double> cum_sum(N);
    para_prefix_sum(weight_vec, cum_sum, nthreads);

    // calculate division_position
    // initialise positions
    double rand = uniform_distribution(generator);
    std::vector<double> division_positions(N);
    // parallel setup
    int ithread, num_particle_per_thread; 
    if (N % nthreads == 0){
        num_particle_per_thread = N/nthreads;//number of particles per thread
    } else{
        num_particle_per_thread = N/nthreads + 1; //number of particles per thread
    }

    #pragma omp parallel private(i, ithread, j) shared(N, division_positions, cum_sum, rand)
    {
        ithread = omp_get_thread_num();
        for(i = num_particle_per_thread * ithread; i < num_particle_per_thread * (ithread + 1) && i < N; i++){
            division_positions[i] = (rand + i)/N;
        }
        // resampling
        i = num_particle_per_thread * ithread;
        j = num_particle_per_thread * ithread;
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
    #pragma omp barrier

}

/*Stratified Resampling*/
void para_stratified_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec){
    int N = weight_vec.size();
    int i, j;
    
    std::default_random_engine generator;
    std::uniform_real_distribution<double> uniform_distribution(0.0,1.0);

    // get cummulative sum
    std::vector<double> cum_sum(N);
    para_prefix_sum(weight_vec, cum_sum, nthreads);

    // calculate division_position
    // initialise positions
    std::vector<double> division_positions(N);
    // parallel setup
    int ithread, num_particle_per_thread; 
    if (N % nthreads == 0){
        num_particle_per_thread = N/nthreads;//number of particles per thread
    } else{
        num_particle_per_thread = N/nthreads + 1; //number of particles per thread
    }

    #pragma omp parallel private(i, ithread, j, generator) shared(N, division_positions, cum_sum)
    {
        ithread = omp_get_thread_num();
        generator = generator_vec[ithread];

        for(i = num_particle_per_thread * ithread; i < num_particle_per_thread * (ithread + 1) && i < N; i++){
            division_positions[i] = (uniform_distribution(generator) + i)/N;
        }
        // resampling
        i = num_particle_per_thread * ithread;
        j = num_particle_per_thread * ithread;
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
    #pragma omp barrier

}


