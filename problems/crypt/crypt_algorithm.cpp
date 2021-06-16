//
// Created by 35116 on 2021/6/9.
#include "crypt_algorithm.h"
#include <iostream>

void rc4_init(RC4_DATATYPE *s_box, const char *key, int key_len) {
    RC4_DATATYPE k[LEN] = {0};
    for (int i = 0; i < LEN; i++) {
        s_box[i] = (RC4_DATATYPE) i;
        k[i] = key[i % key_len];
    }

    int j(0);
    for (int i = 0; i < LEN; i++) {
        j = (j + s_box[i] + k[i]) % LEN;
        swap(s_box[i], s_box[j]);
    }
}


RC4_DATATYPE *rc4_crypt(RC4_DATATYPE *s_box, RC4_DATATYPE *data, int data_len) {
    int pos;
    auto result = new RC4_DATATYPE[data_len + 1];
    auto temp_s_box = new RC4_DATATYPE[LEN];
    for (int k = 0; k < LEN; k++) {
        temp_s_box[k] = s_box[k];
    }
    for (int i = 0; i < data_len; i++) {
        pos = i % LEN;
        result[i] = (RC4_DATATYPE) (data[i] ^ s_box[pos]);
    }
    result[data_len] = '\0';
    return result;
}


void RSA_init_key(int &public_key, int &private_key, int &n) {
    srand(time(0));
    int p = prime[rand() % PRIME_LEN];
    int q = prime[rand() % PRIME_LEN];
    while (p == q) {
        q = prime[rand() % PRIME_LEN];
    }
    n = p * q;
    int phi_n = (p - 1) * (q - 1);
    srand(time(0));
    public_key = rand() % phi_n;
    while (gcd(public_key, phi_n) != 1) {
        srand(time(0));
        public_key = rand() % phi_n;
    }
    private_key = 2;
    while (private_key * public_key % phi_n != 1) {
        private_key++;
    }
}

RSA_DATATYPE *RSA_encrypt(int key, int n, RSA_DATATYPE *data, int data_len) {
    RSA_DATATYPE *res = new RSA_DATATYPE[data_len + 1]{0};
    for (int i = 0; i < data_len; i++) {
        res[i] = (int) (pow(data[i], key)) % n;
    }
    res[data_len] = L'\0';
    return res;
}

RSA_DATATYPE *RSA_decrypt(int key, int n, RSA_DATATYPE *data, int data_len) {
    RSA_DATATYPE *res = new RSA_DATATYPE[data_len + 1]{0};
    for (int i = 0; i < data_len; i++) {
        res[i] = (int) (pow(data[i], key)) % n;
    }
    res[data_len] = L'\0';
    return res;
}
