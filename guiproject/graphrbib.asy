include"gm_graphes";
include"gm_graphes_styles";
size(6cm);

real[][] matadj={{1,1,1},{1,1,1},{1,1,1}};
GRAPHE gr=GRAPHE( matadj,configuration="cercle",style_boule_4);


draw(gr,aff_a_lab=true);
