# -*- coding: utf-8 -*-
"""Contenu du livre « Mon grand livre de lecture et d'écriture — 30 jours » (CE1).

Regroupe et réordonne (du plus facile au plus difficile) les exercices de 4 cahiers :
  [A] Je lis, j'écris ! 21 jours (Lina et Moka)
  [B] Mon livre de lecture et d'écriture — 21 jours (Je lis / J'écris / Je joue)
  [C] Livre CE1 15 jours — lecture et écriture
  [D] Livre CE1 15 jours — version renforcée
Balisage : syllabes séparées par « - », graphème étudié entre { }.
Types d'exercices : complete, entoure, relie, intrus, vraifaux, devinettes, colonnes,
choix, ordre, ponct, groupes, ordre_num.
"""

BLOCS = [
    ("Les bases", "syllabes simples et premiers mots", 1, 5),
    ("Les sons qui chantent", "ou, on, an, in, oi", 6, 10),
    ("Les sons malins", "ch, g/j, au, eu, è", 11, 15),
    ("Les sons difficiles", "gn, ill, c/g, br/tr, s/ss, ph", 16, 20),
    ("Les phrases", "mots-outils, ponctuation, accords", 21, 25),
    ("Les textes", "verbes, compréhension, récit", 26, 30),
]

J = []

# ═════════════════════════ BLOC 1 : LES BASES ═════════════════════════
J.append(dict(
    titre="Les voyelles et le l", son="a e i o u é è", ref="a comme ami",
    regle="Une consonne + une voyelle = une syllabe : l + a → la.",
    syllabes=["a","e","i","o","u","y","é","è","la","le","li","lo","lu","lé","lè"],
    mots=["a-mi","Li-na","lu-ne","é-té","i-ci","é-lè-ve","Lé-o","il","el-le"],
    phrases=["Léa a un ami.","Lili lit.","Il est allé à l'école."],
    outils=["le","la","un"],
    texte_titre="Lina et Moka",
    texte="Voici Lina. Lina a un ami : le chat Moka. Moka a un ami : le vélo de Lina ! "
          "Le vélo file. Moka file. Lina rit.",
    questions=["Comment s'appelle le chat ?","Qui rit ?","Qu'est-ce qui file ?"],
    ecrire=["ami","lune"], copie="Lina a un ami.",
    ex=dict(type="entoure", titre="J'entoure la syllabe que j'entends",
            note="l'adulte dit la 1re syllabe de chaque paire",
            items=[("la","le"),("li","lu"),("lé","lè"),("lo","la"),("lu","li"),("le","lé")]),
    dictee_mots=["la","le","li","lo","lu","ami"], dictee_phrase="Lina a un ami.",
    production="J'écris mon prénom, puis le prénom d'un ami.",
    test="Lili a un lama. Le lama a une jolie laine. Le soir, Lili lit à côté du lama. "
         "Le lama dort.",
    test_q="Que fait le lama à la fin ?",
))
J.append(dict(
    titre="Les lettres m et t", son="m  t", ref="m comme maman · t comme tomate",
    regle="m + a → ma ; t + o → to. Je glisse d'une lettre à l'autre sans m'arrêter.",
    syllabes=["ma","me","mi","mo","mu","ta","te","ti","to","tu"],
    mots=["ma-man","ma-mie","mo-to","to-ma-te","tu-tu","ta-pis","mi-di","ti-mi-de","tê-te"],
    phrases=["Maman aime Toto.","Ma mamie met son tutu.","La tomate est mûre."],
    outils=["une","et","est"],
    texte_titre="La moto de Tim",
    texte="Tim a une moto. Il la met sur le tapis. Moka, le chat, monte sur la moto ! "
          "Mamie rit : « Moka a une moto ! » Tim lit. Moka dort sur le tapis.",
    questions=["Qui a une moto ?","Où Tim met-il la moto ?","Que fait Moka à la fin ?"],
    ecrire=["maman","moto"], copie="La tomate est mûre.",
    ex=dict(type="relie", titre="Je relie la syllabe au mot qui commence pareil",
            items=[("ma","maman"),("to","tomate"),("ta","tapis"),("mi","midi"),("tu","tutu")],
            ordre_droite=[2,4,0,3,1]),
    dictee_mots=["maman","moto","tapis","ami"], dictee_phrase="Mamie a une moto.",
    production="J'écris une phrase avec le mot « maman ».",
    test="Mamie met la tomate sur la table. Tom a vu la tomate. Il dit : « Miam ! » "
         "et il mange la tomate. Mamie rit.",
    test_q="Qui mange la tomate ?",
))
J.append(dict(
    titre="Les lettres p, r et s", son="p  r  s", ref="p comme papa · r comme rose · s comme sac",
    regle="Je lis chaque syllabe, puis je relis le mot d'un seul coup : pi-ra-te → pirate.",
    syllabes=["pa","pe","pi","po","pu","ra","re","ri","ro","ru","sa","se","si","so","su"],
    mots=["pa-pa","pi-ra-te","ro-se","ri-re","sa-la-mi","mur","pa-ra-sol","sa-la-de","mer"],
    phrases=["Papa rit.","Maman a une rose.","Lila a lu sur le lit.",
             "La souris se cache sous le tapis."],
    outils=["il","elle","on"],
    texte_titre="Le livre de Lina",
    texte="Lina a un livre. Moka, le petit chat, est sur le lit. Lina lit. Moka la regarde. "
          "Puis Moka roule sur le tapis. Lina rit.",
    questions=["Qui lit un livre ?","Où est Moka au début ?","Pourquoi Lina rit-elle ?"],
    ecrire=["papa","rose"], copie="Papa rit.",
    ex=dict(type="intrus", titre="Je barre l'intrus",
            note="le mot qui ne commence pas comme les autres",
            items=[(["papa","pirate","lapin","parasol"],"lapin"),
                   (["rue","rose","mur","rire"],"mur"),
                   (["maman","moto","tomate","mamie"],"tomate")]),
    dictee_mots=["papa","rue","mur","rose"], dictee_phrase="Lina lit sur le lit.",
    production="J'écris une phrase avec le mot « papa ».",
    test="Papa a un parasol rose. Il le pose sur le sable. Lina et Moka sont sous le parasol. "
         "Papa lit. Lina rit : Moka a du sable sur le museau !",
    test_q="Où papa pose-t-il le parasol ?",
))
J.append(dict(
    titre="Les lettres d, n, f et v", son="d  n  f  v", ref="d comme dame · v comme vélo",
    regle="Attention : f et v se ressemblent à l'oreille. Pour v, ça vibre !",
    syllabes=["da","de","di","do","du","na","ne","ni","no","nu",
              "fa","fe","fi","fo","fu","va","ve","vi","vo","vu"],
    mots=["da-me","nid","fê-te","vé-lo","fa-ri-ne","sa-von","na-vet","do-do","du-ne"],
    phrases=["La dame va au marché.","Le vélo de Lina est neuf.","La poule a un nid."],
    outils=["je","tu","dans"],
    texte_titre="Le petit sac",
    texte="Nina pose un petit sac près du tapis. Papa arrive. Dans le sac, il y a une tomate "
          "et une petite nappe. Nina aide papa à tout poser.",
    questions=["Que pose Nina ?","Que trouve-t-on dans le sac ?","Qui aide papa ?"],
    ecrire=["vélo","farine"], copie="Le vélo est neuf.",
    ex=dict(type="complete", titre="Je complète avec : da, na, fa ou va",
            items=[("_me","da"),("_rine","fa"),("_vet","na"),("_se","va"),("ma_me","da")]),
    dictee_mots=["dame","nid","vélo","savon"], dictee_phrase="La poule a un nid.",
    production="J'écris une phrase avec « petit » ou « petite ».",
    test="Le vélo de Nina est rouge. Nina va vite, vite ! Elle passe devant la dune, "
         "puis devant le nid de la poule. À la maison, papa a fait une tarte.",
    test_q="De quelle couleur est le vélo ?",
))
J.append(dict(
    titre="b, c, qu et les mots courts", son="b  c  qu", ref="b comme bébé · qu comme quatre",
    regle="q est toujours suivi de u : qu se lit [k], comme dans quatre.",
    syllabes=["ba","be","bi","bo","bu","ca","co","cu","que","qui","lac","sac","bol","bus","sel"],
    mots=["bé-bé","bul-le","ca-ba-ne","cu-be","qua-tre","coq","bus","bol","lac"],
    phrases=["Le chat dort.","Le bus est plein.","Le bébé boit.",
             "Quatre cubes sont dans la cabane."],
    outils=["avec","pour","sur"],
    texte_titre="La cabane",
    texte="Léo va vite à vélo. Il arrive près d'une petite cabane. Il voit quatre cubes "
          "et un ballon. Un bébé joue avec le ballon. Léo pose son vélo et joue avec lui.",
    questions=["Comment Léo se déplace-t-il ?","Combien y a-t-il de cubes ?",
               "Avec quoi joue le bébé ?"],
    ecrire=["bébé","cabane"], copie="Le bébé boit.",
    ex=dict(type="vraifaux", titre="Vrai ou faux ?", note="j'entoure V ou F",
            items=[("Le chat dort.","V"),("Le bus vole.","F"),("Maman rit.","V"),
                   ("Le mur parle.","F")]),
    dictee_mots=["lac","sac","bol","bus"], dictee_phrase="Le bébé joue avec un cube.",
    production="J'écris le nom de trois objets que je vois autour de moi.",
    test="Dans le bus, il y a un bébé. Il a un bol et un cube. Le bus roule. "
         "Le bébé tape sur le bol : bam, bam ! Tout le monde rit dans le bus.",
    test_q="Qu'est-ce que le bébé a dans les mains ?",
))

