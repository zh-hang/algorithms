//
// Created by 35116 on 2021/6/9.
//

#include "crypt.h"

RC4::RC4(const char *key, int key_len) {
    RC4_DATATYPE k[LEN] = {0};
    for (int i = 0; i < LEN; i++) {
        this->s_box[i] = (RC4_DATATYPE)i;
        k[i] = key[i % key_len];
    }

    int j(0);
    for (int i = 0; i < LEN; i++) {
        j = (j + this->s_box[i] + k[i]) % LEN;
        swap(this->s_box[i], this->s_box[j]);
    }
}

void RC4::crypt() {
    int pos;
    this->result=new RC4_DATATYPE[this->data_len + 1];
    for (int i = 0; i < this->data_len; i++) {
        pos = i % LEN;
        this->result[i] = (RC4_DATATYPE)(this->data[i] ^ this->s_box[pos]);
    }
    this->result[data_len]='\0';
}


RC4_DATATYPE *RC4::get_result() {
    return this->result;
}


void RC4::encrypt(RC4_DATATYPE *str, int str_len) {
    this->data = str;
    this->data_len = str_len;
    this->crypt();
}

void RC4::decrypt(RC4_DATATYPE *str, int str_len) {
    this->data = str;
    this->data_len = str_len;
    this->crypt();
}


void RSA::encrypt(unsigned char *str, int str_len) {

}

void RSA::decrypt(unsigned char *str, int str_len) {

}

RC4_DATATYPE *RSA::get_result() {
    return this->result;
}

Crypt::~Crypt() {
    delete(this->result);
    this->result= nullptr;
}
