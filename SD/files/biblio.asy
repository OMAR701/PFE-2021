size(3cm);
include"edited.asy";
mystruct t;
int[] nbrchar;
t.x=5;t.y=2;t.s="gfdf";t.z=2;
int nbrch=6;
void nbrWrite(int[] nbrchar){
	file f=output("nbrchar.txt");
	int[] length={nbrchar.length};
	write(f,length);
write(f,nbrchar);
}
int[] nbrRead(){
	file f=input("nbrchar.txt");
	int[]nbrchar;
	int dim=f.dimension(1);
	for(int i=0;i<dim;++i){
		nbrchar[i]=f.line();	
	}
return nbrchar;
}
string[][] mystructToMatrice(mystruct s[]){
	string[][] mat;
	for(int i=0;i<s.length;++i){
		mat[i]=	mystructTostring(s[i]);
	}
	return mat;
}
void drawlinkedlist(int nbrLigne,string names[],string values[],int nbrchar,pair shifting,int sizing,int color=0){
	pair C=(4,nbrLigne),h=shift(shifting)*(2,0.5);
	if(nbrchar>6){
		C=(4+(nbrchar-6)*0.5,nbrLigne);h=shift(shifting)*((4+(nbrchar-6)*0.5)/2,0.5);
		size(3cm+(nbrchar-6)*0.4cm+sizing*30);
	}else{
		nbrchar=6;	
		size(3cm+sizing*30);
	}
	pair A=(0,0),B=(0,nbrLigne),D=shift(0,-nbrLigne)*C,x=(0,1),y=shift(0,1)*D;
	pair f1=shift(0,.5)*D,f2=shift(2,2)*D;
	path n=A--B--C--D--cycle;
	path last=A--B--C--D--A--x--y;
	path next=A--x--y--D--cycle;
	path up=x--B--C--y--cycle;
	path n1=shift(shifting)*n;
	path up1=shift(shifting)*up;
	path next1=shift(shifting)*next;
	path last1=shift(shifting)*last;
	if(color==1){
		fill(n1,bp+palegreen);
		draw(n1,2*bp+black);
	}else if(color==2){
		fill(n1,bp+lightred);
		draw(n1,2*bp+black);
	}else{
		draw(n1,2*bp+black);
	}
	for(int i=0;i<nbrLigne;++i){
		label(names[i]+" : "+values[i],shift(0,i)*h);
	}
}
void drawNull(pair shifting,int sizing){
	path end=(0,0)--(0,4)--(0,3)--(1,4)--(0,3)--(0,2)--(1,3)--(0,2)--(0,1)--(1,2)--(0,1)--(0,0)--(1,1)--(0,0);
	path end1=shift(shifting)*end;
	draw(end1,bp+black);
}
void drawList(string values[][],int nbrchar[],int total,int index,int color=0,mystruct p=null,int pp=0){
	int s=0,clr=0;
	if(total!=0){
	draw((0,nbr)--(2,nbr),2*bp+black);
		if(color==3 || index==0 && p==null)
			clr=1;
		drawlinkedlist(nbr,names,values[0],nbrchar[0],(2,0),0,clr);
		
		for(int i=1;i<total;++i){
			s=0;clr=0;
			if(color==1 && i==total-1 || i==index && p==null){
				clr=1;			
			}else if(i==index && p!=null){
				clr=2;
				if(i==1)
					drawlinkedlist(nbr,names,mystructTostring(p),pp,(4*i+2+(s-6*i)*0.5,2+names.length),4*i,clr);
				else
					drawlinkedlist(nbr,names,mystructTostring(p),pp,(4*i+2+(s-6*i)*0.5,2+names.length),4*i,clr);
				clr=0;
			}
			for(int j=0;j<i;++j){
				s=s+nbrchar[j];
			}
		if(i==1)
			drawlinkedlist(nbr,names,values[i],nbrchar[i],(4*i+2+(s-6*i)*0.5,0),4*i,clr);
		else
			drawlinkedlist(nbr,names,values[i],nbrchar[i],(4*i+2+(s-6*i)*0.5,0),4*i,clr);
		}
	}
	s=0;
	for(int j=0;j<total;++j){
		s=s+nbrchar[j];
	}
	//drawNull(4*total+2+(s-6*total)*0.5,4*(total-1)+1);
	
	if(p!=null && color==2 || index==nbrchar.length && p!=null){
		s=s+2;
		clr=2;
		drawlinkedlist(nbr,names,mystructTostring(p),pp,(4*(total)+2+(s-6*(total))*0.5,0),4*(total)+2,clr);
		draw((0,nbr)--(4*(total+1)+2+(s+2-6*(total+1))*0.5+4+(pp-6)*0.5,nbr),3*bp+black);
		draw((0,0)--(4*(total+1)+2+(s+2-6*(total+1))*0.5+4+(pp-6)*0.5,0),3*bp+black);
	}else{
	draw((0,nbr)--(4*(total+1)+2+(s+2-6*(total+1))*0.5,nbr),3*bp+black);
	draw((0,0)--(4*(total+1)+2+(s+2-6*(total+1))*0.5,0),3*bp+black);
	}
}
void pushList(){
	mystruct[] m=fileRead();
	nbrchar=nbrRead();
	nbrchar.push(nbrch);
	m.push(t);
	nbrWrite(nbrchar);
	fileWrite(m);
	drawList(mystructToMatrice(m),nbrchar,m.length,-1,1);
}
void popList(){
	mystruct[] m=fileRead();
	nbrchar=nbrRead();
	mystruct p=m.pop();
	int pp=nbrchar.pop();
	nbrWrite(nbrchar);
	fileWrite(m);
	drawList(mystructToMatrice(m),nbrchar,m.length,-1,2,p,pp);
}
void pushFirst(){
	mystruct[] m=fileRead();
	nbrchar=nbrRead();
	nbrchar.insert(0,nbrch);
	m.insert(0,t);
	nbrWrite(nbrchar);
	fileWrite(m);
	drawList(mystructToMatrice(m),nbrchar,m.length,-1,3);
}
void popFirst(){
	mystruct[] m=fileRead();
	nbrchar=nbrRead();
	mystruct p=m[0];
	m.delete(0);
	int pp=nbrchar[0];
	nbrchar.delete(0);
	nbrWrite(nbrchar);
	fileWrite(m);
	drawList(mystructToMatrice(m),nbrchar,m.length,-1,4,p,pp);
}
void pushIndex(int index){
	mystruct[] m=fileRead();
	nbrchar=nbrRead();
	if(index<=nbrchar.length && index>=0){
		nbrchar.insert(index,nbrch);
		m.insert(index,t);
		nbrWrite(nbrchar);
		fileWrite(m);
		drawList(mystructToMatrice(m),nbrchar,m.length,index);
	}
}
void popIndex(int index){
	mystruct[] m=fileRead();
	nbrchar=nbrRead();
	if(index<nbrchar.length && index>=0){
		mystruct p=m[index];
		m.delete(index);
		int pp=nbrchar[index];
		nbrchar.delete(index);
		nbrWrite(nbrchar);
		fileWrite(m);
		drawList(mystructToMatrice(m),nbrchar,m.length,index,5,p,pp);
	}
}