# ═════════════════════════ BLOC 2 : LES SONS QUI CHANTENT ═════════════════════════
J.append(dict(
    titre="Le son ou", son="ou", ref="ou comme loup", auto=["ou","où"],
    regle="o + u se lisent ensemble : ou. Exemple : l-ou-p.",
    syllabes=["mou","lou","pou","tou","sou","fou","nou","rou","jou","bou","cou","vou"],
    mots=["l{ou}p","s{ou}-pe","p{ou}-le","r{ou}-ge","m{ou}-ton","r{ou}e","d{ou}x","b{ou}-le","j{ou}r"],
    phrases=["Le loup est doux.","La roue tourne.","La poule rousse couve."],
    outils=["moi","toi","voici"],
    texte_titre="La boule rouge",
    texte="Moka a une boule rouge. Il roule la boule sous le tapis. Lina court : "
          "« Moka, où est la boule ? » Moka touche le tapis. Lina soulève le tapis : "
          "la boule rouge est là ! Moka joue toute la journée.",
    questions=["De quelle couleur est la boule ?","Où Moka roule-t-il la boule ?",
               "Qui trouve la boule ?"],
    ecrire=["loup","poule"], copie="Moka joue.",
    ex=dict(type="complete", titre="Je complète avec : ou",
            items=[("l_p","ou"),("s_pe","ou"),("p_le","ou"),("r_ge","ou"),("d_x","ou")]),
    dictee_mots=["loup","soupe","boule","roue"], dictee_phrase="Moka joue avec la boule rouge.",
    production="J'écris une phrase avec un mot qui contient « ou ».",
    test="Lou a une poule rousse. Tous les jours, la poule couve sous le houx. "
         "Un matin, Lou trouve un œuf tout doux. « Merci, la poule ! » dit Lou.",
    test_q="Que trouve Lou un matin ?",
))
J.append(dict(
    titre="Le son on", son="on  om", ref="on comme ballon",
    regle="Devant m, b, p, on écrit om : ombre, pompier, nom.",
    syllabes=["mon","lon","pon","ton","son","bon","ron","fon","jon","nom","bom","com"],
    mots=["b{on}-b{on}","p{on}t","ba-l{on}","mou-t{on}","r{on}d","mai-s{on}","n{om}","p{om}-pier","bou-t{on}"],
    phrases=["Mon bouton est rond.","La maison est sous le pont.","Le mouton est blanc."],
    outils=["les","des","de"],
    texte_titre="Le ballon",
    texte="Dimanche, Lina et Moka v{on}t au p{on}t. Lina a un ball{on}. Elle le lance très haut. "
          "Oh n{on} ! Le ball{on} t{om}be dans l'eau. Moka ne bouge pas : il a peur de l'eau. "
          "Un garç{on} a un bât{on}. Il pousse le ball{on} vers le bord. "
          "« Merci ! » dit Lina. Le garç{on} s'appelle Sim{on}.",
    questions=["Où vont Lina et Moka ?","Où tombe le ballon ?","Comment s'appelle le garçon ?"],
    ecrire=["bonbon","ballon"], copie="Simon a un bonbon.",
    ex=dict(type="complete", titre="Je complète avec : ou ou on",
            items=[("l_p","ou"),("b_","on"),("r_e","ou"),("p_t","on"),("d_x","ou"),("m_","on")]),
    dictee_mots=["pont","ballon","bouton","nom"], dictee_phrase="Le ballon roule sous le pont.",
    production="J'écris une phrase avec un mot qui contient « on ».",
    test="Simon a un ballon rond. Il le lance sur le pont. Le ballon tombe dans le jardin "
         "de son oncle. « Mon ballon ! » crie Simon. Son oncle le lui rend avec un bonbon.",
    test_q="Où tombe le ballon ?",
))
J.append(dict(
    titre="Le son an / en", son="an  en  am  em", ref="an comme maman · en comme dent",
    regle="Devant m, b, p, on écrit am ou em : lampe, chambre, temps.",
    syllabes=["man","lan","pan","tan","ban","ran","dan","ven","den","lam","cham","tem"],
    mots=["ma-m{an}","{en}-f{an}t","d{en}t","v{en}t","b{an}c","l{am}-pe","ch{am}-bre","gr{an}d","br{an}-che"],
    phrases=["Le vent souffle fort.","L'enfant joue dans la cour.","Assieds-toi sur le banc."],
    outils=["chez","mais","aussi"],
    texte_titre="Le grand vent",
    texte="Ce matin, le v{en}t souffle. Il est gr{an}d et fort. Mam{an} t{en}d les "
          "p{an}talons de papa sur le fil. Moka a peur du v{en}t : il se cache d{an}s la "
          "ch{am}bre, sous la l{am}pe. Lina ch{an}te douc{em}ent pour lui. {En}fin, Moka sort. "
          "Il saute et attrape un p{an}talon qui d{an}se au v{en}t ! "
          "Mam{an} rit : « Quel chat amus{an}t ! »",
    questions=["Quel temps fait-il ?","Où se cache Moka ?","Qu'attrape Moka ?"],
    ecrire=["maman","enfant"], copie="Maman chante.",
    ex=dict(type="complete", titre="Je complète avec : an, en, am ou em",
            items=[("mam_","an"),("d_t","en"),("l_pe","am"),("ch_bre","am"),("gr_d","an")]),
    dictee_mots=["maman","dent","vent","enfant"], dictee_phrase="Le vent souffle dans la cour.",
    production="J'écris une phrase avec un mot en « an » ou en « en ».",
    test="Dans la cour, les enfants jouent avec un ballon orange. Le vent souffle fort et "
         "pousse le ballon sous un banc. Lina range une branche tombée, puis elle reprend "
         "le ballon et rejoint ses amis.",
    test_q="Où le vent pousse-t-il le ballon ?",
))
J.append(dict(
    titre="Le son in", son="in  ain  ein  un", ref="in comme lapin · ain comme pain",
    regle="Le son in s'écrit in, ain, ein (et im devant m, b, p). un se lit presque pareil.",
    syllabes=["lin","pin","vin","fin","tin","brin","main","pain","bain","plein","un","brun"],
    mots=["la-p{in}","ma-t{in}","jar-d{in}","p{ain}","m{ain}","tr{ain}","pl{ein}","{un}","br{un}"],
    phrases=["Le lapin est brun.","L'enfant mange du pain.","Le matin, je vais au jardin."],
    outils=["deux","peu","leur"],
    texte_titre="Le train de mamie",
    texte="Dem{ain}, Lina prend le tr{ain} avec papa. Ils vont chez mamie. Le mat{in}, Lina "
          "met son manteau et prend son lap{in} en tissu. Moka reste à la maison avec maman. "
          "Dans le tr{ain}, Lina regarde les champs, les moul{in}s et les sap{in}s. "
          "Enf{in}, le tr{ain} fr{ein}e. Mamie est sur le quai, les m{ain}s pl{ein}es de "
          "p{ain} chaud. « Bonjour, ma grande ! »",
    questions=["Avec qui Lina prend-elle le train ?","Qui reste à la maison ?",
               "Qu'est-ce que mamie a dans les mains ?"],
    ecrire=["lapin","pain"], copie="Lina prend le train.",
    ex=dict(type="colonnes", titre="Je range les mots dans la bonne boîte",
            cols=["an / en","in / ain"],
            items=["vent","vin","pain","dent","banc","matin","enfant","jardin"],
            answers=[["vent","dent","banc","enfant"],["vin","pain","matin","jardin"]]),
    dictee_mots=["lapin","matin","pain","main"], dictee_phrase="Lina prend le train le matin.",
    production="J'écris une phrase qui commence par « Ce matin, … ».",
    test="Ce matin, Lina va dans le jardin. Elle voit un lapin brun près d'un poirier. "
         "Un oiseau chante. Lina pose une petite boîte sur le banc, puis elle regarde "
         "le lapin partir.",
    test_q="De quelle couleur est le lapin ?",
))
J.append(dict(
    titre="Le son oi", son="oi", ref="oi comme roi", auto=["oi","oî"],
    regle="o + i se lisent ensemble : oi. Exemple : r-oi.",
    syllabes=["moi","toi","roi","soi","voi","poi","noi","boi","doi","foi","loin","coin"],
    mots=["r{oi}","{oi}-seau","t{oi}t","b{oi}s","p{oi}-re","v{oi}-tu-re","é-t{oi}-le","n{oi}r","b{oî}-te"],
    phrases=["Toi et moi, on joue.","L'oiseau chante.","Une poire est dans la boîte."],
    outils=["au","aux","beaucoup"],
    texte_titre="Chez mamie",
    texte="La maison de mamie est en bois. Sur le toit, il y a un oiseau noir. Le soir, "
          "mamie fait une tarte aux poires. Puis elles regardent les étoiles par la fenêtre. "
          "« Mamie, tu vois l'étoile qui brille, là-bas, très loin ? » "
          "« Oui, c'est l'étoile du berger. » Lina pense à Moka. "
          "Elle voudrait qu'il soit là, avec elle.",
    questions=["En quoi est la maison de mamie ?","Qu'y a-t-il sur le toit ?",
               "À qui pense Lina ?"],
    ecrire=["roi","étoile"], copie="Un oiseau est sur le toit.",
    ex=dict(type="complete", titre="Je complète avec : oi ou ou",
            items=[("r_","oi"),("l_p","ou"),("n_r","oi"),("s_pe","ou"),("b_s","oi")]),
    dictee_mots=["roi","bois","noir","boîte"], dictee_phrase="Un oiseau est sur le toit.",
    production="J'écris une phrase avec le mot « voiture ».",
    test="Le roi a une voiture noire. Un soir, il voit une étoile sur le toit de son château. "
         "« Je la veux ! » dit le roi. Mais l'étoile est trop loin. Alors le roi la regarde "
         "et il sourit.",
    test_q="Que veut le roi ?",
))

