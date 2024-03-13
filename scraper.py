from bs4 import BeautifulSoup
import requests

leagues = [
    {"name": "England", "link": "https://www.livescores.com/football/england/premier-league/?tz=2", "direct": 4,
     "spots": 4},
    {"name": "Spain", "link": "https://www.livescores.com/football/spain/laliga/?tz=2", "direct": 4, "spots": 4},
    {"name": "Germany", "link": "https://www.livescores.com/football/germany/bundesliga/?tz=2", "direct": 4,
     "spots": 4},
    {"name": "Italy", "link": "https://www.livescores.com/football/italy/serie-a/?tz=2", "direct": 4, "spots": 4},
    {"name": "France", "link": "https://www.livescores.com/football/france/ligue-1/?tz=2", "direct": 3, "spots": 4},
    {"name": "Netherlands", "link": "https://www.livescores.com/football/holland/eredivisie/?tz=2", "direct": 2,
     "spots": 3},
    {"name": "Portugal", "link": "https://www.livescores.com/football/portugal/primeira-liga/?tz=2", "direct": 1,
     "spots": 2},
    {"name": "Belgium", "link": "https://www.livescores.com/football/belgium/belgian-pro-league/?tz=2", "direct": 1,
     "spots": 2},
    {"name": "Scotland", "link": "https://www.livescores.com/football/scotland/scotland-premiership/?tz=2",
     "direct": 1, "spots": 2},
    {"name": "Austria", "link": "https://www.livescores.com/football/austria/bundesliga/?tz=2", "direct": 1,
     "spots": 2},
    {"name": "Serbia", "link": "https://www.livescores.com/football/serbia/super-liga/?tz=2", "direct": 0,
     "spots": 2},
    {"name": "Turkey", "link": "https://www.livescores.com/football/turkey/super-lig/?tz=2", "direct": 0,
     "spots": 2},
    {"name": "Switzerland", "link": "https://www.livescores.com/football/switzerland/super-league/?tz=2",
     "direct": 0, "spots": 2},
    {"name": "Ukraine", "link": "https://www.livescores.com/football/ukraine/premier-league/?tz=2", "direct": 0,
     "spots": 2},
    {"name": "Czech Republic", "link": "https://www.livescores.com/football/czech-republic/1st-league/?tz=2",
     "direct": 0, "spots": 2},
    {"name": "Norway", "link": "https://www.livescores.com/football/norway/eliteserien/?tz=2", "direct": 0,
     "spots": 1},
    {"name": "Denmark", "link": "https://www.livescores.com/football/denmark/superliga/?tz=2", "direct": 0,
     "spots": 1},
    {"name": "Croatia", "link": "https://www.livescores.com/football/croatia/1st-league/?tz=2", "direct": 0,
     "spots": 1},
    {"name": "Poland", "link": "https://www.livescores.com/football/poland/ekstraklasa/?tz=2", "direct": 0,
     "spots": 1},
    {"name": "Greece", "link": "https://www.livescores.com/football/greece/super-league/?tz=2", "direct": 0,
     "spots": 1},
    {"name": "Hungary", "link": "https://www.livescores.com/football/hungary/nb-i/?tz=2", "direct": 0,
     "spots": 1},
    {"name": "Israel", "link": "https://www.livescores.com/football/israel/premier-league/?tz=2", "direct": 0,
     "spots": 1},
    {"name": "Slovakia", "link": "https://www.livescores.com/football/slovakia/fortuna-liga/?tz=2", "direct": 0,
     "spots": 1},
]

response = requests.get("https://www.livescores.com/football/england/premier-league/?tz=2")
livescore = response.text

soup = BeautifulSoup(livescore, "html.parser")
class_finder = soup.find("td", string='Arsenal')
CLASS = (class_finder['class'][0])

response = requests.get("https://kassiesa.net/uefa/data/method5/ccoef2024.html")
kassiesa = response.text
soup = BeautifulSoup(kassiesa, "html.parser")
lista = soup.find_all("b")
direct_entries_list = []
performance_entries_list = []
for _ in range(1, 4, 2):
    for i in range(len(leagues)):
        if leagues[i]["name"] == lista[_].get_text():
            response = requests.get(leagues[i]["link"])
            liga = response.text
            soup = BeautifulSoup(liga, "html.parser")

            liga_lista = soup.find_all(class_=CLASS)
            performance_entries_list.append(
                [lista[_].get_text(), lista[_ + 1].get_text(), liga_lista[leagues[i]["direct"]].get_text()])
            leagues[i]["spots"] += 1
            leagues[i]["direct"] += 1
            # print (lista[_].get_text(), lista[_+1].get_text(), liga_lista[item["direct"]].get_text())


response = requests.get("https://kassiesa.net/uefa/data/method5/trank2024.html")
clubs = response.text
soup = BeautifulSoup(clubs, "html.parser")
clubs_list = soup.find_all("td", class_="aleft")
coef_list = soup.find_all(class_="lgray")

