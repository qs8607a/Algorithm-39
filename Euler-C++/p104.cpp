#include <iostream>
bool pandigital(unsigned int n){
   int sum=0,prod=1;
   for(int i=0;i<9;i++){
       int t=n%10;
       n=n/10;
       sum+=t;
       prod*=t;
   } 
   return sum==45 && prod==362880;
}
unsigned int makeInt(unsigned int x0,unsigned int x1){
    unsigned i=1000000000;
    if( x0==0){
        return x1;
    }
    while(x0<100000000){
        x0*=10;
        i/=10;
    }
    x0+=(x1/i);
    return x0;
}
int main(){
    unsigned int a[10000]={1},b[10000]={1};
    unsigned int M=1,c=1;
    while(true){
        unsigned int t1=0,t2=0;
        for(int i=0;i<M;i++){
            t1=a[i]+b[i]+t1;
            t2=a[i]+(b[i]<<1)+t2;
            a[i]=t1%1000000000;
            b[i]=t2%1000000000;
            t1=t1/1000000000;
            t2=t2/1000000000;
        }
        c++;
        if(t2>0 || t1>0){
            M++;
            a[M-1]=t1;
            b[M-1]=t2;
        }
        if (pandigital(a[0]) && pandigital(makeInt(a[M-1],a[M-2]))){
            std::cout<<2*c-1<<std::endl;
            break;
        }
        if (pandigital(b[0]) && pandigital(makeInt(b[M-1],b[M-2]))){
            std::cout<<2*c<<std::endl;
            break;
        }
    }
    return 0;
}
