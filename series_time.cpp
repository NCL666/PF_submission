#include <iostream>
#include <vector>
#include <random>
#include <math.h>
#include <algorithm>
#include <string>
#include <fstream>

//declare the model function
double model(int T, int N, void (*resampling_func)(std::vector<double>&, std::vector<int>&), bool save, std::string file_name);

//declare the resampling function
void rejection_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index);
void metropolis_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index);
void systematic_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index);
void stratified_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index);

int main(){

    int i, j, N; // initilise iterator
    double t1, t2, t3, t4; // initialise time 
    int T = 75;
    int repeat = 10;

    /*
    Change N 
    */
    int N_num = 7;
    std::vector<int> N_vec(N_num); 
    for (i= 0; i < N_num; i ++){
        N_vec[i] = pow(2, 2* i + 6);
    }

    // export the reult into a csv
    std::ofstream csv_writer;
    // file name
    std::string filename = "series_time.csv";

    csv_writer.open(filename);

    for (i= 0; i < N_num; i ++){
        N = N_vec[i];
        // repeat to get the mean execution time
        t1 = 0;
        t2 = 0;
        t3 = 0;
        t4 = 0;
        for (j = 0; j < repeat; j++){
            t1 += model(T , N, &rejection_resampling, false, "rejection");
            t2 += model(T , N, &metropolis_resampling, false, "metropolis");
            t3 += model(T , N, &systematic_resampling, false, "systematic");
            t4 += model(T , N, &stratified_resampling, false, "stratified");
        }
        csv_writer << t1/repeat << ',' << t2/repeat << ',' << t3/repeat << ',' << t4/repeat << '\n';
    }

    csv_writer.close();

    return 0;
}