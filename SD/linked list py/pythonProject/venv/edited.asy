int nbr=3;
string[] names={"a","b","c"};
struct mystruct{
int  a;string  b;int   c;
}
void fileWrite(mystruct[] m){
	file f=output("testing.txt");
int[]a;string[]b;int []c;
	for(int i=0;i<m.length;++i){
a[i]=m[i].a;b[i]=m[i].b;c[i]=m[i].c;
	}
	int[] length={m.length};
	write(f,length);write(f);
write(f,a);write(f,b);write(f,c);
}
mystruct[] fileRead(){
	file f=input("testing.txt");
	int dim=f.dimension(1);
	mystruct[] m;
int[]a;string[]b;int []c;
for(int i=0;i<dim;++i){a[i]=f.line();}for(int i=0;i<dim;++i){b[i]=f.line();}for(int i=0;i<dim;++i){c[i]=f.line();}
	for(int i=0;i<dim;++i){
		mystruct t;
t.a=a[i];t.b=b[i];t.c=c[i];
		m.push(t);
	}
	return m;
}
string[] mystructTostring(mystruct s){
	string[] t;
t[0]=(string)s.a;t[1]=(string)s.b;t[2]=(string)s.c;
	return t;
}
