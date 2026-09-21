#!/usr/bin/env python3
# Générateur one-shot : blog + pages légales.
import os

SITE = "https://spotscreens.com"
OUT = os.path.dirname(os.path.abspath(__file__))
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">'


def head(title, desc, path, noindex=False, article=None):
    canon = f"{SITE}/{path}"
    robots = '\n<meta name="robots" content="noindex">' if noindex else ""
    ogtype = "article" if article else "website"
    ld = ""
    if article:
        ld = f"""
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"BlogPosting",
  "headline":"{article['headline']}",
  "datePublished":"{article['date_iso']}",
  "author":{{"@type":"Organization","name":"SpotScreens"}},
  "publisher":{{"@type":"Organization","name":"SpotScreens","url":"{SITE}"}},
  "mainEntityOfPage":"{canon}",
  "inLanguage":"fr"
}}
</script>"""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">{robots}
<meta name="theme-color" content="#062052">

<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="SpotScreens">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/og-cover.jpg">
<meta property="og:locale" content="fr_TN">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="/assets/logo/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONTS}
<link rel="stylesheet" href="/assets/css/site.css">{ld}
</head>
<body>

<a class="skip" href="#main">Aller au contenu</a>
"""


def header(active="", sub=""):
    c = lambda k: ' aria-current="page"' if active == k else ""
    s = lambda k: ' aria-current="page"' if sub == k else ""
    return f"""
<div class="utility">
  <div class="container utility__inner">
    <a href="tel:+21622249917">+216&nbsp;22&nbsp;249&nbsp;917</a>
    <span class="utility__sep" aria-hidden="true"></span>
    <a href="mailto:contactspotscreens@gmail.com">contactspotscreens@gmail.com</a>
  </div>
</div>

<header class="site-header">
  <div class="container site-header__inner">
    <a class="brand" href="/" aria-label="SpotScreens, retour à l'accueil">SpotScreens</a>
    <button class="burger" data-burger aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="nav">
      <span class="burger__bars" aria-hidden="true"></span>
    </button>
    <nav class="nav" id="nav" data-nav aria-label="Navigation principale">
      <ul class="nav__list">
        <li class="nav__item nav__item--has-menu">
          <a class="nav__link" href="/ecrans-taxi.html"{c('reseau')}>Le réseau <span class="nav__caret" aria-hidden="true"></span></a>
          <ul class="nav__submenu">
            <li><a href="/ecrans-taxi.html"{s('ecrans')}>Les écrans taxi</a></li>
            <li><a href="/formats.html"{s('formats')}>Formats &amp; spécifications</a></li>
            <li><a href="/couverture.html"{s('couverture')}>Couverture</a></li>
            <li><a href="/mesure.html"{s('mesure')}>Mesure &amp; suivi</a></li>
          </ul>
        </li>
        <li class="nav__item"><a class="nav__link" href="/campagne.html"{c('campagnes')}>Campagnes</a></li>
        <li class="nav__item"><a class="nav__link" href="/agences.html"{c('annonceurs')}>Annonceurs</a></li>
        <li class="nav__item"><a class="nav__link" href="/chauffeurs.html"{c('chauffeurs')}>Chauffeurs</a></li>
        <li class="nav__item nav__item--has-menu">
          <a class="nav__link" href="/a-propos.html"{c('apropos')}>À propos <span class="nav__caret" aria-hidden="true"></span></a>
          <ul class="nav__submenu">
            <li><a href="/a-propos.html"{s('apropos')}>Qui nous sommes</a></li>
            <li><a href="/blog.html"{s('blog')}>Blog</a></li>
            <li><a href="/faq.html"{s('faq')}>Questions fréquentes</a></li>
          </ul>
        </li>
      </ul>
      <a class="btn btn--primary btn--sm nav__cta" href="/contact.html">Nous contacter</a>
    </nav>
  </div>
</header>

<main id="main">
"""


GIT = """
  <section class="get-in-touch">
    <div class="container">
      <h2 class="get-in-touch__title">Parlons-en.</h2>
      <p>Parlez-nous de votre campagne&nbsp;: votre objectif, votre période, votre public. Nous revenons vers vous avec une proposition de diffusion.</p>
      <div class="btn-row btn-row--center">
        <a class="btn btn--primary" href="/contact.html">Demander une proposition</a>
        <a class="btn btn--outline" href="/ecrans-taxi.html">Découvrir le réseau</a>
      </div>
      <div class="git-contacts">
        <span><a href="mailto:contactspotscreens@gmail.com">contactspotscreens@gmail.com</a></span>
        <span><a href="tel:+21622249917">+216&nbsp;22&nbsp;249&nbsp;917</a></span>
      </div>
    </div>
  </section>
