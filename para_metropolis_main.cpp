#include <iostream>
#include <random>
#include <math.h>
#include <algorithm>
#include <fstream>

//declare the model function
double model(int T, int N, void (*resampling_func)(std::vector<double>&, std::vector<int>&, int, std::vector<std::default_random_engine>&), bool save, std::string file_name, int nthreads);

//declare the resampling function
void para_metropolis_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec);

int main() {
    int T = 75;
    int N = 10000;
    int nthread = 4;

    int i;

    double time1;
    std::string metropolis_name;

    for (i = 0; i < 50; i++){
        metropolis_name = "para_metropolis_B_10_repeat_" + std::__cxx11::to_string(i);
        time1 += model(T , N, &para_metropolis_resampling, true, metropolis_name, nthread);
    }
    std::cout << time1/50;

    return 0;
}