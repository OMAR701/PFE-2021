int nbr=3;
string[] names={"","",""};
struct mystruct{
int  ;int  ;int  ;
}
void fileWrite(mystruct[] m){
	file f=output("testing.txt");
int[];int[];int[];
	for(int i=0;i<m.length;++i){
[i]=m[i].;[i]=m[i].;[i]=m[i].;
	}
	int[] length={m.length};
	write(f,length);write(f);
write(f,);write(f,);write(f,);
}
mystruct[] fileRead(){
	file f=input("testing.txt");
	int dim=f.dimension(1);
	mystruct[] m;
int[];int[];int[];
for(int i=0;i<dim;++i){[i]=f.line();}for(int i=0;i<dim;++i){[i]=f.line();}for(int i=0;i<dim;++i){[i]=f.line();}
	for(int i=0;i<dim;++i){
		mystruct t;
t.=[i];t.=[i];t.=[i];
		m.push(t);
	}
	return m;
}
string[] mystructTostring(mystruct s){
	string[] t;
t[0]=(string)s.;t[1]=(string)s.;t[2]=(string)s.;
	return t;
}
