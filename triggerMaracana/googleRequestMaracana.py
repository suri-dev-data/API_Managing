import sys
import re
import requests
from datetime import datetime,timedelta
from twillioTriggerMaracana import sendTheMessage
import os
from dotenv import load_dotenv # type: ignore


load_dotenv()
API_KEY = os.getenv("GOOGLE_API_CUSTOMSEARCH_KEY")
CX = os.getenv("GOOGLE_CX")
print(API_KEY)

def buscar_jogo_maracana(time):



    query = f"jogo {time} Maracanã site:ge.globo.com"
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={query}"

    response = requests.get(url)
    data = response.json()

    hoje = datetime.today()
    dia = hoje.day
    mes = hoje.month
    print(f"Hoje é {hoje}")
    if "items" in data:
        for item in data["items"]:
            print("🔗", item["link"])
            print("📄", item["title"])
            print("📃", item.get("snippet", ""))
            print("-" * 40)
            if  bool(re.search(f"{"|".join(map(re.escape, dias_da_semana()))}", item.get("snippet", ""))):
                print("✅ ENCONTREI O JOGO")
                mensagem = f"📢 Essa semana tem jogo importante no Maracanã, cuidado \n\n Link de Referencia: {item["link"]}"
                sendTheMessage(mensagem)
                return
    else:
        print("❌ Nenhum resultado encontrado.")

def dias_da_semana():
    hoje = datetime.today()
    # pega o índice do dia da semana (segunda=0, domingo=6)
    inicio_semana = hoje - timedelta(days=hoje.weekday())

    dias = []
    for i in range(7):
        dia = inicio_semana + timedelta(days=i)
        dias.append(dia.strftime("%d/%m"))

    return dias

if __name__ == "__main__":
    buscar_jogo_maracana("Flamengo")
    buscar_jogo_maracana("Fluminense")