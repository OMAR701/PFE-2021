
include"edited.asy";
mystruct t;
int[] nbrchar;
t.a=11111112111;t.v=211111211111;t.c=1111121111111;
string[][] mystructToMatrice(mystruct s[]){
	string[][] mat;
	for(int i=0;i<s.length;++i){
		mat[i]=	mystructTostring(s[i]);
	}
	return mat;
}
string oneline(string str[]){
    string line;
for(int i=0;i<str.length-1;++i){
		line=line + names[i]+":"+str[i]+" - " ;
	}
	line=line + names[str.length-1]+":"+str[str.length-1];
	return line;
	}
	
void drawlinkedlist(mystruct S[],int color=1){
int x=20;
size(x*0.4cm);

 string line;
 string[][] mat;
   mat=mystructToMatrice(S);
   path A=(0,0)--(10,0)--(10,1)--(0,1)--cycle;
   
	for(int i=0;i<mat.length-1;++i){
	line=oneline(mat[i]);
	label(line,shift(0,i)*(5,0.5));
	path A1=shift(0,i)*A;
	draw(A1);
		
	}
	if(color==1){
	 		 line=oneline(mat[mat.length-1]);
	  		label(line,shift(0,mat.length-1)*(5,0.5));
	        path A1=shift(0,mat.length-1)*A;
			filldraw(A1,bp+palegreen);
			
		}
	if(color==2){
	line=oneline(mat[mat.length-1]);
	label(line,shift(0,mat.length)*(5,0.5));
	path A1=shift(0,mat.length)*A;
	filldraw(A1,bp+palered);
	
	}
	}
	void pushList(){
	
	mystruct[] m=fileRead();
	m.push(t);
	fileWrite(m);
	drawlinkedlist(m,1);
	
   }
   void popList(){
	mystruct[] m=fileRead();
	drawlinkedlist(m,2);
	m.pop();
	fileWrite(m);
}