"""

FOOTER = """
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col footer-brand">
        <a class="footer-brand__logo" href="/">SpotScreens</a>
        <p>La publicité extérieure, enfin simple. Votre marque sur des écrans LED qui sillonnent Tunis.</p>
      </div>
      <div class="footer-col">
        <h5>Le réseau</h5>
        <ul>
          <li><a href="/ecrans-taxi.html">Les écrans taxi</a></li>
          <li><a href="/formats.html">Formats &amp; spécifications</a></li>
          <li><a href="/couverture.html">Couverture</a></li>
          <li><a href="/mesure.html">Mesure &amp; suivi</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Informations</h5>
        <ul>
          <li><a href="/a-propos.html">À propos</a></li>
          <li><a href="/agences.html">Annonceurs &amp; agences</a></li>
          <li><a href="/chauffeurs.html">Chauffeurs partenaires</a></li>
          <li><a href="/blog.html">Blog</a></li>
          <li><a href="/faq.html">Questions fréquentes</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Contact</h5>
        <ul>
          <li><a href="mailto:contactspotscreens@gmail.com">contactspotscreens@gmail.com</a></li>
          <li><a href="tel:+21622249917">+216&nbsp;22&nbsp;249&nbsp;917</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>©&nbsp;<span data-year>2026</span> SpotScreens. Tous droits réservés.</span>
      <nav aria-label="Liens légaux">
        <a href="/mentions-legales.html">Mentions légales</a>
        <a href="/confidentialite.html">Confidentialité</a>
        <a href="/cgv.html">Conditions générales</a>
      </nav>
    </div>
  </div>
</footer>

<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""


def write(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name)


POSTS = [
    dict(slug="blog-publicite-taxi-tunis.html",
         date="15 septembre 2026", date_iso="2026-09-15", cat="Repères",
         title="Publicité sur taxi à Tunis&nbsp;: ce que l'annonceur obtient réellement",
         title_plain="Publicité sur taxi à Tunis : ce que l'annonceur obtient réellement",
         excerpt="Ce que ce média permet, ce qu'il ne permet pas, et comment le comparer honnêtement à un panneau fixe."),
    dict(slug="blog-concevoir-visuel-led.html",
         date="28 août 2026", date_iso="2026-08-28", cat="Création",
         title="Concevoir un visuel pour écran LED mobile&nbsp;: le guide complet",
         title_plain="Concevoir un visuel pour écran LED mobile : le guide complet",
         excerpt="Contraste, densité d'information, placement du logo : les règles qui distinguent un visuel lu d'un visuel ignoré."),
    dict(slug="blog-campagne-evenement.html",
         date="12 août 2026", date_iso="2026-08-12", cat="Campagnes",
         title="Lancer une campagne taxi autour d'un événement",
         title_plain="Lancer une campagne taxi autour d'un événement",
         excerpt="Ouverture, lancement produit, date unique : comment caler une diffusion mobile sur un temps fort."),
]


def post_card(p):
    return f"""        <a class="post" href="/{p['slug']}">
          <span class="post__media" aria-hidden="true"><span class="ph"><span>Illustration article</span></span></span>
          <span class="post__meta">{p['date']} · {p['cat']}</span>
          <h3 class="post__title">{p['title']}</h3>
          <span class="post__excerpt">{p['excerpt']}</span>
          <span class="tlink">Lire l'article</span>
        </a>
"""


# ============================================================ blog index
write("blog.html",
      head("Blog — publicité taxi et affichage mobile à Tunis | SpotScreens",
           "Repères concrets pour préparer une campagne d'affichage mobile à Tunis : ce que le média permet, comment concevoir un visuel, comment lire un bilan de diffusion.",
           "blog.html")
      + header("apropos", "blog")
      + """
  <section class="hero hero--interior">
    <div class="hero__media" aria-hidden="true">
      <span class="ph"><span>Photo&nbsp;#7 — Taxi passant devant un lieu reconnaissable de Tunis</span></span>
    </div>
    <div class="container hero__inner">
      <span class="kicker kicker--light">Blog</span>
      <h1 class="hero__title">Comprendre la publicité taxi.</h1>
      <p class="hero__text">Des repères concrets pour préparer une campagne d'affichage mobile à Tunis.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="posts">
"""
      + "".join(post_card(p) for p in POSTS)
      + """      </div>
    </div>
  </section>
""" + GIT + FOOTER)


# ============================================================ article helper
def article_page(p, desc, standfirst, body, related):
    rel_cards = "".join(post_card(POSTS[i]) for i in related)
    return (head(p['title_plain'] + " | SpotScreens", desc, p['slug'],
                 article=dict(headline=p['title_plain'], date_iso=p['date_iso']))
            + header("apropos", "blog")
            + f"""
  <section class="section">
    <div class="container">
      <article class="article">
        <p class="article__meta"><a href="/blog.html" style="color:var(--blue-600)">Blog</a> · {p['date']} · {p['cat']}</p>
        <h1>{p['title']}</h1>
        <p class="article__standfirst">{standfirst}</p>

        <figure class="frame frame--16-9 mt-l" aria-hidden="true">
          <span class="ph"><span>Illustration article</span></span>
        </figure>

        <div class="article__body mt-l">
{body}
        </div>

        <div class="article__footer">
          <p class="small">Une question sur votre campagne&nbsp;? Écrivez-nous à <a class="link-inline" href="mailto:contactspotscreens@gmail.com">contactspotscreens@gmail.com</a> ou passez par la <a class="link-inline" href="/contact.html">page contact</a>.</p>
          <div class="btn-row">
            <a class="btn btn--primary" href="/contact.html">Demander une proposition</a>
            <a class="btn btn--outline" href="/blog.html">Tous les articles</a>
          </div>
        </div>
      </article>
    </div>
  </section>

  <section class="section section--blue">
    <div class="container">
      <div class="sh">
        <span class="kicker">À lire aussi</span>
        <h2 class="sh__title" style="font-size:clamp(24px,3vw,34px)">Autres articles</h2>
      </div>
      <div class="posts">
{rel_cards}      </div>
    </div>
  </section>
""" + GIT + FOOTER)


