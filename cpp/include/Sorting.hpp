//
// Created by Daniel Tunyan on 31/08/2025.
//

#ifndef SORTING_HPP
#define SORTING_HPP
#include <vector>
#include <iostream>

namespace sorting_toolkit
{

    // Utility Function

    template <typename T>
    void printVector(const std::vector<T>& data)
    {
        for (const T &i: data)
        {
            std::cout << i << " " << std::flush;
        }
    }

    /**
     * @brief Sorts a given vector using bubble sort algorithm
     */
    template <typename T>
    void bubbleSort(std::vector<T>& data)
    {
        for (std::size_t i = 0; i<data.size(); i++)
        {
            bool is_sorted = true;
                for (std::size_t j=0; j< data.size()-i-1; j++)
                {
                    if (data[j] > data[j+1])
                    {
                        std::swap(data[j],data[j+1]);
                        is_sorted = false;
                    }
                }
            if (is_sorted)
            {
                break;
            }
        }
    }

}

#endif //SORTING_HPP
