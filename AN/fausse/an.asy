include 'edit.asy';
import graph;
import contour;
usepackage("mathrsfs");
unitsize(x=4cm,y=1cm);
transform ec=scale(.8);
xaxis(ec*"$x$",Ticks(ec*Label(), NoZero), Arrow(2mm));
yaxis(ec*"$y$", Ticks(ec*Label(), NoZero), Arrow(2mm));
labelx(ec*"$O$",0,SW);
real faussposition(real f(real),real an, real bn, int iterations, real erreur){
path c=graph(f,0,3);
draw(c,bp+blue);
real xn;
int iter=1;
while(iter<=iterations ){

xn=an-((bn-an)/(f(bn)-f(an))*f(an));
path p=(an,f(an))--(bn,f(bn));
draw(p,bp+red);
label("xn"+string(iter),(xn,0),1.2*N,2bp+green);
dot((xn,0),2bp+green);
label("an",(an,f(an)),1.2*SE,bp+green);
label("bn",(bn,f(bn)),1.2*N,bp+green);

if(f(an)*f(xn)<0) {bn=xn;}
else if(f(xn)*f(bn)<0) {an=xn;}
else{
return xn;
break;
}
iter+=1;

 }
return xn;
  }
faussposition(f,0,2,3,0.0001);