# ============================================================ article 1
write(POSTS[0]['slug'], article_page(
    POSTS[0],
    "Ce que la publicité sur écran LED de taxi permet réellement à Tunis, ce qu'elle ne permet pas, et comment la comparer honnêtement à un panneau fixe.",
    "Le format séduit vite&nbsp;: un écran lumineux qui traverse la ville, ça parle. Mais un annonceur qui engage une campagne a besoin de savoir précisément ce qu'il achète. Voici une lecture sans enrobage.",
    """          <h2>Le support en une phrase</h2>
          <p>Un écran LED double face est monté sur le toit d'un taxi en activité. Il est alimenté par le véhicule et piloté à distance&nbsp;: le visuel est envoyé au parc depuis un système central, sans que le chauffeur ait à intervenir. Le taxi travaille normalement, et l'écran diffuse pendant qu'il circule.</p>
          <p>C'est tout. Il n'y a pas de couche technologique cachée, pas d'écran intérieur, pas de dispositif annexe. Le support se résume à un panneau numérique mobile.</p>

          <h2>Ce que ce média fait bien</h2>

          <h3>Il entre dans le flux au lieu de l'attendre</h3>
          <p>Un panneau fixe occupe un point de la ville et attend que le public passe devant lui. Sa performance dépend entièrement du trafic de cet emplacement. Un taxi fait l'inverse&nbsp;: il se déplace vers le public. Il remonte une avenue, s'arrête à un feu au milieu de piétons, dépose un client devant un immeuble de bureaux, repart vers un quartier commerçant.</p>
          <p>Concrètement, cela veut dire qu'un même visuel rencontre des contextes différents dans la même journée, sans que vous ayez à acheter plusieurs emplacements.</p>

          <h3>Il change de public plusieurs fois par jour</h3>
          <p>La composition du public varie selon l'heure et la zone. Le matin, ce sont des trajets domicile-travail sur des axes réguliers. En journée, des quartiers d'affaires et des zones commerçantes. Le soir, des sorties, des restaurants, des cafés — le moment où un écran LED ressort le mieux, parce que la lumière ambiante baisse et que le public est souvent à pied, donc plus disponible visuellement.</p>

          <h3>Il se modifie sans rien réimprimer</h3>
          <p>C'est l'avantage le plus concret sur le plan opérationnel. Le visuel est un fichier. Vous pouvez le remplacer en cours de campagne&nbsp;: corriger une mention, passer d'un teaser à une révélation, adapter un message à une date. Il n'y a ni impression, ni pose, ni dépose.</p>

          <h2>Ce que ce média ne fait pas</h2>

          <h3>Il ne garantit pas une zone unique</h3>
          <p>C'est la limite la plus importante à comprendre avant de signer. Les taxis ne suivent pas de parcours imposé&nbsp;: ils circulent au gré des courses. On peut orienter une campagne vers des priorités géographiques et vous dire ce qui est raisonnablement atteignable, mais on ne peut pas vous promettre que votre visuel restera dans un seul quartier pendant toute la campagne.</p>
          <p>Si votre objectif est de saturer un périmètre de deux rues autour d'un point de vente, un panneau fixe bien placé reste plus adapté. Si votre objectif est une présence en ville, le mobile prend l'avantage.</p>

          <h3>Il ne compte pas les regards</h3>
          <p>Aucun opérateur d'affichage, mobile ou fixe, ne sait combien de personnes ont réellement regardé un visuel. Ce qui circule dans le secteur sous forme de «&nbsp;contacts&nbsp;» ou d'«&nbsp;impressions&nbsp;» est presque toujours une modélisation&nbsp;: un flux de circulation multiplié par un coefficient de visibilité estimé. C'est utile pour comparer des offres entre elles, mais ce n'est pas une mesure.</p>
          <p>Nous préférons vous dire ce que nous pouvons établir&nbsp;: la période pendant laquelle votre visuel a effectivement été diffusé, le volume de diffusions cumulées sur l'ensemble de la flotte, et les zones parcourues. Ces trois éléments sont vérifiables. Le reste relève de l'estimation, et nous ne le vendons pas comme un fait.</p>

          <h3>Il ne remplace pas un plan média</h3>
          <p>Un écran mobile est un support de notoriété et de rappel. Il fonctionne bien en complément d'autres canaux, moins bien en canal unique pour une campagne qui exige une explication détaillée. Si votre message nécessite trois phrases pour être compris, le format n'est pas le bon.</p>

          <h2>Comment le comparer à un panneau fixe</h2>
          <p>La comparaison la plus honnête ne porte pas sur le volume théorique de contacts, mais sur la nature de l'exposition&nbsp;:</p>
          <ul>
            <li><strong>Le panneau fixe</strong> offre une répétition sur un même public&nbsp;: les mêmes personnes passent devant lui chaque jour, ce qui construit de la mémorisation sur un bassin restreint.</li>
            <li><strong>L'écran mobile</strong> offre une variété d'exposition&nbsp;: plus de contextes, plus de quartiers, une répétition qui se construit de manière plus diffuse.</li>
          </ul>
          <p>Aucun des deux n'est supérieur dans l'absolu. Cela dépend de ce que vous cherchez&nbsp;: ancrer une marque dans un quartier, ou la faire exister dans toute la ville.</p>

          <h2>Ce que vous recevez à la fin</h2>
          <p>À l'issue de la campagne, un récapitulatif vous est remis. Il contient la période de diffusion effective, le volume diffusé sur l'ensemble de la flotte, les zones parcourues, et des captures de l'écran en diffusion. C'est un document que vous pouvez transmettre tel quel à votre direction ou à votre agence.</p>
          <p>Si un véhicule a été immobilisé pendant la campagne — entretien, incident, jour sans course — les diffusions manquantes sont reportées sur les autres véhicules ou en prolongation, de manière à honorer le volume prévu.</p>

          <blockquote>Un média se juge sur ce qu'il peut prouver, pas sur ce qu'il peut promettre.</blockquote>

          <h2>En résumé</h2>
          <p>La publicité sur écran de taxi est un bon choix si vous voulez une présence urbaine large, un visuel modifiable, et une mise en diffusion rapide sans logistique d'impression. C'est un choix discutable si vous avez besoin d'un ciblage géographique strict ou d'une garantie d'audience chiffrée.</p>
          <p>Pour savoir ce que cela donnerait dans votre cas, le plus simple est de nous décrire votre objectif et votre période&nbsp;: nous revenons avec une proposition de diffusion adaptée.</p>
""",
    related=[1, 2]))


