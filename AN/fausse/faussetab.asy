include 'edit.asy';
size(10cm);
import graph;
import contour;
usepackage("mathrsfs");
real v=0.000075426843851566;
real t=v*10000;
pair vp=(2,0.5);

path fs1=(0,0)--(9,0)--(9,1)--(0,1)--cycle;
filldraw(fs1,royalblue+opacity(0.5),bp+black);
for(int i=0;i<4;++i){
	draw((i*2+1,0)--shift(0,1)*(i*2+1,0),bp+black);
}
label("$n$",(0.5,0.5));
label("$an$",(2,0.5));
label("$bn$",(4,0.5));
label("$x$",(6,0.5));
label("$e$",(8,0.5));
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
real fausseposition(real f(real),real an,real bn,real nmax,real err){
	path c1=graph(f,0,3);
		real n=1;
		real x;
			real x0;
		while(n<=nmax){
			x=an-((bn-an)/(f(bn)-f(an))*f(an));
			real e=abs(x-x0);
			x0=x;
			for(int i=0;i<4;++i){
				draw((i*2+1,-n)--shift(0,1)*(i*2+1,-n),bp+black);
			}
			draw(shift(0,-n+1)*fs,bp+black);
			label(wrt(n),(0.5,0.5-n));
			label(wrt(an),(2,0.5-n));
			label(wrt(bn),(4,0.5-n));
			label(wrt(x),(6,0.5-n));
			label(wrt(e),(8,0.5-n));

			if(f(an)*f(x)<0){bn=x;}
        else if(f(x)*f(bn)<0){an=x;}

			n=n+1;
		}
		return x;

	}

fausseposition(f,0,2,3,0.0001);
