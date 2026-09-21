#!/usr/bin/env python3
# Générateur one-shot : écrit les pages statiques avec header/footer identiques.
# Outil d'écriture uniquement — le site livré est du HTML statique pur.

import os, re

SITE = "https://spotscreens.com"
OUT = os.path.dirname(os.path.abspath(__file__))

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">'


def head(title, desc, path, noindex=False, og_title=None, og_desc=None):
    canon = f"{SITE}/{path}" if path else f"{SITE}/"
    robots = '\n<meta name="robots" content="noindex">' if noindex else ""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">{robots}
<meta name="theme-color" content="#062052">

<meta property="og:type" content="website">
<meta property="og:site_name" content="SpotScreens">
<meta property="og:title" content="{og_title or title}">
<meta property="og:description" content="{og_desc or desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/og-cover.jpg">
<meta property="og:locale" content="fr_TN">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="/assets/logo/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONTS}
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>

<a class="skip" href="#main">Aller au contenu</a>
"""


def header(active="", sub=""):
    def cur(key):
        return ' aria-current="page"' if active == key else ""

    def scur(key):
        return ' aria-current="page"' if sub == key else ""

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
          <a class="nav__link" href="/ecrans-taxi.html"{cur('reseau')}>Le réseau <span class="nav__caret" aria-hidden="true"></span></a>
          <ul class="nav__submenu">
            <li><a href="/ecrans-taxi.html"{scur('ecrans')}>Les écrans taxi</a></li>
            <li><a href="/formats.html"{scur('formats')}>Formats &amp; spécifications</a></li>
            <li><a href="/couverture.html"{scur('couverture')}>Couverture</a></li>
            <li><a href="/mesure.html"{scur('mesure')}>Mesure &amp; suivi</a></li>
          </ul>
        </li>
        <li class="nav__item"><a class="nav__link" href="/campagne.html"{cur('campagnes')}>Campagnes</a></li>
        <li class="nav__item"><a class="nav__link" href="/agences.html"{cur('annonceurs')}>Annonceurs</a></li>
        <li class="nav__item"><a class="nav__link" href="/chauffeurs.html"{cur('chauffeurs')}>Chauffeurs</a></li>
        <li class="nav__item nav__item--has-menu">
          <a class="nav__link" href="/a-propos.html"{cur('apropos')}>À propos <span class="nav__caret" aria-hidden="true"></span></a>
          <ul class="nav__submenu">
            <li><a href="/a-propos.html"{scur('apropos')}>Qui nous sommes</a></li>
            <li><a href="/blog.html"{scur('blog')}>Blog</a></li>
            <li><a href="/faq.html"{scur('faq')}>Questions fréquentes</a></li>
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

GIT_PHONE = """
  <section class="get-in-touch">
    <div class="container">
      <h2 class="get-in-touch__title">Appelez-nous.</h2>
      <p>Une question urgente&nbsp;? Le téléphone reste le plus rapide.</p>
      <div class="btn-row btn-row--center">
        <a class="btn btn--primary" href="tel:+21622249917">+216&nbsp;22&nbsp;249&nbsp;917</a>
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


def hero(kicker, title, photo, text=""):
    t = f'\n      <p class="hero__text">{text}</p>' if text else ""
    return f"""
  <section class="hero hero--interior">
    <div class="hero__media" aria-hidden="true">
      <span class="ph"><span>{photo}</span></span>
    </div>
    <div class="container hero__inner">
      <span class="kicker kicker--light">{kicker}</span>
      <h1 class="hero__title">{title}</h1>{t}
    </div>
  </section>
"""


def write(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name)


