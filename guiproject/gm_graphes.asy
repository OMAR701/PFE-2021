// Un premier jet d'extension pour tracer des graphes (orientés ou non).

import fontsize;

////%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
////%%%% Une structure pour faciliter la création de styles préconfigurés %%%%
////%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
struct stylegraphe{envelope s_env;
                   pen      s_penlab;
                   pen      s_penenv;
                   filltype s_fill;
                   real     a_ang;
                   real     a_labpos;
                   align    a_labdir;
                   pen      a_pen;
                   pen      a_penbelow;
                   pen      a_penlab;
                   arrowbar a_arrow;
                   filltype a_labfill;
                   void operator init(envelope s_env,
                                      pen      s_penlab,
                                      pen      s_penenv,
                                      filltype s_fill,
                                      real     a_ang,
                                      real     a_labpos,
                                      align    a_labdir,
                                      pen      a_pen,
                                      pen      a_penbelow,
                                      pen      a_penlab,
                                      arrowbar a_arrow,
                                      filltype a_labfill
                                      ) {
                                      this.s_env     = s_env;
                                      this.s_penlab  = s_penlab;
                                      this.s_penenv  = s_penenv;
                                      this.s_fill    = s_fill;
                                      this.a_ang     = a_ang;
                                      this.a_labpos  = a_labpos;
                                      this.a_labdir  = a_labdir;
                                      this.a_pen     = a_pen;
                                      this.a_penbelow= a_penbelow;
                                      this.a_penlab  = a_penlab;
                                      this.a_arrow   = a_arrow;
                                      this.a_labfill = a_labfill;
                                      }
}
////%%%% Le style par défaut...

stylegraphe stylepardefaut=stylegraphe(s_env     = ellipse,
                                       s_penlab  = currentpen,
                                       s_penenv  = currentpen,
                                       s_fill    = NoFill,
                                       a_ang     = -20,
                                       a_labpos  = 0.55,
                                       a_labdir  = Relative(E),
                                       a_pen     = currentpen,
                                       a_penbelow= nullpen,
                                       a_penlab  = currentpen,
                                       a_arrow   = Arrow(HookHead,size=5bp),
                                       a_labfill = UnFill);

////%%%% Des styles supplémentaires dans le fichier annexe gm_graphes_styles.asy
                                       
////%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
////%%%% La structure GRAPHE
////%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
struct GRAPHE {pair[]     s_xy;
               string[]   s_lab;
               envelope[] s_env;
               pen[]      s_penlab;
               pen[]      s_penenv;
               filltype[] s_fill;
               real[][]     a_k; // MATRICE D'ADJACENCE (OU MATRICE BOOLEENNE)
               real[][]     a_ang;
               string[][]   a_lab;
               real[][]     a_labpos;
               align[][]    a_labdir;
               pen[][]      a_pen;
               pen[][]      a_penbelow;
               pen[][]      a_penlab;
               arrowbar[][] a_arrow;
               filltype[][] a_labfill;
               string       configuration; // configuration des sommets en cercle, en ...
               stylegraphe  grstyle;

    // Définition des "array" 
    // - de taille n pour les s_* relatifs aux sommets
    // - de taille nxn pour les a_* relatifs aux arêtes
    void initialisations(int n){
            this.s_env     = new envelope[n];
            this.s_penlab  = new pen[n];
            this.s_penenv  = new pen[n];
            this.s_fill    = new filltype[n];
            this.a_ang     = new real[n][n];
            this.a_labpos  = new real[n][n];
            this.a_labdir  = new align[n][n];
            this.a_pen     = new pen[n][n];
            this.a_penbelow= new pen[n][n];
            this.a_penlab  = new pen[n][n];
            this.a_arrow   = new arrowbar[n][n];
            this.a_labfill = new filltype[n][n];
    }

    // Calculs des (x;y) des sommets dans des configurations particulières.
    void calculdesxy(int n){
            if(configuration=="cerclecentre"){
                real[] nbliaisons=array(n,0);
                for(int i=0;i<n;++i){
                    if(this.a_k[i][i]==0)
                        for(int j=0;j<n;++j){
                            if(this.a_k[i][j]!=0) nbliaisons[i]+=1;
                            if(this.a_k[j][i]!=0) nbliaisons[i]+=1;
                        }
                }
                int imax=0;
                for(int i=0;i<n;++i) imax=(nbliaisons[i]>nbliaisons[imax])?i:imax;    
                this.s_xy[imax]=(0,0);
                for(int k=0 ; k<n-1 ; ++k){
                   this.s_xy[(imax+k+1)%n]=dir(k*360/(n-1));
                }
                write(this.s_xy);
            }
            else 
            {   if(configuration!="cercle"){
                   this.configuration="cercle";
                   warning("ConfigurationInexistante",
                           "La configuration demandee n'existant pas, elle est remplacee par la configuration en cercle.");
                }
                for(int k=0 ; k<n ; ++k){
                   this.s_xy[k]=dir(k*360/n);
                }
            }
    }