# ============================================================ article 2
write(POSTS[1]['slug'], article_page(
    POSTS[1],
    "Contraste, densité d'information, placement du logo, image fixe ou vidéo : les règles de création pour un visuel diffusé sur écran LED mobile.",
    "Un écran de taxi n'est pas une affiche, et encore moins un post Instagram. Le contexte de lecture est très particulier&nbsp;: quelques secondes, en mouvement, souvent de biais. Voici comment concevoir en conséquence.",
    """          <h2>Le contexte de lecture change tout</h2>
          <p>Avant de parler de règles, il faut se représenter la situation réelle de lecture. Votre visuel est vu par quelqu'un qui&nbsp;:</p>
          <ul>
            <li>ne cherchait pas à le voir&nbsp;;</li>
            <li>le découvre pendant deux à quatre secondes, parfois moins&nbsp;;</li>
            <li>le regarde souvent de biais, rarement de face&nbsp;;</li>
            <li>est lui-même en mouvement, à pied ou en voiture&nbsp;;</li>
            <li>a un fond urbain chargé derrière l'écran.</li>
          </ul>
          <p>Chaque règle qui suit découle de cette réalité. Un visuel qui fonctionne sur un écran d'ordinateur peut échouer complètement dans ce contexte.</p>

          <h2>Règle 1 — Un seul message</h2>
          <p>C'est la règle qui compte le plus, et celle qu'on enfreint le plus souvent. Vous avez une idée à faire passer, une seule. Pas trois arguments, pas un slogan plus une promotion plus une adresse plus un QR code.</p>
          <p>Test simple&nbsp;: affichez votre visuel, regardez-le deux secondes, détournez les yeux. Qu'est-ce qui reste&nbsp;? Si la réponse est «&nbsp;je ne sais pas trop&nbsp;», le visuel est trop chargé.</p>
          <p>Un QR code, en particulier, n'a aucun sens sur un support mobile&nbsp;: personne ne scanne un code sur un véhicule en mouvement.</p>

          <h2>Règle 2 — Du contraste et de la graisse</h2>
          <p>Les typographies fines disparaissent en mouvement. Les nuances proches — gris clair sur blanc, bleu marine sur noir — se confondent dès que la distance augmente ou que la lumière ambiante change.</p>
          <p>Ce qui fonctionne&nbsp;:</p>
          <ul>
            <li>Des caractères gras ou extra-gras, jamais en dessous d'une graisse medium.</li>
            <li>Un contraste franc entre le texte et le fond. Blanc sur couleur saturée, ou couleur saturée sur blanc.</li>
            <li>Peu de mots, en gros. Mieux vaut quatre mots lisibles que douze mots illisibles.</li>
          </ul>
          <p>Ce qui échoue&nbsp;: le texte posé sur une photo chargée, les dégradés derrière du texte, les ombres portées censées «&nbsp;détacher&nbsp;» un texte d'un fond trop proche.</p>

          <h2>Règle 3 — Laissez respirer le bas de l'image</h2>
          <p>Selon l'angle de vue, le bord inférieur de l'écran peut être partiellement masqué&nbsp;: par le rebord du dispositif, par un véhicule devant, ou simplement parce que le regard du piéton arrive de biais et par le haut.</p>
          <p>Conséquence pratique&nbsp;: ne placez rien d'essentiel dans la bande basse. Ni le nom de la marque, ni l'information clé, ni l'appel à l'action. Cette zone doit rester du décor.</p>

          <h2>Règle 4 — Le logo, tout le temps</h2>
          <p>Un visuel mémorisé sans marque associée est un visuel perdu. Le logo doit être présent et lisible sur toute la durée de diffusion, pas seulement à la fin d'une animation.</p>
          <p>C'est particulièrement important en vidéo&nbsp;: si votre logo n'apparaît qu'au dernier plan, la majorité des personnes qui auront vu l'écran ne l'auront pas vu. Elles auront croisé le taxi pendant deux secondes, au milieu de votre séquence.</p>

          <h2>Image fixe ou vidéo&nbsp;?</h2>
          <p>Les deux sont acceptés. Le choix dépend de votre message.</p>
          <p><strong>L'image fixe</strong> est souvent le meilleur choix, et c'est contre-intuitif. Elle garantit que tout le monde voit la totalité du message, quel que soit le moment où le regard se pose. Pour une campagne de notoriété avec un message simple, c'est difficile à battre.</p>
          <p><strong>La vidéo</strong> a du sens quand le mouvement sert le message&nbsp;: un produit qui se transforme, une progression, une révélation courte. Deux précautions&nbsp;: gardez le logo à l'écran en permanence, et construisez la séquence pour qu'un extrait de deux secondes soit compréhensible seul.</p>
          <p>Dans tous les cas, la diffusion se fait sans son. Aucun élément de votre message ne doit dépendre d'une bande audio.</p>

          <h2>Les contraintes techniques</h2>
          <p>Les fichiers acceptés sont JPG, PNG et MP4. La résolution, le rapport d'image, la durée maximale et le poids maximal figurent sur la page <a class="link-inline" href="/formats.html">Formats &amp; spécifications</a>. Respectez-les à la livraison&nbsp;: un fichier non conforme devra être retravaillé, et cela décale la mise en diffusion.</p>

          <h2>La checklist avant envoi</h2>
          <ul>
            <li>Mon visuel porte-t-il un seul message&nbsp;?</li>
            <li>Est-il lisible si je le regarde deux secondes&nbsp;?</li>
            <li>Les caractères sont-ils assez gras et contrastés&nbsp;?</li>
            <li>La bande basse est-elle libre d'information essentielle&nbsp;?</li>
            <li>Mon logo est-il visible en permanence&nbsp;?</li>
            <li>S'il s'agit d'une vidéo&nbsp;: un extrait de deux secondes reste-t-il compréhensible&nbsp;?</li>
            <li>Le fichier respecte-t-il le format, la durée et le poids indiqués&nbsp;?</li>
            <li>Ai-je les droits sur tous les éléments utilisés — images, polices, musiques, visages&nbsp;?</li>
          </ul>

          <p>Si vous voulez un avis avant de lancer la production, envoyez-nous une maquette. Nous vérifions la lisibilité et la conformité, et nous vous disons franchement ce qui risque de ne pas passer.</p>
""",
    related=[0, 2]))