# ============================================================ ecrans-taxi
write("ecrans-taxi.html",
      head("Écrans LED sur taxis à Tunis — Le réseau | SpotScreens",
           "Un écran LED double face installé sur le toit du taxi, alimenté par le véhicule, piloté à distance. Un média mobile qui traverse le Grand Tunis toute la journée.",
           "ecrans-taxi.html")
      + header("reseau", "ecrans")
      + hero("Le réseau", "Des écrans LED qui traversent la ville.",
             "Photo&nbsp;#3 — Gros plan de l'écran allumé avec une publicité lisible")
      + """
  <section class="section">
    <div class="container">
      <div class="split split--text-wide">
        <div>
          <span class="kicker">Ce qu'est le dispositif</span>
          <h2 class="sh__title" style="font-size:clamp(26px,3.4vw,40px)">Un écran LED double face, monté sur le toit.</h2>
          <div class="prose mt-m">
            <p>L'écran est alimenté par le véhicule et piloté à distance. Le visuel est envoyé au parc depuis notre système&nbsp;; aucune intervention du chauffeur n'est nécessaire pour lancer ou modifier une diffusion.</p>
            <p>Chaque face diffuse le même visuel, afin que la lecture soit possible aussi bien pour un piéton sur le trottoir que pour un automobiliste placé derrière le taxi.</p>
            <p>La diffusion est assurée de 7&nbsp;h à 23&nbsp;h, tant que le véhicule est en circulation.</p>
          </div>
        </div>
        <div class="split__media">
          <figure class="frame frame--square" aria-hidden="true">
            <span class="ph"><span>Photo&nbsp;#4 — Détail du montage sur le toit</span></span>
          </figure>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--blue">
    <div class="container">
      <div class="sh">
        <span class="kicker">Pourquoi le toit d'un taxi</span>
        <h2 class="sh__title">Trois raisons qui font la différence.</h2>
      </div>
      <div class="features">
        <article class="feature">
          <h4>À hauteur de regard</h4>
          <p>Le toit place l'écran juste au-dessus du flux&nbsp;: piétons sur le trottoir, automobilistes en carrefour, terrasses en soirée. Le message arrive dans le champ de vision naturel, sans qu'on ait à lever la tête.</p>
        </article>
        <article class="feature">
          <h4>Dans le flux, pas en bord de route</h4>
          <p>Un panneau attend que la ville passe devant lui. Un taxi entre dans le flux et va chercher le public là où il se trouve, en changeant de quartier plusieurs fois par jour.</p>
        </article>
        <article class="feature">
          <h4>Une répétition naturelle</h4>
          <p>Sur un même trajet, un piéton croise plusieurs taxis équipés, parfois le même une seconde fois. La répétition d'exposition se construit sans média-planning complexe.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="sh">
        <span class="kicker">Galerie</span>
        <h2 class="sh__title">Le dispositif en situation.</h2>
      </div>
      <div class="gallery">
        <figure>
          <div class="frame frame--16-9" aria-hidden="true"><span class="ph"><span>Photo&nbsp;#1 — Taxi de nuit, écran allumé</span></span></div>
          <figcaption>De nuit, l'écran reste lisible dans les avenues éclairées.</figcaption>
        </figure>
        <figure>
          <div class="frame frame--16-9" aria-hidden="true"><span class="ph"><span>Photo&nbsp;#2 — Taxi de jour dans la circulation</span></span></div>
          <figcaption>De jour, la haute luminosité maintient la lecture en plein soleil.</figcaption>
        </figure>
        <figure>
          <div class="frame frame--16-9" aria-hidden="true"><span class="ph"><span>Photo&nbsp;#4 — Détail du montage</span></span></div>
          <figcaption>Un montage discret, pensé pour ne pas gêner le chauffeur.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="section section--dark">
    <div class="container">
      <div class="sh">
        <span class="kicker kicker--light">Le parc</span>
        <h2 class="sh__title sh__title--light">Un réseau qui circule chaque jour.</h2>
        <p class="sh__intro sh__intro--light">Nos taxis équipés circulent quotidiennement dans le Grand Tunis, avec une diffusion assurée de 7&nbsp;h à 23&nbsp;h. Le parc s'étoffe régulièrement à mesure que de nouveaux chauffeurs partenaires rejoignent le réseau.</p>
        <p class="sh__intro sh__intro--light">Les taxis ne suivent pas de trajet imposé&nbsp;: ils circulent au gré des courses. Votre visuel rencontre ainsi, dans une même journée, des publics et des zones successifs.</p>
      </div>
      <div class="btn-row">
        <a class="btn btn--light" href="/couverture.html">Voir la couverture</a>
        <a class="btn btn--ghost-light" href="/formats.html">Formats &amp; spécifications</a>
      </div>
    </div>
  </section>
""" + GIT + FOOTER)


# ============================================================ formats
write("formats.html",
      head("Formats et spécifications techniques — écran LED taxi | SpotScreens",
           "Formats acceptés, résolution, rapport d'image, poids maximal et recommandations de création pour vos visuels diffusés sur les écrans LED de taxis SpotScreens.",
           "formats.html")
      + header("reseau", "formats")
      + hero("Fiche technique", "Formats &amp; spécifications.",
             "Photo&nbsp;#3 — Écran affichant un visuel net",
             "Toutes les caractéristiques utiles à un graphiste ou à une agence pour préparer un visuel destiné à la diffusion.")
      + """
  <section class="section">
    <div class="container">
      <div class="sh">
        <h2 class="sh__title" style="font-size:clamp(24px,3vw,34px)">Caractéristiques techniques</h2>
      </div>
      <table class="spec-table">
        <tbody>
          <tr><th scope="row">Types de fichiers acceptés</th><td>JPG, PNG, MP4</td></tr>
          <tr><th scope="row">Résolution recommandée</th><td><span class="todo">À COMPLÉTER — résolution native de la dalle</span></td></tr>
          <tr><th scope="row">Rapport d'image</th><td><span class="todo">À COMPLÉTER — rapport d'image de la dalle</span></td></tr>
          <tr><th scope="row">Durée maximale d'une vidéo</th><td><span class="todo">À COMPLÉTER — durée max</span></td></tr>
          <tr><th scope="row">Poids maximal du fichier</th><td><span class="todo">À COMPLÉTER — poids max</span></td></tr>
          <tr><th scope="row">Espace colorimétrique</th><td><span class="todo">À COMPLÉTER — sRGB ou autre</span></td></tr>
          <tr><th scope="row">Fréquence d'images (vidéo)</th><td><span class="todo">À COMPLÉTER — 25 ou 30 fps</span></td></tr>
          <tr><th scope="row">Son</th><td>Non applicable — les écrans diffusent sans son.</td></tr>
        </tbody>
      </table>
      <p class="small mt-m">Ces valeurs seront confirmées avec les caractéristiques réelles des dalles avant la mise en ligne du site.</p>
    </div>
  </section>

  <section class="section section--blue">
    <div class="container">
      <div class="sh">
        <span class="kicker">Recommandations de création</span>
        <h2 class="sh__title">Quatre principes pour un visuel qui fonctionne.</h2>
      </div>
      <div class="cards cards--2">
        <article class="card">
          <span class="card__num">01</span>
          <h3>Un message unique par visuel</h3>
          <p>Un écran mobile n'a que quelques secondes pour être lu. Une seule idée, un seul appel. Tout ce qui s'ajoute réduit ce qui sera retenu.</p>
        </article>
        <article class="card">
          <span class="card__num">02</span>
          <h3>Caractères épais, fort contraste</h3>
          <p>Privilégiez des typographies grasses et un contraste élevé entre le texte et le fond. Les traits fins et les nuances proches disparaissent en mouvement.</p>
        </article>
        <article class="card">
          <span class="card__num">03</span>
          <h3>Pas de texte en bas de l'image</h3>
          <p>Le bord inférieur peut être partiellement masqué selon l'angle de lecture. Gardez les informations essentielles dans la partie centrale et haute.</p>
        </article>
        <article class="card">
          <span class="card__num">04</span>
          <h3>Logo visible en permanence</h3>
          <p>Image fixe ou vidéo, votre logo doit rester visible sur toute la durée de diffusion. Un visuel mémorisé sans marque associée est un visuel perdu.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="sh">
        <span class="kicker">Vérifications</span>
        <h2 class="sh__title">Ce que nous vérifions avant diffusion.</h2>
      </div>
      <div class="features">
        <article class="feature">
          <h4>Lisibilité</h4>
          <p>Contraste, taille des caractères, densité d'information&nbsp;: le visuel doit rester lisible à distance et en mouvement.</p>
        </article>
        <article class="feature">
          <h4>Conformité au format</h4>
          <p>Résolution, rapport d'image, encodage. Si un ajustement est nécessaire, nous vous le signalons immédiatement.</p>
        </article>
        <article class="feature">
          <h4>Conformité réglementaire</h4>
          <p>Le visuel doit respecter la réglementation publicitaire applicable en Tunisie.</p>
        </article>
      </div>
      <div class="btn-row">
        <a class="btn btn--primary" href="/contact.html">Envoyer un visuel pour vérification</a>
        <a class="btn btn--outline" href="/blog-concevoir-visuel-led.html">Lire le guide de création</a>
      </div>
    </div>
  </section>
""" + GIT + FOOTER)