    // SYNTAXE 1 : GRAPHE(pair[] s_xy, real[][] a_k)
    // paramètres obligatoires : 1. coordonnées des sommets, 
    //                           2. matrice d'adjacence (complète ou partielle)
    //
    // paramètres optionnels : s_lab (étiquettes des sommets)
    //                         grstyle (style du graphe)
    void operator init(pair[]      s_xy,
                       string[]    s_lab  = new string[],
                       real[][]    a_k,
                       stylegraphe grstyle = stylepardefaut
                       ) {write("ok");
            int n      = s_xy.length;
            this.s_xy  = s_xy;
            this.s_lab = s_lab;
            this.a_k   = new real[n][n];
            this.a_lab = new string[n][n];
            this.grstyle= grstyle;
            initialisations(n);
            for(int i=0; i<n; ++i)
            {
                this.s_lab[i]    = (i<s_lab.length) ? s_lab[i]:format("$S_%i$",i);
                this.s_env[i]    = grstyle.s_env;
                this.s_penlab[i] = grstyle.s_penlab;
                this.s_penenv[i] = grstyle.s_penenv;
                this.s_fill[i]   = grstyle.s_fill;
                for(int j=0; j<n; ++j)
                {
                    this.a_k[i][j]       = (i<a_k.length && j<a_k[0].length) ? a_k[i][j]:0;
                    this.a_lab[i][j]     = string(this.a_k[i][j]);
                    this.a_ang[i][j]     = grstyle.a_ang;
                    this.a_labpos[i][j]  = grstyle.a_labpos;
                    this.a_labdir[i][j]  = grstyle.a_labdir;
                    this.a_pen[i][j]     = grstyle.a_pen;
                    this.a_penbelow[i][j]= grstyle.a_penbelow;
                    this.a_penlab[i][j]  = grstyle.a_penlab;
                    this.a_arrow[i][j]   = grstyle.a_arrow;
                    this.a_labfill[i][j] = grstyle.a_labfill;
                }
            }
    } 
    // SYNTAXE 2 : GRAPHE(real[][] a_k, string configuration)
    // paramètres obligatoires : 1. matrice d'adjacence (complète ou partielle)
    //                           2. configuration
    //
    // paramètres optionnels : s_lab (étiquettes des sommets)
    //                         grstyle (style du graphe)
    void operator init(string[]    s_lab  = new string[],
                       real[][]    a_k,
                       string      configuration,
                       stylegraphe grstyle = stylepardefaut
                       ) {
            int n       = max(a_k.length,a_k[0].length);
            this.s_lab = s_lab;
            this.a_k   = new real[n][n];
            this.a_lab = new string[n][n];
            this.grstyle= grstyle;
            initialisations(n);
            this.configuration=configuration;
            for(int i=0; i<n; ++i)
            {
                this.s_lab[i]    = (i<s_lab.length) ? s_lab[i]:format("$S_%i$",i);
                this.s_env[i]    = grstyle.s_env;
                this.s_penlab[i] = grstyle.s_penlab;
                this.s_penenv[i] = grstyle.s_penenv;
                this.s_fill[i]   = grstyle.s_fill;
                for(int j=0; j<n; ++j)
                {
                    this.a_k[i][j]       = (i<a_k.length && j<a_k[0].length) ? a_k[i][j]:0;
                    this.a_lab[i][j]     = string(this.a_k[i][j]);
                    this.a_ang[i][j]     = grstyle.a_ang;
                    this.a_labpos[i][j]  = grstyle.a_labpos;
                    this.a_labdir[i][j]  = grstyle.a_labdir;
                    this.a_pen[i][j]     = grstyle.a_pen;
                    this.a_penbelow[i][j]= grstyle.a_penbelow;
                    this.a_penlab[i][j]  = grstyle.a_penlab;
                    this.a_arrow[i][j]   = grstyle.a_arrow;
                    this.a_labfill[i][j] = grstyle.a_labfill;
                }
            }
            calculdesxy(n);
    } 
}
    // SYNTAXE 3 : 
    // void operator init(string[]    grdescriptif,
                       // string      configuration,
                       // stylegraphe grstyle = stylepardefaut
                       // ) {

