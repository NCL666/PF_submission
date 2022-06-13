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


int main(){
    int i, j, N;
    double t1, t2, t3, t4; // initialise time 
    int T = 75;
    int repeat = 20;
    int nthread = 32;

    /*Change N */
    int N_num = 7;
    std::vector<int> N_vec(N_num); 
    for (i= 0; i < N_num; i ++){
        N_vec[i] = pow(2, 2*i + 4);
    }

    // export the reult into a csv
    std::ofstream csv_writer;
    // file name
    std::string filename = "para_time_thread32.csv";

    csv_writer.open(filename);

    for (i= 0; i < N_num; i ++){
        N = N_vec[i];
        // repeat to get the mean execution time
        t1 = 0;
        t2 = 0;
        t3 = 0;
        t4 = 0;
        for (j = 0; j < repeat; j++){
            t1 += model(T , N, &para_rejection_resampling, false, "para_rejection", nthread);
            t2 += model(T , N, &para_metropolis_resampling, false, "para_metropolis", nthread);
            t3 += model(T , N, &para_systematic_resampling, false, "para_systematic", nthread);
            t4 += model(T , N, &para_stratified_resampling, false, "para_stratified", nthread);
        }
        csv_writer << t1/repeat << ',' << t2/repeat << ',' << t3/repeat << ',' << t4/repeat << '\n';
    }

    csv_writer.close();

    return 0;
}