# ============================================================ campagne
write("campagne.html",
      head("Déroulé d'une campagne publicitaire taxi | SpotScreens",
           "Comment se déroule une campagne sur écrans LED de taxis à Tunis : brief, proposition, transmission du visuel, diffusion, changement de visuel en cours de route.",
           "campagne.html")
      + header("campagnes")
      + hero("Une campagne, étape par étape", "Le déroulé d'une campagne.",
             "Photo&nbsp;#9 — Écran affichant deux publicités différentes",
             "De la première prise de contact à la remise du récapitulatif.")
      + """
  <section class="section">
    <div class="container">
      <div class="page-toc">
        <aside class="toc" aria-label="Sommaire">
          <h5>Sommaire</h5>
          <ul>
            <li><a href="#brief">1. Votre brief</a></li>
            <li><a href="#proposition">2. Notre proposition</a></li>
            <li><a href="#visuel">3. Votre visuel</a></li>
            <li><a href="#diffusion">4. La diffusion</a></li>
            <li><a href="#delais">Les délais</a></li>
            <li><a href="#changement">Changer de visuel</a></li>
            <li><a href="#immobilisation">Véhicule immobilisé</a></li>
            <li><a href="#fin">Fin de campagne</a></li>
          </ul>
        </aside>

        <div class="toc-body">
          <h2 id="brief">1. Votre brief</h2>
          <p>Vous nous transmettez, en quelques lignes ou par téléphone, les éléments qui cadrent votre campagne&nbsp;: l'objectif visé, la période souhaitée, le public cible, et vos zones d'intérêt le cas échéant. Un visuel de référence ou un lien vers votre univers de marque suffit à démarrer&nbsp;; nous n'avons pas besoin d'un cahier des charges complet à ce stade.</p>
          <p>Si vous êtes une agence, précisez à quel nom la proposition doit être établie et qui sera l'interlocuteur pour le suivi.</p>

          <h2 id="proposition">2. Notre proposition</h2>
          <p>Nous vous adressons une proposition de diffusion qui précise la période, la durée, le volume de diffusion estimé sur l'ensemble de la flotte et les modalités techniques. Elle tient sur une page et se lit en quelques minutes.</p>
          <p>Vous nous confirmez, nous bloquons les créneaux. La confirmation vaut engagement de diffusion sur la période convenue.</p>

          <h2 id="visuel">3. Votre visuel</h2>
          <p>Vous nous transmettez un visuel image ou vidéo, conforme aux formats indiqués sur la page <a class="link-inline" href="/formats.html">Formats &amp; spécifications</a>. Nous vérifions la lisibilité, la conformité au format et la conformité à la réglementation publicitaire avant la mise en diffusion.</p>
          <p>Si un ajustement est nécessaire, nous vous le signalons immédiatement afin de ne pas retarder le lancement.</p>

          <h2 id="diffusion">4. La diffusion</h2>
          <p>Le visuel est envoyé au parc depuis notre système. À la date convenue, il est diffusé sur l'ensemble de la flotte, de 7&nbsp;h à 23&nbsp;h. Aucune intervention du chauffeur n'est nécessaire.</p>
          <p>Pendant toute la campagne, un interlocuteur unique reste joignable pour vos questions.</p>

          <h2 id="delais">Les délais</h2>
          <p>Le délai standard entre la confirmation d'une campagne et sa mise en diffusion est de <span class="todo">À COMPLÉTER — délai de mise en diffusion</span>, sous réserve de la conformité du visuel transmis. Un délai plus court est possible sur demande, selon la période.</p>

          <h2 id="changement">Changer de visuel en cours de campagne</h2>
          <p>Le visuel est numérique. Vous pouvez le remplacer en cours de campagne&nbsp;: envoyez-nous le nouveau fichier, nous le mettons en ligne sur le parc dans un délai court, sans frais supplémentaires.</p>
          <p>C'est utile lorsqu'une campagne comporte plusieurs vagues, un teaser suivi d'une révélation, ou un message lié à une date précise.</p>

          <h2 id="immobilisation">Si un véhicule est immobilisé</h2>
          <p>Un taxi peut être ponctuellement immobilisé — entretien, incident, jour sans course. Dans ce cas, les diffusions manquantes sont reportées&nbsp;: elles sont rattrapées sur les autres véhicules du parc pendant la campagne, ou en prolongation à la fin. Le volume prévu dans votre proposition est honoré.</p>

          <h2 id="fin">Fin de campagne</h2>
          <p>À l'issue de la diffusion, vous recevez un récapitulatif reprenant la période couverte, le volume diffusé sur l'ensemble de la flotte, les zones parcourues, ainsi que des captures de l'écran en diffusion. Ce document peut être remis tel quel à votre agence ou à vos parties prenantes.</p>
          <p class="mt-m"><a class="tlink" href="/mesure.html">En savoir plus sur le suivi</a></p>
        </div>
      </div>
    </div>
  </section>
""" + GIT + FOOTER)


