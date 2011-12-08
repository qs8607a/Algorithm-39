#include <iostream>
#include <vector>
#include <set>
using std::vector;
using std::set;
int maxTurns(vector<int> cards){
    bool hasValue=false;
    int valueNum=0;
    int result=0;
    set<int> cardsSet(cards.begin(),cards.end());
    for(int i=1;i<=500;i++){
        if(cardsSet.count(i)){
            if(hasValue){
                valueNum++;
            }else{
                valueNum=1;
                hasValue=true;
            }
        }else{
            if(hasValue){
                result+=(valueNum+1)/2;
                hasValue=false;
            }
        }
    }
    return result;
}
int main(){
    vector<int> cards;
    //cards.push_back(498);
    //cards.push_back(499);
    //cards.push_back(100);
    //cards.push_back(200);
    //cards.push_back(300);
    //cards.push_back(400);
    cards.push_back(11);
    cards.push_back(12);
    cards.push_back(102);
    cards.push_back(13);
    cards.push_back(100);
    cards.push_back(101);
    cards.push_back(99);
    cards.push_back(9);
    cards.push_back(8);
    cards.push_back(1);
    std::cout<<maxTurns(cards)<<std::endl;
    return 0;
}
