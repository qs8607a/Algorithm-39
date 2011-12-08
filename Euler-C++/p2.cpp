#include <iostream>
int m1();
int main(){
    std::cout<<m1()<<std::endl;
    return 0;
}
int m1(){
    int a=0,b=1,c=1;
    int result=0;
    while ((b+c)<4000000){
        a=b+c;
        b=c+a;
        c=a+b;
        result+=a;
    }
    return result;
}