# ============================================================ couverture
MAP_SVG = """
        <svg class="map-svg" viewBox="0 0 800 500" role="img" xmlns="http://www.w3.org/2000/svg">
          <title>Zones de circulation dans le Grand Tunis</title>
          <path d="M 120 190 C 140 130, 220 100, 290 108 C 340 112, 380 120, 420 140 L 440 175 L 495 180 L 520 205 L 560 215 C 610 225, 650 260, 660 305 C 665 340, 640 380, 590 405 C 540 430, 460 435, 380 425 C 300 415, 220 400, 170 360 C 130 325, 105 260, 120 190 Z"
            fill="none" stroke="#1B4FD8" stroke-width="2.2" stroke-linejoin="round"/>
          <path d="M 460 220 C 500 215, 550 235, 555 265 C 555 295, 520 315, 480 310 C 445 305, 435 275, 445 245 C 448 232, 452 226, 460 220 Z"
            fill="#DCE6FF" stroke="#1B4FD8" stroke-width="1.6"/>
          <g fill="none" stroke="#1B4FD8" stroke-width="1.5" stroke-dasharray="4 6" opacity=".5">
            <path d="M 270 200 C 320 220, 350 260, 370 315"/>
            <path d="M 370 315 C 430 300, 470 280, 485 270"/>
            <path d="M 485 270 C 520 260, 560 240, 610 215"/>
            <path d="M 220 290 C 260 300, 320 315, 370 315"/>
            <path d="M 320 245 C 340 265, 360 290, 370 315"/>
          </g>
          <g fill="#1B4FD8">
            <circle cx="270" cy="200" r="6"/><circle cx="320" cy="245" r="6"/>
            <circle cx="285" cy="290" r="6"/><circle cx="220" cy="290" r="6"/>
            <circle cx="370" cy="315" r="6"/><circle cx="485" cy="270" r="6"/>
            <circle cx="545" cy="285" r="6"/><circle cx="610" cy="215" r="6"/>
          </g>
          <g font-family="Poppins,Arial,sans-serif" font-size="14" fill="#0D1424" font-weight="500">
            <text x="270" y="185" text-anchor="middle">Ariana</text>
            <text x="334" y="238" text-anchor="start">Menzah</text>
            <text x="299" y="311" text-anchor="start">El Manar</text>
            <text x="206" y="311" text-anchor="end">Bardo</text>
            <text x="370" y="337" text-anchor="middle">Tunis Centre</text>
            <text x="485" y="255" text-anchor="middle">Lac 1</text>
            <text x="545" y="307" text-anchor="middle">Lac 2</text>
            <text x="610" y="200" text-anchor="middle">La Marsa</text>
          </g>
        </svg>
"""

write("couverture.html",
      head("Couverture — écrans SpotScreens dans le Grand Tunis",
           "Où circulent les écrans SpotScreens : Tunis Centre, Lac 1 et Lac 2, La Marsa, Ariana, Bardo, Menzah, El Manar. Une couverture au gré des courses.",
           "couverture.html")
      + header("reseau", "couverture")
      + hero("Couverture", "Où circulent nos écrans.",
             "Photo&nbsp;#8 — Vue de nuit depuis le trottoir",
             "Les taxis ne suivent pas de parcours fixe : ils circulent dans le Grand Tunis au gré des courses.")
      + """
  <section class="section">
    <div class="container">
      <div class="sh">
        <span class="kicker">Grand Tunis</span>
        <h2 class="sh__title">Une couverture qui suit la ville.</h2>
        <p class="sh__intro">Parce que les trajets ne sont pas imposés, votre visuel est exposé à des publics successifs dans la même journée&nbsp;: quartiers résidentiels le matin, zones d'affaires en journée, lieux de sortie le soir.</p>
      </div>

      <figure class="map-figure" aria-label="Représentation stylisée du Grand Tunis et de ses principales zones">
""" + MAP_SVG + """
        <figcaption class="small mt-s">Représentation schématique. Les taxis circulent librement au sein de ces zones et entre elles.</figcaption>
      </figure>

      <div class="mt-l">
        <h3 style="font-size:17px;text-transform:uppercase;letter-spacing:.02em;margin-bottom:18px">Zones couvertes</h3>
        <ul class="pills">
          <li class="pill">Tunis Centre</li><li class="pill">Lac 1</li><li class="pill">Lac 2</li>
          <li class="pill">La Marsa</li><li class="pill">Ariana</li><li class="pill">Bardo</li>
          <li class="pill">Menzah</li><li class="pill">El Manar</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section section--blue">
    <div class="container">
      <div class="sh">
        <span class="kicker">Moments forts de la journée</span>
        <h2 class="sh__title">Une même journée, plusieurs publics.</h2>
      </div>
      <div class="features">
        <article class="feature">
          <h4>Le matin</h4>
          <p>Trajets domicile-travail&nbsp;: axes d'entrée dans la ville, grandes avenues, abords des zones résidentielles. Un public régulier, sur des itinéraires répétés.</p>
        </article>
        <article class="feature">
          <h4>En journée</h4>
          <p>Quartiers d'affaires, zones commerçantes, centres administratifs. Le taxi rencontre un public actif, en déplacement professionnel.</p>
        </article>
        <article class="feature">
          <h4>Le soir</h4>
          <p>Sorties, restaurants, cafés. Un public disponible visuellement, souvent à pied à proximité de l'écran, dans une ambiance où la LED ressort le mieux.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--dark">
    <div class="container">
      <div class="sh">
        <span class="kicker kicker--light">Au-delà de Tunis</span>
        <h2 class="sh__title sh__title--light">Extension du réseau prévue.</h2>
        <p class="sh__intro sh__intro--light">Une extension à d'autres villes est prévue. Écrivez-nous si votre campagne cible une ville en dehors du Grand Tunis, nous vous dirons où nous en sommes.</p>
      </div>
      <div class="btn-row">
        <a class="btn btn--light" href="/contact.html">Nous écrire</a>
      </div>
    </div>
  </section>
""" + GIT + FOOTER)


