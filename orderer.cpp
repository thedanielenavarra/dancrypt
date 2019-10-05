#include"orderer.h"
#include<iostream>
int main(){
	int s, o=0;
	cout<<"Size: ";
	cin>>s;
	vector<int> r;
	while(o<factorial(s)){
		r=getorder(o, s);
		for(int i=0; i<s; i++){
			cout<<r[i];
		}
		cout<<endl;
		o++;
	}
	return 0;
}
