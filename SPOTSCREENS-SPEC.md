# SPOTSCREENS — SPÉCIFICATION COMPLÈTE DU SITE

> Document de référence pour la construction du nouveau site vitrine SpotScreens.
> À lire intégralement avant d'écrire du code. Ne rien inventer qui ne figure pas ici :
> aucun produit, aucun chiffre, aucune ville, aucun client qui n'est pas explicitement listé.

---

## 0. RÈGLES ABSOLUES

1. **Un seul produit existe : l'écran LED installé sur le toit des taxis.** Il n'y a pas de wraps, pas d'écrans intérieurs, pas de camions LED, pas d'hologrammes, pas de bus, pas de panneaux fixes. Ne jamais en ajouter, même pour « remplir » une page.
2. **La marque est SpotScreens.** Aucune mention d'EL BARAKA nulle part.
3. **Aucune adresse postale. Aucun horaire d'ouverture.** Le contact se limite à : email, téléphone, formulaire.
4. **Aucun nom de client, aucun logo de marque tierce, aucun témoignage** tant qu'ils ne sont pas fournis. Pas de faux logos « ils nous font confiance ».
5. **Deux couleurs seulement** : bleu et blanc, plus des gris neutres pour le texte. Pas de vert, pas d'orange, pas de dégradés multicolores.
6. Tout le site est en **français**, avec les espaces typographiques françaises (insécable avant `? ! : ;` et `%`, et dans les nombres : `10 000`).
7. **Aucun prix, aucun tarif, aucun budget, aucun montant, nulle part sur le site.** Ni page tarifs, ni « à partir de », ni fourchette, ni mention de TVA, ni modalités de paiement. Le tarif se donne en réponse à une demande, jamais en ligne.
8. **Ne rien afficher que les grands réseaux du secteur n'affichent pas.** Pas de compteur de véhicules, pas de détail d'exploitation, pas de délai de réponse chiffré, pas de lien de réservation en ligne. Le site présente un réseau et ouvre une conversation, rien de plus.
9. Chaque page se termine par **la même bande d'appel à l'action** avant le footer. C'est la mécanique centrale du site : toutes les routes mènent au contact.

---

## 1. STACK ET STRUCTURE DE FICHIERS

HTML statique, sans framework. Hébergement GitHub Pages. Pas de build step, pas de npm, pas de bundler.

```
/
├── index.html                  Accueil
├── ecrans-taxi.html            Le réseau d'écrans
├── formats.html                Formats & spécifications
├── campagnes.html              Déroulé d'une campagne
├── couverture.html             Couverture Grand Tunis
├── mesure.html                 Mesure & suivi de campagne
├── agences.html                Annonceurs & agences
├── chauffeurs.html             Devenir chauffeur partenaire
├── a-propos.html               À propos
├── faq.html                    Questions fréquentes
├── contact.html                Contact
├── merci.html                  Confirmation d'envoi du formulaire
├── mentions-legales.html
├── confidentialite.html
├── cgv.html
├── 404.html
├── robots.txt
├── sitemap.xml
├── /assets
│   ├── /css/site.css           feuille unique, partagée
│   ├── /js/site.js             menu mobile, accordéons, année du footer
│   ├── /img/                   photos (voir section 12)
│   └── /logo/                  logo-blanc.svg, logo-bleu.svg, favicon
```

Le header et le footer sont **identiques sur chaque page** — copiés tels quels dans chaque fichier HTML. Ne pas tenter de les injecter en JavaScript : cela casse le référencement et provoque un flash au chargement.

---

## 2. SYSTÈME VISUEL

### 2.1 Couleurs

```css
:root{
  --blue-900:#062052;   /* bandeau supérieur, footer */
  --blue-700:#0C36A0;   /* survol de boutons, liens actifs */
  --blue-600:#1B4FD8;   /* boutons, liens, accents */
  --blue-100:#DCE6FF;   /* bordures claires, séparateurs sur fond bleu */
  --blue-50:#F2F6FF;    /* fonds de section alternés */
  --white:#FFFFFF;
  --ink:#0D1424;        /* titres */
  --body:#495468;       /* texte courant */
  --muted:#7C879B;      /* légendes, mentions */
  --rule:#E3E8F1;       /* filets, bordures de cartes */
}
```