# ============================================================ mesure
write("mesure.html",
      head("Suivi et mesure de campagne taxi LED | SpotScreens",
           "À la fin de votre campagne SpotScreens, un récapitulatif de diffusion vous est remis : période couverte, volume diffusé, zones parcourues. Rien n'est déclaratif.",
           "mesure.html")
      + header("reseau", "mesure")
      + hero("Mesure &amp; suivi", "Ce que vous saurez de votre campagne.",
             "Photo — Écran en diffusion pendant une campagne",
             "Un récapitulatif établi à partir des données du parc. Rien n'est déclaratif.")
      + """
  <section class="section">
    <div class="container">
      <div class="sh">
        <span class="kicker">Ce que nous suivons</span>
        <h2 class="sh__title">Trois indicateurs, tous vérifiables.</h2>
      </div>
      <div class="features">
        <article class="feature">
          <h4>La période effective</h4>
          <p>Les dates exactes pendant lesquelles votre visuel a été diffusé, jour par jour, avec l'amplitude horaire couverte.</p>
        </article>
        <article class="feature">
          <h4>Le volume de diffusion</h4>
          <p>Le nombre de diffusions cumulées sur l'ensemble de la flotte pendant la durée de la campagne.</p>
        </article>
        <article class="feature">
          <h4>Les zones parcourues</h4>
          <p>Les zones du Grand Tunis où les taxis équipés ont circulé pendant que votre visuel était en diffusion.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--blue">
    <div class="container">
      <div class="split">
        <div>
          <span class="kicker">Récapitulatif de fin de campagne</span>
          <h2 class="sh__title" style="font-size:clamp(26px,3.4vw,40px)">Un document remis en fin de diffusion.</h2>
          <div class="prose mt-m">
            <p>Vous recevez un récapitulatif reprenant la période couverte, le volume diffusé sur l'ensemble de la flotte et les zones parcourues, accompagné de captures de l'écran en diffusion.</p>
            <p>Ce document est adressé à l'interlocuteur qui a suivi votre campagne, et peut être remis tel quel à votre agence ou à vos parties prenantes.</p>
          </div>
        </div>
        <div class="split__media">
          <figure class="frame frame--16-9" aria-hidden="true">
            <span class="ph"><span>Photo — Écran en diffusion (capture)</span></span>
          </figure>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="sh">
        <span class="kicker">En cas d'imprévu</span>
        <h2 class="sh__title">Une diffusion qui s'ajuste, pas qui se perd.</h2>
        <p class="sh__intro">Si un véhicule est immobilisé — entretien, incident, jour sans course — les diffusions manquantes sont reportées sur la suite de la campagne, sur les autres véhicules du parc ou en prolongation, afin que le volume prévu soit honoré.</p>
      </div>
    </div>
  </section>

  <section class="section section--dark">
    <div class="container">
      <div class="sh">
        <span class="kicker kicker--light">Ce que nous ne mesurons pas</span>
        <h2 class="sh__title sh__title--light">Nous ne comptons pas les regards.</h2>
        <p class="sh__intro sh__intro--light">Nous ne vendons pas d'estimations d'audience invérifiables ni de projections construites à partir de coefficients de passage. Ces chiffres, lorsqu'ils sont annoncés, sont rarement reproductibles.</p>
        <p class="sh__intro sh__intro--light">Nous rendons compte de ce que nous pouvons établir&nbsp;: une durée de diffusion réelle, un volume mesuré, des zones effectivement parcourues. Un annonceur expérimenté sait ce que cela vaut.</p>
      </div>
      <div class="btn-row">
        <a class="btn btn--light" href="/contact.html">Demander une proposition</a>
      </div>
    </div>
  </section>
""" + GIT + FOOTER)


# ============================================================ agences
write("agences.html",
      head("Annonceurs &amp; agences — plan média digital mobile | SpotScreens",
           "Support digital mobile pour annonceurs et agences à Tunis : disponibilité en amont, éléments de fin de campagne, interlocuteur unique, compatibilité plan média.",
           "agences.html")
      + header("annonceurs")
      + hero("Annonceurs &amp; agences", "Un support mobile à intégrer à vos plans média.",
             "Photo&nbsp;#5 — Plusieurs taxis équipés alignés",
             "Pour les annonceurs et les agences qui cherchent à compléter leur dispositif d'affichage extérieur.")
      + """
  <section class="section">
    <div class="container">
      <div class="sh">
        <span class="kicker">Ce que nous apportons</span>
        <h2 class="sh__title">Quatre garanties de travail.</h2>
      </div>
      <div class="cards cards--2">
        <article class="card">
          <span class="card__num">01</span>
          <h3>Disponibilité et réservation en amont</h3>
          <p>Les créneaux se réservent à l'avance, pour sécuriser une période stratégique — lancement, temps fort commercial, campagne saisonnière. La réservation vaut engagement de diffusion sur la période convenue.</p>
        </article>
        <article class="card">
          <span class="card__num">02</span>
          <h3>Éléments de fin de campagne</h3>
          <p>En fin de diffusion, un récapitulatif est adressé à votre agence&nbsp;: période effective, volume diffusé sur l'ensemble de la flotte, zones parcourues, captures de l'écran en diffusion. Le tout dans un document unique.</p>
        </article>
        <article class="card">
          <span class="card__num">03</span>
          <h3>Interlocuteur unique</h3>
          <p>Un seul contact, joignable directement, du brief à la remise du récapitulatif. Pas de standard, pas de renvoi d'un service à l'autre.</p>
        </article>
        <article class="card">
          <span class="card__num">04</span>
          <h3>Compatible avec un plan média existant</h3>
          <p>Le média s'insère dans un plan classique en tant que support digital extérieur mobile. Il vient compléter l'affichage fixe, la radio ou le digital in-app, sans s'y substituer.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--blue">
    <div class="container">
      <div class="split">
        <div>
          <span class="kicker">Contact commercial</span>
          <h2 class="sh__title" style="font-size:clamp(26px,3.4vw,40px)">Un échange direct, sans intermédiaire.</h2>
          <p class="mt-m">Pour discuter d'une campagne, d'un plan média ou d'une réservation de créneau, contactez-nous par email ou par téléphone.</p>
        </div>
        <aside class="info-card" aria-label="Coordonnées commerciales">
          <h3>Nos coordonnées</h3>
          <dl>
            <div>
              <dt>Email</dt>
              <dd><a href="mailto:contactspotscreens@gmail.com">contactspotscreens@gmail.com</a></dd>
            </div>
            <div>
              <dt>Téléphone</dt>
              <dd><a href="tel:+21622249917">+216&nbsp;22&nbsp;249&nbsp;917</a></dd>
            </div>
          </dl>
          <p class="info-card__note">Vous préférez un formulaire&nbsp;? <a class="link-inline" href="/contact.html">Passer par la page contact</a>.</p>
        </aside>
      </div>
    </div>
  </section>
""" + GIT + FOOTER)


