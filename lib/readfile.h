#pragma once
#include<fstream>
#include<string>

class readfile
{
private:
    std::ifstream infile;
public:
    readfile(std::string filename);
    std::string getData(){
        std::string data;
        infile>>data;
        return data;
    }
    ~readfile();
};

readfile::readfile(std::string filename)
{
    infile.open(filename);
}

readfile::~readfile()
{
    infile.close();
}