// }
//////////////////
/// Fonctions de modification du style :
/// modif_s : pour un sommet particulier
/// modif_a : pour une arête particulière
void modif_s(GRAPHE   gr, 
             int      is_, // indice du sommet
             pair     s_xy=999N, // un bricolage qui va être modifié
             string   s_lab="",
             envelope s_env=null,
             filltype s_fill=NoFill,
             pen      s_penlab=nullpen,
             pen      s_penenv=nullpen
             ){
             if(s_xy!=999N)        gr.s_xy[is_]=s_xy;
             if(s_lab!="")         gr.s_lab[is_]=s_lab;
             if(s_env!=null)       gr.s_env[is_]=s_env;
             if(s_fill!=NoFill)    gr.s_fill[is_]=s_fill;
             if(s_penlab!=nullpen) gr.s_penlab[is_]=s_penlab;
             if(s_penenv!=nullpen) gr.s_penenv[is_]=s_penenv;
}                 
void modif_a(GRAPHE gr, 
             int ip1, int ip2, // indices des sommets que l'on relie
             real     a_k=999, // un bricolage qui va être modifié
             real     a_ang=999, // un bricolage qui va être modifié
             string   a_lab="",
             real     a_labpos=999, // un bricolage qui va être modifié
             align    a_labdir=NoAlign,
             pen      a_pen=nullpen,
             pen      a_penbelow=nullpen,
             pen      a_penlab=nullpen,
             arrowbar a_arrow=None,
             filltype a_labfill=NoFill
             ){
             if(a_k!=999)            gr.a_k[ip1][ip2]=a_k;
             if(a_ang!=999)          gr.a_ang[ip1][ip2]=a_ang;
             if(a_lab!="")           gr.a_lab[ip1][ip2]=a_lab;
             if(a_labpos!=999)       gr.a_labpos[ip1][ip2]=a_labpos;
             if(a_labdir!=NoAlign)   gr.a_labdir[ip1][ip2]=a_labdir;
             if(a_pen!=nullpen)      gr.a_pen[ip1][ip2]=a_pen;
             if(a_penbelow!=nullpen) gr.a_penbelow[ip1][ip2]=a_penbelow;
             if(a_penlab!=nullpen)   gr.a_penlab[ip1][ip2]=a_penlab;
             if(a_arrow!=None)       gr.a_arrow[ip1][ip2]=a_arrow;
             if(a_labfill!=NoFill)   gr.a_labfill[ip1][ip2]=a_labfill;
}                 

////////////////////////////////////
/////////  DRAW (GRAPHE gr)
////////////////////////////////////
void draw(picture pic=currentpicture, 
          GRAPHE gr,
          bool aff_a=true,
          bool aff_a_lab=false) {
  object[] im;
  pair ptmoy=sum(gr.s_xy)/gr.s_xy.length;
  for(int k=0 ; k<gr.s_xy.length ; ++k)
    im.push(draw(pic,Label(gr.s_lab[k],gr.s_penlab[k]),
                 gr.s_env[k],gr.s_xy[k],xmargin=.1cm,gr.s_penenv[k],filltype=gr.s_fill[k]));
  if(aff_a) pic.add(new void(picture pic3, transform t)
  {
    for(int k=0 ; k<gr.s_xy.length ; ++k)
    {
        for(int m=0 ; m<gr.s_xy.length ; ++m){
            if(gr.a_k[k][m]!=0)
            {
                if(k!=m)
                {
                  pair d  = gr.s_xy[m]-gr.s_xy[k],
                       dr = rotate(gr.a_ang[k][m])*d;
                  if(gr.a_penbelow[k][m]!=nullpen) 
                  draw(pic3, (aff_a_lab)?Label(gr.a_lab[k][m],position=Relative(gr.a_labpos[k][m]),
                                   align=gr.a_labdir[k][m],
                                   gr.a_penlab[k][m],filltype=gr.a_labfill[k][m]):"",
                             point(im[k],d,t){dr}..point(im[m],-d,t),
                             gr.a_penbelow[k][m],gr.a_arrow[k][m]);
                  draw(pic3, (aff_a_lab)?Label(gr.a_lab[k][m],position=Relative(gr.a_labpos[k][m]),
                                   align=gr.a_labdir[k][m],
                                   gr.a_penlab[k][m],filltype=gr.a_labfill[k][m]):"",
                             point(im[k],d,t){dr}..point(im[m],-d,t),
                             gr.a_pen[k][m],gr.a_arrow[k][m]);
                }
                else
                {
                  pair d  = gr.s_xy[k]-ptmoy, 
                       da = rotate(-45-gr.a_ang[k][k])*d,
                       debutfleche  = point(im[k],rotate(-45)*d,t),
                       finfleche    = point(im[k],rotate(45)*d,t),
                       ctmp         = (debutfleche+finfleche)/2,
                       //milieufleche = ((debutfleche+finfleche)/2-gr.s_xy[k])*3+gr.s_xy[k];
                       milieufleche = shift(ctmp)*scale(2)*shift(-ctmp)*rotate(90,ctmp)*debutfleche;
                  if(gr.a_penbelow[k][k]!=nullpen) 
                  draw(pic3, (aff_a_lab)?Label(gr.a_lab[k][k],position=Relative(gr.a_labpos[k][k]),
                                   align=gr.a_labdir[k][k],
                                   gr.a_penlab[k][k],filltype=gr.a_labfill[k][k]):"",
                             debutfleche..milieufleche..finfleche,
                             gr.a_penbelow[k][k],gr.a_arrow[k][k]);
                  draw(pic3, (aff_a_lab)?Label(gr.a_lab[k][k],position=Relative(gr.a_labpos[k][k]),
                                   align=gr.a_labdir[k][k],
                                   gr.a_penlab[k][k],filltype=gr.a_labfill[k][k]):"",
                             debutfleche..milieufleche..finfleche,
                             gr.a_pen[k][k],gr.a_arrow[k][k]);
                }
            }
        }
    }
  });
}
