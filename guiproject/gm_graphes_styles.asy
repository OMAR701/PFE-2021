// Des styles prédéfinis de graphes pour l'extension gm_graphes

import gm_graphes;


/////**** Nouveau filltype
/////**** RadialShade avec centre légèrement décalé
filltype EffetBalle(pen penc, pen penr)
{
  return filltype(new void(frame f, path[] g, pen) {
    pair c=(min(g)+max(g))/2+(-4,4);
    radialshade(f,g,penc,c,0,penr,c,abs(max(g)-min(g))/2);
    });
}
/////****************************************************************
///// STYLE 0 : stylepardefaut (défini dans gm_graphes.asy
/////****************************************************************

/////****************************************************************
///// STYLE 1 : style_boule_1
/////****************************************************************
stylegraphe style_boule_1
            =stylegraphe(s_env     = ellipse,
                         s_penlab  = yellow,
                         s_penenv  = currentpen,
                         s_fill    = EffetBalle(orange,black),
                         a_ang     = -20,
                         a_labpos  = 0.55,
                         a_labdir  = Relative(E),
                         a_pen     = orange,
                         a_penbelow= 1bp+black,
                         a_penlab  = currentpen,
                         a_arrow   = Arrow(10bp),
                         a_labfill = NoFill);

/////****************************************************************
///// STYLE 2 : style_boule_2
/////****************************************************************
stylegraphe style_boule_2
            =stylegraphe(s_env     = ellipse,
                         s_penlab  = blue,
                         s_penenv  = currentpen,
                         s_fill    = EffetBalle(yellow,paleblue),
                         a_ang     = -20,
                         a_labpos  = 0.55,
                         a_labdir  = Relative(E),
                         a_pen     = 1bp+yellow,
                         a_penbelow= 1.5bp+black,
                         a_penlab  = currentpen,
                         a_arrow   = Arrow(SimpleHead,8bp),
                         a_labfill = NoFill);

/////****************************************************************
///// STYLE 3 : style_boule_3
/////****************************************************************
stylegraphe style_boule_3
            =stylegraphe(s_env     = ellipse,
                         s_penlab  = fontsize(24pt),
                         s_penenv  = 1bp+red,
                         s_fill    = FillDraw(paleblue),
                         a_ang     = -20,
                         a_labpos  = 0.45,
                         a_labdir  = Relative(E),
                         a_pen     = .8bp+.5green,
                         a_penbelow= 1bp+.3green,
                         a_penlab  = fontsize(16pt)+.5blue,
                         a_arrow   = Arrow(HookHead,size=5bp),
                         a_labfill = Fill(paleblue));
                         
/////****************************************************************
///// Pour un nouveau style :
///// 1. copier-coller le style précédent ;
///// 2. changer le nom pour un nouveau
///// 3. modifier les paramètres selon ses préférences.
/////****************************************************************
stylegraphe style_boule_4
            =stylegraphe(s_env     = ellipse,
                         s_penlab  = fontsize(24pt),
                         s_penenv  = 2bp+black,
                         s_fill    = FillDraw(royalblue),
                         a_ang     = -20,
                         a_labpos  = 0.4,
                         a_labdir  = Relative(E),
                         a_pen     = .8bp+.5black,
                         a_penbelow= 1bp+.3black,
                         a_penlab  = fontsize(16pt)+.5black,
                         a_arrow   = Arrow(HookHead,size=5bp),
                         a_labfill = Fill(paleblue));
                         
