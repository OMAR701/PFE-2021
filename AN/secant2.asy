
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
void secant(real f(real),real x1,real x2,int nmax,real err){
	path c1=graph(f,0,3); 
	draw(c1,bp+blue);
	int iterations=1;
	real x3,y1,y2,n,e;
    for(int i=0;i<nmax;++i){
	y1=f(x1);y2=f(x2);						
	//x=x2-((y2*(x2-x1))/(y2-y1));
	x3=(x1*f(x2)-x2*f(x1))/(f(x2)-f(x1));
	real e=abs((x3-x2)/x3);
	n=e;
  	/*label(string(iterations)+"  "+string(x)+"    "+string(e)+"    "+string(abs(e/n)),(0,-2*iterations)); */
	//label(string(f(x0)));
	//dot((x0,f(x0)),red);
	
	if(err<e){
	dot((x1,y1));
		dot((x3,f(x3)));
		path p1=(x2,0)--((x1,f(x1)));
		path p2=(x3,0)--((x2,f(x2)));
	label("x"+string(i+1),        (x2,0),SW);
	draw(p1,bp+red);
	dot((0,f(x2)));
	path p3=((x1,0)--(x1,f(x1))--(0,f(x1)));
	draw(p3,dashed+bp+green);
	draw(p2,bp+red);
	x1=x2;x2=x3;
	//iterations+=1;
	}else{
	break;
	}
	}	
	}
secant(f,1,3,10,0.0001);