# ============================================================ chauffeurs
write("chauffeurs.html",
      head("Devenir chauffeur partenaire SpotScreens | Tunis",
           "Chauffeurs de taxi à Tunis : équipez votre toit d'un écran LED SpotScreens et percevez un revenu complémentaire chaque mois, sans rien changer à vos journées.",
           "chauffeurs.html")
      + header("chauffeurs")
      + hero("Chauffeurs partenaires", "Votre taxi peut vous rapporter plus.",
             "Photo&nbsp;#6 — Chauffeur devant son taxi équipé",
             "Sans rien changer à vos journées de travail.")
      + """
  <section class="section">
    <div class="container">
      <div class="sh">
        <span class="kicker">Comment ça marche</span>
        <h2 class="sh__title">Trois étapes, et vous êtes équipé.</h2>
      </div>
      <div class="features">
        <article class="feature">
          <h4>01 — Nous installons l'écran</h4>
          <p>Le montage est pris en charge par notre équipe technique, sans frais pour vous. L'installation est pensée pour ne pas gêner votre conduite.</p>
        </article>
        <article class="feature">
          <h4>02 — Vous travaillez normalement</h4>
          <p>L'écran est piloté à distance. Vous n'avez rien à lancer, rien à arrêter, rien à surveiller. Vos habitudes de travail ne changent pas.</p>
        </article>
        <article class="feature">
          <h4>03 — Vous percevez une rémunération</h4>
          <p>Un revenu complémentaire vous est versé chaque mois, en fonction de votre activité et de votre zone de circulation.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--blue">
    <div class="container">
      <div class="split">
        <div>
          <span class="kicker">Ce que nous prenons en charge</span>
          <h2 class="sh__title" style="font-size:clamp(24px,3vw,34px)">Zéro frais à votre charge.</h2>
          <ul class="prose mt-m" style="list-style:disc;padding-left:1.3em">
            <li>Le matériel et son installation.</li>
            <li>L'entretien courant de l'écran.</li>
            <li>Le remplacement en cas de panne.</li>
            <li>La consommation électrique liée au dispositif.</li>
          </ul>
        </div>
        <div>
          <span class="kicker">Conditions</span>
          <h2 class="sh__title" style="font-size:clamp(24px,3vw,34px)">Ce qui est demandé.</h2>
          <ul class="prose mt-m" style="list-style:disc;padding-left:1.3em">
            <li>Un taxi en activité dans le Grand Tunis.</li>
            <li>Un véhicule en bon état général.</li>
            <li>Une circulation régulière.</li>
          </ul>
          <p class="mt-s"><em>La rémunération est convenue lors de l'entretien, en fonction de votre zone et de votre volume de circulation.</em></p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container container--narrow">
      <div class="sh sh--center">
        <span class="kicker">Rejoindre le réseau</span>
        <h2 class="sh__title">Envoyez-nous un message.</h2>
        <p class="sh__intro">Laissez vos coordonnées et votre zone de circulation. Nous vous rappelons pour un entretien.</p>
      </div>

      <form class="form" action="https://api.web3forms.com/submit" method="POST">
        <input type="hidden" name="access_key" value="VOTRE_CLE_ICI">
        <input type="hidden" name="subject" value="Candidature chauffeur — spotscreens.com">
        <input type="hidden" name="from_name" value="Site SpotScreens">
        <input type="hidden" name="redirect" value="https://spotscreens.com/merci.html">
        <input type="hidden" name="type" value="chauffeur">
        <input class="form__hp" type="checkbox" name="botcheck" tabindex="-1" autocomplete="off">

        <div class="form__row form__row--2">
          <div class="form__row">
            <label for="c-nom">Nom complet</label>
            <input id="c-nom" type="text" name="nom" required autocomplete="name">
          </div>
          <div class="form__row">
            <label for="c-tel">Téléphone</label>
            <input id="c-tel" type="tel" name="telephone" required autocomplete="tel">
          </div>
        </div>
        <div class="form__row">
          <label for="c-zone">Zone de circulation habituelle</label>
          <input id="c-zone" type="text" name="zone" placeholder="Tunis Centre, La Marsa, Ariana…" required>
        </div>
        <div class="form__row">
          <label for="c-message">Message</label>
          <textarea id="c-message" name="message" placeholder="Type de véhicule, année, volume de circulation moyen…"></textarea>
        </div>
        <button type="submit" class="btn btn--primary form__submit">Envoyer ma candidature</button>
        <p class="form__note">Vos données sont utilisées uniquement pour vous recontacter. Voir notre <a class="link-inline" href="/confidentialite.html">politique de confidentialité</a>.</p>
      </form>
    </div>
  </section>
""" + GIT + FOOTER)


