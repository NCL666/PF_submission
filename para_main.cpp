#include <iostream>
#include <random>
#include <math.h>
#include <algorithm>
#include <fstream>

//declare the model function
double model(int T, int N, void (*resampling_func)(std::vector<double>&, std::vector<int>&, int, std::vector<std::default_random_engine>&), bool save, std::string file_name, int nthreads);

//declare the resampling function
void para_rejection_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec);
void para_metropolis_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec);
void para_systematic_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec);
void para_stratified_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec);

int main() {
    int T = 75;
    int N = 100000;
    int nthread = 4;

    double time1;

    time1 = model(T , N, &para_rejection_resampling, true, "para_rejection", nthread);
    time1 = model(T , N, &para_metropolis_resampling, true, "para_metropolis", nthread);
    time1 = model(T , N, &para_systematic_resampling, true, "para_systematic", nthread);
    time1 = model(T , N, &para_stratified_resampling, true, "para_stratified", nthread);

    return 0;
}