# ═════════════════════════ BLOC 3 : LES SONS MALINS ═════════════════════════
J.append(dict(
    titre="Le son ch", son="ch", ref="ch comme chat", auto=["ch"],
    regle="c + h se lisent ensemble et font un seul son : ch.",
    syllabes=["cha","che","chi","cho","chu","ché","chou","chon","chan","chin","choi","chè"],
    mots=["{ch}at","{ch}ien","{ch}e-val","va-{ch}e","bou-{ch}e","{ch}o-co-lat","{ch}e-min","mou-{ch}e","mar-{ch}é"],
    phrases=["La vache mange de l'herbe.","Le chat se cache.","Julie marche sur le chemin."],
    outils=["très","après","faire"],
    texte_titre="Moka et le chien",
    texte="Lundi, Lina rentre de l'école par le chemin du marché. Moka la suit en cachette. "
          "Soudain, un grand chien noir arrive. Moka se met à souffler et hérisse ses poils. "
          "Le chien recule : il a peur ! Lina rit et caresse Moka : « Tu es un chat très "
          "courageux ! » Elle achète un petit morceau de fromage au marché pour son champion.",
    questions=["Par où passe Lina pour rentrer ?","Quel animal arrive ?","Que fait le chien ?"],
    ecrire=["chat","vache"], copie="Le chat est courageux.",
    ex=dict(type="devinettes", titre="Je trouve la réponse de la devinette",
            items=[("Je dis miaou, je suis un …","chat"),("Elle donne du lait, c'est la …","vache"),
                   ("Il aboie, c'est le …","chien"),("Je suis marron et sucré, je suis le …","chocolat")]),
    dictee_mots=["chat","chien","chemin","vache"], dictee_phrase="Le chien a peur du chat.",
    production="J'écris une phrase avec le mot « chat » et un verbe.",
    test="Julie marche avec son chat. Sur le chemin, elle voit une grande affiche avec une "
         "girafe. Le chat saute sur une feuille. Julie le regarde et dit : "
         "« Tu es un drôle de chat ! »",
    test_q="Que voit Julie sur l'affiche ?",
))
J.append(dict(
    titre="Les sons g et j", son="ga go gu · ge gi · j", ref="g comme gare · j comme jupe",
    regle="Devant a, o, u, le g se lit [g] (gare). Devant e, i, il se lit [j] (girafe).",
    syllabes=["ga","go","gu","ge","gi","ja","je","ji","jo","ju","gue","gui"],
    mots=["{g}a-re","{g}om-me","{g}i-ra-fe","{j}u-pe","{j}o-li","{g}i-let","{j}ar-din","{gu}i-ta-re","o-ran-{g}e"],
    phrases=["Julie a un joli gilet.","La girafe marche sur le chemin.","Gaston gomme le mot."],
    outils=["qui","que","quand"],
    texte_titre="Le chat de Julie",
    texte="Julie traverse le jardin avec son chat. Elle aperçoit une affiche jaune près du "
          "chemin : on y voit une girafe et un cheval. Le chat s'approche, puis un bruit le "
          "surprend. Il court se cacher derrière une chaise. Julie l'appelle doucement. "
          "Quelques secondes plus tard, le chat revient et se frotte contre sa jambe.",
    questions=["Où Julie se promène-t-elle ?","Quels animaux voit-on sur l'affiche ?",
               "Pourquoi le chat court-il se cacher ?"],
    ecrire=["girafe","jupe"], copie="Julie a un joli gilet.",
    ex=dict(type="complete", titre="Je complète avec : g ou j",
            items=[("_upe","j"),("_omme","g"),("_oli","j"),("_are","g"),("_ardin","j")]),
    dictee_mots=["girafe","jaune","chemin","jupe"],
    dictee_phrase="Le chat jaune se cache derrière une chaise.",
    production="J'écris une phrase avec un mot en « ch » et un mot en « j ».",
    test="Gaspard joue au jardin avec Julie. Il a une gomme jaune et un joli gilet vert. "
         "Soudain, une grosse guêpe arrive ! Julie court se cacher derrière la grange. "
         "Gaspard rigole : la guêpe part sur une fleur.",
    test_q="Où se cache Julie ?",
))
J.append(dict(
    titre="Le son o : au / eau", son="au  eau", ref="au comme auto · eau comme bateau",
    auto=["eau","au"],
    regle="Le son o peut s'écrire o, au ou eau. Le mot « eau » se lit o !",
    syllabes=["pau","mau","sau","chau","jau","tau","beau","peau","veau","seau","reau","teau"],
    mots=["{au}-to","ch{au}d","j{au}-ne","s{au}-ter","b{eau}","ba-t{eau}","gâ-t{eau}","cha-p{eau}","{eau}"],
    phrases=["Le bateau est beau.","L'eau est chaude.","Le seau est plein d'eau."],
    outils=["ce","ici","encore"],
    texte_titre="Le gâteau au chocolat",
    texte="Mercredi, Lina et papa font un gâteau au chocolat. Lina met un chapeau de chef. "
          "Elle verse le sucre, la farine, les œufs et le beurre fondu. Papa met le gâteau "
          "au four. Il fait chaud dans la cuisine. Moka saute sur la table pour voir. "
          "« Non, Moka ! Descends ! » Le gâteau est enfin prêt. Il sent très bon. "
          "Lina en donne un morceau à maman. « Il est beau et délicieux ! » dit maman.",
    questions=["Quel gâteau font-ils ?","Que met Lina sur sa tête ?","Où saute Moka ?"],
    ecrire=["gâteau","chapeau"], copie="Le gâteau est beau.",
    ex=dict(type="complete", titre="Je complète avec : au ou eau",
            items=[("ch_d","au"),("bat_","eau"),("j_ne","au"),("cad_","eau"),("s_ter","au")]),
    dictee_mots=["chaud","beau","bateau","jaune"], dictee_phrase="Le gâteau est au four.",
    production="J'écris deux mots avec « eau » ou « au », puis une phrase.",
    test="Il neige un peu. Lina met son beau chapeau et regarde la rue. Plus tard, elle boit "
         "un verre de lait chaud. Son frère montre un petit bateau en papier posé près de l'eau.",
    test_q="Que montre le frère de Lina ?",
))
J.append(dict(
    titre="Le son eu", son="eu  œu", ref="eu comme feu · œu comme cœur", auto=["eu","œu"],
    regle="e + u se lisent ensemble : eu. On l'écrit parfois œu : sœur, œuf, cœur.",
    syllabes=["peu","feu","jeu","bleu","deu","meu","neu","leu","seu","cheu","fleu","cœu"],
    mots=["f{eu}","j{eu}","bl{eu}","d{eu}x","fl{eu}r","p{eu}r","s{œu}r","{œu}f","c{œu}r"],
    phrases=["Le ciel est bleu.","Il y a deux feux.","Ma sœur a un cœur rouge."],
    outils=["ne","pas","plus"],
    texte_titre="Les fleurs bleues",
    texte="Mardi, c'est l'anniversaire de la sœur de maman, tata Zoé. Lina veut lui offrir "
          "un cadeau. Elle cueille des fleurs bleues dans le jardin. Mais Moka joue avec une "
          "feuille et casse deux fleurs ! Lina n'est pas heureuse… Puis elle a une idée : "
          "elle fait un joli dessin de fleurs et elle écrit : « Joyeux anniversaire ! » "
          "Tata Zoé a les yeux qui brillent : « C'est le plus beau cadeau ! »",
    questions=["Pour qui est le cadeau ?","Que casse Moka ?","Quel cadeau Lina fait-elle à la fin ?"],
    ecrire=["fleur","deux"], copie="Le ciel est bleu.",
    ex=dict(type="complete", titre="Je complète avec : eu ou œu",
            items=[("f_","eu"),("bl_","eu"),("s_r","œu"),("_f","œu"),("d_x","eu")]),
    dictee_mots=["feu","bleu","deux","fleur"], dictee_phrase="Lina a peur du feu.",
    production="J'écris une phrase avec « deux » et une couleur.",
    test="Le petit lapin a deux amis : un chat peureux et une souris heureuse. Un jour, il "
         "pleut. Les trois amis jouent sous un grand arbre. Le chat a peur du tonnerre, "
         "mais ses amis le rassurent.",
    test_q="Qui a peur du tonnerre ?",
))
J.append(dict(
    titre="Le son è", son="è  ê  ai  ei", ref="è comme mère · ai comme lait",
    regle="Le son è s'écrit è, ê, ai, ei, ou et à la fin d'un mot (jouet).",
    syllabes=["mè","pè","lè","rè","tê","fê","mai","lai","rai","bai","nei","rei"],
    mots=["m{è}-re","p{è}-re","fr{è}-re","t{ê}-te","f{ê}-te","l{ai}t","m{ai}-son","r{ei}-ne","n{ei}-ge"],
    phrases=["La reine boit du lait.","La neige tombe sur la maison.","Mon frère a un jouet."],
    outils=["nous","vous","ils"],
    texte_titre="La fête de l'école",
    texte="Jeudi, il y a une f{ê}te à l'école. Lina se f{ai}t une couronne de r{ei}ne. Son grand "
          "fr{è}re, Tom, met un masque d'ours. Les parents arrivent. La m{aî}tresse chante "
          "une chanson avec la classe. Ensuite, chaque él{è}ve lit un petit po{è}me. Lina a un "
          "peu peur, m{ai}s elle lit tr{è}s bien. Son p{è}re et sa m{è}re applaudissent. "
          "Apr{è}s la f{ê}te, il y a du l{ai}t au chocolat et des cr{ê}pes pour tout le monde.",
    questions=["Que se fait Lina ?","Qui porte un masque d'ours ?","Que mange-t-on après la fête ?"],
    ecrire=["mère","fête"], copie="Lina lit très bien.",
    ex=dict(type="complete", titre="Je complète avec : è, ê, ai ou ei",
            items=[("m_re","è"),("t_te","ê"),("l_t","ai"),("r_ne","ei"),("n_ge","ei")]),
    dictee_mots=["père","mère","tête","lait"], dictee_phrase="Il y a une fête à l'école.",
    production="J'écris une phrase sur ma famille avec « père », « mère » ou « frère ».",
    test="La neige tombe depuis le matin. Lina enfile son manteau et son beau chapeau avant de "
         "sortir quelques minutes. Elle construit une petite boule de neige, puis elle rentre "
         "se réchauffer. Dans la cuisine, elle boit du lait chaud.",
    test_q="Que boit Lina dans la cuisine ?",
))