# ============================================================ article 3
write(POSTS[2]['slug'], article_page(
    POSTS[2],
    "Ouverture de point de vente, lancement produit, date unique : comment caler une campagne d'affichage mobile sur un temps fort, avant, pendant et après.",
    "Un événement a une date. Un média mobile a l'avantage de pouvoir se caler dessus précisément, et de changer de message en cours de route. Voici comment structurer une campagne autour d'un temps fort.",
    """          <h2>Pourquoi le mobile convient à un temps fort</h2>
          <p>Un événement pose un problème classique en affichage&nbsp;: le message doit évoluer. Avant, il faut créer l'attente. Le jour même, il faut rappeler l'information pratique. Après, il faut prolonger ou remercier. Avec un support imprimé, chaque changement implique une réimpression et une repose.</p>
          <p>Un écran numérique règle cette contrainte. Le visuel est un fichier&nbsp;: on le remplace en cours de campagne, sans frais supplémentaires et dans un délai court. C'est ce qui rend ce média particulièrement adapté aux campagnes à phases.</p>

          <h2>Caler la période</h2>
          <p>Trois fenêtres sont à considérer, et elles ne servent pas la même chose.</p>

          <h3>Avant — créer l'attente</h3>
          <p>C'est la phase la plus rentable en termes d'attention. Le public ne sait pas encore, donc le message a une valeur d'information. Un visuel simple&nbsp;: la marque, la promesse, la date. Rien d'autre.</p>
          <p>La durée dépend de la nature de l'événement. Pour une ouverture de point de vente, une phase d'attente plus longue construit la curiosité locale. Pour un lancement produit ponctuel, une fenêtre courte et dense fonctionne mieux.</p>

          <h3>Pendant — rappeler</h3>
          <p>Le jour J ou la semaine de l'événement, le message change de nature&nbsp;: il devient un rappel pratique. «&nbsp;C'est aujourd'hui&nbsp;», «&nbsp;jusqu'à dimanche&nbsp;», le lieu. C'est là que la mobilité du support joue à plein&nbsp;: les taxis circulent dans les zones où se trouve votre public au moment où il peut encore agir.</p>

          <h3>Après — prolonger</h3>
          <p>Phase souvent négligée, parfois utile. Un message de continuité — «&nbsp;désormais ouvert&nbsp;», «&nbsp;disponible en boutique&nbsp;» — transforme un temps fort en présence durable. À arbitrer selon votre objectif&nbsp;: tous les événements ne méritent pas une phase d'après.</p>

          <h2>La mécanique teaser puis révélation</h2>
          <p>C'est le schéma qui exploite le mieux la possibilité de changer de visuel. Le principe&nbsp;: une première phase intrigue sans tout dire, une seconde phase révèle.</p>
          <p>Deux conditions pour que ça marche&nbsp;:</p>
          <ul>
            <li><strong>Le teaser doit rester attribuable.</strong> Un visuel mystérieux sans logo ne construit rien&nbsp;: le public ne saura pas à qui rattacher l'intrigue, et la révélation ne bénéficiera pas de l'attente créée. Gardez votre marque visible, même en phase teaser.</li>
            <li><strong>L'écart entre les deux phases doit être court.</strong> Si la révélation arrive trois semaines après le teaser, l'effet est perdu. Le public croise votre écran de manière diffuse, pas quotidiennement.</li>
          </ul>

          <h2>Ce qu'il faut préparer en amont</h2>
          <p>Une campagne à phases demande un peu plus d'organisation qu'une campagne à visuel unique. Pour éviter les décalages&nbsp;:</p>
          <ul>
            <li><strong>Produisez tous les visuels avant le début de la campagne.</strong> Ne comptez pas sur la phase 1 pour finaliser la phase 2 — c'est le meilleur moyen de rater une date.</li>
            <li><strong>Faites-les vérifier ensemble.</strong> Nous contrôlons la lisibilité et la conformité de chaque visuel. Autant traiter l'ensemble en une fois.</li>
            <li><strong>Fixez les dates de bascule à l'avance.</strong> Indiquez-nous à quelle date chaque visuel doit prendre le relais&nbsp;; nous programmons le changement.</li>
            <li><strong>Gardez une version de secours.</strong> Un événement peut être reporté. Un visuel neutre, sans date, permet de continuer à diffuser sans annoncer une information devenue fausse.</li>
          </ul>

          <h2>Les délais à connaître</h2>
          <p>Le délai standard entre la confirmation d'une campagne et sa mise en diffusion est de <span class="todo">À COMPLÉTER — délai de mise en diffusion</span>, sous réserve de la conformité des visuels. Pour une campagne calée sur une date fixe, prévoyez une marge&nbsp;: c'est ce qui vous protège d'un aller-retour sur un fichier non conforme.</p>
          <p>Les changements de visuel en cours de campagne sont mis en ligne dans un délai plus court, mais mieux vaut les annoncer à l'avance que la veille.</p>

          <h2>Et la mesure&nbsp;?</h2>
          <p>À la fin, vous recevez un récapitulatif avec la période de diffusion effective de chaque phase, le volume diffusé sur l'ensemble de la flotte et les zones parcourues. Pour une campagne à phases, cela permet de voir ce que chaque séquence a représenté en volume.</p>
          <p>Ce que ce document ne vous dira pas, c'est combien de personnes sont venues à votre événement grâce à l'affichage. Aucun support d'affichage ne peut l'établir seul. Si l'attribution vous importe, prévoyez un mécanisme de votre côté — un code, une question à l'accueil, une page dédiée.</p>

          <p>Pour caler une campagne sur une date précise, écrivez-nous en amont avec l'événement, la date et les zones qui vous intéressent. Nous revenons avec une proposition de diffusion structurée par phases.</p>
""",
    related=[0, 1]))


