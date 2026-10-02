# -*- coding: utf-8 -*-
"""Contenu pédagogique du livre « Je lis, j'écris ! » — 21 jours, CE1.

Conventions de balisage :
  - mots syllabés : syllabes séparées par « - » (affichage en couleurs alternées)
  - {xx} : graphème étudié, affiché en gras
  - « _ » dans un exercice à compléter : case vide à remplir
"""

JOURS = [
# ───────────────────────── SEMAINE 1 : les sons de base ─────────────────────────
dict(
    n=1, titre="Les voyelles et les syllabes",
    son="a e i o u é", ref="a comme ami",
    regle="Une consonne + une voyelle = une syllabe : m + a → ma.",
    syllabes=["ma","mi","mo","mu","mé","la","li","lo","lu","lé",
              "pa","pi","po","pu","pé","ta","ti","to","tu","té"],
    mots=["a-mi","pa-pa","vé-lo","mi-di","ta-pis","sa-la-de",
          "mo-to","ca-fé","ju-pe","ra-di-o","ro-bot","li-re"],
    outils=["le","la","un"],
    histoire_titre="Lina et Moka",
    histoire="Voici Lina. Lina a un ami : le chat Moka. "
             "Moka a un ami : le vélo de Lina ! "
             "Le vélo file. Moka file. Lina rit. "
             "Papa dit : « Lina, il est midi ! »",
    questions=["Comment s'appelle le chat ?",
               "Qui rit ?",
               "Que dit papa ?"],
    ecrire=["ami","vélo","midi"],
    completer_titre="Complète avec la bonne lettre.",
    completer=[("v_lo","é"),("m_di","i"),("p_pa","a"),("t_pis","a"),("mo_o","t")],
    copie="Lina a un vélo.",
    dictee_mots=["papa","ami","vélo"],
    dictee_phrase="Lina a un ami.",
),
dict(
    n=2, titre="Le son ou",
    son="ou", ref="ou comme loup",
    regle="o + u se lisent ensemble : ou. Exemple : l-ou-p.",
    syllabes=["mou","lou","pou","tou","sou","fou","nou","rou",
              "jou","bou","cou","vou","dou","gou","zou"],
    mots=["l{ou}p","s{ou}-pe","p{ou}-le","r{ou}-ge","t{ou}-pie","m{ou}-ton",
          "b{ou}-le","f{ou}r","c{ou}-pe","d{ou}-che","j{ou}r","n{ou}-n{ou}rs"],
    outils=["une","et","est"],
    histoire_titre="La boule rouge",
    histoire="Moka a une b{ou}le r{ou}ge. Il r{ou}le la b{ou}le s{ou}s le tapis. "
             "Lina c{ou}rt : « Moka, {où} est la b{ou}le ? » "
             "Moka t{ou}che le tapis. Lina s{ou}lève le tapis : "
             "la b{ou}le r{ou}ge est là ! Moka j{ou}e t{ou}te la j{ou}rnée.",
    questions=["De quelle couleur est la boule ?",
               "Où Moka roule-t-il la boule ?",
               "Qui trouve la boule ?"],
    ecrire=["loup","poule","rouge"],
    completer_titre="Complète avec : ou",
    completer=[("l_p","ou"),("s_pe","ou"),("p_le","ou"),("r_ge","ou"),("b_le","ou")],
    copie="Moka joue.",
    dictee_mots=["loup","soupe","boule"],
    dictee_phrase="Moka joue avec la boule rouge.",
),
dict(
    n=3, titre="Le son on",
    son="on  om", ref="on comme ballon",
    regle="Devant m, b, p, on écrit om : ombre, pompier, compote.",
    syllabes=["mon","lon","pon","ton","son","fon","non","ron",
              "jon","bon","con","von","bom","com","tom"],
    mots=["b{on}-b{on}","p{on}t","ba-l{on}","mou-t{on}","c{on}-te","m{on}-de",
          "r{on}d","l{on}g","{om}-bre","p{om}-pier","c{om}-po-te","n{om}"],
    outils=["il","elle","on"],
    histoire_titre="Le ballon",
    histoire="Dimanche, Lina et Moka v{on}t au p{on}t. Lina a un ball{on}. "
             "Elle le lance très haut. Oh n{on} ! Le ball{on} t{om}be dans l'eau. "
             "Moka ne bouge pas : il a peur de l'eau. "
             "Un garç{on} a un bât{on}. Il pousse le ball{on} vers le bord. "
             "« Merci ! » dit Lina. Le garç{on} s'appelle Sim{on}.",
    questions=["Où vont Lina et Moka ?",
               "Où tombe le ballon ?",
               "Comment s'appelle le garçon ?"],
    ecrire=["bonbon","ballon","mouton"],
    completer_titre="Complète avec : on ou om",
    completer=[("p_t","on"),("m_de","on"),("p_pier","om"),("c_pote","om"),("ball_","on")],
    copie="Simon a un bonbon.",
    dictee_mots=["pont","ballon","nom"],
    dictee_phrase="Simon a un bonbon.",
),
dict(
    n=4, titre="Le son an / en",
    son="an  en  am  em", ref="an comme maman · en comme dent",
    regle="Devant m, b, p, on écrit am ou em : lampe, chambre, temps.",
    syllabes=["man","lan","pan","tan","san","fan","ran","ban",
              "dan","gran","plan","ven","den","lam","cham"],
    mots=["ma-m{an}","d{en}t","{en}-f{an}t","gr{an}d","l{am}-pe","ch{am}-bre",
          "v{en}t","pa-r{en}t","p{an}-ta-lon","m{en}-ton","{an}-ge","j{am}-be"],
    outils=["je","tu","dans"],
    histoire_titre="Le grand vent",
    histoire="Ce matin, le v{en}t souffle. Il est gr{an}d et fort. "
             "Mam{an} t{en}d les p{an}talons de papa sur le fil. "
             "Moka a peur du v{en}t : il se cache d{an}s la ch{am}bre, sous la l{am}pe. "
             "Lina ch{an}te douc{em}ent pour lui. {En}fin, Moka sort. "
             "Il saute et attrape un p{an}talon qui d{an}se au v{en}t ! "
             "Mam{an} rit : « Quel chat amus{an}t ! »",
    questions=["Quel temps fait-il ?",
               "Où se cache Moka ?",
               "Qu'attrape Moka ?"],
    ecrire=["maman","enfant","lampe"],
    completer_titre="Complète avec : an, en, am ou em",
    completer=[("mam_","an"),("d_t","en"),("l_pe","am"),("ch_bre","am"),("gr_d","an")],
    copie="Maman chante.",
    dictee_mots=["maman","dent","grand"],
    dictee_phrase="Maman chante dans la chambre.",
),
dict(
    n=5, titre="Le son in",
    son="in  ain  ein  im", ref="in comme lapin · ain comme pain",
    regle="Le son in s'écrit de plusieurs façons : in, ain, ein (et im devant m, b, p).",
    syllabes=["lin","pin","min","vin","fin","rin","tin","sin",
              "main","pain","bain","dain","plein","frein","sim"],
    mots=["la-p{in}","ma-t{in}","p{ain}","m{ain}","b{ain}","tr{ain}",
          "jar-d{in}","p{ein}-tu-re","pl{ein}","s{im}-ple","c{in}q","cou-s{in}"],
    outils=["avec","pour","sur"],
    histoire_titre="Le train de mamie",
    histoire="Dem{ain}, Lina pr{en}d le tr{ain} avec papa. Ils vont chez mamie. "
             "Le mat{in}, Lina met son manteau et pr{en}d son lap{in} en tissu. "
             "Moka reste à la maison avec maman. "
             "Dans le tr{ain}, Lina regarde les champs, les moul{in}s et les sap{in}s. "
             "Enf{in}, le tr{ain} fr{ein}e. Mamie est sur le quai, "
             "les m{ain}s pl{ein}es de p{ain} chaud. « Bonjour, ma grande ! »",
    questions=["Avec qui Lina prend-elle le train ?",
               "Qui reste à la maison ?",
               "Qu'est-ce que mamie a dans les mains ?"],
    ecrire=["lapin","pain","matin"],
    completer_titre="Complète avec : in, ain ou ein",
    completer=[("lap_","in"),("p_","ain"),("m_","ain"),("pl_","ein"),("mat_","in")],
    copie="Lina prend le train.",
    dictee_mots=["lapin","pain","main"],
    dictee_phrase="Lina prend le train le matin.",
),
dict(
    n=6, titre="Le son oi",
    son="oi", ref="oi comme roi",
    regle="o + i se lisent ensemble : oi. Exemple : r-oi.",
    syllabes=["moi","toi","loi","roi","soi","foi","noi","boi",
              "voi","poi","doi","coi","loin","coin","soin"],
    mots=["r{oi}","{oi}-seau","t{oi}t","b{oi}s","p{oi}-re","v{oi}-tu-re",
          "é-t{oi}-le","m{oi}","n{oi}r","mi-r{oi}r","l{oi}n","c{oi}n"],
    outils=["moi","toi","voici"],
    histoire_titre="Chez mamie",
    histoire="La maison de mamie est en b{oi}s. Sur le t{oi}t, il y a un {oi}seau n{oi}r. "
             "Le s{oi}r, mamie fait une tarte aux p{oi}res. "
             "Puis elles regardent les ét{oi}les par la fenêtre. "
             "« Mamie, tu v{oi}s l'ét{oi}le qui brille, là-bas, très l{oi}n ? » "
             "« Oui, c'est l'ét{oi}le du berger. » "
             "Lina pense à Moka. Elle voudrait qu'il s{oi}t là, avec elle.",
    questions=["En quoi est la maison de mamie ?",
               "Qu'y a-t-il sur le toit ?",
               "À qui pense Lina ?"],
    ecrire=["roi","étoile","voiture"],
    completer_titre="Complète avec : oi ou ou",
    completer=[("r_","oi"),("l_p","ou"),("n_r","oi"),("s_pe","ou"),("b_s","oi")],
    copie="Un oiseau est sur le toit.",
    dictee_mots=["roi","bois","noir"],
    dictee_phrase="Un oiseau est sur le toit.",
),
dict(
    n=7, titre="Révision de la semaine 1", revision=True,
    son="ou · on · an · in · oi", ref="Je révise tous mes sons",
    regle="Je lis lentement, syllabe par syllabe, puis je relis le mot d'un coup.",
    syllabes=["mou","bon","dan","lin","roi","pou","ton","ran",
              "pain","toi","jou","son","ven","main","loin"],
    mots=["b{on}-j{ou}r","mai-s{on}","di-m{an}-che","la-p{in}","é-t{oi}-le","mou-t{on}",
          "{en}-f{an}t","s{ou}-ris","tr{ain}","v{oi}-tu-re","l{am}-pe","p{on}t"],
    outils=["les","des","de"],
    histoire_titre="Le retour",
    histoire="Dimanche, Lina et papa reprennent le train. "
             "Lina a un cadeau pour Moka : une petite souris en tissu. "
             "À la maison, Moka attend devant la porte. Il miaule très fort. "
             "Lina le prend dans ses bras. « Bonjour, mon Moka ! Voici ton cadeau. » "
             "Moka renifle la souris, puis il part en courant avec elle sous le lit. "
             "Maman sourit : « Je crois qu'il aime son cadeau ! »",
    questions=["Quel cadeau Lina apporte-t-elle ?",
               "Où attend Moka ?",
               "Où part Moka avec la souris ?"],
    ecrire=["maison","bonjour","souris"],
    completer_titre="Complète avec : ou, on, an, in ou oi",
    completer=[("m_ton","ou"),("dim_che","an"),("p_t","on"),("lap_","in"),("r_","oi")],
    copie="Moka attend devant la porte.",
    dictee_mots=["bonjour","maman","lapin","roi"],
    dictee_phrase="Moka attend devant la porte.",
),
# ───────────────────────── SEMAINE 2 : les sons complexes ─────────────────────────
dict(
    n=8, titre="Le son ch",
    son="ch", ref="ch comme chat",
    regle="c + h se lisent ensemble et font un seul son : ch.",
    syllabes=["cha","che","chi","cho","chu","ché",
              "chou","chon","chan","chin","choi","chè"],
    mots=["{ch}at","{ch}ien","{ch}e-val","va-{ch}e","bou-{ch}e","mar-{ch}é",
          "{ch}o-co-lat","{ch}e-min","ri-{ch}e","{ch}ou","mou-{ch}e","{ch}an-son"],
    outils=["chez","mais","aussi"],
    histoire_titre="Moka et le chien",
    histoire="Lundi, Lina rentre de l'école par le {ch}emin du mar{ch}é. "
             "Moka la suit en ca{ch}ette. Soudain, un grand {ch}ien noir arrive. "
             "Moka se met à souffler et hérisse ses poils. Le {ch}ien recule : il a peur ! "
             "Lina rit et caresse Moka : « Tu es un {ch}at très courageux ! » "
             "Elle a{ch}ète un petit morceau de fromage au mar{ch}é pour son {ch}ampion.",
    questions=["Par où passe Lina pour rentrer ?",
               "Quel animal arrive ?",
               "Que fait le chien ?"],
    ecrire=["chat","chien","vache"],
    completer_titre="Complète avec : ch",
    completer=[("_at","ch"),("va_e","ch"),("bou_e","ch"),("_emin","ch"),("mar_é","ch")],
    copie="Le chat est courageux.",
    dictee_mots=["chat","chien","chemin"],
    dictee_phrase="Le chien a peur du chat.",
),
dict(
    n=9, titre="Le son eu",
    son="eu  œu", ref="eu comme feu · œu comme cœur",
    regle="e + u se lisent ensemble : eu. On l'écrit parfois œu : sœur, œuf, cœur.",
    syllabes=["peu","feu","deu","jeu","bleu","meu",
              "neu","leu","seu","reu","beu","cheu"],
    mots=["f{eu}","j{eu}","bl{eu}","d{eu}x","che-v{eu}","fl{eu}r",
          "p{eu}r","s{œu}r","{œu}f","c{œu}r","n{eu}f","chan-t{eu}r"],
    outils=["deux","peu","leur"],
    histoire_titre="Les fleurs bleues",
    histoire="Mardi, c'est l'anniversaire de la s{œu}r de maman, tata Zoé. "
             "Lina v{eu}t lui offrir un cadeau. Elle cueille des fl{eu}rs bl{eu}es dans le jardin. "
             "Mais Moka joue avec une f{eu}ille et casse d{eu}x fl{eu}rs ! "
             "Lina n'est pas h{eu}reuse… Puis elle a une idée : "
             "elle fait un joli dessin de fl{eu}rs et elle écrit : « Joy{eu}x anniversaire ! » "
             "Tata Zoé a les y{eu}x qui brillent : « C'est le plus beau cadeau ! »",
    questions=["Pour qui est le cadeau ?",
               "Que casse Moka ?",
               "Quel cadeau Lina fait-elle à la fin ?"],
    ecrire=["feu","fleur","deux"],
    completer_titre="Complète avec : eu ou œu",
    completer=[("f_","eu"),("bl_","eu"),("s_r","œu"),("_f","œu"),("d_x","eu")],
    copie="Lina a peur du feu.",
    dictee_mots=["feu","bleu","deux","fleur"],
    dictee_phrase="Lina a peur du feu.",
),
dict(
    n=10, titre="Le son o : au / eau",
    son="au  eau", ref="au comme auto · eau comme bateau",
    regle="Le son o peut s'écrire o, au ou eau. Le mot « eau » se lit o !",
    syllabes=["pau","mau","sau","fau","tau","chau",
              "beau","peau","veau","seau","reau","teau"],
    mots=["{au}-to","ch{au}d","j{au}-ne","s{au}-ter","ch{au}s-set-te","b{eau}",
          "ba-t{eau}","gâ-t{eau}","ca-d{eau}","oi-s{eau}","cha-p{eau}","{eau}"],
    outils=["au","aux","beaucoup"],
    histoire_titre="Le gâteau au chocolat",
    histoire="Mercredi, Lina et papa font un gât{eau} {au} chocolat. "
             "Lina met un chap{eau} de chef. Elle verse le sucre, la farine, "
             "les œufs et le beurre fondu. Papa met le gât{eau} {au} four. "
             "Il fait ch{au}d dans la cuisine. Moka s{au}te sur la table pour voir. "
             "« Non, Moka ! Descends ! » Le gât{eau} est enfin prêt. Il sent très bon. "
             "Lina en donne un morc{eau} à maman. « Il est b{eau} et délicieux ! » dit maman.",
    questions=["Quel gâteau font-ils ?",
               "Que met Lina sur sa tête ?",
               "Où saute Moka ?"],
    ecrire=["gâteau","chapeau","jaune"],
    completer_titre="Complète avec : au ou eau",
    completer=[("ch_d","au"),("bat_","eau"),("j_ne","au"),("cad_","eau"),("s_ter","au")],
    copie="Le gâteau est beau.",
    dictee_mots=["chaud","beau","bateau","auto"],
    dictee_phrase="Le gâteau est au four.",
),
dict(
    n=11, titre="Le son è",
    son="è  ê  ai  ei  et", ref="è comme mère · ai comme lait",
    regle="Le son è s'écrit è, ê, ai, ei, ou et à la fin d'un mot (jouet).",
    syllabes=["mè","pè","lè","rè","tê","fê",
              "mai","lai","rai","vai","nei","rei"],
    mots=["m{è}-re","p{è}-re","fr{è}-re","t{ê}-te","f{ê}-te","l{ai}t",
          "m{ai}-son","r{ei}-ne","n{ei}-ge","jou-{et}","fo-r{ê}t","ba-l{ai}"],
    outils=["très","après","faire"],
    histoire_titre="La fête de l'école",
    histoire="Jeudi, il y a une f{ê}te à l'école. Lina se f{ai}t une couronne de r{ei}ne. "
             "Son grand fr{è}re, Tom, met un masque d'ours. Les parents arrivent. "
             "La m{aî}tresse chante une chanson avec la classe. "
             "Ensuite, chaque él{è}ve lit un petit po{è}me. "
             "Lina a un peu peur, m{ai}s elle lit tr{è}s bien. "
             "Son p{è}re et sa m{è}re applaudissent. "
             "Apr{è}s la f{ê}te, il y a du l{ai}t au chocolat et des cr{ê}pes pour tout le monde.",
    questions=["Que se fait Lina ?",
               "Qui porte un masque d'ours ?",
               "Que mange-t-on après la fête ?"],
    ecrire=["mère","fête","maison"],
    completer_titre="Complète avec : è, ê, ai ou ei",
    completer=[("m_re","è"),("t_te","ê"),("l_t","ai"),("r_ne","ei"),("n_ge","ei")],
    copie="Lina lit très bien.",
    dictee_mots=["père","mère","tête","lait"],
    dictee_phrase="Il y a une fête à l'école.",
),
dict(
    n=12, titre="Les sons gn et ill",
    son="gn  ill", ref="gn comme montagne · ill comme fille",
    regle="gn se lit comme dans « agneau ». ill se lit comme dans « fille » ; "
          "on trouve aussi ail, eil, euil, ouill.",
    syllabes=["gna","gne","gni","gno","gnon","ille",
              "illa","illon","ail","eil","euil","ouille"],
    mots=["mon-ta-{gn}e","a-{gn}eau","cy-{gn}e","cham-pi-{gn}on","li-{gn}e","f{ill}e",
          "b{ill}e","so-l{eil}","tra-v{ail}","a-b{eill}e","gre-n{ouill}e","f{euill}e"],
    outils=["qui","que","quand"],
    histoire_titre="Le pique-nique",
    histoire="Vendredi, la fam{ill}e de Lina part en pique-nique à la monta{gn}e. "
             "Moka reste dormir à la maison. Il fait beau, le sol{eil} br{ill}e. "
             "Papa porte le panier. Lina et Tom cherchent des champi{gn}ons. "
             "Soudain, une ab{eill}e vole autour de Lina ! Lina ne bouge pas. "
             "L'ab{eill}e part sur une fleur. Près du ruisseau, Tom voit une gren{ouill}e verte "
             "qui saute dans l'eau. « Regarde ! » "
             "Le soir, toute la fam{ill}e est fatiguée, mais heureuse.",
    questions=["Où part la famille ?",
               "Que cherchent Lina et Tom ?",
               "Quel animal saute dans l'eau ?"],
    ecrire=["montagne","fille","soleil"],
    completer_titre="Complète avec : gn, ill ou eil",
    completer=[("monta_e","gn"),("cy_e","gn"),("f_e","ill"),("sol_","eil"),("b_e","ill")],
    copie="Le soleil brille.",
    dictee_mots=["fille","soleil","montagne"],
    dictee_phrase="Une abeille vole près de Lina.",
),
dict(
    n=13, titre="Les lettres c et g",
    son="c  ç  g  gu  ge", ref="c comme citron · g comme girafe",
    regle="Devant e, i, y : c fait [s] et g fait [j]. "
          "Devant a, o, u : on écrit ç pour [s] (garçon) et ge pour [j] (pigeon). "
          "Devant e, i : on écrit gu pour [g] (guitare).",
    syllabes=["ca","co","cu","ce","ci","cy","ça","ço","çu",
              "ga","go","gu","ge","gi","gy","gue","gui","geo"],
    mots=["{c}a-rot-te","{c}i-tron","gar-{ç}on","le-{ç}on","{g}a-re","{g}i-ra-fe",
          "{gu}i-ta-re","ba-{gu}e","pi-{ge}on","{c}e-ri-se","{c}o-chon","{g}o-ril-le"],
    outils=["ce","ici","encore"],
    histoire_titre="Le cirque",
    histoire="Samedi, Lina va au {c}irque avec son cousin Hugo. "
             "Sous le chapiteau, il y a un gar{ç}on qui joue de la {gu}itare, "
             "un clown ri{g}olo et des chevaux. "
             "Le clown lance des {c}itrons en l'air et les rattrape. "
             "Puis il fait semblant de glisser sur une carotte ! Tout le monde rit. "
             "À la fin, Hugo gagne un ballon en forme de {g}irafe. "
             "Il le donne à Lina : « Il est pour Moka ! »",
    questions=["Avec qui Lina va-t-elle au cirque ?",
               "Que lance le clown ?",
               "Que gagne Hugo ?"],
    ecrire=["garçon","girafe","citron"],
    completer_titre="Complète avec : ç, ge ou gu",
    completer=[("gar_on","ç"),("le_on","ç"),("pi_on","ge"),("_itare","gu"),("ba_e","gu")],
    copie="Le garçon joue de la guitare.",
    dictee_mots=["garçon","girafe","leçon"],
    dictee_phrase="Le garçon joue de la guitare.",
),
dict(
    n=14, titre="Révision de la semaine 2", revision=True,
    son="ch · eu · au · è · gn · ill", ref="Je révise tous mes sons",
    regle="Si un mot est difficile : je le coupe en syllabes, puis je le relis d'un coup.",
    syllabes=["chou","feu","beau","mai","gne","ille",
              "cho","bleu","pau","tê","gnon","eil"],
    mots=["{ch}e-min","fl{eu}r","ba-t{eau}","m{è}-re","mon-ta-{gn}e","f{ill}e",
          "{ch}a-p{eau}","s{œu}r","j{au}-ne","n{ei}-ge","so-l{eil}","gar-{ç}on"],
    outils=["ne","pas","plus"],
    histoire_titre="Un dimanche de pluie",
    histoire="Dimanche matin, il pleut. Toute la famille reste à la maison. "
             "Papa lit le journal, maman peint un tableau et Tom joue aux cartes. "
             "Lina s'ennuie un peu. Alors, elle prend une feuille et des crayons. "
             "Elle écrit une petite histoire : « Il était une fois un chat qui voulait voler "
             "comme un oiseau… » Moka s'assoit à côté d'elle et regarde. "
             "Lina dessine Moka avec deux grandes ailes bleues. "
             "Le soir, elle lit son histoire à toute la famille. Tout le monde applaudit. "
             "« Tu seras une grande écrivaine ! » dit maman.",
    questions=["Quel temps fait-il ?",
               "Que fait Lina quand elle s'ennuie ?",
               "Comment Lina dessine-t-elle Moka ?"],
    ecrire=["feuille","histoire","crayon"],
    completer_titre="Complète avec : ch, eu, eau, è ou gn",
    completer=[("_at","ch"),("bl_","eu"),("bat_","eau"),("m_re","è"),("monta_e","gn")],
    copie="Il pleut à la maison.",
    dictee_mots=["chat","fleur","bateau","fille"],
    dictee_phrase="Dimanche, Lina reste à la maison.",
),
# ───────────────────────── SEMAINE 3 : lire avec fluidité et écrire juste ─────────────────────────
dict(
    n=15, titre="La lettre s : [s] ou [z] ?",
    son="s  ss  z", ref="s comme sac · s comme rose",
    regle="Entre deux voyelles, un seul s chante [z] : rose, maison. "
          "Pour entendre [s] entre deux voyelles, on écrit ss : poisson.",
    syllabes=["sa","so","si","ssa","sso","ssi",
              "za","zo","zi","ase","ose","ise"],
    mots=["ro-{s}e","mai-{s}on","oi-{s}eau","poi-{ss}on","poi-{s}on","cou-{s}in",
          "cou-{ss}in","{z}è-bre","{s}a-la-de","va-{s}e","tas-{s}e","dou-{z}e"],
    outils=["nous","vous","ils"],
    histoire_titre="Poisson ou poison ?",
    histoire="Lundi, la maîtresse écrit deux mots au tableau : POISSON et POISON. "
             "« Lisez bien ! » dit-elle. Lina lève la main : "
             "« Le premier, c'est un animal qui nage dans la rivière. "
             "Le deuxième, c'est un produit très dangereux ! » "
             "« Bravo, Lina ! Avec deux s, le s siffle comme un serpent. "
             "Avec un seul s entre deux voyelles, il bourdonne comme une abeille. » "
             "Le soir, à la maison, Lina explique la règle à Tom. "
             "Tom rigole : « Alors, mon cousin est assis sur un coussin ! » "
             "Lina rit aussi. Moka, lui, préfère le poisson !",
    questions=["Quels mots la maîtresse écrit-elle ?",
               "Lequel est un animal ?",
               "Combien de s y a-t-il dans « poisson » ?"],
    ecrire=["maison","poisson","rose"],
    completer_titre="Complète avec : s ou ss",
    completer=[("ro_e","s"),("ta_e","ss"),("mai_on","s"),("trou_e","ss"),("oi_eau","s")],
    copie="Le poisson nage.",
    dictee_mots=["rose","maison","poisson","trousse"],
    dictee_phrase="Le poisson nage dans la rivière.",
    chrono=True,
),
dict(
    n=16, titre="Un ou plusieurs : le pluriel",
    son="un chat → des chats", ref="Au pluriel, j'ajoute un s muet",
    regle="Au pluriel : le, la, un, une deviennent les ou des, et le nom prend un s. "
          "Le s final est une lettre muette : on ne l'entend pas.",
    paires=[("un chat","des chat{s}"),("une fleur","des fleur{s}"),
            ("le lapin","les lapin{s}"),("la poule","les poule{s}"),
            ("un ami","des ami{s}"),("une étoile","des étoile{s}"),
            ("le chaton","les chaton{s}"),("la fille","les fille{s}")],
    outils=["mon","ton","son"],
    histoire_titre="Les chatons",
    histoire="Mardi, une grande nouvelle arrive : la chatte de la voisine, "
             "Madame Rose, a eu quatre chatons ! Lina et Tom vont les voir. "
             "Les chatons sont tout petits. Ils dorment dans un panier, "
             "collés contre leur maman. Il y a deux chatons gris, un chaton blanc "
             "et un chaton roux. Le chaton roux ouvre ses yeux bleus et miaule doucement. "
             "« Il ressemble à Moka quand il était bébé ! » dit Lina. "
             "Madame Rose sourit : « Dans deux mois, les chatons pourront partir "
             "dans une nouvelle famille. » Lina regarde papa avec de grands yeux… "
             "Papa répond : « On verra ! »",
    questions=["Combien de chatons y a-t-il ?",
               "De quelle couleur est le chaton qui ouvre les yeux ?",
               "Que répond papa ?"],
    ecrire=["des chats","les fleurs","mes amis"],
    completer_titre="J'écris au pluriel.",
    completer=[("un chat → des chat_","s"),("une fleur → des fleur_","s"),
               ("le lapin → l_ lapins","es"),("une poule → d_ poules","es"),
               ("la fille → les fille_","s")],
    copie="Les chatons dorment.",
    dictee_mots=["des chats","les fleurs","deux amis"],
    dictee_phrase="Les chatons dorment dans un panier.",
    chrono=True,
),
dict(
    n=17, titre="Les verbes être et avoir",
    son="être · avoir", ref="Je suis… J'ai…",
    regle="Attention aux mots qui se ressemblent : il est (être) / et (= en plus) ; "
          "il a (avoir) / à (la maison) ; ils sont / son chat ; ils ont / on.",
    conjugaison=[("je suis","j'ai"),("tu es","tu as"),("il / elle est","il / elle a"),
                 ("nous sommes","nous avons"),("vous êtes","vous avez"),
                 ("ils / elles sont","ils / elles ont")],
    outils=["suis","sont","ont"],
    histoire_titre="La lettre de mamie",
    histoire="Mercredi, le facteur apporte une lettre. Elle est pour Lina ! C'est mamie qui écrit.\n"
             "« Ma chère Lina,\n"
             "Je suis très contente de t'écrire. Ici, tout va bien. "
             "Les poules ont pondu beaucoup d'œufs et le jardin est plein de fleurs. "
             "Ton oncle Paul a un nouveau chien : il s'appelle Biscuit. "
             "Il est petit et très gentil. Nous sommes pressés de te revoir. "
             "Est-ce que tu as encore ton lapin en tissu ? "
             "Fais un gros câlin à Moka pour moi.\n"
             "Je t'embrasse très fort. Mamie »\n"
             "Lina est si heureuse qu'elle décide de lui répondre bientôt.",
    questions=["Qui écrit la lettre ?",
               "Comment s'appelle le chien de l'oncle Paul ?",
               "Qu'est-ce que les poules ont fait ?"],
    ecrire=["je suis","il a","ils ont"],
    completer_titre="Complète avec : suis, as, est, ont ou sommes",
    completer=[("Je _ contente.","suis"),("Tu _ un lapin.","as"),
               ("Moka _ un chat.","est"),("Les poules _ des œufs.","ont"),
               ("Nous _ à la maison.","sommes")],
    copie="Mamie a un jardin.",
    dictee_mots=["je suis","tu as","il est","ils ont"],
    dictee_phrase="Mamie a un jardin plein de fleurs.",
    chrono=True,
),
dict(
    n=18, titre="ph, et les fins de mots er / ez",
    son="ph · er · ez", ref="ph comme photo · er comme goûter",
    regle="p + h se lit [f] : photo. À la fin d'un mot, er et ez se lisent souvent é : "
          "goûter, nez.",
    syllabes=["pha","pho","phi","phé","phan",
              "phin","phon","phou","phar","phra"],
    mots=["{ph}o-to","é-lé-{ph}ant","dau-{ph}in","{ph}a-re","ro-ch{er}","goû-t{er}",
          "pa-pi{er}","chan-t{er}","n{ez}","as-s{ez}","dî-n{er}","{ph}ra-se"],
    outils=["toujours","jamais","souvent"],
    histoire_titre="La photo du zoo",
    histoire="Jeudi, la classe de Lina visite le zoo. La maîtresse a un appareil {ph}oto. "
             "Devant l'enclos des élé{ph}ants, elle dit : « Ven{ez} près de moi pour la {ph}oto ! » "
             "Mais un élé{ph}ant s'approche. Il lève sa trompe et… pchhh ! "
             "Il arrose toute la classe ! Les enfants crient et rient en même temps. "
             "Ils sont tout mouillés. Ensuite, ils vont voir les dau{ph}ins, "
             "puis ils mangent leur goût{er} sur un banc. "
             "Le soir, Lina raconte tout à ses parents. Papa demande : « Et la {ph}oto ? » "
             "Lina la montre : on voit seulement une grosse trompe grise "
             "et des enfants qui rient !",
    questions=["Où va la classe ?",
               "Que fait l'éléphant ?",
               "Que voit-on sur la photo ?"],
    ecrire=["photo","éléphant","goûter"],
    completer_titre="Complète avec : ph ou f",
    completer=[("élé_ant","ph"),("_leur","f"),("dau_in","ph"),("_ête","f"),("_oto","ph")],
    copie="Les enfants rient.",
    dictee_mots=["photo","éléphant","nez","goûter"],
    dictee_phrase="Les enfants vont visiter le zoo.",
    chrono=True,
),
dict(
    n=19, titre="Lire avec le ton : la ponctuation",
    son=". ? ! ,", ref="Je lis avec ma voix",
    regle="Une phrase commence par une majuscule et finit par un point. "
          "Le point : je m'arrête. La virgule : je respire. "
          "Le point d'interrogation : je pose une question. "
          "Le point d'exclamation : je montre la joie, la peur ou la surprise.",
    ponctuation=["Moka dort.","Moka dort ?","Moka dort !",
                 "Il pleut.","Il pleut ?","Il pleut !",
                 "Tu viens.","Tu viens ?","Tu viens !"],
    outils=["parce que","comme","alors"],
    histoire_titre="Moka a disparu !",
    histoire="Vendredi soir, Lina cherche Moka partout. "
             "Il n'est pas sous le lit, ni dans son panier, ni sur le canapé. "
             "« Moka ! Moka ! Où es-tu ? » Personne ne répond. Lina commence à pleurer. "
             "Toute la famille l'aide à chercher. Papa regarde dans le jardin avec une lampe. "
             "Maman appelle les voisins. Tom fouille le garage. "
             "Soudain, Lina entend un petit bruit : « Miaou… » "
             "Le bruit vient de l'armoire de sa chambre ! Elle ouvre la porte doucement. "
             "Moka est là, couché sur ses pulls, bien au chaud. "
             "Il s'est endormi quand maman a rangé le linge. "
             "Lina le serre très fort dans ses bras. « Tu m'as fait peur, petit coquin ! » "
             "Moka ronronne, comme si de rien n'était.",
    questions=["Où Lina cherche-t-elle Moka en premier ?",
               "Que fait papa pour aider ?",
               "Où Lina trouve-t-elle Moka ?",
               "Pourquoi Moka est-il là ?"],
    ecrire=["armoire","chercher","jardin"],
    completer_titre="Je remets les mots dans l'ordre.",
    completer=[("dort / Le / chat / .","Le chat dort."),
               ("Lina / Moka / cherche / .","Lina cherche Moka."),
               ("es-tu / Où / ?","Où es-tu ?")],
    ordre=True,
    copie="Moka dort dans l'armoire.",
    dictee_mots=["armoire","jardin","toujours","famille"],
    dictee_phrase="Moka dort dans l'armoire.",
    chrono=True,
),
dict(
    n=20, titre="Je lis de façon fluide",
    son="Je lis sans m'arrêter", ref="Lire comme on parle",
    regle="Je lis d'abord en silence. Puis je lis à voix haute, en regroupant les mots "
          "qui vont ensemble : « Le petit chat / dort / dans son panier. »",
    groupes=["Le petit chat / dort / dans son panier.",
             "Ce matin, / Lina / mange une tartine.",
             "Le chien de mamie / court / dans le jardin.",
             "Après l'école, / Tom / joue au ballon / avec ses amis.",
             "Quand il pleut, / Moka / reste au chaud / sous la couverture."],
    outils=["hier","aujourd'hui","demain"],
    histoire_titre="Caramel",
    histoire="Samedi matin, papa réveille Lina et Tom très tôt. "
             "« Habillez-vous vite, j'ai une surprise ! » "
             "Toute la famille va chez Madame Rose. Dans le panier, il reste un seul chaton : "
             "le petit roux aux yeux bleus. Il a bien grandi. "
             "Madame Rose le pose dans les bras de Lina. "
             "« Il est à toi, si tes parents sont d'accord. » "
             "Lina regarde papa et maman. Ils disent oui en souriant. Lina saute de joie ! "
             "Elle choisit un nom pour le chaton : Caramel. "
             "À la maison, Moka n'est pas content du tout. "
             "Il souffle et il part se cacher sous le canapé. "
             "Caramel, lui, n'a pas peur. Il avance doucement et vient se coucher contre Moka. "
             "Moka le regarde longtemps… puis il commence à lui lécher la tête. "
             "Le soir, les deux chats dorment ensemble dans le même panier. "
             "« Ils sont devenus amis ! » chuchote Lina.",
    questions=["Quelle est la surprise de papa ?",
               "Quel nom Lina choisit-elle pour le chaton ?",
               "Que fait Moka au début ?",
               "Que font les deux chats le soir ?"],
    ecrire=["Caramel","ensemble","amis"],
    completer_titre="Complète avec : et ou est",
    completer=[("Moka _ un chat.","est"),("Lina _ Tom jouent.","et"),
               ("Le chaton _ roux.","est"),("Papa _ maman sourient.","et"),
               ("Caramel _ content.","est")],
    copie="Les deux chats sont amis.",
    dictee_mots=["chaton","ensemble","content","surprise"],
    dictee_phrase="Les deux chats sont devenus amis.",
    chrono=True,
),
dict(
    n=21, titre="Grande révision", revision=True,
    son="Tous mes sons", ref="Je suis prête pour le bilan !",
    regle="Pour bien écrire un mot : je le lis, je l'épelle, je le cache, je l'écris, je vérifie.",
    syllabes=["chou","bon","main","roi","feu","beau","pei","gne",
              "ille","ça","gui","pho","ssi","dan","ose","neu"],
    mots=["bon-j{ou}r","{é}-co-le","m{ai}-son","{en}-f{an}t","gâ-t{eau}","f{ill}e",
          "pois-s{on}","é-lé-ph{an}t","tou-j{ou}rs","beau-c{ou}p","au-jour-d'hui","mer-ci"],
    outils=["bien","tout","rien"],
    histoire_titre="La réponse de Lina",
    histoire="Dimanche, Lina écrit enfin sa réponse à mamie. Elle s'applique beaucoup.\n"
             "« Chère mamie,\n"
             "Merci pour ta jolie lettre. Moi aussi, je vais bien. "
             "Il s'est passé beaucoup de choses ! À l'école, nous sommes allés au zoo "
             "et un éléphant nous a arrosés. J'ai écrit une histoire sur Moka avec des ailes. "
             "Moka s'est caché dans mon armoire et j'ai eu très peur. "
             "Et surtout, nous avons un nouveau chaton ! Il s'appelle Caramel. "
             "Il est roux, avec des yeux bleus. Au début, Moka était jaloux, "
             "mais maintenant, ils dorment toujours ensemble. "
             "Oui, j'ai encore mon lapin en tissu : Caramel aime bien jouer avec ses oreilles ! "
             "Je lis de mieux en mieux et j'écris presque sans fautes. Viens vite nous voir !\n"
             "Gros bisous. Lina »\n"
             "Elle colle un timbre sur l'enveloppe. Demain, la lettre partira chez mamie.",
    questions=["À qui Lina écrit-elle ?",
               "Raconte deux choses que Lina écrit à mamie.",
               "Comment s'appelle le nouveau chaton ?",
               "À ton avis, que va faire mamie en lisant la lettre ?"],
    ecrire=["merci","bisous","toujours"],
    lettre=True,
    copie="Je lis de mieux en mieux.",
    dictee_mots=["merci","beaucoup","toujours","aujourd'hui"],
    dictee_phrase="Je lis de mieux en mieux.",
    chrono=True,
),
]