# ═════════════════════════ BLOC 4 : LES SONS DIFFICILES ═════════════════════════
J.append(dict(
    titre="Les sons gn et ill", son="gn  ill  eil", ref="gn comme montagne · ill comme fille",
    regle="gn se lit comme dans « agneau ». ill se lit comme dans « fille » ; "
          "on trouve aussi ail, eil, euil, ouill.",
    syllabes=["gna","gne","gni","gno","gnon","ille","illa","ail","eil","euil","ouille","eille"],
    mots=["mon-ta-{gn}e","a-{gn}eau","cham-pi-{gn}on","a-rai-{gn}ée","f{ill}e","b{ill}e","so-l{eil}","a-b{eill}e","o-r{eill}e"],
    phrases=["La montagne est haute.","La fille joue aux billes.","L'abeille butine les fleurs."],
    outils=["mon","ton","son"],
    texte_titre="Le pique-nique",
    texte="Vendredi, la fam{ill}e de Lina part en pique-nique à la monta{gn}e. Moka reste dormir "
          "à la maison. Il fait beau, le sol{eil} br{ill}e. Papa porte le panier. Lina et Tom "
          "cherchent des champi{gn}ons. Soudain, une ab{eill}e vole autour de Lina ! Lina ne "
          "bouge pas. L'ab{eill}e part sur une fleur. Près du ruisseau, Tom voit une "
          "gren{ouill}e verte qui saute dans l'eau. Le soir, toute la fam{ill}e est fatiguée, "
          "mais heureuse.",
    questions=["Où part la famille ?","Que cherchent Lina et Tom ?","Quel animal saute dans l'eau ?"],
    ecrire=["montagne","soleil"], copie="Le soleil brille.",
    ex=dict(type="complete", titre="Je complète avec : gn, ill ou eil",
            items=[("f_e","ill"),("b_e","ill"),("sol_","eil"),("monta_e","gn"),("li_e","gn")]),
    dictee_mots=["fille","soleil","montagne","abeille"], dictee_phrase="Une abeille vole près de Lina.",
    production="J'écris une phrase avec le mot « soleil ».",
    test="Le petit agneau Gaston vit à la montagne. Chaque matin, le soleil le réveille. "
         "Il joue avec une abeille et une grenouille près du ruisseau. Le soir, il rentre "
         "avec sa famille et s'endort sur la paille.",
    test_q="Avec qui joue l'agneau ?",
))
J.append(dict(
    titre="Les lettres c et g", son="c  ç  g  gu  ge", ref="c comme citron · ç comme garçon",
    regle="Devant e, i : c fait [s], g fait [j]. Devant a, o, u : ç fait [s] (garçon) et "
          "ge fait [j] (pigeon). Devant e, i : gu fait [g] (guitare).",
    syllabes=["ca","co","cu","ce","ci","ça","ço","ga","go","gu","ge","gi","gue","gui","geo"],
    mots=["{c}i-tron","gar-{ç}on","le-{ç}on","{g}a-re","{g}i-ra-fe","{gu}i-ta-re","pi-{ge}on","{c}e-ri-se","{c}o-chon"],
    phrases=["Le garçon joue de la guitare.","Le pigeon mange une cerise.","La leçon est facile."],
    outils=["toujours","jamais","souvent"],
    texte_titre="Le cirque",
    texte="Samedi, Lina va au cirque avec son cousin Hugo. Sous le chapiteau, il y a un "
          "garçon qui joue de la guitare, un clown rigolo et des chevaux. Le clown lance des "
          "citrons en l'air et les rattrape. Puis il fait semblant de glisser sur une carotte ! "
          "Tout le monde rit. À la fin, Hugo gagne un ballon en forme de girafe. "
          "Il le donne à Lina : « Il est pour Moka ! »",
    questions=["Avec qui Lina va-t-elle au cirque ?","Que lance le clown ?","Que gagne Hugo ?"],
    ecrire=["garçon","citron"], copie="Le garçon joue.",
    ex=dict(type="complete", titre="Je complète avec : ç, ge ou gu",
            items=[("gar_on","ç"),("le_on","ç"),("pi_on","ge"),("_itare","gu"),("ba_e","gu")]),
    dictee_mots=["garçon","girafe","leçon","citron"], dictee_phrase="Le garçon joue de la guitare.",
    production="J'écris une phrase avec « garçon » ou « girafe ».",
    test="Ce matin, François prépare un gâteau au citron avec sa grand-mère. Il casse les œufs, "
         "verse la farine et ajoute un peu de sucre. Pendant la cuisson, ils jouent de la "
         "guitare. Quelle bonne odeur dans la cuisine !",
    test_q="Quel gâteau prépare François ?",
))
J.append(dict(
    titre="Les groupes de consonnes", son="br cr tr pl cl gr fr", ref="tr comme train · pl comme plume",
    regle="Deux consonnes collées se lisent vite, ensemble : t-r-ain → train.",
    syllabes=["bra","bri","cro","cre","tra","tri","pla","pli","cla","clo","gra","gri","fra","fro","dra"],
    mots=["{br}as","{br}i-que","{cr}a-be","{tr}ous-se","{pl}u-me","{cl}as-se","{gr}is","{fr}ai-se","{fr}uit"],
    phrases=["Le train arrive.","La trousse est grise.","Le crabe marche sur le sable."],
    outils=["parce que","comme","alors"],
    texte_titre="Le jardin de l'école",
    texte="La classe travaille dans le jardin de l'école. Les élèves plantent des graines, "
          "retirent quelques feuilles sèches et remplissent un arrosoir. Près d'une pierre grise, "
          "Karim trouve une plume. Lina remarque aussi une petite branche cassée. Le groupe "
          "nettoie l'endroit, puis transporte deux plantes près de la grille avant de "
          "retourner calmement en classe.",
    questions=["Où travaille la classe ?","Que trouve Karim ?",
               "Que font-ils avant de rentrer en classe ?"],
    ecrire=["train","classe"], copie="La trousse est grise.",
    ex=dict(type="complete", titre="Je complète avec : br, cr, tr, pl ou fr",
            items=[("_ain","tr"),("_abe","cr"),("_ume","pl"),("_aise","fr"),("_as","br")]),
    dictee_mots=["train","plume","classe","fruit"], dictee_phrase="La trousse grise est dans la classe.",
    production="J'écris une phrase avec « classe » et « trousse ».",
    test="La classe va au jardin. Chaque enfant plante une graine. Lina prend une petite pelle. "
         "Karim apporte de l'eau. Près d'une pierre grise, ils trouvent une plume. Tout le "
         "groupe observe, puis retourne en classe.",
    test_q="Que trouvent-ils près de la pierre ?",
))
J.append(dict(
    titre="La lettre s : [s] ou [z] ?", son="s  ss  z", ref="s comme sac · s comme rose",
    regle="Entre deux voyelles, un seul s chante [z] : rose, maison. Pour entendre [s] entre "
          "deux voyelles, on écrit ss : poisson.",
    syllabes=["sa","so","si","ssa","sso","ssi","za","zo","zi","ase","ose","ise"],
    mots=["ro-{s}e","mai-{s}on","oi-{s}eau","poi-{ss}on","poi-{s}on","cou-{s}in","cou-{ss}in","{z}è-bre","tas-{s}e"],
    phrases=["La rose est dans le vase.","Le poisson nage.","Le zèbre a des rayures."],
    outils=["hier","aujourd'hui","demain"],
    texte_titre="Poisson ou poison ?",
    texte="Lundi, la maîtresse écrit deux mots au tableau : POISSON et POISON. « Lisez bien ! » "
          "dit-elle. Lina lève la main : « Le premier, c'est un animal qui nage dans la rivière. "
          "Le deuxième, c'est un produit très dangereux ! » « Bravo, Lina ! Avec deux s, le s "
          "siffle comme un serpent. Avec un seul s entre deux voyelles, il bourdonne comme une "
          "abeille. » Le soir, Tom rigole : « Alors, mon cousin est assis sur un coussin ! »",
    questions=["Quels mots la maîtresse écrit-elle ?","Lequel est un animal ?",
               "Combien de s y a-t-il dans « poisson » ?"],
    ecrire=["maison","poisson"], copie="Le poisson nage.",
    ex=dict(type="complete", titre="Je complète avec : s ou ss",
            items=[("ro_e","s"),("ta_e","ss"),("mai_on","s"),("trou_e","ss"),("oi_eau","s")]),
    dictee_mots=["rose","maison","poisson","trousse"], dictee_phrase="Le poisson nage dans la rivière.",
    production="J'écris une phrase avec « maison » et une phrase avec « poisson ».",
    test="Lisa a une petite maison pour son hamster Zizou. Elle y met un coussin rose et une "
         "tasse d'eau. Zizou fait la sieste toute la journée. Le soir, il sort et grignote une "
         "graine de tournesol.",
    test_q="Comment s'appelle le hamster ?",
))
J.append(dict(
    titre="ph, y et la fin er / ez", son="ph  y  er  ez", ref="ph comme photo · y comme yeux",
    regle="p + h se lit [f] : photo. y se lit souvent [i] ou [j] : yeux, yaourt. "
          "À la fin d'un mot, er et ez se lisent é : goûter, nez.",
    syllabes=["pha","pho","phi","phé","phan","phin","phon","phou","ya","yo","you","yeu"],
    mots=["{ph}o-to","té-lé-{ph}o-ne","{ph}a-re","é-lé-{ph}ant","dau-{ph}in","{y}a-ourt","{y}eux","goû-t{er}","n{ez}"],
    phrases=["Papa prend une photo.","Le phare guide les bateaux.","Ouvre grand les yeux !"],
    outils=["bien","tout","rien"],
    texte_titre="La photo du zoo",
    texte="Jeudi, la classe de Lina visite le zoo. La maîtresse a un appareil photo. Devant "
          "l'enclos des éléphants, elle dit : « Venez près de moi pour la photo ! » Mais un "
          "éléphant s'approche. Il lève sa trompe et… pchhh ! Il arrose toute la classe ! Les "
          "enfants crient et rient en même temps. Ensuite, ils vont voir les dauphins, puis ils "
          "mangent leur goûter sur un banc. Le soir, Lina montre la photo : on voit seulement "
          "une grosse trompe grise et des enfants qui rient !",
    questions=["Où va la classe ?","Que fait l'éléphant ?","Que voit-on sur la photo ?"],
    ecrire=["photo","éléphant"], copie="Papa prend une photo.",
    ex=dict(type="complete", titre="Je complète avec : ph ou f",
            items=[("élé_ant","ph"),("_leur","f"),("dau_in","ph"),("_ête","f"),("_oto","ph")]),
    dictee_mots=["photo","phare","yaourt","yeux"], dictee_phrase="Les enfants vont visiter le zoo.",
    production="J'écris une phrase avec « photo » ou « téléphone ».",
    test="Sophie part en voyage au bord de la mer. Elle prend une photo du phare et des dauphins "
         "qui sautent dans les vagues. Le soir, elle téléphone à sa mamie pour tout lui raconter. "
         "Ses yeux brillent de joie.",
    test_q="Quels animaux Sophie voit-elle ?",
))

