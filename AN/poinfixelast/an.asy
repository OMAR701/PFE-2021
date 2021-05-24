include 'edit.asy';
import graph;
import contour;
usepackage("mathrsfs");
unitsize(x=4cm,y=1cm);
transform ec=scale(.8);
xaxis(ec*"$x$",Ticks(ec*Label(), NoZero), Arrow(2mm));
yaxis(ec*"$y$", Ticks(ec*Label(), NoZero), Arrow(2mm));
labelx(ec*"$O$",0,SW);

real y(real x){return x;}
void pointfixe(real g(real),real x0, real iterations, real epsilon){
path c=graph(g,0,9);
path c2=graph(y,0,28);
draw(c,bp+blue);
label("g(x)",(3,g(3)),2bp+green);
draw(c2,bp+heavygreen);
real x;
real rk=epsilon+1;
int iter=1;
dot((x0,0),2bp+red);
label("x0",(x0,0),S);
path p1=(x0,0)--(x0,g(x0));
draw(p1,MidArrow(HookHead,Fill(green)));

while(rk>epsilon & iter<=iterations ){
path p3=(x0,y(x0))--(x0,g(x0));
draw(p3,MidArrow(HookHead,Fill(green)));
x=g(x0);
rk=abs(x-x0);


path p2=(x0,g(x0))--(x,y(x));
draw(p2,MidArrow(HookHead,Fill(green)));
dot((x,0),2bp+red);
label("x"+string(iter),(x,0),S);

iter+=1;
x0=x;
 }

  }
pointfixe(g,1,3,0.001);
