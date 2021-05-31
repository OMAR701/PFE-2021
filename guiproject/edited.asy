int nbr=1;
string[] names={"a"};
struct mystruct{
int  a;
}
void fileWrite(mystruct[] m){
	file f=output("testing.txt");
int[]a;
	for(int i=0;i<m.length;++i){
a[i]=m[i].a;
	}
	int[] length={m.length};
	write(f,length);write(f);
write(f,a);
}
mystruct[] fileRead(){
	file f=input("testing.txt");
	int dim=f.dimension(1);
	mystruct[] m;
int[]a;
for(int i=0;i<dim;++i){a[i]=f.line();}
	for(int i=0;i<dim;++i){
		mystruct t;
t.a=a[i];
		m.push(t);
	}
	return m;
}
string[] mystructTostring(mystruct s){
	string[] t;
t[0]=(string)s.a;
	return t;
}