# ═════════════════════════ BLOC 5 : LES PHRASES ═════════════════════════
J.append(dict(
    titre="Les mots-outils", son="le · un · dans · avec", ref="Les petits mots qu'on lit partout",
    regle="Les mots-outils reviennent dans toutes les phrases. Je dois les lire d'un coup d'œil, "
          "sans les déchiffrer.",
    grille=["le","la","les","un","une","des","est","et","dans","avec","sur","pour","pendant","chez","puis"],
    phrases=["Le livre est sur la table.","Une fille joue avec un ballon.",
             "Les enfants sont dans la cour.","Après le repas, les enfants rangent leurs affaires."],
    outils=["pendant","chez","puis"],
    texte_titre="Le sac de Lina",
    texte="Le matin, Lina vérifie son sac avant de partir. Elle y met un cahier, deux livres, "
          "une trousse et une petite bouteille. Sur la table, elle trouve aussi une feuille pour "
          "la maîtresse. Elle la glisse avec soin dans une pochette. Ensuite, elle ferme son sac "
          "et part avec son père pour arriver à l'école à l'heure.",
    questions=["Que vérifie Lina ?","Quels objets met-elle dans son sac ?",
               "Pour qui est la feuille ?"],
    ecrire=["avec","dans"], copie="Le livre est sur la table.",
    ex=dict(type="choix", titre="Je choisis le bon mot-outil",
            items=[("Les crayons sont _ la trousse.",["dans","sur"],"dans"),
                   ("Lina part _ son père.",["avec","chez"],"avec"),
                   ("Elle prend un cahier _ écrire.",["pour","mais"],"pour"),
                   ("Le chat dort _ le lit.",["sur","pour"],"sur")]),
    dictee_mots=["avec","dans","pour","pendant"], dictee_phrase="Les crayons sont dans la trousse.",
    production="J'écris une phrase avec au moins trois mots-outils.",
    test="Le soir, Lina met son pyjama et se brosse les dents. Elle choisit un livre sur la table "
         "et s'installe dans son lit avec Moka. Papa lit une page, puis Lina lit la suivante. "
         "Ensuite, la lumière s'éteint.",
    test_q="Que fait Lina avant de choisir un livre ?",
))
J.append(dict(
    titre="La ponctuation", son=". ? ! ,", ref="Je lis avec la bonne voix",
    regle="Le point : je m'arrête. La virgule : je respire. Le point d'interrogation : je pose "
          "une question. Le point d'exclamation : je montre la joie ou la surprise.",
    ponctuation=["Moka dort.","Moka dort ?","Moka dort !","Il pleut.","Il pleut ?","Il pleut !"],
    mots=["bon-jour","pour-quoi","dou-ce-ment","en-sui-te","a-lors","sou-dain"],
    phrases=["Bonjour, Lina !","Où est mon cahier ?","Le chat court, mais il s'arrête devant la porte.",
             "« Attention, la porte est ouverte ! » crie son frère."],
    outils=["pourquoi","soudain","alors"],
    texte_titre="Où est Moka ?",
    texte="« Où est Moka ? » demande Lina. Elle regarde sous la table, derrière le canapé, puis "
          "près de la porte. Soudain, elle entend un bruit léger dans l'entrée. « Moka, viens "
          "ici ! » appelle-t-elle. Le chat apparaît avec une petite ficelle entre les pattes. "
          "Lina sourit, récupère la ficelle et ferme doucement la porte.",
    questions=["Que cherche Lina ?","Où regarde-t-elle ?","Qu'a Moka entre les pattes ?"],
    ecrire=["bonjour","pourquoi"], copie="Où est mon cahier ?",
    ex=dict(type="ponct", titre="Je mets le bon signe : .  ?  ou  !",
            items=[("Où est Moka _","?"),("Quel beau gâteau _","!"),("Lina lit un livre _","."),
                   ("Tu viens jouer _","?"),("Attention, ça brûle _","!")]),
    dictee_mots=["bonjour","pourquoi","ensuite","porte"],
    dictee_phrase="Où est mon livre ? Il est sur la table.",
    production="J'écris une question, puis une phrase qui y répond.",
    test="« Maman, où est mon pull bleu ? » demande Tom. Maman répond : « Regarde dans "
         "l'armoire ! » Tom ouvre l'armoire. Surprise : Moka dort sur son pull ! "
         "« Moka, tu exagères ! » rit Tom.",
    test_q="Où dort Moka ?",
))
J.append(dict(
    titre="Lire par groupes de mots", son="Je lis sans hacher", ref="Lire comme on parle",
    regle="Je regroupe les mots qui vont ensemble et je fais une petite pause à chaque / .",
    groupes=["Le matin / Lina prépare son sac / puis elle part.",
             "Dans la cour / les enfants / jouent ensemble.",
             "Le chien de mamie / court / dans le jardin.",
             "Quand il pleut, / Moka / reste au chaud / sous la couverture."],
    mots=["ra-pi-de-ment","dou-ce-ment","main-te-nant","en-sem-ble","tou-jours","par-fois"],
    outils=["maintenant","ensemble","parfois"],
    texte_titre="Lina s'entraîne",
    texte="Après l'école, Lina choisit un passage de son livre. Elle le lit une première fois "
          "doucement pour reconnaître tous les mots. Ensuite, elle marque les groupes de mots "
          "avec son doigt et recommence. À la troisième lecture, sa voix devient plus régulière "
          "et elle respecte mieux les points. Son père l'écoute à la fin et lui demande de "
          "raconter en une phrase ce qu'elle a compris.",
    questions=["Pourquoi Lina lit-elle doucement la première fois ?",
               "Que marque-t-elle avec son doigt ?","Que change-t-elle à la troisième lecture ?"],
    ecrire=["ensemble","toujours"], copie="Je relis pour mieux lire.",
    ex=dict(type="groupes", titre="Je coupe la phrase en groupes de mots avec des /",
            items=[("Le petit chat dort dans son panier.","Le petit chat / dort / dans son panier."),
                   ("Ce matin Lina mange une tartine.","Ce matin / Lina / mange une tartine."),
                   ("Après l'école Tom joue au ballon.","Après l'école / Tom / joue au ballon.")]),
    dictee_mots=["après","ensemble","toujours","doucement"],
    dictee_phrase="Après l'école, Lina lit doucement puis elle relit.",
    production="J'écris deux phrases pour dire comment j'ai lu aujourd'hui.",
    test="Le mercredi, Karim va à la piscine avec son père. Il met son maillot, son bonnet et ses "
         "lunettes. Dans l'eau, il nage doucement, puis de plus en plus vite. À la fin, il saute "
         "du petit plongeoir. Son père applaudit très fort !",
    test_q="Que fait Karim à la fin ?",
))
J.append(dict(
    titre="Un ou plusieurs : le pluriel", son="un chat → des chats", ref="Au pluriel, j'ajoute un s muet",
    regle="Au pluriel : le, la, un, une deviennent les ou des, et le nom prend un s qu'on n'entend pas.",
    paires=[("un chat","des chat{s}"),("une fleur","des fleur{s}"),("le lapin","les lapin{s}"),
            ("la poule","les poule{s}"),("un livre rouge","des livre{s} rouge{s}"),
            ("le chat noir","les chat{s} noir{s}")],
    outils=["les","des","plusieurs"],
    texte_titre="Les chatons",
    texte="Mardi, une grande nouvelle arrive : la chatte de la voisine, Madame Rose, a eu "
          "quatre chatons ! Lina et Tom vont les voir. Les chatons sont tout petits. Ils dorment "
          "dans un panier, collés contre leur maman. Il y a deux chatons gris, un chaton blanc "
          "et un chaton roux. Le chaton roux ouvre ses yeux bleus et miaule doucement. "
          "Madame Rose sourit : « Dans deux mois, les chatons pourront partir dans une nouvelle "
          "famille. » Lina regarde papa avec de grands yeux… Papa répond : « On verra ! »",
    questions=["Combien de chatons y a-t-il ?","De quelle couleur est le chaton qui ouvre les yeux ?",
               "Que répond papa ?"],
    ecrire=["des chats","les fleurs"], copie="Les chatons dorment.",
    ex=dict(type="complete", titre="J'écris au pluriel",
            items=[("un chat → des chat_","s"),("une fleur → des fleur_","s"),
                   ("le lapin → l_ lapins","es"),("une poule → d_ poules","es")]),
    dictee_mots=["des chats","les fleurs","deux amis","livres"],
    dictee_phrase="Les chatons dorment dans un panier.",
    production="J'écris un groupe de mots au singulier, puis je l'écris au pluriel.",
    test="Dans le jardin de mamie, il y a trois poules, deux lapins et un gros chien. Les poules "
         "picorent des graines. Les lapins mangent des carottes. Le chien dort près des fleurs. "
         "Lina compte les animaux : ils sont six !",
    test_q="Combien d'animaux y a-t-il ?",
))
J.append(dict(
    titre="Le féminin et les accords", son="petit → petite", ref="Au féminin, j'ajoute souvent un e",
    regle="Avec une fille ou une chose féminine (une, la), l'adjectif prend souvent un e : "
          "un petit sac, une petite trousse.",
    paires=[("un petit sac","une petit{e} trousse"),("un grand garçon","une grand{e} fille"),
            ("un ami","une ami{e}"),("un ballon vert","une robe vert{e}"),
            ("un joli chat","une joli{e} fleur"),("un chien noir","une poule noir{e}")],
    outils=["petit","grand","joli"],
    texte_titre="La chambre de Lina",
    texte="Lina range sa chambre avant de recevoir une amie. Elle place les petits livres sur les "
          "étagères et les grandes boîtes sous le bureau. Deux peluches rouges restent sur le lit. "
          "Les crayons bleus vont dans une trousse verte. Quand elle a terminé, Lina vérifie les "
          "accords dans une petite liste : « les livres rouges », « les grandes boîtes », "
          "« une petite lampe ».",
    questions=["Pourquoi Lina range-t-elle sa chambre ?","Où place-t-elle les boîtes ?",
               "De quelle couleur est la trousse ?"],
    ecrire=["petite","grande"], copie="Une petite trousse verte.",
    ex=dict(type="choix", titre="Je choisis le bon mot",
            items=[("une _ fille",["petit","petite"],"petite"),
                   ("un _ garçon",["petit","petite"],"petit"),
                   ("une _ maison",["grand","grande"],"grande"),
                   ("des livres _",["rouge","rouges"],"rouges")]),
    dictee_mots=["petite","grande","rouges","boîtes"],
    dictee_phrase="Les petits livres rouges sont sur la table.",
    production="J'écris deux groupes de mots au masculin, puis au féminin.",
    test="Lina a une nouvelle amie : Inès. Inès est grande et blonde. Elle porte une robe verte "
         "et des chaussures noires. Les deux amies jouent ensemble dans la cour. Elles partagent "
         "leurs petits gâteaux.",
    test_q="Comment est Inès ?",
))