# ============================================================ a-propos
write("a-propos.html",
      head("À propos de SpotScreens — publicité sur taxis à Tunis",
           "SpotScreens rend la publicité extérieure accessible : un réseau d'écrans LED numériques sur taxis, une diffusion mobile, des visuels modifiables, dans le Grand Tunis.",
           "a-propos.html")
      + header("apropos", "apropos")
      + hero("À propos", "Nous rendons la publicité extérieure accessible.",
             "Photo&nbsp;#5 — Plusieurs taxis équipés alignés")
      + """
  <section class="section">
    <div class="container container--narrow">
      <div class="prose lead">
        <p>En Tunisie, l'affichage publicitaire repose encore largement sur des emplacements fixes, des contrats longs et des impressions papier. Le résultat&nbsp;: des campagnes rigides, des délais qui n'épousent pas le rythme des marques, et un support qui attend que la ville passe devant lui.</p>
        <p>SpotScreens propose une autre approche&nbsp;: un réseau d'écrans LED numériques installés sur le toit de taxis qui circulent dans le Grand Tunis. La diffusion est mobile, les visuels sont modifiables, la campagne peut démarrer rapidement et être ajustée en cours de route.</p>
        <p>Nous étoffons le réseau régulièrement et prévoyons d'étendre la couverture à d'autres villes. Notre priorité reste la même&nbsp;: un support fiable, un interlocuteur direct, et un compte rendu de fin de campagne établi sur des données vérifiables.</p>
      </div>
    </div>
  </section>

  <section class="section section--blue">
    <div class="container">
      <div class="sh">
        <span class="kicker">Nos principes</span>
        <h2 class="sh__title">Ce qui guide nos choix.</h2>
      </div>
      <div class="cards cards--2">
        <article class="card">
          <h3>Un média qui va vers le public</h3>
          <p>Nous préférons rencontrer le public plutôt que de l'attendre. Un taxi équipé traverse la ville&nbsp;; un panneau, non.</p>
        </article>
        <article class="card">
          <h3>Des campagnes courtes possibles</h3>
          <p>Pas de contrat long imposé. Une campagne peut être brève si c'est ce qui convient à votre message.</p>
        </article>
        <article class="card">
          <h3>Une diffusion dont nous rendons compte</h3>
          <p>Nous remettons un récapitulatif en fin de campagne, construit sur des données vérifiables, sans estimation d'audience invérifiable.</p>
        </article>
        <article class="card">
          <h3>Un interlocuteur direct</h3>
          <p>Un seul contact, joignable, du brief à la remise du bilan. Pas de standard, pas d'intermédiaire.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <figure class="frame frame--wide" aria-hidden="true">
        <span class="ph"><span>Photo&nbsp;#5 — Plusieurs taxis équipés alignés</span></span>
      </figure>
    </div>
  </section>
""" + GIT + FOOTER)


# ============================================================ faq
write("faq.html",
      head("Questions fréquentes — publicité taxi LED | SpotScreens",
           "Délais, changement de visuel, amplitude horaire, zones, formats vidéo, durée minimale : réponses aux questions les plus fréquentes sur une campagne SpotScreens.",
           "faq.html")
      + header("apropos", "faq")
      + hero("FAQ", "Questions fréquentes.",
             "Photo&nbsp;#2 — Taxi de jour dans la circulation",
             "Une question qui manque ? Écrivez-nous, nous répondons directement.")
      + """
  <section class="section">
    <div class="container">
      <div class="faq">
        <details>
          <summary>Quel est le délai de mise en diffusion&nbsp;?</summary>
          <p>Le délai standard entre la confirmation d'une campagne et sa mise en diffusion est de <span class="todo">À COMPLÉTER — délai standard</span>, sous réserve de la conformité du visuel transmis. Un délai plus court est possible sur demande, selon la période.</p>
        </details>
        <details>
          <summary>Puis-je changer de visuel en cours de campagne&nbsp;?</summary>
          <p>Oui. Le visuel est numérique&nbsp;: vous nous envoyez le nouveau fichier, nous le mettons en ligne sur le parc dans un délai court, sans frais supplémentaires. C'est utile pour un teaser suivi d'une révélation, une actualité, ou un message lié à une date précise.</p>
        </details>
        <details>
          <summary>Sur quelle amplitude horaire mon visuel est-il diffusé&nbsp;?</summary>
          <p>La diffusion est assurée de 7&nbsp;h à 23&nbsp;h, tous les jours de la campagne, tant que le taxi équipé est en circulation.</p>
        </details>
        <details>
          <summary>Puis-je choisir les zones de circulation&nbsp;?</summary>
          <p>Les taxis ne suivent pas de parcours fixe&nbsp;: ils circulent au gré des courses dans le Grand Tunis. On ne peut donc pas garantir une zone unique, mais on peut orienter une campagne vers des priorités géographiques. Dites-nous vos zones stratégiques, nous vous indiquerons ce qu'il est possible de faire.</p>
        </details>
        <details>
          <summary>Acceptez-vous les vidéos&nbsp;?</summary>
          <p>Oui, au format MP4, dans les limites de durée et de poids indiquées sur la page <a class="link-inline" href="/formats.html">Formats &amp; spécifications</a>. Les diffusions se font sans son.</p>
        </details>
        <details>
          <summary>Quelle est la durée minimale d'une campagne&nbsp;?</summary>
          <p>La durée minimale est de <span class="todo">À COMPLÉTER — durée minimale</span>. Cela laisse le temps à votre message d'être vu par des publics différents dans la même semaine.</p>
        </details>
        <details>
          <summary>Puis-je prolonger une campagne&nbsp;?</summary>
          <p>Oui. Faites-nous savoir avant la fin de la période prévue et nous étendons la diffusion sur la ou les périodes souhaitées, si les créneaux sont disponibles.</p>
        </details>
        <details>
          <summary>Que se passe-t-il si un véhicule est immobilisé&nbsp;?</summary>
          <p>Les diffusions manquantes sont reportées sur les autres véhicules du parc pendant la campagne, ou en prolongation à la fin, afin que le volume prévu dans votre proposition soit honoré. Le suivi est détaillé sur la page <a class="link-inline" href="/mesure.html">Mesure &amp; suivi</a>.</p>
        </details>
      </div>
    </div>
  </section>
""" + GIT + FOOTER)