# ───────────────────────── BILAN FINAL ─────────────────────────
TEST_SYLLABES = ["ma","li","pou","bon","dan","fin","roi","che",
                 "feu","beau","mai","gne","ille","ça","gui","pho",
                 "ven","loin","jeu","chau","plein","ssi","soi","geon",
                 "tra","blé","cri","fro","gli","pré"]
TEST_MOTS = ["vélo","poule","ballon","enfant","lapin","étoile",
             "cheval","fleur","bateau","fête","montagne","fille",
             "garçon","girafe","maison","poisson","photo","goûter",
             "chemin","jaune","neige","soleil","pigeon","rose",
             "trousse","chapeau","grenouille","éléphant","voiture","dauphin"]
TEST_OUTILS = ["le","une","est","elle","dans","avec","voici","des","chez","beaucoup",
               "très","quand","encore","pas","nous","son","sont","toujours","parce que","demain"]

TEST_TEXTE_TITRE = "Le bonhomme de neige"
TEST_TEXTE = ("Un matin d'hiver, Lina ouvre les volets. Tout est blanc ! "
              "La neige est tombée pendant la nuit. Elle appelle Tom : "
              "« Viens vite, on va faire un bonhomme de neige ! » "
              "Les enfants mettent leurs bonnets, leurs gants et leurs bottes. "
              "Dans le jardin, ils roulent une grosse boule pour le ventre, "
              "puis une plus petite pour la tête. Tom trouve deux cailloux noirs pour les yeux. "
              "Lina met une carotte pour le nez et une vieille écharpe rouge autour du cou. "
              "Moka et Caramel les regardent par la fenêtre. "
              "Ils ne veulent pas sortir : la neige est trop froide pour leurs pattes ! "
              "À midi, maman appelle les enfants : « Venez manger, la soupe est chaude ! » "
              "Lina et Tom rentrent, les joues toutes rouges. "
              "Par la fenêtre, le bonhomme de neige semble leur sourire.")
TEST_QCM = [
    ("En quelle saison se passe l'histoire ?", ["en été","en hiver","au printemps"], 1),
    ("Que trouve Tom pour faire les yeux ?", ["des boutons","des bonbons","des cailloux"], 2),
    ("Que met Lina pour faire le nez ?", ["une carotte","une pomme","un bâton"], 0),
    ("Pourquoi les chats ne sortent-ils pas ?",
     ["ils dorment","la neige est trop froide","ils ont faim"], 1),
    ("Que mangent les enfants à midi ?", ["une soupe","un gâteau","des crêpes"], 0),
]
TEST_DICTEE_MOTS = ["maman","école","maison","chat","bonjour",
                    "toujours","beaucoup","enfant","fille","gâteau"]
TEST_DICTEE_PHRASES = ["Le petit chat dort dans la maison.",
                       "Aujourd'hui, Lina va à l'école avec son frère."]
TEST_COPIE = "Les enfants font un bonhomme de neige."
