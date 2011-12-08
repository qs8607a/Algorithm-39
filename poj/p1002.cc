#include <iostream>
#include <string>
#include <map>
#include <utility>
using std::map;
using std::string;
using std::cin;
int main(){
    int length;
    std::cin>>length;
    map<int,int> m;
    for(int i=0;i<=length;i++){
        string line;
        getline(cin,line);
        if(line.size()==0){
            continue;
        }
        int result=0;
        for (int j=0;j<line.size();j++){
            int n=0;
            if (line[j]>='0' && line[j]<='9'){
                n=line[j]-'0';
                result=result*10+n;
            }
            if (line[j]>='A' && line[j]<='Z'){
                n=line[j]-'A';
                if (n>15){
                    n=n-1;
                }
                n=n/3;
                n=n+2;
                result=result*10+n;
            }
        }
        if(m.count(result)){
            m[result]=m[result]+1;
        }else{
            m[result]=1;
        }
    }
    map<int,int>::const_iterator map_it=m.begin();
    while(map_it!=m.end()){
        if (map_it->second>1){
            std::cout<<map_it->first/10000<<"-"<<map_it->first%10000<<"  "<<map_it->second<<std::endl;
        }
        ++map_it;
    }
}
