#include <iostream>
#include <vector>
#define MAXSIZE 500
using std::vector;
double probabilityToLose(int N,vector<int> decisions){
    int V[MAXSIZE];
    for(int i=0;i<N;i++){
        V[i]=0;
    }
    int max=0;
    for(vector<int>::const_iterator iter=decisions.begin();iter!=decisions.end();++iter){
        int x=*iter;
        V[x]++;
        if(V[x]>max){
            max=V[x];
        }
    }
    if(max==1){
        return 0;
    }
    int re=0;
    for(int i=0;i<N;i++){
        if(V[i]==max){
            re++;
        }
    }
    double result=((double)1.0)/re;
    if(re==1){
        return 1;
    }
    while(re>1){
        re=N%re;
    }
    if(re==1){
        return result;
    }else{
        return 0;
    }
}
int main(){
    //int N=3;
    //vector<int> decisions(3,1);
    //int N=5;
    //vector<int> decisions;
    //decisions.push_back(1);
    //decisions.push_back(2);
    //decisions.push_back(3);
    int N=20;
    vector<int> decisions;
    decisions.push_back(1);
    decisions.push_back(2);
    decisions.push_back(3);
    decisions.push_back(4);
    decisions.push_back(5);
    decisions.push_back(6);
    decisions.push_back(7);

    decisions.push_back(1);
    decisions.push_back(2);
    decisions.push_back(3);
    decisions.push_back(4);
    decisions.push_back(5);
    decisions.push_back(6);
    decisions.push_back(7);
    std::cout.precision(9);
    std::cout<<probabilityToLose(N,decisions)<<std::endl;
    return 0;
}