lista_klubova = [[clubs_list[i].get_text(), coef_list[i].get_text()] for i in range(len(clubs_list))]

for _ in range(len(lista_klubova)):
    if lista_klubova[_][0] == "Bayern MÃ¼nchen":
        lista_klubova[_][0] = "Bayern Munich"
    elif lista_klubova[_][0] == "Internazionale":
        lista_klubova[_][0] = "Inter"
    elif lista_klubova[_][0] == "AS Roma":
        lista_klubova[_][0] = "Roma"
    elif lista_klubova[_][0] == "FC Barcelona":
        lista_klubova[_][0] = "Barcelona"
    elif lista_klubova[_][0] == "AtlÃ©tico Madrid":
        lista_klubova[_][0] = "Atletico Madrid"
    elif lista_klubova[_][0] == "Glasgow Rangers":
        lista_klubova[_][0] = "Rangers"
    elif lista_klubova[_][0] == "FC Basel":
        lista_klubova[_][0] = "Basel"
    elif lista_klubova[_][0] == "Sporting Braga":
        lista_klubova[_][0] = "SC Braga"
    elif lista_klubova[_][0] == "Sporting CP Lisbon":
        lista_klubova[_][0] = "Sporting CP"
    elif lista_klubova[_][0] == "Olympique Lyon":
        lista_klubova[_][0] = "Lyon"
    elif lista_klubova[_][0] == "Slavia Praha":
        lista_klubova[_][0] = "Slavia Prague"
    elif lista_klubova[_][0] == "FC KÃ¸benhavn":
        lista_klubova[_][0] = "FC Copenhagen"
    elif lista_klubova[_][0] == "Red Star Belgrade":
        lista_klubova[_][0] = "FK Crvena Zvezda"
    elif lista_klubova[_][0] == "AA Gent":
        lista_klubova[_][0] = "Gent"
    elif lista_klubova[_][0] == "Stade Rennais":
        lista_klubova[_][0] = "Rennes"
    elif lista_klubova[_][0] == "Olympiakos Piraeus":
        lista_klubova[_][0] = "Olympiacos"
    elif lista_klubova[_][0] == "Olympique Marseille":
        lista_klubova[_][0] = "Marseille"
    elif lista_klubova[_][0] == "Lille OSC":
        lista_klubova[_][0] = "Lille"
    elif lista_klubova[_][0] == "Partizan Belgrade":
        lista_klubova[_][0] = "Partizan Beograd"
    elif lista_klubova[_][0] == "PAOK Thessaloniki":
        lista_klubova[_][0] = "PAOK FC"
    elif lista_klubova[_][0] == "FerencvÃ¡ros":
        lista_klubova[_][0] = "Ferencvaros"
    elif lista_klubova[_][0] == "Molde FK":
        lista_klubova[_][0] = "Molde"
    elif lista_klubova[_][0] == "BodÃ¸/Glimt":
        lista_klubova[_][0] = "Bodo/Glimt"
    elif lista_klubova[_][0] == "FenerbahÃ§e":
        lista_klubova[_][0] = "Fenerbahce"
    elif lista_klubova[_][0] == "Maccabi Tel-Aviv":
        lista_klubova[_][0] = "Maccabi Tel Aviv"


champions_list = []
non_and_champions_list = []
all_teams = {}
for item in leagues:
    response = requests.get(item["link"])
    direct_entries = response.text
    soup = BeautifulSoup(direct_entries, "html.parser")
    teams = soup.find_all(class_=CLASS)
    champions_list.append(teams[0].get_text())
    if item["direct"] - item["spots"] != 0:
        for _ in range(len(teams)):
            all_teams[teams[_].get_text()] = _+1
    for _ in range(item["direct"]):
        direct_entries_list.append(teams[_].get_text())
    if item["name"] not in ["Serbia", "Turkey", "Switzerland", "Ukraine", "Czech Republic"]:
        for _ in range(item["direct"], item["spots"]):
            non_and_champions_list.append(teams[_].get_text())
    else:
        for _ in range(item["direct"]):
            non_and_champions_list.append(teams[_].get_text())

kvalifikanti = []
kvalifikanti_champions = []

for item in lista_klubova:
    if item[0] not in direct_entries_list and item[0] in champions_list:
        kvalifikanti_champions.append(item)

direct_entries_list.append(kvalifikanti_champions[0][0])

for item in lista_klubova:
    if item[0] not in direct_entries_list and item[0] in non_and_champions_list:
        kvalifikanti.append(item)

direct_entries_list.append(kvalifikanti[0][0])

lista_minimuma = []
for _ in range(3):
    lista_minimuma.append(float(kvalifikanti[_][1]))
    lista_minimuma.append(float(kvalifikanti_champions[_][1]))
minimum = min(lista_minimuma)
challengers = []

for item in lista_klubova:
    if float(item[1]) > minimum:
        if item[0] not in direct_entries_list not in kvalifikanti not in kvalifikanti_champions:
            if item[0] in list(all_teams.keys()):
                item.append(all_teams[item[0]])
                challengers.append(item)


