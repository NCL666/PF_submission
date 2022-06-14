#include <iostream>
#include <random>
#include <math.h>
#include <algorithm>
#include <fstream>
#include <vector>

//declare the model function
std::vector<double> model(int T, int N, void (*resampling_func)(std::vector<double>&, std::vector<int>&, int, std::vector<std::default_random_engine>&), bool save, std::string file_name, int nthreads, int redraw_num, double EPN_threshold, double rough_var);

//declare the resampling function
void para_rejection_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec);
void para_metropolis_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec);
void para_systematic_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec);
void para_stratified_resampling(std::vector<double> &weight_vec, std::vector<int> &sample_index, int nthreads, std::vector<std::default_random_engine> &generator_vec);

int main() {
    int T = 75;
    int nthread = 4;
    int redraw_num = 3;
    int i, j, N;
    int repeat = 10;
    double EPN_threshold = 0.5;
    double rough_var = 1.0;

    double ENP_sum, MSE_sum, time_sum;

    /*Change N */
    int N_num = 6;
    std::vector<int> N_vec(N_num);
    for (i= 0; i < N_num; i ++){
        N_vec[i] = pow(2, 2* i + 6);
    }

    // export the reult into a csv
    std::ofstream csv_writer;
    // file name
    std::string filename = "para_opt_test.csv";
    std::vector<double> result(3);

    csv_writer.open(filename);
    for (i = 0; i < N_num; i++){
        N = N_vec[i];

        // average over repeats of parallel rejection
        ENP_sum = 0;
        MSE_sum = 0;
        time_sum = 0;
        for (j = 0; j < repeat; j++){
            result = model(T, N, &para_rejection_resampling, false, "para_rejection", nthread, redraw_num, EPN_threshold, rough_var);
            ENP_sum += result[0];
            MSE_sum += result[1];
            time_sum += result[2];
        }
        csv_writer << ENP_sum/repeat << ',' << MSE_sum/repeat << ',' << time_sum/repeat << ',';

        // average over repeats of parallel metropolis
        ENP_sum = 0;
        MSE_sum = 0;
        time_sum = 0;
        for (j = 0; j < repeat; j++){
            result = model(T, N, &para_metropolis_resampling, false, "para_metropolis", nthread, redraw_num, EPN_threshold, rough_var);
            ENP_sum += result[0];
            MSE_sum += result[1];
            time_sum += result[2];
        }
        csv_writer << ENP_sum/repeat << ',' << MSE_sum/repeat << ',' << time_sum/repeat << ',';

        // average over repeats of parallel systematic
        ENP_sum = 0;
        MSE_sum = 0;
        time_sum = 0;
        for (j = 0; j < repeat; j++){
            result = model(T, N, &para_systematic_resampling, false, "para_systematic", nthread, redraw_num, EPN_threshold, rough_var);
            ENP_sum += result[0];
            MSE_sum += result[1];
            time_sum += result[2];
        }
        csv_writer << ENP_sum/repeat << ',' << MSE_sum/repeat << ',' << time_sum/repeat << ',';

        // average over repeats of parallel stratified
        ENP_sum = 0;
        MSE_sum = 0;
        time_sum = 0;
        for (j = 0; j < repeat; j++){
            result = model(T, N, &para_stratified_resampling, false, "para_stratified", nthread, redraw_num, EPN_threshold, rough_var);
            ENP_sum += result[0];
            MSE_sum += result[1];
            time_sum += result[2];
        }
        csv_writer << ENP_sum/repeat << ',' << MSE_sum/repeat << ',' << time_sum/repeat << '\n';
    }
    csv_writer.close(); 

    return 0;
}