Répartition : **fond blanc par défaut**. Une section sur trois environ passe en `--blue-50` pour rythmer la page. Le bandeau de navigation et le footer sont en `--blue-900`. Les boutons principaux sont en `--blue-600`, texte blanc. Aucun autre fond coloré.

### 2.2 Typographie

Deux familles Google Fonts, chargées avec `display=swap` :

- **Titres** — `Archivo`, graisses 600 et 700, `letter-spacing:-0.02em`.
- **Texte** — `Inter`, graisses 400 et 500.

Échelle (desktop → mobile) :

| Rôle | Desktop | Mobile |
|---|---|---|
| H1 hero | 58px / 1.05 | 34px / 1.12 |
| H1 page intérieure | 46px / 1.1 | 30px |
| H2 section | 34px / 1.2 | 25px |
| H3 carte | 20px / 1.3 | 18px |
| Texte | 17px / 1.65 | 16px / 1.6 |
| Légende | 14px / 1.5 | 13px |
| Sur-titre | 12px, `letter-spacing:.16em`, majuscules, `--blue-600` |

Largeur de ligne maximale du texte courant : **68 caractères** (`max-width:34rem`). Titres : jamais plus de 18 mots.

### 2.3 Grille et espacement

- Conteneur : `max-width:1180px`, `padding:0 24px` (16px sous 640px).
- Espacement vertical des sections : 104px desktop, 64px mobile.
- Rayon des angles : 10px sur les cartes et les images, 6px sur les boutons. Une seule valeur par famille d'éléments, pas de mélange.
- Ombres : **aucune**, sauf le bandeau de navigation en position collée (`0 1px 0 rgba(0,0,0,.08)`). La hiérarchie passe par les filets `--rule` et les fonds `--blue-50`.

### 2.4 Boutons

```
Primaire   : fond --blue-600, texte blanc, 15px/600, padding 14px 28px, radius 6px
             survol : fond --blue-700
Secondaire : fond transparent, bordure 1px --blue-600, texte --blue-600
             survol : fond --blue-50
Sur fond bleu : fond blanc, texte --blue-900
```

Pas de flèche « → » collée au libellé. Le libellé dit ce qui se passe : `Demander une proposition`, `Nous contacter`, `Découvrir le réseau`, `Devenir chauffeur partenaire`.

### 2.5 Mouvement

Uniquement les transitions de survol (`.15s ease` sur couleur et fond) et l'ouverture des accordéons de la FAQ. **Aucune animation d'apparition au défilement.** Respecter `prefers-reduced-motion`.

---

### 2.6 Placeholders d'images et marqueurs de travail

Les photos et les logos ne sont pas encore fournis. Construire le site en entier sans les attendre, avec deux utilitaires dédiés.

**Bloc image en attente** — à la place de chaque photo, un bloc de la bonne taille :

```css
.ph{background:var(--blue-50);border:1px dashed var(--rule);border-radius:10px;
    display:grid;place-items:center;color:var(--muted);font-size:13px;text-align:center;padding:16px}
```

```html
<div class="ph" style="aspect-ratio:16/9">assets/img/hero-nuit.jpg<br>2400 × 1350</div>
```

Le bloc porte **le chemin exact du fichier attendu et ses dimensions**. Respecter le `aspect-ratio` prévu pour chaque photo (section 12) afin que la mise en page ne bouge pas lors du remplacement. Remplacer un bloc revient alors à échanger une seule ligne contre une balise `<img>`.

**Logo en attente** — le mot `SPOTSCREENS` en `Archivo` 700, 21px, `letter-spacing:-.01em`, blanc sur les fonds bleus, `--blue-900` sur les fonds clairs. Même emplacement et même hauteur que le futur SVG.

**Marqueur d'information manquante** — utilitaire `.todo` : fond `#FFF1F1`, texte `#B42318`, `padding:2px 6px`, `border-radius:4px`. C'est un outil de chantier, pas une couleur de la charte : **aucun `.todo` ne doit subsister à la mise en ligne**, et la recherche globale de `À COMPLÉTER` doit renvoyer zéro résultat avant publication.

---

## 3. EN-TÊTE (identique partout)

Barre pleine largeur en `--blue-900`, hauteur 74px, collée en haut au défilement (`position:sticky`).

