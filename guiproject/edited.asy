int nbr=1;
string[] names={"q"};
struct mystruct{
int  q;
}
void fileWrite(mystruct[] m){
	file f=output("testing.txt");
int[]q;
	for(int i=0;i<m.length;++i){
q[i]=m[i].q;
	}
	int[] length={m.length};
	write(f,length);write(f);
write(f,q);
}
mystruct[] fileRead(){
	file f=input("testing.txt");
	int dim=f.dimension(1);
	mystruct[] m;
int[]q;
for(int i=0;i<dim;++i){q[i]=f.line();}
	for(int i=0;i<dim;++i){
		mystruct t;
t.q=q[i];
		m.push(t);
	}
	return m;
}
string[] mystructTostring(mystruct s){
	string[] t;
t[0]=(string)s.q;
	return t;
}
