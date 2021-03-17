#include <iostream>
#include "../lib/readfile.h"
#include <string>
#include <vector>

class sort
{
private:
public:
    std::vector<int> seq;
    sort(std::vector<int> seq);
    std::vector<int> quickSort(int low, int high);
    inline int getLength()
    {
        return this->seq.size();
    }
    inline std::vector<int> getSeq()
    {
        return this->seq;
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
    int l = low+1, h = high;
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

    if (seq[l] > seq[low])
    {
        int temp = seq[l - 1];
        seq[l - 1] = seq[low];
        seq[low] = temp;
        this->quickSort(low, l - 2);
        this->quickSort(l, high);
    }
    else
    {
        int temp = seq[l];
        seq[l] = seq[low];
        seq[low] = temp;
        this->quickSort(low, l - 1);
        this->quickSort(l + 1, high);
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
    solve.quickSort(0, solve.getLength()-1);
    for (int i = 0; i < solve.seq.size(); i++)
    {
        std::cout << solve.seq[i] << " ";
    }

    return 0;
}