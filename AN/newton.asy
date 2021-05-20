
import graph;
import contour;
usepackage("mathrsfs");
unitsize(x=4cm,y=1cm);
transform ec=scale(.8);
xaxis(ec*"$x$",Ticks(ec*Label(), NoZero), Arrow(2mm));
yaxis(ec*"$y$", Ticks(ec*Label(), NoZero), Arrow(2mm));
labelx(ec*"$O$",0,SW);
real f(real x) {return x^2-2;}
real fprime(real x){return 2*x;}
// on évite les valeurs 

//label(string(v),(0,0));
//dot((30,f(30)));
xlimits(0,60,Crop); // on coupe ce qui dépasse
real newton(real f(real),real fprime(real),int nmax,real err=0.001, real x0=4){
	path c1=graph(f,0,3); 
	draw(c1,bp+blue);
	int iterations=0;
	real x;
	real n;
	while(iterations<=nmax){
							
	x=x0-(f(x0)/fprime(x0));
	real e=(abs(x-x0));
	n=e;
  	/*label(string(iterations)+"     "+string(x)+"    "+string(e)+"    "+string(abs(e/n)),(0,-2*iterations)); */
	
	//label(string(f(x0)));
	dot((x0,f(x0)),red);
	
	if(abs(x-x0)<err){
	return x;
	
	}else{
	dot((x0,f(x0)));
	path p1=(x0,0)--((x0,f(x0)));
	label("x"+string(iterations),(x0,0),SE);
	draw(p1,bp+dashed+green);
	path p2=(0,f(x0))--((x0,f(x0)));
	label("f("+string(iterations)+")",(0,f(x0)),NW);
	draw(p2,bp+dashed+green);
	path p=(x0,f(x0))--(x,0);
	
	draw(p,bp+red);
	x0=x;
	iterations=iterations+1;}
	
	 }
	return x;
	}
newton(f,fprime,10,0.00001,2);
