size(10cm);
import graph;
import contour;
usepackage("mathrsfs");
real v=0.000075426843851566;
real t=v*10000;
pair vp=(2,0.5);

path fs1=(0,0)--(15,0)--(15,1)--(0,1)--cycle;
filldraw(fs1,royalblue+opacity(0.5),bp+black);
for(int i=0;i<7;++i){
	draw((i*2+1,0)--shift(0,1)*(i*2+1,0),bp+black);
}
label("$k$",(0.5,0.5));
label("$a_k$",(2,0.5));
label("$f(a_k)$",(4,0.5));
label("$b_k$",(6,0.5));
label("$f(b_k)$",(8,0.5));
label("$x_k$",(10,0.5));
label("$f(x_k)$",(12,0.5));
label("$err_k$",(14,0.5));	
path fs=shift(0,-1)*fs1;
real f(real x) {return x^2-4;}
string wrt(real val){
	if(length(string(val))>6){
		real t=v*100000;
		if(t<1){
			return substr(string(val),0,4)+substr(string(v),length(string(val))-4,-1);
		}else{
			return substr(string(val),0,6);
		}	
	}
	return string(val);
}
real decho(real a,real b,real nmax,real err=0.001){
	path c1=graph(f,0,3); 
	if(f(a)==0)
		return a;
	else if(f(b)==0)
		return b;
	else if(f(a)*f(b)>0)
		return -1;
	else{
		real n=1;
		real x;
			
		while(n<=nmax){
			x=(a+b)/2;
			for(int i=0;i<7;++i){
				draw((i*2+1,-n)--shift(0,1)*(i*2+1,-n),bp+black);
			}
			draw(shift(0,-n+1)*fs,bp+black);
			label(wrt(n),(0.5,0.5-n));
			label(wrt(a),(2,0.5-n));
			label(wrt(f(a)),(4,0.5-n));
			label(wrt(b),(6,0.5-n));
			label(wrt(f(b)),(8,0.5-n));
			label(wrt(x),(10,0.5-n));
			label(wrt(f(x)),(12,0.5-n));
			label(wrt((b-a)/2),(14,0.5-n));		
			if(f(x)==0 || (b-a)/2<err)
				return x;
			if(f(a)*f(x)>0)
				a=x;
			else
				b=x;

			n=n+1;
		}
		return x;
		
	}
}
decho(0,3,12);