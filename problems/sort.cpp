#include <iostream>
#include "../lib/readfile.h"
#include <string>
#include <vector>

class sort
{
private:
    std::vector<int> seq;

public:
    sort(std::vector<int> seq);
    std::vector<int> quickSort(int low, int high);
    std::vector<int> bubbleSort();
    inline int getLength()
    {
        return this->seq.size();
    }
    inline std::vector<int> getSeq()
    {
        return this->seq;
    }
    inline void printSeq()
    {
        std::cout << std::endl;
        for (int i = 0; i < seq.size(); i++)
            std::cout << seq[i] << " ";
        std::cout << std::endl;
    }
    inline void setSeq(std::vector<int> seq)
    {
        this->seq = seq;
    }
    ~sort();
};

sort::sort(std::vector<int> seq)
{
    this->seq = seq;
}

sort::~sort()
{
}

std::vector<int> sort::quickSort(int low, int high)
{
    if (low >= high)
        return seq;
    int l = low + 1, h = high;
    while (l < h)
    {
        if (seq[l] <= seq[low])
        {
            l++;
            continue;
        }
        if (seq[h] >= seq[low])
        {
            h--;
            continue;
        }
        int temp = seq[l];
        seq[l] = seq[h];
        seq[h] = temp;
    }
    int middle;
    if (seq[l] > seq[low])
        middle = l - 1;
    else
        middle = l;
    int temp = seq[middle];
    seq[middle] = seq[low];
    seq[low] = temp;
    this->quickSort(low, middle - 1);
    this->quickSort(middle + 1, high);
    return seq;
}

std::vector<int> sort::bubbleSort()
{
    for (int i = 0; i < seq.size(); i++)
    {
        for (int j = 0; j < seq.size() - i - 1; j++)
        {
            if (seq[j] > seq[j + 1])
            {
                int temp = seq[j];
                seq[j] = seq[j + 1];
                seq[j + 1] = temp;
            }
        }
    }
    return seq;
}


int main()
{
    readfile f("../test/sort.txt");
    std::string data = f.getData();
    std::string num = "";
    std::vector<int> seq;
    for (int i = 0; i < data.length(); i++)
    {
        if (data[i] == ',')
        {
            seq.push_back(std::stoi(num));
            num = "";
            continue;
        }
        num.push_back(data[i]);
    }
    for (int i = 0; i < seq.size(); i++)
    {
        std::cout << seq[i] << " ";
    }

    sort solve(seq);
    std::cout << std::endl;
    solve.quickSort(0, solve.getLength() - 1);
    std::cout << "quickSort:";
    solve.printSeq();
    solve.setSeq(seq);
    solve.bubbleSort();
    std::cout << "bublleSort:";
    solve.printSeq();
    solve.setSeq(seq);
    std::cout<<std::endl<<"testttttttttttttttttttttttttttt!"<<std::endl;
    std::vector<int> res=solve.getSeq();
    for (int i = 0; i < res.size(); i++)
    {
        std::cout<<res[i]<<" ";
    }
    
    return 0;
}