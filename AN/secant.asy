
import graph;
import contour;
usepackage("mathrsfs");
unitsize(x=4cm,y=1cm);
transform ec=scale(.8);
xaxis(ec*"$x$",Ticks(ec*Label(), NoZero), Arrow(2mm));
yaxis(ec*"$y$", Ticks(ec*Label(), NoZero), Arrow(2mm));
labelx(ec*"$O$",0,SW);
real f(real x) {return exp(x)+x;}
// on évite les valeurs 

//label(string(v),(0,0));
//dot((30,f(30)));
xlimits(0,60,Crop); // on coupe ce qui dépasse
real secant(real f(real),real x1,real x2,int nmax,real err){
	path c1=graph(f,0,3); 
	draw(c1,bp+blue);
	int iterations=1;
	real x,y1,y2,n,e;
	while(iterations<=nmax ){
	y1=f(x1);y2=f(x2);						
	x=x2-((y2*(x2-x1))/(y2-y1));
	real e=(abs(x-x2)/abs(x));
	n=e;
  	/*label(string(iterations)+"  "+string(x)+"    "+string(e)+"    "+string(abs(e/n)),(0,-2*iterations)); */
	
	//label(string(f(x0)));
	//dot((x0,f(x0)),red);
	
	if(e<err){
	iterations=nmax;
	return x;}
	else{
	dot((x1,y1));
	path p1=(x2,0)--((x1,y1));
	label("x"+string(iterations+1),(x2,0),SW);
	draw(p1,bp+red);
	path p2=(x,0)--((x2,y2));
	draw(p2,bp+red);
	
	x1=x2;x2=x;
	y1=y2;y2=f(x);
	iterations=iterations+1;}
	
	 }
	return x;
	}
secant(f,1,3,10,0.00000001);