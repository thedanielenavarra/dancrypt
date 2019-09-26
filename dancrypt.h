//#include"danlib.h"
#include<cstring>

void crypt(string fi, string fo, Code code){
    Codedata data=code.getdata();
    ofstream debug("debugc");
    ifstream file_i(fi.c_str(), ios::binary);
    ofstream file_o(fo.c_str(), ios::binary);
    int bts_tot=flen(fi), bts_now=0, addnow=data._int.COD0;
    long int valnow;
    char ibts[2], obts[2];
    bool disp=data._int.EVEN%2;
    while((bts_now-2*disp)<bts_tot){
        file_i.read(&ibts[0], 2);
        valnow=(unsigned int)(ibts[1]*256+ibts[0]);
        //cout<<valnow;
        valnow=(valnow+addnow)%65536;
        //cout<<"\t+\t"<<addnow<<"\t="<<valnow<<endl;
        obts[0]=valnow%256;
        obts[1]=int(double(valnow/256));
        debug<<int((unsigned char)(obts[0]))<<" _ "<<int((unsigned char)(obts[1]))<<" = "<<valnow<<endl;
        //cout<<addnow<<endl;
        //cout<<addnow<<endl;
        addnow=(addnow+data._int.COD1)%65536;    
        //cout<<valnow<<"="<<int(obts[0])<<" "<<int(obts[1])<<endl;
        file_o.write(&obts[0], 2);
        bts_now+=2;
    }
    if(disp){
        file_i.read(&ibts[0], 1);
        ibts[1]=0;
        valnow=ibts[1]*256+ibts[0];
        valnow=(valnow+addnow)%65536;
        obts[0]=valnow%256;
        obts[1]=int(double(valnow/256));
        file_o.write(&obts[0], 1);
        bts_now+=1;
    }
    //cout<<endl<<data._str.CODE<<endl;
}


void decrypt(string fi, string fo, Code code){
    Codedata data=code.getdata();
    ofstream debug("debugd");
    ifstream file_i(fi.c_str(), ios::binary);
    ofstream file_o(fo.c_str(), ios::binary);
    int bts_tot=flen(fi), bts_now=0, addnow=data._int.COD0;
    long valnow;
    char ibts[2], obts[2];
    bool disp=data._int.EVEN%2;
    while((bts_now-2*disp)<bts_tot){
        file_i.read(&ibts[0], 2);
        cout<<int((unsigned char)(ibts[0]))<<" _ "<<int((unsigned char)(ibts[1]));
        valnow=(unsigned char)(ibts[1])*256+ibts[0];
        //cout<<valnow;
        debug<<" = "<<valnow<<endl;
        debug<<int((unsigned char)(ibts[0]))<<"+"<<int((unsigned char)(ibts[1]))<<"*256"<<"="<<valnow<<endl;
        valnow-=addnow;
        while(valnow<0)valnow+=65536;
        //cout<<"\t-\t"<<addnow<<"\t="<<valnow<<endl;
        obts[0]=valnow%256;
        obts[1]=int((valnow-obts[0])/256);  
        //cout<<"SECONDO IL PC "<<valnow<<"/"<<256<<" FA "<<int(obts[1])<<endl;
        //cout<<addnow<<endl;
        addnow=(addnow+data._int.COD1)%65536; 
        //cout<<valnow<<"="<<int(obts[0])<<" "<<int(obts[1])<<endl;
        file_o.write(&obts[0], 2);
        bts_now+=2;
    }
    if(disp){
        file_i.read(&ibts[0], 1);
        ibts[1]=0;
        valnow=ibts[1]*256+ibts[0];
        //valnow=(valnow+addnow)%65536;
        valnow-=addnow;
        while(valnow<0)valnow+=65536;
        obts[0]=valnow%256;
        obts[1]=int(double(valnow/256));
        file_o.write(&obts[0], 1);
        bts_now+=1;
    }
}