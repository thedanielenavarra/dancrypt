#include<iostream>
#include"danlib.h"
#include"dancrypt.h"
#include<ctime>

using namespace std;

void help(){
	cout<<"\ndancrypt-beta usage:\n"<<
		"\n\tCrypt:\n\t\tdancrypt-beta c [FILE_TO_CRYPT] [SAVE_CRYPTED_FILE_AS]\n"<<
		"\n\tDecrypt:\n\t\tdancrypt-beta d [FILE_TO_DECRYPT] [SAVE_DECRYPTED_FILE_AS] [CODE]\n";
}
void help(string s){cout<<s<<endl;help();}
/*
usage of class Code:

	constructor: 
		crypt: 		Code code(string filename);
					auto generation of code & keys
				code.getcode();
					returns string code

		decrypt: 	Code code(string filename, string code);
					code validation and auto setting of keys

*/



int main(int argc, char* argv[]){
    clock_t start=clock();
    double duration, p_duration=0;
    int bts, p_bts=0;
    if(fexists("dancrypt.log")){
        cout<<"READING LOG";
        ifstream f("dancrypt.log");
        f>>p_bts;
        f>>p_duration;
    }else{
        cout<<"NO LOG FOUND";
    }
    ofstream log("dancrypt.log");
	if(argc>2){
		if(argv[1][0]=='c'){//CRYPT
			try{
                string fi=argv[2], fo=argv[3];
                string c;
                Code code(fi);
                c=code.getcode();
                cout<<c<<endl;
                crypt(fi, fo, code);
                duration=p_duration+(clock()-start)/(double)CLOCKS_PER_SEC;
                bts=p_bts+flen(fi);
                log<<(double)(bts)<<endl<<duration;
			}catch(...){
				help("ARGUMENT in crypt ERROR");
			}
		}else if(argv[1][0]=='d'){//DECRYPT
			try{
				string fi=argv[2], fo=argv[3];
				string c=argv[4];
				Code code(fi, c);
                decrypt(fi, fo, code);
                duration=p_duration+(clock()-start)/(double)CLOCKS_PER_SEC;
                bts=p_bts+flen(fi);
                log<<(double)(bts)<<endl<<duration;
			}catch(...){
				help("ARGUMENT in decrypt ERROR");
			}
		}else{
			cout<<argv[1]<<endl;
			help("Wrong instruction");
			return 0;
		}
	}else{
		help("No instruction");
	}
	log.close();
    return 0;
    

}
