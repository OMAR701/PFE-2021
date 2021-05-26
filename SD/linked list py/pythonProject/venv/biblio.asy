size(3.9cm);
include"edited.asy";
mystruct t;
int[] nbrchar;
t.a=1;t.b="test";t.c=2;
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
void drawlinkedlist(int nbrLigne,string names[],string values[],int nbrchar,pair shifting,real sizing,int color=0){
	pair C=(4,nbrLigne+1),h=shift(shifting)*(2,0.5);
	if(nbrchar>6)
		C=(4+(nbrchar-6)*0.5,nbrLigne+1);h=shift(shifting)*((4+(nbrchar-6)*0.5)/2,0.5);
	size(sizing*27);
	pair A=(0,0),B=(0,nbrLigne+1),D=shift(0,-(nbrLigne+1))*C,x=(0,1),y=shift(0,1)*D;
	pair f1=shift(0,.5)*D,f2=shift(2,2)*D;
	path n=A--B--C--D--A--x--y--f1--f2;
	path last=A--B--C--D--A--x--y;
	path next=A--x--y--D--cycle;
	path up=x--B--C--y--cycle;
	path n1=shift(shifting)*n;
	path up1=shift(shifting)*up;
	path next1=shift(shifting)*next;
	path last1=shift(shifting)*last;
	fill(next1,bp+heavycyan);
	if(color==1){
		fill(up1,bp+palegreen);
		draw(n1,bp+black,Arrow);
	}else if(color==2){
		fill(up1,bp+lightred);
		draw(last1,bp+black);
	}else{
		draw(n1,bp+black,Arrow);
	}
	label("$next$",h);
	for(int i=0;i<nbrLigne;++i){
		label(names[i]+" : "+values[i],shift(0,i+1)*h,NoAlign,bp+black);
	}
}
void drawNull(pair shifting,real sizing){
	size(sizing*27+1cm);
	path end=(0,0)--(0,4)--(0,3)--(1,4)--(0,3)--(0,2)--(1,3)--(0,2)--(0,1)--(1,2)--(0,1)--(0,0)--(1,1)--(0,0);
	path end1=shift(shifting)*end;
	draw(end1,bp+black);
}
void drawList(string values[][],int nbrchar[],int total,int index,int color=0,mystruct p=null,int pp=0){
	int s=0,clr=0;
	real size=0,tsize=0;
	if(total!=0){
		if(nbrchar[0]>6){
			size=3.9+(nbrchar[0]-6)*0.4;
		}else{
			nbrchar[0]=6;	
			size=3.9;
		}
		tsize=tsize+size;
		if(color==3 || index==0 && p==null)
			clr=1;
		drawlinkedlist(nbr,names,values[0],nbrchar[0],(0,0),tsize,clr);
		for(int i=1;i<total;++i){
			if(nbrchar[i]>6){
				size=3.9+(nbrchar[i]-6)*0.4;
			}else{
				nbrchar[i]=6;	
				size=3.9;
			}
			tsize=tsize+size;
			s=0;clr=0;
			if(color==1 && i==total-1 || i==index && p==null){
				clr=1;			
			}else if(i==index && p!=null){
				clr=2;
				drawlinkedlist(nbr,names,mystructTostring(p),pp,(6*i+(s-6*i)*0.5,2+names.length),tsize,clr);
				clr=0;
			}
			for(int j=0;j<i;++j){
				s=s+nbrchar[j];
			}
			drawlinkedlist(nbr,names,values[i],nbrchar[i],(6*i+(s-6*i)*0.5,0),tsize,clr);
		}
	}
	s=0;
	for(int j=0;j<total;++j){
		s=s+nbrchar[j];
	}
	drawNull(6*total+(s-6*total)*0.5,tsize);
	if(p!=null && color==2 || index==nbrchar.length && p!=null){
		s=s+pp;
		clr=2;
		size=3.9+(pp-6)*0.4;
		tsize=tsize+size*1.8;
		drawlinkedlist(nbr,names,mystructTostring(p),pp,6*(total)+(s-6*(total))*0.5,tsize,clr);
	}else if(p!=null && color==4 || index==0 && p!=null){
		clr=2;
		size=3.9+(pp-6)*0.4;
		tsize=tsize+size*1.8;
		drawlinkedlist(nbr,names,mystructTostring(p),pp,(-6-(pp-6)*0.5,0),tsize,clr);
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
