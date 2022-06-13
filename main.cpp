#include <iostream>
#include <random>
#include <math.h>
#include <algorithm>
#include <fstream>

//declare the model function
double model(int T, int N, void (*resampling_func)(std::vector<double>&, std::vector<int>&), bool save, std::string file_name);

//declare the resampling function
void rejection_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index);
void metropolis_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index);
void systematic_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index);
void stratified_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index);

int main() {
    int T = 75;
    int N = 100000;
    double time1;

    time1 = model(T , N, &rejection_resampling, true, "rejection");
    time1 = model(T , N, &metropolis_resampling, true, "metropolis");
    time1 = model(T , N, &systematic_resampling, true, "systematic");
    time1 = model(T , N, &stratified_resampling, true,"stratified");

    return 0;
}