```
[ logo-blanc.svg, h:30px ]   Le réseau   Campagnes   Annonceurs   Chauffeurs   À propos   [ Nous contacter ]
```

- Logo à gauche, lien vers `/`.
- Navigation centrée-droite, `Inter` 15px/500, blanc à 88 % d'opacité, blanc plein au survol et sur la page active (avec un filet de 2px `--blue-100` sous l'item actif).
- Un seul menu déroulant, sur **Le réseau** : `Les écrans taxi`, `Formats & spécifications`, `Couverture`, `Mesure & suivi`. Panneau blanc, texte `--ink`, ouverture au survol sur desktop et au clic au clavier.
- Bouton `Nous contacter` à l'extrême droite, style « sur fond bleu » (fond blanc, texte `--blue-900`).
- Sous 900px : logo + bouton hamburger. Le menu s'ouvre en panneau plein écran bleu, items empilés à 22px, sous-menu déplié à plat.

---

## 4. BANDE D'APPEL À L'ACTION (avant le footer, sur toutes les pages)

Fond `--blue-50`, centrée, 96px de padding vertical.

> **H2** — Votre marque peut être dans les rues de Tunis cette semaine.
> **Texte** — Parlez-nous de votre campagne : votre objectif, votre période, votre public. Nous revenons vers vous avec une proposition de diffusion.
> **Boutons** — `Demander une proposition` (primaire, vers `/contact`) · `Découvrir le réseau` (secondaire, vers `/ecrans-taxi`)

Sur la page Contact, remplacer cette bande par un simple rappel du téléphone.

---

## 5. PIED DE PAGE (identique partout)

Fond `--blue-900`, texte blanc, 72px de padding haut, 28px bas.

Quatre colonnes :

| Colonne 1 | Colonne 2 — Le réseau | Colonne 3 — Informations | Colonne 4 — Contact |
|---|---|---|---|
| logo-blanc.svg + phrase de positionnement | Les écrans taxi · Formats & spécifications · Couverture · Mesure & suivi | À propos · Annonceurs & agences · Chauffeurs partenaires · Questions fréquentes | contactspotscreens@gmail.com · +216 22 249 917 |

Phrase de positionnement (colonne 1) :
> La publicité extérieure, enfin simple. Votre marque sur des écrans LED qui sillonnent Tunis.

Filet `rgba(255,255,255,.14)` puis barre inférieure :
`© 2026 SpotScreens. Tous droits réservés.` à gauche · `Mentions légales · Confidentialité · CGV` à droite.

L'année est injectée par `site.js` pour ne jamais devenir obsolète.

**Aucune adresse. Aucun horaire.**

---

## 6. LES PAGES

### 6.1 `index.html` — Accueil

**Section 1 — Hero.** Photo pleine largeur, hauteur 78vh (min 560px), taxi de nuit avec l'écran allumé. Voile bleu foncé par-dessus : `linear-gradient(90deg, rgba(6,32,82,.88) 0%, rgba(6,32,82,.55) 55%, rgba(6,32,82,.25) 100%)`. Texte aligné à gauche, calé sur le conteneur.

> Sur-titre — PUBLICITÉ DIGITALE MOBILE · TUNIS
> H1 — Votre marque roule à travers la ville.
> Texte — Des écrans LED haute luminosité installés sur le toit de taxis qui circulent dans le Grand Tunis, du matin jusqu'à tard le soir.
> Boutons — `Demander une proposition` · `Découvrir le réseau`

**Section 2 — Bande de repères.** Fond blanc, filet en haut et en bas, quatre colonnes séparées par des filets verticaux. Valeur en `Archivo` 38px `--blue-600`, libellé en 14px `--muted` dessous.

| Grand Tunis | 7 h – 23 h | LED haute luminosité | Visuel modifiable |
|---|---|---|---|
| zone de circulation | amplitude de diffusion quotidienne | lisible de jour comme de nuit | image ou vidéo, remplaçable en cours de campagne |

> ⚠️ **Ne jamais publier le nombre de taxis ni le nombre de diffusions.** Un réseau se juge sur sa couverture et sa présence, pas sur son inventaire — c'est exactement ce que font les grands opérateurs du secteur, qui annoncent des villes et des zones, jamais un nombre de véhicules. Ces chiffres se donnent en rendez-vous, adaptés à l'interlocuteur.

