def remise_parametre():
    texte =  "Pour calculer le prix à payer, nous avons besoin de connaitre\n"
    texte += "- le nombre de tee-shirts achetés\n- le prix d'un seul tee-shirt de ce modèle\n\n"
    texte += "Notons n le nombre de tee-shirts du même modèle achetés\n"
    texte += "       p le prix d'un tee-shirt en euros\n\n"
    texte += "Notre fonction devra avoir deux paramètres n et p."
    return texte

def remise_entete():
    texte =  "La fonction Python qui calculera le prix total à payer:\n"
    texte += "- se nomme solde (voir énoncé)\n"
    texte += "- prend pour paramètres n et p\n"
    texte += "Son en-tête s'écrira"
    texte += "def solde(n, p):"
    return texte

def remise_communiquer():
    texte =  "La fonction doit retourner le prix total à payer\n"
    texte += "Nous avons choisi d'utiliser la variable prix_total pour stocker sa valeur\n"
    texte += "La dernière ligne de notre fonction sera\n\n"
    texte +=  "return prix_total"
    return texte

def remise_bloc():
    texte =  "Distinguons bien toutes les variables en jeu\n"
    texte += "- le nombre de tee-shirts achetés. Ce nombre est noté n et est passé en paramètre\n"
    texte += "- le prix en euros d'un seul tee-shirts. Ce nombre est noté p et est passé en paramètre\n"
    texte += "- le prix a payer sans réduction. Nous le noterons prix_total\n"
    texte += "- le prix a payer avec réduction. Nous le noterons aussi prix_total\n\n"
    texte += "Calculons prix_total sans réduction: n * p\n"
    texte += "          prix_total avec réduction: n * p * 0.6\n\n"
    texte += "Rappel: avec une réduction de 40 %, il reste 60 % du prix à payer\n"
    texte += "        ainsi baisser un prix de 40 % revient à le multiplier par 0,6"
    return texte

def taux_parametre():
    texte =  "Le taux d'évolution indique ce que 'pèse' une variation de valeurs par rapport à la valeur initiale.\n"
    texte += "Pour calculer un taux d'évolution, il nous suffit de connaitre:\n"
    texte += "  - la valeur initiale que l'on stockera dons une variable nommée initiale\n"
    texte += "  - la valeur finale que l'on stockera dans une variable nommée finale\n\n"
    texte += "Notre fonction devra avoir deux paramètres 'initiale' et 'finale'."
    return texte

def taux_entete():
    texte =  "La fonction Python qui calculera le taux d'évolution:\n"
    texte += "  - se nommer taux (on peut choisir un autre nom)\n"
    texte += "  - prend pour paramètres initiale et finale (on peut choisir d'autres noms)\n"
    texte += "Son en-tête s'écrira"
    texte += "def taux(initiale, finale):"
    return texte

def taux_communiquer():
    texte =  "La fonction doit retourner le taux d'évaolution\n"
    texte += "Nous avons choisi d'utiliser la variable t pour stocker sa valeur\n"
    texte += "La dernière ligne de notre fonction sera\n\n"
    texte +=  "return t"
    return texte

def taux_bloc():
    texte =  "Quand la grandeur passe de la valeur initiale à la valeur finale\n"
    texte += "elle varie de: \t valeur finale - valeur initiale\n"
    texte += "par rapport à la valeur initiale\n\n"
    texte += "- le prix a payer sans réduction. Nous le noterons prix_total\n"
    texte += "- le prix a payer avec réduction. Nous le noterons aussi prix_total\n\n"
    texte += "Le taux d'évolution est:  t = (finale - initiale) / initiale"
    return texte

def taux_exemple():
    texte =  "Quand la grandeur passe de 80 € à 70 €\n"
    texte += "elle varie de: -10 € (négatif car c'est une baisse)\n"
    texte += "par rapport à 80 € au départ.\n\n"
    texte += "Le taux d'évolution est:  t = (70 - 80) / 80 = 0,125\n"
    texte += "Le taux d'évolution est: 0,125 qui s'écrit aussi 12,5/100"
    return texte
