#include<fstream>
#include<math.h>
#include<ctime>
#include<cstdlib>
#include<iostream>

using namespace std;

int flen(string fn){
	ifstream i(fn.c_str(), ios::binary | ios::ate);
	int p=i.tellg();
	i.close();
	return p;
}

struct strcode{
	string CODE, COD0, COD1, EVEN;
};

struct intcode{
	int COD0, COD1, EVEN;
};


struct codedata{
	strcode _str;
	intcode _int;
};

typedef struct codedata Codedata;

int len(string s){
	int c=0;
	while(s[c]!='\0')c++;
	return c;
}

int c_int_hex(int i){
	string hex_alpha="0123456789ABCDEF";
	return hex_alpha[i];
}
char c_hex_int(char c){
	string hex_alpha="0123456789ABCDEF";
	for(int cc=0; cc<16; cc++)if(c==hex_alpha[cc])return cc;
	return 'X';
}
string int_hex(int i, int mustbe){
	int c=0, res, cics=(int)(log(i)/log(16))+1;
	string out="";
	while(c<cics){
		res=i/pow(16.0, cics-c-1);
		i=i-(res*pow(16.0, cics-c-1));
		out+=c_int_hex(res);
		c++;
	}
	while(len(out)<mustbe)out='0'+out;
	return out;
}
int hex_int(string s){
	int ind=len(s)-1, out=0, tot=ind;
	while(ind>=0){
		out+=pow(16.0, ind)*c_hex_int(s[tot-ind]);
		ind--;
	}
	return out;
}

class Code{
	private:
		string hex_alpha="0123456789ABCDEF";
		Codedata CODE;

		void codegen(bool even){
			int r1, r2, r3;
			r1=rand();
			CODE._int.COD0=r1%65536;
			nanosleep((const struct timespec[]){{0, 500000000L}}, NULL);
			//cout<<"\nR1="<<r1<<" f: "<<CODE._int.COD0;

			r2=rand();
			CODE._int.COD1=r2%65536;
			nanosleep((const struct timespec[]){{0, 500000000L}}, NULL);
			//cout<<"\nR2="<<r2<<" f: "<<CODE._int.COD1;

			r3=rand();
			CODE._int.EVEN=2*(r3%127)+int(even);
			//cout<<"\nR3="<<r3<<" f: "<<CODE._int.EVEN;
			
			//cout<<"int: "<<CODE._int.COD0<<" "<<CODE._int.COD1<<" "<<CODE._int.EVEN<<endl;
			setcode(int_hex(CODE._int.COD0, 4)+int_hex(CODE._int.COD1, 4)+int_hex(CODE._int.EVEN, 2));
			//cout<<"str: "<<CODE._str.COD0<<" k "<<CODE._str.COD1<<" k "<<CODE._str.EVEN<<endl;

		}

		void setcode(string s){
			//cout<<"TOSET: "<<s<<endl;
			CODE._str.CODE=s;
			CODE._str.COD0=string({s[0], s[1], s[2], s[3]});
			CODE._str.COD1=string({s[4], s[5], s[6], s[7]});
			CODE._str.EVEN=string({s[8], s[9]});
			CODE._int.COD0=hex_int(CODE._str.COD0);
			CODE._int.COD1=hex_int(CODE._str.COD1);
			CODE._int.EVEN=hex_int(CODE._str.EVEN);
            //cout<<CODE._int.COD0<<" "<<CODE._int.COD1<<" "<<CODE._int.EVEN<<endl;
		}
	public:

		string getcode(){
                        return CODE._str.CODE;
        }
        
        Codedata getdata(){
            return CODE;
        }

		Code(string fn){
			srand(time(NULL));
			this->codegen(!flen(fn)%2);
			//cout<<this->getcode();
		}
		Code(string fn, string c){
			srand(time(NULL));
			this->setcode(c);
			//cout<<this->getcode();
		}
};

/*	
*	Code: AABBCCDDEE
*		AABB:
*			hex -> dec 
*					COD0
*
*		CCDD:
*			hex -> dec
*					COD1
*		EE:
*			hex -> dec
*					EVEN
*
*/