**Section 3 — Le principe.** Deux colonnes, texte à gauche, photo à droite (taxi de jour dans la circulation).

> H2 — Un média qui va vers le public, au lieu de l'attendre.
> Texte — Un panneau attend que la ville passe devant lui. Un taxi, lui, traverse les avenues, les quartiers d'affaires, les zones commerçantes et les sorties de soirée dans la même journée. Votre visuel change de public toutes les quelques minutes.
> Lien — `Comment fonctionne le réseau`

**Section 4 — Trois arguments.** Fond `--blue-50`, trois cartes blanches, bordure `--rule`, pictogramme en trait fin `--blue-600` (24px, sans fond coloré).

1. **Visible de jour comme de nuit** — Des dalles LED haute luminosité, lisibles en plein soleil comme après la tombée de la nuit.
2. **Aucune impression, aucun délai** — Votre visuel est numérique. Il part en diffusion dès la campagne confirmée, et peut être remplacé en cours de route.
3. **Une diffusion mesurée** — Vous savez combien de fois votre visuel a été diffusé sur l'ensemble de la flotte pendant la campagne.

**Section 5 — Déroulé en quatre étapes.** Fond blanc, quatre blocs numérotés en ligne, numéro en `Archivo` 34px `--blue-100` derrière le titre.

1. **Vous nous parlez de votre campagne** — votre objectif, la période souhaitée, le public visé.
2. **Nous vous envoyons une proposition** — durée de diffusion, période, volume de diffusion estimé.
3. **Vous transmettez votre visuel** — image ou vidéo, aux formats indiqués.
4. **La campagne part en diffusion** — sur l'ensemble de la flotte, aux dates convenues.

Lien sous les étapes : `Le détail d'une campagne`.

**Section 6 — Mesure.** Fond `--blue-50`, deux colonnes : texte à gauche, photo de l'écran en diffusion à droite.
> H2 — Une campagne dont vous voyez le résultat.
> Texte — À la fin de votre campagne, vous recevez un récapitulatif de diffusion : la période couverte, le volume diffusé sur l'ensemble de la flotte et les zones parcourues. Rien n'est déclaratif.
> Lien — `En savoir plus sur le suivi de campagne` → `/mesure`

**Section 7 — Chauffeurs.** Bande deux colonnes, photo de chauffeur à gauche, texte à droite.
> H2 — Vous conduisez un taxi à Tunis ?
> Texte — Nous installons l'écran, nous prenons en charge l'entretien, et vous percevez un revenu complémentaire chaque mois sans rien changer à vos habitudes de travail.
> Bouton — `Devenir chauffeur partenaire`

**Section 8** — bande d'appel à l'action standard (section 4 de ce document).

---

### 6.2 `ecrans-taxi.html` — Le réseau d'écrans

Hero court (hauteur 42vh) : photo rapprochée de l'écran allumé, voile bleu, H1 **Des écrans LED qui traversent la ville.**

Sections :
1. **Ce qu'est le dispositif** — texte sur deux colonnes : un écran LED double face monté sur le toit du taxi, alimenté par le véhicule, piloté à distance. Le visuel est envoyé au parc depuis notre système ; aucune intervention du chauffeur.
2. **Pourquoi le toit d'un taxi** — trois paragraphes courts : hauteur du regard des piétons et des automobilistes, présence dans le flux au lieu du bord de route, répétition d'exposition sur un même trajet.
3. **Galerie** — trois photos en grille (nuit / jour / détail du montage), légendes en 14px `--muted`.
4. **Le parc** — texte factuel et sans chiffre : des taxis équipés circulant quotidiennement dans le Grand Tunis, une diffusion de 7 h à 23 h, un réseau qui s'étoffe régulièrement. **Ne pas indiquer le nombre de véhicules.**
5. Bande d'appel à l'action.

---

### 6.3 `formats.html` — Formats & spécifications

Page technique, sobre, faite pour être envoyée à un graphiste ou à une agence.

- **Tableau des spécifications** : type de fichier acceptés (JPG, PNG, MP4), durée maximale d'une vidéo, résolution recommandée, rapport d'image, poids maximal, espace colorimétrique.
  > ⚠️ Ne pas inventer ces valeurs. Laisser des champs `À COMPLÉTER` bien visibles en rouge dans le HTML, à remplir avec les caractéristiques réelles des dalles avant la mise en ligne.