# ============================================================ contact
write("contact.html",
      head("Contact SpotScreens — publicité taxi LED à Tunis",
           "Contactez SpotScreens pour une proposition de campagne publicitaire sur écrans LED de taxis à Tunis. Email, téléphone ou formulaire, nous vous répondons rapidement.",
           "contact.html")
      + header()
      + """
  <section class="section">
    <div class="container">
      <div class="sh">
        <span class="kicker">Contact</span>
        <h1 class="sh__title">Parlez-nous de votre campagne.</h1>
        <p class="sh__intro">Décrivez votre projet en quelques lignes&nbsp;: objectif, période souhaitée, public visé. Nous revenons vers vous avec une proposition de diffusion.</p>
      </div>

      <div class="form-grid">
        <form class="form" action="https://api.web3forms.com/submit" method="POST">
          <input type="hidden" name="access_key" value="VOTRE_CLE_ICI">
          <input type="hidden" name="subject" value="Nouveau message — spotscreens.com">
          <input type="hidden" name="from_name" value="Site SpotScreens">
          <input type="hidden" name="redirect" value="https://spotscreens.com/merci.html">
          <input type="hidden" name="type" value="contact">
          <input class="form__hp" type="checkbox" name="botcheck" tabindex="-1" autocomplete="off">

          <div class="form__row">
            <label for="f-nom">Nom complet</label>
            <input id="f-nom" type="text" name="nom" required autocomplete="name">
          </div>
          <div class="form__row form__row--2">
            <div class="form__row">
              <label for="f-email">Email</label>
              <input id="f-email" type="email" name="email" required autocomplete="email">
            </div>
            <div class="form__row">
              <label for="f-tel">Téléphone</label>
              <input id="f-tel" type="tel" name="telephone" autocomplete="tel">
            </div>
          </div>
          <div class="form__row">
            <label for="f-societe">Société (facultatif)</label>
            <input id="f-societe" type="text" name="societe" autocomplete="organization">
          </div>
          <div class="form__row">
            <label for="f-sujet">Sujet</label>
            <select id="f-sujet" name="sujet" required>
              <option value="Demande de proposition">Demande de proposition</option>
              <option value="Question sur le réseau">Question sur le réseau</option>
              <option value="Agence / média">Agence / média</option>
              <option value="Chauffeur partenaire">Chauffeur partenaire</option>
              <option value="Autre">Autre</option>
            </select>
          </div>
          <div class="form__row">
            <label for="f-message">Message</label>
            <textarea id="f-message" name="message" required></textarea>
          </div>
          <button type="submit" class="btn btn--primary form__submit">Envoyer le message</button>
          <p class="form__note">En envoyant ce formulaire, vous acceptez que vos coordonnées soient utilisées pour vous répondre. Voir notre <a class="link-inline" href="/confidentialite.html">politique de confidentialité</a>.</p>
        </form>

        <aside class="info-card" aria-label="Coordonnées">
          <h3>Nos coordonnées</h3>
          <dl>
            <div>
              <dt>Email</dt>
              <dd><a href="mailto:contactspotscreens@gmail.com">contactspotscreens@gmail.com</a></dd>
            </div>
            <div>
              <dt>Téléphone</dt>
              <dd><a href="tel:+21622249917">+216&nbsp;22&nbsp;249&nbsp;917</a></dd>
            </div>
          </dl>
          <p class="info-card__note">Écrivez-nous, nous revenons vers vous rapidement.</p>
        </aside>
      </div>
    </div>
  </section>
""" + GIT_PHONE + FOOTER)


# ============================================================ merci
write("merci.html",
      head("Message reçu — SpotScreens",
           "Votre message est bien arrivé. L'équipe SpotScreens revient vers vous rapidement.",
           "merci.html", noindex=True)
      + header()
      + """
  <section class="section">
    <div class="container">
      <div class="centered-msg">
        <span class="kicker">Confirmation</span>
        <h1>Votre message est bien arrivé.</h1>
        <p>Nous revenons vers vous rapidement, à l'adresse ou au numéro que vous nous avez communiqué.</p>
        <div class="btn-row btn-row--center">
          <a class="btn btn--primary" href="/">Retour à l'accueil</a>
          <a class="btn btn--outline" href="/blog.html">Lire le blog</a>
        </div>
      </div>
    </div>
  </section>
""" + FOOTER)


# ============================================================ 404
write("404.html",
      head("Page introuvable — SpotScreens",
           "Cette page n'existe pas ou plus. Retournez à l'accueil SpotScreens ou contactez-nous.",
           "404.html", noindex=True)
      + header()
      + """
  <section class="section">
    <div class="container">
      <div class="centered-msg">
        <span class="kicker">Erreur 404</span>
        <h1>Cette page a pris un autre chemin.</h1>
        <p>Le lien est peut-être obsolète, ou l'adresse comporte une coquille. Revenons à l'accueil, ou passons directement au contact.</p>
        <div class="btn-row btn-row--center">
          <a class="btn btn--primary" href="/">Retour à l'accueil</a>
          <a class="btn btn--outline" href="/contact.html">Nous contacter</a>
        </div>
      </div>
    </div>
  </section>
""" + FOOTER)

print("done")
