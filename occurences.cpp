#include<iostream>
using namespace std;





int main(){
int arr[20]={1,2,5,5,3,4,5,5,5,5,5,5,5,5,55,7};
// int n= arr.size();
     int count=0;

    for(int i=0;i<=20;i++){
   
    if(arr[i]==5){
        count=count+1;

    }
   
}
 cout<<"occerences is: "<<count;

    return 0;
}