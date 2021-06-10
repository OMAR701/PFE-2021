int nbr=1;
string[] names={"wdf"};
struct mystruct{
int  wdf;
}
void fileWrite(mystruct[] m){
	file f=output("testing.txt");
int[]wdf;
	for(int i=0;i<m.length;++i){
wdf[i]=m[i].wdf;
	}
	int[] length={m.length};
	write(f,length);write(f);
write(f,wdf);
}
mystruct[] fileRead(){
	file f=input("testing.txt");
	int dim=f.dimension(1);
	mystruct[] m;
int[]wdf;
for(int i=0;i<dim;++i){wdf[i]=f.line();}
	for(int i=0;i<dim;++i){
		mystruct t;
t.wdf=wdf[i];
		m.push(t);
	}
	return m;
}
string[] mystructTostring(mystruct s){
	string[] t;
t[0]=(string)s.wdf;
	return t;
}
