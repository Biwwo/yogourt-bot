import pickle 

#Save function
def load_file(files):
    with open(files, 'rb') as f:
        p = pickle.load(f)
        return p

def save_file(files, save):
    with open(files, 'wb') as f:
        pickle.dump(save, f)

name_list = [
    "La Laitière",
    "Mamie Nova",
    "La Bergère",
    "Nestlé",
    "Lacia",
    "Blédilacté",
    "Perle de Lait",
    "Yakult",
    "Yofrutta",
    "Alpro",
    "Gervais",
    "Hirz",
    "Isey",
    "Yorük",
    "Yoplait",
    "Yop",
    "Yolado",
    "Vilvi",
    "Verka",
    "Skyr",
    "Siggi's",
    "Pechalou",
    "Pascual",
    "Milkana",
    "Liégeois",
    "Ferme Collet",
    "Emmi",
    "Danone",
    "Climont",
    "Candia",
    "Biedermann",
    "Yopa",
    "Yomo",
    "Yayla",
    "Yogosan",
    "Yaos",
    "Ya",
    "Valblanc",
    "tcby",
    "Swiss",
    "Suntat",
    "Stonyfield",
    "Sterilgada",
    "Soignon",
    "Ramdy",
    "Rians",
    "Quidarré",
    "Pur Natur",
    "Provamel",
    "Petit Montebourg",
    "Paturages",
    "Pastoret",
    "Onken",
    "Num Nom’s",
    "Nomadic",
    "NatureO",
    "Müller",
    "Mont Berry",
    "MinusL",
    "Milsani",
    "Milsa",
    "Milky Lux",
    "Milbona",
    "Mcennedy",
    "Mavrommátis",
    "Malo",
    "Lynos ",
    "Lou Perac",
    "Les2vaches",
    "Le Petit Basque",
    "Le Graulois",
    "Le Chamois",
    "Lactel",
    "Lacia",
    "La Roche aux Fées",
    "La Ferme à Desiris",
    "La Fontaine à Yaourt",
    "Kerguillet",
    "Ker Konan",
    "J’nina",
    "Jaouda",
    "Inex",
    "Heirler",
    "GrandeurNatur",
    "Gaborit",
    "Flore d’Etable",
    "FanMilk",
    "Faiz",
    "Fage",
    "Ekia",
    "Dolait",
    "Dodoni",
    "Densia",
    "Delta",
    "Danette",
    "Dahi",
    "Chobani",
    "Chapman’s",
    "Cazaubon",
    "Campina",
    "Bonneterre",
    "Baskalia",
    "Asgaar",
    "Andros",
    "Alpengut",
    "Ehrmann",
    "Danonino",
    "Elo",
    "Fantasia",
    "Fromital",
    "Gazi",
    "Great Dairy",
    "Happy Coco!",
    "Kpi Kpi",
    "Zott",
]

save_file("nickname_list.data", name_list)