# ============================================================ mentions légales
write("mentions-legales.html",
      head("Mentions légales — SpotScreens",
           "Mentions légales du site SpotScreens : éditeur, directeur de publication, hébergeur, propriété intellectuelle.",
           "mentions-legales.html", noindex=True)
      + header()
      + """
  <section class="section">
    <div class="container">
      <article class="legal">
        <h1>Mentions légales</h1>

        <h2>Éditeur du site</h2>
        <p>Le site <strong>spotscreens.com</strong> est édité par&nbsp;:</p>
        <ul>
          <li>Raison sociale&nbsp;: <span class="todo">À COMPLÉTER — raison sociale</span></li>
          <li>Forme juridique&nbsp;: <span class="todo">À COMPLÉTER</span></li>
          <li>Siège social&nbsp;: <span class="todo">À COMPLÉTER — adresse du siège (mention légale obligatoire)</span></li>
          <li>Matricule fiscal&nbsp;: <span class="todo">À COMPLÉTER — identifiant fiscal</span></li>
          <li>Registre du commerce&nbsp;: <span class="todo">À COMPLÉTER</span></li>
          <li>Email&nbsp;: <a href="mailto:contactspotscreens@gmail.com">contactspotscreens@gmail.com</a></li>
          <li>Téléphone&nbsp;: <a href="tel:+21622249917">+216&nbsp;22&nbsp;249&nbsp;917</a></li>
        </ul>

        <h2>Directeur de la publication</h2>
        <p><span class="todo">À COMPLÉTER — nom du directeur de publication</span></p>

        <h2>Hébergement</h2>
        <p>Le site est hébergé par <strong>GitHub, Inc.</strong>, 88 Colin P Kelly Jr Street, San Francisco, CA 94107, États-Unis — <a class="link-inline" href="https://github.com" rel="noopener">github.com</a>.</p>

        <h2>Propriété intellectuelle</h2>
        <p>L'ensemble des contenus présents sur ce site — textes, images, éléments graphiques, logo, marque, mise en page — sont la propriété exclusive de l'éditeur, sauf mention contraire, et sont protégés par les législations tunisiennes et internationales relatives à la propriété intellectuelle.</p>
        <p>Toute reproduction, représentation, modification, publication ou adaptation, totale ou partielle, sans autorisation écrite préalable, est interdite et constitue une contrefaçon.</p>

        <h2>Responsabilité</h2>
        <p>L'éditeur s'efforce de fournir sur ce site des informations à jour et exactes, mais ne saurait garantir l'exactitude, la complétude ou l'actualité des informations diffusées. L'utilisateur reconnaît utiliser ces informations sous sa responsabilité exclusive.</p>

        <h2>Contact</h2>
        <p>Pour toute question relative aux présentes mentions légales, écrivez-nous à <a class="link-inline" href="mailto:contactspotscreens@gmail.com">contactspotscreens@gmail.com</a>.</p>

        <p class="legal__updated">Dernière mise à jour&nbsp;: <span class="todo">À COMPLÉTER — date</span>.</p>
      </article>
    </div>
  </section>
""" + GIT + FOOTER)


