//
// Created by 35116 on 2021/6/9.
//

#ifndef CRYPT_CRYPTO_ALGORITHM_H
#define CRYPT_CRYPTO_ALGORITHM_H


#include "crypt.h"
#include <cmath>
#include <ctime>

#define CRYPT
#ifndef CRYPT

#define DATATYPE unsigned RSA_DATATYPE

template<typename T>
void swap(T &a, T &b) {
    T temp = a;
    a = b;
    b = temp;
}
#endif

#define PRIME_LEN 4
static int prime[PRIME_LEN] = {2, 3,5,7};
//int prime[PRIME_LEN] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53};

void rc4_init(RC4_DATATYPE *s_box, const char *key, int key_len);

RC4_DATATYPE *rc4_crypt(RC4_DATATYPE *s_box, RC4_DATATYPE *data, int data_len);


void RSA_init_key(int &public_key, int &private_key,int&n);

RSA_DATATYPE *RSA_encrypt(int key, int n, RSA_DATATYPE *data, int data_len);

RSA_DATATYPE *RSA_decrypt(int key, int n, RSA_DATATYPE *data, int data_len);

#endif //CRYPT_CRYPTO_ALGORITHM_H
