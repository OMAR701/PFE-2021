int nbr=2;
string[] names={"a","b"};
struct mystruct{
int   a;int   b;
}
void fileWrite(mystruct[] m){
	file f=output("testing.txt");
int []a;int []b;
	for(int i=0;i<m.length;++i){
a[i]=m[i].a;b[i]=m[i].b;
	}
	int[] length={m.length};
	write(f,length);write(f);
write(f,a);write(f,b);
}
mystruct[] fileRead(){
	file f=input("testing.txt");
	int dim=f.dimension(1);
	mystruct[] m;
int []a;int []b;
for(int i=0;i<dim;++i){a[i]=f.line();}for(int i=0;i<dim;++i){b[i]=f.line();}
	for(int i=0;i<dim;++i){
		mystruct t;
t.a=a[i];t.b=b[i];
		m.push(t);
	}
	return m;
}
string[] mystructTostring(mystruct s){
	string[] t;
t[0]=(string)s.a;t[1]=(string)s.b;
	return t;
}
