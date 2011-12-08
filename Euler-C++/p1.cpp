#include <iostream>
int m1(int);
int m2(int);
int main(){
    std::cout<<m2(1000)<<std::endl;
    return 0;
}
int m1(int n){
    int result=0;
    for(int i=1;i<n;i++){
        if(i%3==0 || i%5==0)
            result+=i;
    }
    return result;
}
int sum(int n){
    return n*(n+1)/2;
}
int divisionsum(int n,int m){
    return m*sum(n/m);
}
int m2(int n){
    return divisionsum(n-1,3)+divisionsum(n-1,5)-divisionsum(n-1,15);
}