- **Recommandations de création** : quatre conseils — un message unique par visuel, des caractères épais et un fort contraste, pas de texte en bas de l'image, logo visible sur toute la durée.
- **Ce que nous vérifions avant diffusion** : lisibilité, conformité au format, conformité à la réglementation publicitaire.
- Bouton : `Envoyer un visuel pour vérification` → `/contact`.

---

### 6.4 `campagnes.html` — Le déroulé d'une campagne

Reprend les quatre étapes de l'accueil et les développe : ce que vous nous transmettez, ce que nous faisons, les délais, ce qui se passe si vous voulez changer de visuel en cours de campagne, ce qu'il advient si un véhicule est immobilisé (les diffusions manquantes sont reportées).

Mise en page : sommaire collant à gauche sur desktop (liste d'ancres), contenu à droite. Une seule colonne sur mobile.

---

### 6.5 `couverture.html` — Couverture

- H1 — **Où circulent nos écrans.**
- Texte : les taxis ne suivent pas de parcours fixe ; ils circulent dans le Grand Tunis au gré des courses, ce qui expose le visuel à des publics successifs dans la même journée.
- **Carte** : SVG simple du Grand Tunis, tracé en `--blue-600` sur fond `--blue-50`, zones principales nommées (Tunis Centre, Lac 1 & Lac 2, La Marsa, Ariana, Bardo, Menzah, El Manar). Pas de carte interactive, pas de Mapbox, pas de clé d'API.
- Bande de contexte : les moments forts de la journée — trajets domicile-travail le matin, zones d'affaires en journée, sorties et restaurants le soir.
- Mention : *Extension du réseau à d'autres villes prévue. Écrivez-nous si votre campagne cible une ville en dehors du Grand Tunis.*

---

### 6.6 `mesure.html` — Mesure & suivi de campagne

C'est la page qui remplace celle des tarifs, et c'est elle qui porte la valeur perçue. Elle répond à la seule question que pose un annonceur sérieux : qu'est-ce que je saurai à la fin ?

- H1 — **Ce que vous saurez de votre campagne.**
- **Ce que nous suivons** — trois blocs : la période de diffusion effective · le volume de diffusion sur l'ensemble de la flotte · les zones parcourues pendant la campagne.
- **Le récapitulatif de fin de campagne** — décrire le document remis : période, volume diffusé, zones couvertes, captures de l'écran en diffusion.
- **En cas d'imprévu** — si un véhicule est immobilisé, les diffusions manquantes sont reportées sur la suite de la campagne.
- **Ce que nous ne prétendons pas mesurer** — paragraphe court et assumé : nous ne comptons pas les regards et nous ne vendons pas d'estimations d'audience invérifiables. Nous rendons compte de ce que nous pouvons établir.

> Ce dernier paragraphe vaut plus que dix arguments commerciaux devant un annonceur expérimenté. Le garder.

Bouton de fin de page : `Demander une proposition`.

### 6.7 `agences.html` — Annonceurs & agences

Page de crédibilité, ton plus institutionnel.

- H1 — **Un support digital mobile à intégrer à vos plans média.**
- Sections : disponibilité des créneaux et réservation en amont · fourniture des éléments de diffusion en fin de campagne · interlocuteur unique pour le suivi · compatibilité avec un plan média existant.
- Bloc `Contact commercial` avec email et téléphone, sans formulaire (lien vers `/contact`).

---

### 6.8 `chauffeurs.html` — Devenir chauffeur partenaire

- Hero court, photo de chauffeur devant son taxi équipé.
- H1 — **Votre taxi peut vous rapporter plus, sans rien changer à vos journées.**
- **Comment ça marche** en trois points : installation de l'écran par nos soins · vous travaillez normalement · rémunération mensuelle.
- **Ce que nous prenons en charge** : matériel, installation, entretien, remplacement en cas de panne, consommation électrique.
- **Conditions** : taxi en activité dans le Grand Tunis, véhicule en bon état, circulation régulière.
  > ⚠️ Le montant de la rémunération n'est **pas** affiché. Écrire : *La rémunération est convenue lors de l'entretien, en fonction de votre zone et de votre volume de circulation.*
- **Formulaire court** : nom, téléphone, zone de circulation, message. Même relais que le formulaire de contact, avec un champ caché `type=chauffeur` pour distinguer les messages dans la boîte mail.

---

### 6.9 `a-propos.html` — À propos

- H1 — **Nous rendons la publicité extérieure accessible.**
- Trois paragraphes : le constat (en Tunisie, l'affichage publicitaire repose encore sur des emplacements fixes, des contrats longs et des impressions papier) · ce que nous faisons (un réseau d'écrans numériques sur taxis, une diffusion mobile, des visuels modifiables) · où nous allons (étoffer le réseau, étendre la couverture).
- **Nos principes** : un média qui va vers le public · des campagnes courtes possibles · une diffusion dont nous rendons compte · un interlocuteur direct, sans intermédiaire.
- Photo pleine largeur de la flotte.
- Pas d'équipe, pas de photos de collaborateurs, pas de date de fondation tant qu'ils ne sont pas fournis.

---

### 6.10 `faq.html` — Questions fréquentes

Accordéons, une seule question ouverte à la fois, `<details>`/`<summary>` natifs stylés (accessible sans JavaScript).

Questions à couvrir : Quel est le délai de mise en diffusion ? · Puis-je changer de visuel en cours de campagne ? · Sur quelle amplitude horaire mon visuel est-il diffusé ? · Puis-je choisir les zones de circulation ? · Acceptez-vous les vidéos ? · Quelle durée minimale pour une campagne ? · Puis-je prolonger une campagne ? · Que se passe-t-il si un véhicule est immobilisé ?

> ⚠️ Aucune question ne porte sur le prix ou le paiement. Si l'une d'elles semble manquer, la réponse est la page Contact.

Réponses en trois à cinq lignes, sans jargon. Toute réponse qui dépend d'une information non confirmée doit être marquée `À COMPLÉTER`.

---

### 6.11 `contact.html` — Contact

Deux colonnes : formulaire à gauche (60 %), bloc de coordonnées à droite (40 %).

Formulaire : Nom complet · Email · Téléphone · Société (facultatif) · Sujet (liste : Demande de proposition · Question sur le réseau · Agence / média · Chauffeur partenaire · Autre) · Message · bouton `Envoyer le message`.

Bloc de coordonnées, en carte `--blue-50` :
- **Email** — contactspotscreens@gmail.com (lien `mailto:`)
- **Téléphone** — +216 22 249 917 (lien `tel:+21622249917`)
- Phrase : *Écrivez-nous, nous revenons vers vous rapidement.*
- **Rien d'autre. Pas d'adresse, pas d'horaires, pas de tarifs.**

---

### 6.12 Pages légales et `merci.html`

Gabarit sobre : titre, texte sur une seule colonne à 34rem, dernière mise à jour en bas.
`merci.html` : message de confirmation centré, `Votre message est bien arrivé. Nous revenons vers vous rapidement.` + bouton `Retour à l'accueil`.

Le fichier `cgv.html` porte le titre **Conditions générales** et décrit les conditions de diffusion (fourniture du visuel, conformité, droits sur les éléments transmis, report en cas d'immobilisation). **Il ne contient aucun montant ni aucune modalité de paiement.**

> ⚠️ Les mentions légales exigent une raison sociale et un identifiant fiscal. Ces informations doivent être fournies avant la mise en ligne — laisser `À COMPLÉTER` en attendant plutôt que d'inventer.

---

## 7. FORMULAIRE → GMAIL

GitHub Pages ne peut pas envoyer d'email. Utiliser **Web3Forms** (gratuit, sans compte serveur) :

1. Aller sur web3forms.com, saisir `contactspotscreens@gmail.com`, recevoir une clé d'accès par email.
2. Coller la clé dans le champ caché du formulaire.

```html
<form action="https://api.web3forms.com/submit" method="POST">
  <input type="hidden" name="access_key" value="VOTRE_CLE_ICI">
  <input type="hidden" name="subject" value="Nouveau message — spotscreens.com">
  <input type="hidden" name="from_name" value="Site SpotScreens">
  <input type="hidden" name="redirect" value="https://spotscreens.com/merci.html">
  <!-- piège à robots : doit rester vide -->
  <input type="checkbox" name="botcheck" class="hidden" style="display:none">

  <label for="nom">Nom complet</label>
  <input id="nom" type="text" name="nom" required>
  <!-- … autres champs … -->
  <button type="submit">Envoyer le message</button>
</form>
```

Exigences : chaque champ a un `<label>` visible (pas de `placeholder` en guise d'étiquette), `required` sur nom, email et message, `type="email"` et `type="tel"`, et un état de survol et de focus visible sur le bouton (`outline:2px solid var(--blue-600); outline-offset:2px`).

Alternative équivalente si Web3Forms pose problème : Formspree (50 messages/mois en gratuit). Même principe, seule l'URL du `action` change.

---

## 8. RÉFÉRENCEMENT

Sur chaque page : `<title>` unique de 55 à 60 caractères, `<meta name="description">` de 150 à 160 caractères, `<link rel="canonical">`, balises Open Graph (`og:title`, `og:description`, `og:image`, `og:url`, `og:locale` = `fr_TN`), `<html lang="fr">`.

Exemples :
- Accueil — `Publicité sur écrans LED de taxis à Tunis | SpotScreens`
- Mesure — `Suivi et mesure de campagne taxi LED | SpotScreens`
- Chauffeurs — `Devenir chauffeur partenaire SpotScreens | Tunis`

Données structurées sur l'accueil : un bloc JSON-LD `Organization` avec `name`, `url`, `logo`, `email`, `telephone`, `areaServed: "Tunis, Tunisie"`. **Sans `address`.**

Un seul `<h1>` par page. Les titres de section sont des `<h2>`. Toutes les images portent un `alt` descriptif en français.

Reprendre les mots-clés du site actuel dans les textes, naturellement : publicité taxi Tunisie, écran LED taxi, publicité digitale extérieure, DOOH Tunisie, publicité mobile Tunis. Ne jamais construire de page ni de balise autour d'un mot-clé de prix (« tarif », « prix », « combien ») : ces recherches doivent arriver sur la page Contact.

---

## 9. ACCESSIBILITÉ ET QUALITÉ

- Contraste minimum 4,5:1 sur tout le texte. Le texte blanc sur `--blue-600` passe ; le texte `--muted` sur `--blue-50` doit être vérifié.
- Navigation complète au clavier, focus toujours visible, lien d'évitement `Aller au contenu` en début de page.
- Images en `.webp` avec repli `.jpg`, `loading="lazy"` sauf sur l'image du hero, `width` et `height` renseignés pour éviter les sauts de mise en page.
- Objectif : moins de 250 Ko par page hors photo de hero.

---

## 10. RESPONSIVE

Points de rupture : 1180px, 900px, 640px.
- Sous 900px : navigation en panneau plein écran, sections deux colonnes empilées, hero à 62vh.
- Sous 640px : cartes sur une seule colonne, bande de repères sur deux lignes de deux, padding de conteneur à 16px.
- Tester à 360px de large : aucun débordement horizontal, aucun texte tronqué.

---

## 11. ORDRE DE CONSTRUCTION SUGGÉRÉ

1. `assets/css/site.css` — variables, typographie, conteneur, boutons, en-tête, pied de page, bande d'appel à l'action.
2. `index.html` en entier.
3. `contact.html` + `merci.html` + branchement de Web3Forms (tester un envoi réel avant d'aller plus loin).
4. `ecrans-taxi.html`, `chauffeurs.html`, `mesure.html`.
5. `campagnes.html`, `formats.html`, `couverture.html`, `agences.html`, `a-propos.html`, `faq.html`.
6. Pages légales, `404.html`, `robots.txt`, `sitemap.xml`. **Pas de fichier `CNAME`** : le domaine sera branché plus tard, dans une étape séparée.
7. Relecture finale, dans cet ordre :
   - rechercher dans tout le projet `DT`, `dinar`, `prix`, `tarif`, `TVA`, `budget`, `paiement`, `devis` → **zéro résultat** ;
   - rechercher `taxis`, `flotte`, `diffusions par jour` → aucun chiffre publié ;
   - aucun `lorem`, aucun `À COMPLÉTER` oublié ;
   - aucune adresse, aucun horaire d'ouverture ;
   - aucun produit autre que l'écran sur toit de taxi.

---

## 12. PHOTOS NÉCESSAIRES

Le site repose visuellement sur de vraies photos. Sans elles, il aura l'air d'un gabarit. Voici précisément ce qu'il faut.

### Indispensables

| # | Photo | Où | Cadrage | Notes |
|---|---|---|---|---|
| 1 | Taxi de nuit, écran allumé, dans une avenue de Tunis | Hero accueil | Horizontal 16:9, min 2400 px de large | La plus importante du site. Prise au crépuscule ou de nuit, l'écran doit être net et lisible. Laisser de l'espace vide à gauche du cadre pour le texte. |
| 2 | Taxi de jour dans la circulation, écran visible | Accueil, section « le principe » | Horizontal 3:2, min 1800 px | Montre que l'écran reste lisible en plein jour. |
| 3 | Gros plan de l'écran avec une publicité lisible | Hero de `ecrans-taxi.html` | Horizontal 16:9, min 2000 px | Le visuel affiché doit être réel et net. |
| 4 | Détail du montage sur le toit | Galerie `ecrans-taxi.html` | Carré ou 4:3, min 1400 px | Rassure sur la qualité de l'installation. |
| 5 | Plusieurs taxis équipés alignés | `a-propos.html`, pleine largeur | Horizontal panoramique, min 2400 px | C'est la photo qui fait croire au « réseau ». |
| 6 | Chauffeur devant son taxi équipé, souriant | `chauffeurs.html` | Vertical 4:5 ou carré, min 1400 px | Demander son accord écrit pour l'utilisation. |

### Souhaitables

| # | Photo | Où |
|---|---|---|
| 7 | Taxi passant devant un lieu reconnaissable de Tunis | Galerie |
| 8 | Vue de nuit depuis le trottoir, plusieurs passants et le taxi au fond | Galerie, `couverture.html` |
| 9 | Écran affichant deux publicités différentes (deux prises) | `campagnes.html`, section changement de visuel |

### Consignes de prise de vue

- **Horizontal** pour tout ce qui est bandeau ou hero. Le vertical ne fonctionne que pour le portrait du chauffeur.
- Photographier **au crépuscule** : c'est le moment où l'écran et le décor sont tous deux exposés correctement. En pleine nuit, l'écran brûle et le fond disparaît ; en plein midi, l'écran paraît terne.
- Ne pas utiliser le zoom numérique. S'approcher.
- Éviter les plaques d'immatriculation lisibles et les visages de passants au premier plan.
- Livrer les fichiers originaux, non recadrés et sans filtre. Le recadrage se fera à l'intégration.
- Format de livraison : JPG qualité maximale. La compression pour le web sera faite ensuite (objectif : moins de 400 Ko par image, moins de 700 Ko pour le hero).

### Logo

Trois fichiers nécessaires : `logo-blanc.svg` (pour le bandeau et le pied de page bleus), `logo-bleu.svg` (pour les fonds clairs), et un favicon 512×512 en PNG. Si seul un PNG existe, le vectoriser : le logo actuel s'affiche flou sur les écrans haute densité.

### Image de partage

Une image Open Graph de 1200×630 px : la photo n°1 recadrée, avec le logo blanc et la phrase *Publicité sur écrans LED de taxis — Tunis* incrustés.

---

## 13. CE QU'IL FAUT ÉVITER

- Les photos de banque d'images de taxis new-yorkais ou de foules génériques. Un seul taxi jaune de Manhattan sur le site et toute la crédibilité tombe.
- Les pictogrammes en couleurs vives ou en 3D. Trait fin, une seule couleur.
- Les compteurs animés sur les chiffres.
- Les bandeaux de témoignages vides ou inventés.
- Les mentions « leader », « n°1 », « révolutionnaire ».
- **Toute forme de prix**, y compris déguisée : « à partir de », « budget minimum », « formules », « abonnement », « devis gratuit en 2 minutes », un comparatif de durées avec des montants.
- Tout ce qui révèle la taille de l'exploitation : nombre de véhicules, nom des chauffeurs, ou la photo d'un seul et même taxi répétée sur toutes les pages.
- Les textes de plus de 68 caractères par ligne.
- Un `border-radius` différent sur chaque élément.
