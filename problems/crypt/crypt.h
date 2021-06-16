//
// Created by 35116 on 2021/6/9.
//

#ifndef CRYPTALGORITHM_CRYPT_H
#define CRYPTALGORITHM_CRYPT_H

#include <cstdlib>
#include <string>

#define RC4_DATATYPE unsigned char
#define RSA_DATATYPE wchar_t
#define LEN 256
template<typename T>
static void swap(T &a, T &b) {
    T temp = a;
    a = b;
    b = temp;
}

template<typename T>
static T phi(T n) {
    T res = n;
    for (T i = 2; i * i <= n; ++i) {
        if (n % i == 0) {
            res = res / i * (i - 1);
            while (n % i == 0) {
                n /= i;
            }
        }
    }
    return n > 1 ? (res / n * (n - 1)) : res;
}

template<typename T>
static T gcd(T a,T b) {
    if (a < b) swap(a, b);
    return b == 0 ? a : gcd(b, a % b);
}



class Crypt {
public:
    RC4_DATATYPE *result = nullptr;

    Crypt() = default;

    virtual ~Crypt();

    virtual void encrypt(RC4_DATATYPE *str, int str_len) = 0;

    virtual void decrypt(RC4_DATATYPE *str, int str_len) = 0;

    virtual RC4_DATATYPE *get_result() = 0;
};


class RC4 : public Crypt {
    RC4_DATATYPE s_box[256]{0};
    RC4_DATATYPE *data = nullptr;
    int data_len = 0;

    void crypt();


public:
    RC4(const char *key, int key_len);

    ~RC4() override = default;

    void encrypt(RC4_DATATYPE *str, int str_len) override;

    void decrypt(RC4_DATATYPE *str, int str_len) override;

    RC4_DATATYPE *get_result() override;
};

class RSA : public Crypt {

public:
    RSA() = default;

    ~RSA() override = default;

    void encrypt(RC4_DATATYPE *str, int str_len) override;

    void decrypt(RC4_DATATYPE *str, int str_len) override;

    RC4_DATATYPE *get_result() override;
};


#endif //CRYPTALGORITHM_CRYPT_H
