include 'edit.asy';
size(10cm);
import graph;
import contour;
usepackage("mathrsfs");
real v=0.000075426843851566;
real t=v*10000;
pair vp=(2,0.5);

path fs1=(0,0)--(7,0)--(7,1)--(0,1)--cycle;
filldraw(fs1,royalblue+opacity(0.5),bp+black);
for(int i=0;i<4;++i){
	draw((i*2+1,0)--shift(0,1)*(i*2+1,0),bp+black);
}
label("$n$",(0.5,0.5));
label("$|En|$",(4,0.5));
label("$xn$",(2,0.5));
label("$|k|$",(6,0.5));

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
real pointfixe(real g(real),real nmax,real err=0.001, real x0){
	path c1=graph(g,0,3);
	real n=1,x,En,Enn,val;
		while(n<=nmax){
		x=g(x0);
		En=abs((x-x0)/x																										);
		val=En-Enn;
	Enn=En;
			for(int i=0;i<4;++i){
				draw((i*2+1,-n)--shift(0,1)*(i*2+1,-n),bp+black);
			}
			draw(shift(0,-n+1)*fs,bp+black);
			label(wrt(n),(0.5,0.5-n));


label(wrt(x),(2,0.5-n));
			label(wrt(En),(4,0.5-n));
							label(wrt(val),(6,0.5-n));
			x0=x;
			n=n+1;
		}
		return x;

	}

pointfixe(g,3,0.001,1);
