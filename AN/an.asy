
import graph;
import contour;
usepackage("mathrsfs");
unitsize(x=1cm,y=1cm);
transform ec=scale(.8);
xaxis(ec*"$x$",Ticks(ec*Label(), NoZero), Arrow(2mm));
yaxis(ec*"$y$", Ticks(ec*Label(), NoZero), Arrow(2mm));
labelx(ec*"$O$",0,SW);
real f(real x) {return x^2-2;}
// on évite les valeurs 
path c1=graph(f,-3,3);
draw(c1,red+bp);
//label(string(v),(0,0));
//dot((30,f(30)));
//xlimits(0,60,Crop); // on coupe ce qui dépasse
/*real decho(real a,real b,int nmax,real err=0.001){
	path c1=graph(f,0,3); 
	if(f(a)==0)
		return a;
	else if(f(b)==0)
		return b;
	else if(f(a)*f(b)>0)
		return -1;
	else{
		int n=1;
		real x;
		dot((a,f(a)),blue);
		dot((b,f(b)),blue);
		draw((a,0)--(a,f(a)),bp+dashed+blue);
		draw((b,0)--(b,f(b)),bp+dashed+blue);
		fill((a,0)--c1--(b,0)--cycle,lightblue+opacity(0.5));
		draw(c1,bp+red);
		if(f(a)<0)
			label("a",(a,f(a)),SE,bp+blue);
		else
			label("a",(a,f(a)),N,bp+blue);
		if(f(b)<0)
			label("b",(b,f(b)),S,bp+blue);
		else
			label("b",(b,f(b)),N,bp+blue);	
		while(n<nmax+1){
			x=(a+b)/2;
					//	label(string(n)+" "+string(a)+" "+string(f(a))+"  "+string(b)+" "+string(f(b))+"  "+string(x)+""+string(f(x))+"   "+string((b-a)/2),(0,-n*10));
			if(f(x)==0 ||  (b-a)/2<err)
				return x;
			else
				n=n+1;
			if(f(a)*f(x)>0)
				a=x;
			else
				b=x;
			if(n<6 || n==nmax){
				dot((x,f(x)),blue);
				if(f(x)<0)
					label("x"+string(n-1),(x,f(x)),filltype=Fill(lightyellow),S);
				else{
					label("x"+string(n-1),(x,f(x)),filltype=Fill(lightyellow),N);}
				draw((x,0)--(x,f(x)),bp+dashed+green);
			}
		}
		return x;
		
	}
}
decho(0,3,12);*/
