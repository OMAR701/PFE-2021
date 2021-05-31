int nbr=1;
string[] names={"df"};
struct mystruct{
int  df;
}
void fileWrite(mystruct[] m){
	file f=output("testing.txt");
int[]df;
	for(int i=0;i<m.length;++i){
df[i]=m[i].df;
	}
	int[] length={m.length};
	write(f,length);write(f);
write(f,df);
}
mystruct[] fileRead(){
	file f=input("testing.txt");
	int dim=f.dimension(1);
	mystruct[] m;
int[]df;
for(int i=0;i<dim;++i){df[i]=f.line();}
	for(int i=0;i<dim;++i){
		mystruct t;
t.df=df[i];
		m.push(t);
	}
	return m;
}
string[] mystructTostring(mystruct s){
	string[] t;
t[0]=(string)s.df;
	return t;
}
