descRequete = {
    1: "Lister les tous les agences",
    2: "Lister tous les caissiers par ordre croissant de leur nom",
    3: "Lister tous chef d’agence ainsi que le nom de l’agence",
    4: "Lister les comptes de transaction de l’agence Plateau par ordre croissant du solde",
    5: "Lister la somme des montants déposés par un caissier dans un compte de transaction de l’agence dont le chef est moussa dop par ordre croissant du montant",
    6: "Lister les utilisateurs de l’agence Plateau ",
    7: "Lister le nombre de compte par agence",
    8: "Lister les comptes affectés à l’utilisateur moussa diop durant le mois de Mai 2021",
    9: "Lister les utilisateurs à qui on a affecté le compte numéro 001 durant année 2021",
    10: "Lister le montant des transactions effectué par utilisateur et par date dans l’agence dont le numéro est 001",
    11: "Lister le nombre d’affectation par utilisateur et numéro de compte durant le premier trimestre de l’année 2021 par ordre croissant de ce nombre d’affectation dans l’agence dont le numéro est 001",
    12: "Lister les dépôts effectués et les retraits par jour dans l’agence dont le chef est moussa diop par ordre croissant du montant",
    13: "Lister les montants de transactions et les frais associés effectués par l’utilisateur Assane Faye dans l’agence dont le chef est moussa diop",
    14: "Lister la somme des parts de l’agence, de l'état et de l’état des transactions par date dans l’agence dont le numéro est 001",
    15: "Lister la somme des parts de l’agence et de l'état par agence durant deuxième de l’année 2021",
    16: "Lister l’agence qui a fait le plus d transfert durant le mois de Juin 2021",
    17: "Lister l’agence qui a fait le moins de transfert de dépôt le 10-08-2021",
    18: "Lister l’agence qui a fait le retrait le plus grand durant le mois de MAI 221",
    19: "Lister les agences qui n’ont pas fait de dépôt le 10-08-2021",
    20: "Lister les noms utilisés par l’agence numéro 001 durant le mois de MAI 221",
    21: "Lister le ou les clients qui ont effectué le dépôt le plus petit durant le mois de MAI 2021",
    22: "Lister le ou les clients qui ont effectué le plus de dépôt durant le mois de MAI 2021",
    23:"Lister les 5 agences qui ont effectué le plus de transactions durant l’année 2021",
    24:"Lister les 5 agences dont le montant gagné (somme des frais gagnés sur les transactions) sont les plus faibles en 2021.",
    25:"Lister l’utilisateur qui fait le plus de transfert dans l’agence dont le chef est moussa diop",
    "E|e":"Pour afficher les requêtes déjà choisi pour les ré exécuter",
    "R|r":"Pour réafficher tout le menu initial",
    "Q|q": "Pour quitter"
}

requete = {

    1:"SELECT numero_AGENCE, adresse_AGENCE,etat_AGENCE FROM AGENCE",

    2:"SELECT nom_USER FROM USERS WHERE id_PROFIL_PROFIL=3 ORDER BY nom_USER",

    3:"SELECT nom_USER, adresse_AGENCE FROM USERS JOIN AGENCE ON id_USER = id_USER_USER AND id_PROFIL_PROFIL = 1",

    4:"SELECT * FROM COMPTE_TRANSACTION JOIN TRANSACTIONS ON numero = numero_COMPTE_TRANSACTION AND numero_AGENCE_AGENCE = 10 ORDER BY solde_COMPTE_TRANSACTION ASC",
    
    5:"SELECT nom_USER, sum(montant_TRANSACTION),COUNT(montant_TRANSACTION) FROM TRANSACTIONS JOIN COMPTE_TRANSACTION JOIN USERS ON numero = numero_COMPTE_TRANSACTION AND id_USER = id_USER_USER AND id_PROFIL_PROFIL=3 GROUP BY id_USER_USER",

    6: "SELECT nom_USER,libelle_PROFIL, adresse_AGENCE FROM USERS JOIN AGENCE JOIN PROFIL ON id_USER = id_USER_USER AND id_PROFIL_PROFIL = id_PROFIL AND numero_AGENCE_AGENCE = 8"
}