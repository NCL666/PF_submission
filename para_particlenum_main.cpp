#include <iostream>
#include <random>
#include <math.h>
#include <algorithm>
#include <fstream>
#include <string>  

double model(int T, int N, void (*resampling_func)(std::vector<double>&, std::vector<int>&, int, std::vector<std::default_random_engine>&), bool save, std::string file_name, int nthreads);

//declare the resampling function
void para_rejection_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec);
void para_metropolis_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec);
void para_systematic_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec);
void para_stratified_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec);

int main() {
    int T = 75;
    int nthread = 4;
    int repeat = 20;
    int N;

    std::string rejection_name, metropolis_name, systematic_name, stratified_name;
    int i,j;
    std::vector<int> N_vec = {100, 200, 300, 400, 500, 600, 700, 800, 900, 1000};

    for (i = 0; i < 10 ; i++) {
        N = N_vec[i];
        for (j = 1; j < 101; j++) {
            rejection_name = "para_rejection_N_" + std::__cxx11::to_string(N) + "_repeat_" + std::__cxx11::to_string(j);
            metropolis_name = "para_metropolis_N_" + std::__cxx11::to_string(N) + "_repeat_" + std::__cxx11::to_string(j);
            systematic_name = "para_systematic_N_" + std::__cxx11::to_string(N) + "_repeat_" + std::__cxx11::to_string(j);
            stratified_name = "para_stratified_N_" + std::__cxx11::to_string(N) + "_repeat_" + std::__cxx11::to_string(j);
            model(T , N, &para_rejection_resampling, true, rejection_name , nthread);
            model(T , N, &para_metropolis_resampling, true, metropolis_name , nthread);
            model(T , N, &para_systematic_resampling, true, systematic_name , nthread);
            model(T , N, &para_stratified_resampling, true, stratified_name , nthread);
        }
    }
}
