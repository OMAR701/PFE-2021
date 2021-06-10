 real x0=5; 
include "new_edit.asy";
import graph;
import contour;

// on évite les valeurs

//label(string(v),(0,0));
//dot((30,f(30)));

 // on coupe ce qui dépasse
real newton(real f(real),real fprime(real),int nmax,real err, real x0){

if (f(x0)>x0){
	real a=abs((2*x0)/f(x0));
unitsize(x=2cm,y= a*1cm);
} else{
real b = abs((2*f(x0))/x0);
unitsize(x=b*1cm,y= 2cm);
}

usepackage("mathrsfs");
transform ec=scale(.8);
xaxis(ec*"$x$",Ticks(ec*Label(), NoZero), Arrow(2mm));
yaxis(ec*"$y$", Ticks(ec*Label(), NoZero), Arrow(2mm));
labelx(ec*"$O$",0,SW);
xlimits(0,60,Crop);

	path c1=graph(f,0,x0);
	draw(c1,bp+blue);
	int iterations=0;
	real x;
	real n;
	while(iterations<=nmax){
	x=x0-(f(x0)/fprime(x0));
	real e=(abs(x-x0));
	n=e;
	dot((x0,f(x0)),red);
	if(abs(x-x0)<err){
	return x;

	}else{
	if(iterations==0 || iterations==1 || iterations==nmax){
	dot((x0,f(x0)));
	path p1=(x0,0)--((x0,f(x0)));
	label("x"+string(iterations),(x0,0),SE);
	draw(p1,dashed+green);
	path p2=(0,f(x0))--((x0,f(x0)));
	label("f("+string(iterations)+")",(0,f(x0)),NW);
	draw(p2,dashed+green);
	path p=(x0,f(x0))--(x,0);

	draw(p,red);

	}
	x0=x;
	}
	iterations=iterations+1;
	 }
	return x;
	}
newton(f,fprime,10,0.0001,5);
