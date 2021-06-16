//
// Created by 35116 on 2021/6/9.
//

#include <iostream>
#include <string>
#include <fstream>
#include "crypt.h"
#include "crypt_algorithm.h"

void print_res(RC4_DATATYPE *res, int res_len) {
    std::ofstream out;
    out.open("log.log", std::ios::app);
    out << res << '\n';
    out.close();
}

void print_res(RSA_DATATYPE *res, int res_len) {
    std::wofstream out;
    out.open("log_w.log",  std::ios::app);
    out << res << '\n';
    out.close();
}



int main() {

    RC4_DATATYPE *res = nullptr;
    auto *str = new unsigned char[6]{'h', 'e', 'l', 'l', 'o', '\0'};
    int str_len = 5;
    char *key = new char[5]{'1', '2', '3', '4', '5'};
    int key_len = 5;



    Crypt *crypt;
    crypt = new RC4(key, key_len);

    std::cout<<"rc4 init finished\n";

    crypt->encrypt(str, str_len);

    std::cout<<"encrypt finished.\n";

    res=crypt->get_result();
    print_res(res,str_len);
    crypt->decrypt(res,str_len);

    std::cout<<"decrypt finished.\n";

    res=crypt->get_result();
    print_res(res,str_len);
    return 0;
}