# ═════════════════════════ BLOC 6 : LES TEXTES ═════════════════════════
J.append(dict(
    titre="Les verbes être et avoir", son="être · avoir", ref="Je suis… J'ai…",
    regle="Attention : il est (être) / et (= en plus) ; il a (avoir) / à (la maison) ; "
          "ils sont / son chat ; ils ont / on.",
    conjugaison=[("je suis","j'ai"),("tu es","tu as"),("il / elle est","il / elle a"),
                 ("nous sommes","nous avons"),("vous êtes","vous avez"),("ils / elles sont","ils / elles ont")],
    outils=["suis","sont","ont"],
    texte_titre="La lettre de mamie",
    texte="Mercredi, le facteur apporte une lettre. Elle est pour Lina ! C'est mamie qui écrit.\n"
          "« Ma chère Lina, je suis très contente de t'écrire. Ici, tout va bien. Les poules ont "
          "pondu beaucoup d'œufs et le jardin est plein de fleurs. Ton oncle Paul a un nouveau "
          "chien : il s'appelle Biscuit. Il est petit et très gentil. Est-ce que tu as encore ton "
          "lapin en tissu ? Fais un gros câlin à Moka pour moi. Je t'embrasse. Mamie »",
    questions=["Qui écrit la lettre ?","Comment s'appelle le chien de l'oncle Paul ?",
               "Qu'ont fait les poules ?"],
    ecrire=["je suis","ils ont"], copie="Mamie a un jardin.",
    ex=dict(type="complete", titre="Je complète avec : suis, as, est, ont ou sommes",
            items=[("Je _ contente.","suis"),("Tu _ un lapin.","as"),("Moka _ un chat.","est"),
                   ("Les poules _ des œufs.","ont"),("Nous _ à la maison.","sommes")]),
    dictee_mots=["je suis","tu as","il est","ils ont"],
    dictee_phrase="Mamie a un jardin plein de fleurs.",
    production="J'écris une phrase avec « je suis » et une phrase avec « j'ai ».",
    test="Je suis Tom, le frère de Lina. J'ai neuf ans. Nous avons un chat qui s'appelle Moka. "
         "Il est roux et il a des yeux verts. Mes amis ont des chiens, mais moi, je suis "
         "content avec mon chat !",
    test_q="Quel âge a Tom ?",
))
J.append(dict(
    titre="Je comprends ce que je lis", son="Qui ? Où ? Quand ? Pourquoi ?", ref="Je cherche les indices",
    regle="Pour répondre, je relis le texte et je cherche le passage qui donne la réponse.",
    grille=["qui ?","où ?","quand ?","quoi ?","pourquoi ?"],
    mots=["per-son-na-ge","en-droit","mo-ment","ac-tion","rai-son","in-di-ce"],
    phrases=["Qui est le personnage principal ?","Où se passe l'histoire ?",
             "Pourquoi Lina prend-elle un parapluie ?"],
    outils=["où","quoi","pourquoi"],
    texte_titre="La promenade sous la pluie",
    texte="Samedi matin, Lina devait aller au parc avec son cousin. Mais le ciel devient sombre "
          "et la pluie commence avant leur départ. Sa mère propose une promenade plus courte avec "
          "des bottes et un imperméable. Lina accepte. Sur le chemin, elle remarque que les "
          "escargots sortent près des murs. Elle comprend alors que la pluie permet aussi "
          "d'observer des choses différentes.",
    questions=["Quel projet Lina avait-elle au début ?","Pourquoi le projet change-t-il ?",
               "Que remarque Lina pendant la promenade ?"],
    ecrire=["personnage","réponse"], copie="Je cherche la réponse.",
    ex=dict(type="relie", titre="Je relie la question à la bonne réponse",
            items=[("Qui ?","Lina et sa mère"),("Où ?","sur le chemin"),("Quand ?","samedi matin"),
                   ("Pourquoi ?","parce qu'il pleut")], ordre_droite=[2,3,0,1]),
    dictee_mots=["samedi","parc","bottes","pluie"], dictee_phrase="Samedi, Lina met ses bottes car il pleut.",
    production="Je réponds par une phrase : pourquoi Lina met-elle des bottes ?",
    test="Dimanche matin, Yassine et sa sœur Salma vont au marché avec leur papa. Il y a des "
         "pommes, des bananes et des oranges. Salma choisit une grappe de raisin. "
         "Yassine veut des dattes. À la maison, maman prépare une salade de fruits. "
         "« Hum, c'est délicieux ! » dit toute la famille.",
    test_q="Que choisit Salma ? Et Yassine ?",
))
J.append(dict(
    titre="Je lis un long texte", son="Je lis avec fluidité", ref="Je lis sans m'arrêter",
    regle="Je lis d'abord en silence. Puis je lis à voix haute, par groupes de mots, en "
          "respectant les points.",
    groupes=["Samedi matin, / papa réveille Lina / très tôt.",
             "Dans le panier, / il reste / un seul chaton.",
             "Le soir, / les deux chats / dorment ensemble."],
    mots=["sur-pri-se","cha-ton","ca-na-pé","en-sem-ble","long-temps","con-tent"],
    outils=["vite","tôt","tard"], chrono=True,
    texte_titre="Caramel",
    texte="Samedi matin, papa réveille Lina et Tom très tôt. « Habillez-vous vite, j'ai une "
          "surprise ! » Toute la famille va chez Madame Rose. Dans le panier, il reste un seul "
          "chaton : le petit roux aux yeux bleus. Madame Rose le pose dans les bras de Lina. "
          "« Il est à toi, si tes parents sont d'accord. » Papa et maman disent oui en souriant. "
          "Lina choisit un nom : Caramel. À la maison, Moka n'est pas content du tout. Il souffle "
          "et part se cacher sous le canapé. Caramel, lui, n'a pas peur. Il vient se coucher "
          "contre Moka. Moka le regarde longtemps… puis il lui lèche la tête. Le soir, les deux "
          "chats dorment ensemble. « Ils sont devenus amis ! » chuchote Lina.",
    questions=["Quelle est la surprise de papa ?","Quel nom Lina choisit-elle ?",
               "Que fait Moka au début ?","Que font les deux chats le soir ?"],
    ecrire=["Caramel","ensemble"], copie="Les deux chats sont amis.",
    ex=dict(type="complete", titre="Je complète avec : et ou est",
            items=[("Moka _ un chat.","est"),("Lina _ Tom jouent.","et"),("Le chaton _ roux.","est"),
                   ("Papa _ maman sourient.","et")]),
    dictee_mots=["chaton","ensemble","content","surprise"],
    dictee_phrase="Les deux chats sont devenus amis.",
    production="J'écris deux phrases pour décrire Caramel.",
    test="Minou le chat a vu une petite souris près du placard. La souris court vite vers son "
         "trou. Minou la poursuit en silence. Mais la souris est maligne : elle grimpe sur "
         "l'étagère où il y a un gros morceau de fromage. Minou essaie de sauter, mais il est "
         "trop gros ! Depuis ce jour, ils partagent le fromage : un petit bout pour chacun.",
    test_q="Que partagent-ils à la fin ?",
))
J.append(dict(
    titre="Je raconte : d'abord, puis, enfin", son="d'abord · puis · enfin", ref="Je raconte dans l'ordre",
    regle="Pour raconter, j'utilise des mots qui donnent l'ordre : d'abord, puis, ensuite, enfin.",
    grille=["d'abord","puis","ensuite","après","enfin"],
    mots=["va-li-se","a-vi-on","nu-a-ge","hô-tes-se","va-can-ces","hu-blot"],
    phrases=["D'abord, je prends mon cahier.","Puis je lis une histoire.","Enfin, je vais dormir."],
    outils=["d'abord","ensuite","enfin"],
    texte_titre="Le voyage de Nina",
    texte="C'est les vacances ! D'abord, Nina prépare sa valise : des robes, un maillot de bain et "
          "son doudou préféré. Puis, à l'aéroport, elle monte dans un grand avion blanc. "
          "« Attachez vos ceintures ! » dit l'hôtesse en souriant. Ensuite, l'avion décolle et "
          "monte très haut, au-dessus des nuages. Par le hublot, Nina voit la mer bleue et des "
          "petites maisons. Enfin, après deux heures de vol, l'avion atterrit. Le soleil brille, "
          "les vacances commencent !",
    questions=["Que met Nina dans sa valise ?","Que voit-elle par le hublot ?",
               "Combien de temps dure le vol ?"],
    ecrire=["d'abord","enfin"], copie="Nous allons à l'école.",
    ex=dict(type="ordre_num", titre="Je numérote les phrases dans l'ordre (1, 2, 3, 4)",
            items=[("Ensuite, elle monte dans l'avion.",2),("D'abord, Nina prépare sa valise.",1),
                   ("Enfin, les vacances commencent !",4),("Puis l'avion décolle.",3)]),
    dictee_mots=["école","cahier","histoire","demain"],
    dictee_phrase="Demain matin, je prends mon cahier.",
    production="Je raconte ma journée en 3 phrases : D'abord… Puis… Enfin…", prod_rows=2,
    test="Samedi, Sara va au parc avec son frère Karim. Sara monte "
         "sur le toboggan : « Youhou ! » Karim préfère la balançoire. À midi, toute la famille "
         "fait un pique-nique sur l'herbe. Pour le goûter, mamie a préparé un gâteau au chocolat. "
         "« C'est la plus belle journée ! » dit Sara.",
    test_q="Que préfère Karim ?",
))
J.append(dict(
    titre="Grande révision", son="Tous mes sons", ref="Je suis prête pour le grand test !",
    regle="Pour bien écrire un mot : je le lis, je l'épelle, je le cache, je l'écris, je vérifie.",
    syllabes=["chou","bon","main","roi","feu","beau","gne","ille","ça","gui","pho","ssi"],
    mots=["bon-j{ou}r","{é}-co-le","m{ai}-s{on}","{en}-f{an}t","gâ-t{eau}","f{ill}e","tou-j{ou}rs","beau-c{ou}p","mer-ci"],
    outils=["merci","bravo","bientôt"], chrono=True,
    texte_titre="La réponse de Lina",
    texte="Dimanche, Lina écrit sa réponse à mamie.\n"
          "« Chère mamie, merci pour ta jolie lettre. Il s'est passé beaucoup de choses ! À l'école, "
          "nous sommes allés au zoo et un éléphant nous a arrosés. Je suis allée au cirque avec "
          "Hugo. Et surtout, nous avons un nouveau chaton ! Il s'appelle Caramel. Il est roux, avec "
          "des yeux bleus. Au début, Moka était jaloux, mais maintenant, ils dorment toujours "
          "ensemble. Je lis de mieux en mieux et j'écris presque sans fautes. Viens vite nous voir ! "
          "Gros bisous. Lina »",
    questions=["À qui Lina écrit-elle ?","Raconte deux choses que Lina écrit à mamie.",
               "Comment s'appelle le nouveau chaton ?"],
    ecrire=["merci","bisous"], copie="Je lis de mieux en mieux.",
    ex=dict(type="complete", titre="Je complète avec le bon son",
            items=[("bat_","eau"),("sol_","eil"),("_oto","ph"),("poi_on","ss"),("monta_e","gn")]),
    dictee_mots=["merci","beaucoup","toujours","aujourd'hui"],
    dictee_phrase="Je lis de mieux en mieux.",
    production="J'écris une petite lettre (2 phrases) à quelqu'un que j'aime.", prod_rows=2,
    test="Depuis trente jours, Lina travaille un peu chaque jour. Au début, elle découpait les mots "
         "longs en syllabes et elle avançait lentement. Maintenant, elle reconnaît beaucoup de mots, "
         "lit des phrases plus longues et pense à la ponctuation. Quand elle écrit, elle commence "
         "par une majuscule, laisse des espaces et relit avant de poser son crayon.",
    test_q="Qu'est-ce que Lina fait maintenant quand elle écrit ?",
))

