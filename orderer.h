#include<vector>

using namespace std;

int factorial(int i){
	int o=1;
	while(i>1){
		o*=i;
		i--;
	}
	return o;
}

vector<int> getorder(int order, int size){
	vector<int> orig(size, 0), facts(size, 0), takefrom(size, 0), out;
	int c=0;
	while(c<size){
		orig[c]=c;
		takefrom[c]=c;
		facts[c]=factorial(c);
		c++;
	}
	int divider, totake;
	while(out.size()<size){
		divider=facts[size-out.size()-1];
		totake=int(order/divider);
		order=order%divider;
		out.push_back(takefrom[totake]);
		takefrom.erase(takefrom.begin()+totake);
	}
	return out;
}
