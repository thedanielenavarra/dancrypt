#include"danlib.h"

void crypt(string fi, string fo, Code code){
    Codedata data=code.getdata();
    ifstream file_i(c_str(fi), ios::binary);
    ofstream file_o(c_str(fo), ios::binary);
    int bts_tot=flen(fi), bts_now=0, valnow, addnow=data._int.CODE0;
    char ibts[2], obts[2];
    bool disp=data._int.EVEN%2;
    while((bts_now-2*disp)<bts_tot){
        file_i.read(&ibts[0], 2);
        valnow=ibts[1]*256+ibts[0];
        valnow=(valnow+addnow)%65536;
        addnow=(addnow+data._int.COD1)%65536;
        obts={valnow%256, int(double(valnow/256))};
        file_o.write(obts);
        bts_now+=2;
    }
}