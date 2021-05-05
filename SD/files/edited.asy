size(3.6cm);
int nbr=4;
string[] names={"x","y","s","z"};
struct mystruct{
int  x;int  y;string  s;int  z;
}
void fileWrite(mystruct[] m){
	file f=output("testing.txt");
int[]x;int[]y;string[]s;int[]z;
	for(int i=0;i<m.length;++i){
x[i]=m[i].x;y[i]=m[i].y;s[i]=m[i].s;z[i]=m[i].z;
	}
	int[] length={m.length};
	write(f,length);write(f);
write(f,x);write(f,y);write(f,s);write(f,z);
}
mystruct[] fileRead(){
	file f=input("testing.txt");
	int dim=f.dimension(1);
	mystruct[] m;
int[]x;int[]y;string[]s;int[]z;
for(int i=0;i<dim;++i){x[i]=f.line();}for(int i=0;i<dim;++i){y[i]=f.line();}for(int i=0;i<dim;++i){s[i]=f.line();}for(int i=0;i<dim;++i){z[i]=f.line();}
	for(int i=0;i<dim;++i){
		mystruct t;
t.x=x[i];t.y=y[i];t.s=s[i];t.z=z[i];
		m.push(t);
	}
	return m;
}
string[] mystructTostring(mystruct s){
	string[] t;
t[0]=(string)s.x;t[1]=(string)s.y;t[2]=(string)s.s;t[3]=(string)s.z;
	return t;
}