# ============================================================ confidentialité
write("confidentialite.html",
      head("Politique de confidentialité — SpotScreens",
           "Politique de confidentialité du site SpotScreens : données collectées, finalités, durée de conservation, droits des personnes, contact.",
           "confidentialite.html", noindex=True)
      + header()
      + """
  <section class="section">
    <div class="container">
      <article class="legal">
        <h1>Politique de confidentialité</h1>

        <p>La présente politique décrit la manière dont SpotScreens collecte, utilise et protège les données personnelles que vous nous communiquez via le site <strong>spotscreens.com</strong>.</p>

        <h2>Données que nous collectons</h2>
        <p>Nous collectons uniquement les données que vous nous transmettez volontairement via l'un des formulaires du site&nbsp;:</p>
        <ul>
          <li>Nom complet</li>
          <li>Adresse email</li>
          <li>Numéro de téléphone</li>
          <li>Société (facultatif)</li>
          <li>Sujet et message</li>
          <li>Zone de circulation (formulaire chauffeur uniquement)</li>
        </ul>
        <p>Aucune donnée n'est collectée à votre insu. Le site n'utilise ni cookie de suivi, ni outil de mesure d'audience, ni traceur publicitaire.</p>

        <h2>Finalité du traitement</h2>
        <p>Vos données sont utilisées exclusivement pour&nbsp;:</p>
        <ul>
          <li>répondre à votre demande et vous rappeler si nécessaire&nbsp;;</li>
          <li>établir une proposition de campagne, si votre message le concerne&nbsp;;</li>
          <li>organiser un entretien, dans le cas d'une candidature de chauffeur partenaire.</li>
        </ul>

        <h2>Base légale</h2>
        <p>Le traitement repose sur votre consentement, exprimé par l'envoi volontaire du formulaire, ainsi que sur notre intérêt légitime à répondre à une sollicitation que vous nous avez adressée.</p>

        <h2>Destinataires</h2>
        <p>Vos données sont reçues et traitées uniquement par l'équipe SpotScreens. Elles ne sont ni vendues, ni louées, ni cédées à des tiers à des fins commerciales.</p>
        <p>Le traitement du formulaire transite techniquement par le service <strong>Web3Forms</strong>, qui joue le rôle de relais entre le site et notre boîte email. Ce prestataire n'utilise pas vos données à d'autres fins que la transmission du message.</p>

        <h2>Durée de conservation</h2>
        <p>Les messages reçus sont conservés le temps nécessaire au suivi de votre demande, et au maximum <span class="todo">À COMPLÉTER — durée, par exemple 24 mois</span> après le dernier échange, sauf obligation légale contraire.</p>

        <h2>Vos droits</h2>
        <p>Conformément à la réglementation applicable en Tunisie sur la protection des données à caractère personnel, vous disposez d'un droit&nbsp;:</p>
        <ul>
          <li>d'accès à vos données&nbsp;;</li>
          <li>de rectification des données inexactes&nbsp;;</li>
          <li>de suppression de vos données&nbsp;;</li>
          <li>d'opposition au traitement&nbsp;;</li>
          <li>de retrait de votre consentement à tout moment.</li>
        </ul>
        <p>Pour exercer ces droits, écrivez-nous à <a class="link-inline" href="mailto:contactspotscreens@gmail.com">contactspotscreens@gmail.com</a>.</p>

        <h2>Sécurité</h2>
        <p>Nous prenons les mesures raisonnables pour protéger vos données contre tout accès non autorisé, altération ou divulgation. Aucun système n'étant infaillible, nous vous invitons à ne pas transmettre par formulaire d'informations sensibles non indispensables.</p>

        <h2>Cookies et ressources externes</h2>
        <p>Le site n'utilise aucun cookie non essentiel et ne charge aucun script tiers de suivi. Les seules ressources externes sont les polices d'écriture (Google Fonts) et le service de traitement de formulaire, ce dernier étant sollicité uniquement lorsque vous soumettez un formulaire.</p>

        <h2>Contact</h2>
        <p>Pour toute question sur la présente politique&nbsp;: <a class="link-inline" href="mailto:contactspotscreens@gmail.com">contactspotscreens@gmail.com</a>.</p>

        <p class="legal__updated">Dernière mise à jour&nbsp;: <span class="todo">À COMPLÉTER — date</span>.</p>
      </article>
    </div>
  </section>
""" + GIT + FOOTER)


