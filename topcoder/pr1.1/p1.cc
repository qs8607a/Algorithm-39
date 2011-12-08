//Inv 2001R1
#include <iostream>
#include <string>
using std::string;

int pointVal(string param0){
    int result=0;
    int wordslong=0;
    int l=0;
    bool isword=false;
    for(int i=0;i<param0.size();i++){
        char c=param0[i];
        if(isword){
            if((c>='a'&&c<='z') ||(c>='A' && c<='Z')){
                l++;
                continue;
            }
            if(c==' '){
                wordslong+=l;
                result+=1;
            }
            if(c=='.'&&(i+1==param0.size() || param0[i+1]==' ')){
                i++;
                wordslong+=l;
                result+=1;
            }
            isword=false;
        }else{
            if((c>='a'&&c<='z') ||(c>='A' && c<='Z')){
                l=1;
                isword=true;
            }
        }
    }
    if(isword){
        wordslong+=l;
        result++;
    }
    result=wordslong/result;
    if(result<=3){
        result=250;
    }else if (result<=5){
        result=500;
    }else{
        result=1000;
    }
    return result;
}
int main(){
    string s1;
    getline(std::cin,s1);
    std::cout<<s1<<" : "<<pointVal(s1)<<std::endl;
    return 0;
}