for i, d in enumerate(J, 1):
    d["n"] = i
assert len(J) == 30

# ═════════════════════════ BILANS (après les jours 5, 10, 15, 20, 25, 30) ═════════════════════════
BILANS = [
    dict(n=1, apres=5,
         lecture=["maman","tapis","cabane","vélo","tomate","rose","cube","petit"],
         choix=[("Le _ roule près de la cabane.",["vélo","livre"],"vélo"),
                ("Nina pose la _ sur la table.",["tomate","moto"],"tomate"),
                ("Le _ joue avec une balle.",["bébé","mur"],"bébé")],
         ordre=[("pose / Nina / le sac / .","Nina pose le sac."),
                ("à vélo / Léo / vite / va / .","Léo va vite à vélo.")],
         defi="J'écris deux phrases pour raconter ce que font Nina et Léo.",
         jeux=[dict(type="motsmeles", titre="Mots mêlés", note="je retrouve 6 mots et je les entoure",
                    mots=["MAMAN","PAPA","VELO","TOMATE","CUBE","LAC"]),
               dict(type="relie", titre="Qui fait quoi ? Je relie",
                    items=[("Le bébé","dort."),("Mon ami","joue."),("Le soleil","brille."),
                           ("Lina","va à l'école.")], ordre_droite=[2,0,3,1])]),
    dict(n=2, apres=10,
         lecture=["ballon","branche","lapin","voisin","oiseau","poire","enfant","matin"],
         choix=[("Le vent pousse le _ sous le banc.",["ballon","bateau"],"ballon"),
                ("Le _ brun court dans le jardin.",["lapin","voisin"],"lapin"),
                ("Un _ chante sur une branche.",["oiseau","enfant"],"oiseau")],
         ordre=[("dans le jardin / Lina / un lapin / voit / .","Lina voit un lapin dans le jardin."),
                ("le ballon / le vent / pousse / .","Le vent pousse le ballon.")],
         defi="J'écris deux phrases avec un mot en « on », un mot en « an » et un mot en « in ».",
         jeux=[dict(type="entoure_son", titre="J'entoure le son que j'entends",
                    items=[("maison",["ou","on","in"],"on"),("lapin",["in","an","on"],"in"),
                           ("roi",["oi","ou","on"],"oi"),("enfant",["an","in","on"],"an"),
                           ("poule",["ou","oi","on"],"ou")]),
               dict(type="devinettes", titre="Devinettes",
                    items=[("Je chante dans le ciel, je suis un …","oiseau"),
                           ("On y monte pour rouler, c'est la …","voiture"),
                           ("Il a une couronne, c'est le …","roi")])]),
    dict(n=3, apres=15,
         lecture=["chat","girafe","chapeau","fleur","neige","bateau","jaune","frère"],
         choix=[("Le _ mange une souris.",["chat","chapeau"],"chat"),
                ("La _ tombe en hiver.",["neige","reine"],"neige"),
                ("Le _ flotte sur l'eau.",["bateau","gâteau"],"bateau")],
         ordre=[("boit / La reine / du lait / .","La reine boit du lait."),
                ("son chapeau / met / Lina / .","Lina met son chapeau.")],
         defi="J'écris deux phrases avec des mots en « eau », « au » ou « ai ».",
         jeux=[dict(type="motmystere", titre="Le mot mystère", note="je remets les syllabes dans l'ordre",
                    items=[("teau — ba","bateau"),("ra — fe — gi","girafe"),
                           ("co — lat — cho","chocolat"),("peau — cha","chapeau")]),
               dict(type="motsmeles", titre="Mots mêlés", note="je retrouve 6 mots",
                    mots=["CHAT","VACHE","BATEAU","FLEUR","NEIGE","JUPE"])]),
    dict(n=4, apres=20,
         lecture=["montagne","soleil","garçon","guitare","trousse","plume","poisson","photo"],
         choix=[("Le _ brille.",["soleil","sommeil"],"soleil"),
                ("Le _ nage dans la rivière.",["poisson","poison"],"poisson"),
                ("Papa prend une _.",["photo","phrase"],"photo")],
         ordre=[("joue / Le garçon / de la guitare / .","Le garçon joue de la guitare."),
                ("est / La trousse / dans la classe / .","La trousse est dans la classe.")],
         defi="J'écris deux phrases avec « soleil », « poisson » ou « photo ».",
         jeux=[dict(type="entoure_son", titre="Le bon son : j'entoure",
                    items=[("soleil",["eil","ail","ill"],"eil"),("bateau",["au","ou","eau"],"eau"),
                           ("photo",["ph","f","p"],"ph"),("montagne",["gn","ne","an"],"gn"),
                           ("poisson",["s","ss","z"],"ss"),("garçon",["c","ç","s"],"ç")]),
               dict(type="motmystere", titre="Le mot mystère",
                    items=[("gne — ta — mon","montagne"),("leil — so","soleil"),
                           ("phant — é — lé","éléphant"),("son — pois","poisson")])]),
    dict(n=5, apres=25,
         lecture=["pendant","chez","soudain","ensemble","toujours","petites","grandes","pourquoi"],
         choix=[("Le chat dort _ le lit.",["sur","pour"],"sur"),
                ("Je relis _ pour comprendre.",["doucement","rouge"],"doucement"),
                ("Les _ dorment dans le panier.",["chatons","chaton"],"chatons")],
         ordre=[("dans le texte / la réponse / cherche / Lina / .","Lina cherche la réponse dans le texte."),
                ("relit / elle / doucement / .","Elle relit doucement.")],
         defi="J'écris deux phrases reliées par « puis » ou « mais ».",
         jeux=[dict(type="vraifaux_texte", titre="Je lis, puis je réponds vrai ou faux",
                    texte="Un matin, le petit loup se promène dans la forêt. Il entend un oiseau qui "
                          "chante sur une branche. « Bonjour, oiseau ! » dit le loup. L'oiseau a peur "
                          "et s'envole vers sa maison. Le loup rit : « Je voulais seulement écouter ta "
                          "chanson ! » Depuis ce jour, l'oiseau chante pour le loup chaque matin.",
                    items=[("Le loup se promène le soir.","F"),("L'oiseau chante sur une branche.","V"),
                           ("Le loup veut manger l'oiseau.","F"),
                           ("L'oiseau chante chaque matin pour le loup.","V")])]),
    dict(n=6, apres=30, final=True,
         texte_titre="Moka a disparu !",
         texte="Vendredi soir, Lina cherche Moka partout. Il n'est pas sous le lit, ni dans son panier, "
               "ni sur le canapé. « Moka ! Moka ! Où es-tu ? » Personne ne répond. Toute la famille "
               "l'aide à chercher. Papa regarde dans le jardin avec une lampe. Tom fouille le garage. "
               "Soudain, Lina entend un petit bruit : « Miaou… » Le bruit vient de l'armoire de sa "
               "chambre ! Moka est là, couché sur ses pulls, bien au chaud. Il s'est endormi quand "
               "maman a rangé le linge. « Tu m'as fait peur, petit coquin ! » Moka ronronne, comme si "
               "de rien n'était.",
         questions=["Où Lina cherche-t-elle Moka en premier ?","Que fait papa pour aider ?",
                    "Où Lina trouve-t-elle Moka ?","Pourquoi Moka est-il là ?"],
         checklist=["Je lis les syllabes sans hésiter.","Je lis les mots en entier, sans découper.",
                    "Je lis un texte en respectant les points.","Je comprends ce que je lis.",
                    "J'écris les mots sans modèle.","Je fais une dictée de phrases.",
                    "Je commence mes phrases par une majuscule et je finis par un point."],
         phrases=["Je sais lire des syllabes.","Je sais lire des mots.","Je sais lire des phrases.",
                  "Je sais lire des textes.","Je suis prête pour le grand test !"]),
]