# ============================================================ CGV
write("cgv.html",
      head("Conditions générales — SpotScreens",
           "Conditions générales de diffusion SpotScreens : fourniture du visuel, conformité, droits sur les éléments transmis, report en cas d'immobilisation d'un véhicule.",
           "cgv.html", noindex=True)
      + header()
      + """
  <section class="section">
    <div class="container">
      <article class="legal">
        <h1>Conditions générales</h1>

        <p>Les présentes conditions générales encadrent la relation entre SpotScreens et l'annonceur (ci-après <em>le Client</em>) qui confie à SpotScreens la diffusion d'un visuel publicitaire sur son réseau d'écrans LED installés sur le toit de taxis, dans le Grand Tunis.</p>

        <h2>1. Objet</h2>
        <p>Les présentes conditions définissent les modalités de la prestation de diffusion. Elles s'appliquent à toute campagne confirmée par écrit entre SpotScreens et le Client, sur la base d'une proposition de diffusion transmise par SpotScreens.</p>

        <h2>2. Fourniture du visuel</h2>
        <p>Le Client transmet à SpotScreens un visuel image ou vidéo respectant les caractéristiques techniques indiquées sur la page <a class="link-inline" href="/formats.html">Formats &amp; spécifications</a>. Le Client est responsable de la conformité technique du fichier fourni.</p>
        <p>Le visuel doit être remis dans un délai raisonnable permettant sa vérification et sa mise en diffusion à la date convenue.</p>

        <h2>3. Vérification et conformité</h2>
        <p>Avant la mise en diffusion, SpotScreens procède à une vérification portant sur&nbsp;:</p>
        <ul>
          <li>la lisibilité du visuel une fois affiché sur écran mobile&nbsp;;</li>
          <li>la conformité au format technique&nbsp;;</li>
          <li>la conformité à la réglementation publicitaire applicable en Tunisie.</li>
        </ul>
        <p>SpotScreens se réserve le droit de refuser tout visuel non conforme, contraire aux bonnes mœurs, à l'ordre public, ou de nature à porter atteinte à un tiers. Un ajustement peut être proposé au Client.</p>

        <h2>4. Droits sur les éléments transmis</h2>
        <p>Le Client déclare et garantit détenir l'ensemble des droits nécessaires — droits d'auteur, droits à l'image, droits sur les marques, autorisations éventuelles — pour la diffusion des éléments qu'il transmet à SpotScreens.</p>
        <p>Le Client garantit SpotScreens contre toute réclamation d'un tiers relative à la propriété intellectuelle ou aux droits de la personnalité liés aux éléments diffusés.</p>
        <p>SpotScreens n'acquiert aucun droit sur le visuel autre que celui de le diffuser sur son réseau, pendant la durée convenue.</p>

        <h2>5. Diffusion</h2>
        <p>La diffusion est assurée sur l'ensemble des taxis équipés du parc SpotScreens, dans le Grand Tunis, aux dates convenues et sur l'amplitude horaire de 7&nbsp;h à 23&nbsp;h.</p>
        <p>Le Client peut demander à changer de visuel en cours de campagne. Le nouveau visuel doit respecter les mêmes exigences de conformité.</p>

        <h2>6. Immobilisation d'un véhicule</h2>
        <p>Si un ou plusieurs véhicules du parc sont ponctuellement immobilisés pendant la campagne — entretien, incident, jour sans course — les diffusions manquantes sont reportées sur les autres véhicules du parc pendant la campagne, ou en prolongation à la fin, de manière à honorer le volume de diffusion prévu dans la proposition.</p>

        <h2>7. Suivi et récapitulatif</h2>
        <p>À la fin de la campagne, SpotScreens remet au Client un récapitulatif de diffusion précisant la période effective, le volume diffusé sur l'ensemble de la flotte, les zones parcourues, et incluant des captures de l'écran en diffusion.</p>

        <h2>8. Confidentialité</h2>
        <p>Chacune des parties s'engage à conserver la confidentialité des informations échangées dans le cadre de la campagne — brief, éléments techniques, données de diffusion — et à ne pas les divulguer à des tiers sans accord préalable.</p>

        <h2>9. Force majeure</h2>
        <p>Aucune des parties ne pourra être tenue responsable d'un manquement causé par un cas de force majeure au sens de la législation applicable, notamment&nbsp;: événement climatique majeur, indisponibilité générale des réseaux de télécommunication, décision d'une autorité publique restreignant la circulation.</p>

        <h2>10. Droit applicable</h2>
        <p>Les présentes conditions sont soumises au droit tunisien. Tout litige relatif à leur exécution ou à leur interprétation sera soumis aux tribunaux compétents de <span class="todo">À COMPLÉTER — juridiction</span>, après tentative préalable de règlement amiable.</p>

        <p class="legal__updated">Dernière mise à jour&nbsp;: <span class="todo">À COMPLÉTER — date</span>.</p>
      </article>
    </div>
  </section>
""" + GIT + FOOTER)

print("done")
