int nbr=3;
string[] names={"a","b","nom"};
struct mystruct{
int  a;int  b;string  nom;
}
void fileWrite(mystruct[] m){
	file f=output("testing.txt");
int[]a;int[]b;string[]nom;
	for(int i=0;i<m.length;++i){
a[i]=m[i].a;b[i]=m[i].b;nom[i]=m[i].nom;
	}
	int[] length={m.length};
	write(f,length);write(f);
write(f,a);write(f,b);write(f,nom);
}
mystruct[] fileRead(){
	file f=input("testing.txt");
	int dim=f.dimension(1);
	mystruct[] m;
int[]a;int[]b;string[]nom;
for(int i=0;i<dim;++i){a[i]=f.line();}for(int i=0;i<dim;++i){b[i]=f.line();}for(int i=0;i<dim;++i){nom[i]=f.line();}
	for(int i=0;i<dim;++i){
		mystruct t;
t.a=a[i];t.b=b[i];t.nom=nom[i];
		m.push(t);
	}
	return m;
}
string[] mystructTostring(mystruct s){
	string[] t;
t[0]=(string)s.a;t[1]=(string)s.b;t[2]=(string)s.nom;
	return t;
}
