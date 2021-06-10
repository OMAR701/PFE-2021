include 'new_edit.asy';
size(20cm);
import graph;
import contour;
real v=0.000075426843851566;
real t=v*10000;
pair vp=(2,0.5);
path fs1=(0,0)--(7,0)--(7,1)--(0,1)--cycle;
filldraw(fs1,royalblue+opacity(0.5),bp+black);
for(int i=0;i<4;++i){
	draw((i*2+1,0)--shift(0,1)*(i*2+1,0),bp+black);
}
label("$n$",(0.5,0.5));
label("$xn-1$",(4,0.5));
label("$xn$",(2,0.5));
label("$|en|$",(6,0.5));

path fs=shift(0,-1)*fs1;
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
real newton(real f(real),real fprime(real),real nmax,real err=0.001, real x0){
	path c1=graph(f,0,3);
	real n=1,x;
		while(n<=nmax){
		x=x0-(f(x0)/fprime(x0));
		real e;
		e=((x-x0));


			for(int i=0;i<4;++i){
				draw((i*2+1,-n)--shift(0,1)*(i*2+1,-n),bp+black);
			}
			draw(shift(0,-n+1)*fs,bp+black);
			label(wrt(n),(0.5,0.5-n));


label(wrt(x0),(2,0.5-n));
			label(wrt(x),(4,0.5-n));
							label(wrt(e),(6,0.5-n));
			x0=x;
			n=n+1;
			if(e==0) return x;
		}
		return x;

	}
newton(f,fprime,10,0.0001,4);settings.outformat='png';settings.render=2;