# ═════════════════════════ GRAND TEST FINAL (sur 100 points) ═════════════════════════
T_SYLLABES = ["ma","tri","chou","loin","pan","gui","fro","ble","tein","reau",
              "vin","plu","che","son","brin","jou","cla","feu","ran","doi"]
T_MOTS = ["maman","jardin","chapeau","oiseau","trousse","enfant","voiture","lecture","question","petite",
          "ballon","classe","histoire","matin","rouges","bateau","branche","école","montagne","éléphant"]
T_FLUENCE_TITRE = "Le bonhomme de neige"
T_FLUENCE = ("Un matin d'hiver, Lina ouvre les volets. Tout est blanc ! La neige est tombée pendant la "
             "nuit. Elle appelle Tom : « Viens vite, on va faire un bonhomme de neige ! » Les enfants "
             "mettent leurs bonnets, leurs gants et leurs bottes. Dans le jardin, ils roulent une grosse "
             "boule pour le ventre, puis une plus petite pour la tête. Tom trouve deux cailloux noirs "
             "pour les yeux. Lina met une carotte pour le nez et une vieille écharpe rouge autour du "
             "cou. Moka et Caramel les regardent par la fenêtre. Ils ne veulent pas sortir : la neige "
             "est trop froide pour leurs pattes ! À midi, maman appelle les enfants : « Venez manger, "
             "la soupe est chaude ! » Lina et Tom rentrent, les joues toutes rouges. Par la fenêtre, "
             "le bonhomme de neige semble leur sourire.")
T_COMP_TITRE = "La surprise de Lina"
T_COMP = ("Dimanche matin, Lina se lève tôt car elle veut préparer une surprise pour sa grand-mère. "
          "Elle prend une feuille, des crayons et une petite boîte. Elle dessine un jardin avec un arbre, "
          "deux oiseaux et un chat gris. Ensuite, elle écrit un petit message et vérifie chaque phrase. "
          "Quand sa grand-mère arrive, Lina lui donne la boîte. La grand-mère sourit et lit le message "
          "à voix haute.")
T_COMP_Q = [("Quel jour se passe l'histoire ?","dimanche (matin)"),
            ("Que prend Lina pour préparer sa surprise ?","une feuille, des crayons et une petite boîte"),
            ("Que dessine-t-elle ?","un jardin avec un arbre, deux oiseaux et un chat gris"),
            ("Pourquoi relit-elle son message ?","pour vérifier ses phrases (les mots, le point)"),
            ("Comment réagit la grand-mère ?","elle sourit et lit le message à voix haute")]
T_DICTEE_MOTS = ["matin","maison","enfant","chapeau","trousse","jardin","oiseau","petit","école","rouge"]
T_DICTEE_PHRASES = ["Le petit chat joue dans le jardin.","Demain matin, Lina prend son cahier rouge."]
T_PRODUCTION = ("Raconte une matinée d'école, une sortie ou ta plus belle journée en 5 à 7 phrases. "
                "Utilise au moins trois mots parmi : d'abord, puis, ensuite, mais, parce que, enfin.")
