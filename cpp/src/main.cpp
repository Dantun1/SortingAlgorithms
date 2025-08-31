#include "../include/Sorting.hpp"
#include <iostream>
#include <chrono>
#include <random>
#include <numeric>
#include <algorithm>

int main()
{

    const int DATA_SIZE = 10000;
    std::vector<int> numbers(DATA_SIZE);

    std::iota(numbers.begin(), numbers.end(), 0);
    std::random_device rd;
    std::mt19937 g(rd());
    std::shuffle(numbers.begin(), numbers.end(), g);

    std::cout << "Benchmarking bubbleSort with " << DATA_SIZE << " random integers..." << std::endl;

    auto start = std::chrono::high_resolution_clock::now();
    sorting_toolkit::bubbleSort(numbers);
    auto stop = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);

    std::cout << "Time taken by function: "
              << duration.count() << " milliseconds" << std::endl;

    return 0;
}