import httpx
from bs4 import BeautifulSoup

def extraer_tasa_bcv():
    print("Conectando con el servidor del BCV")
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x6_64)"}
    try:
        response = httpx.get("https://www.bcv.org.ve/", headers=headers, verify=False)
        soup = BeautifulSoup(response.text, "html.parser")
        #Extracción Dolar BCV $
        texto_dolar_crudo = soup.find(id="dolar").text
        texto_dolar_limpio = texto_dolar_crudo.replace("USD", "").replace(",", ".").strip()
        precio_usd = float(texto_dolar_limpio)
        #Extracción Euro
        texto_euro_crudo = soup.find(id="euro").text
        texto_euro_limpio = texto_euro_crudo.replace("EUR", "").replace(",", ".").strip()
        precio_eur = float(texto_euro_limpio)

        return {
            "bcv_usd": precio_usd,
            "bcv_eur": precio_eur
        }

    except Exception as e:
        print("Error al conectar con el servidor del BCV")
        print(e)
        return None

print(extraer_tasa_bcv())