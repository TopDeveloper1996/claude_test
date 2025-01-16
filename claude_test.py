import os
import json
from anthropic import Anthropic

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the client
api_key = os.getenv('ANTHROPIC_API_KEY')  # or set api_key = 'Your-API-Key'
client = Anthropic(api_key=api_key)

# Load JSON input from file
with open('input_data.json', 'r') as f:
    input_data = json.load(f)

# Define your prompt
PROMPT = f"""
Sistema: Sei un esperto consulente finanziario italiano che lavora per uno studio di commercialisti. Stai analizzando i dati finanziari di un cliente e devi preparare un commento iniziale per il report. Il tuo compito è fornire un'analisi approfondita ma accessibile, mantenendo un tono professionale ma caloroso, come se conoscessi personalmente il proprietario dell'azienda da tempo.

Utente: Analizza i seguenti dati finanziari per {input_data['company_info']['name']} (codice ATECO {input_data['company_info']['ateco code']} - {input_data['company_info']['ateco description']}) e genera un commento iniziale in italiano. Ecco i dati:

{json.dumps(input_data)}

Nella tua analisi, segui queste linee guida:

1. Inizia con un saluto personale ma professionale.

2. Fornisci un'analisi dettagliata e significativa, evitando informazioni superflue. Concentrati sugli aspetti più rilevanti per un imprenditore italiano.

3. Esamina attentamente tutti i dati forniti, inclusi tabelle, metriche di riepilogo e grafici. Non tralasciare alcuna informazione importante.

4. Identifica tendenze, punti di forza e aree di miglioramento. Sii specifico e usa i numeri per supportare le tue osservazioni.

5. Presta attenzione a possibili anomalie nei dati, come spese una tantum o picchi di fine anno. Se noti qualcosa di insolito, menzionalo con cautela, suggerendo la possibilità di "artefatti" nei dati.

6. Usa un linguaggio diretto e sostanziale, evitando tecnicismi eccessivi. L'analisi deve essere profonda ma comprensibile.

7. Conclude con un breve accenno alle possibili azioni da intraprendere, senza entrare troppo nel dettaglio.

8. Limita il commento a circa 250-300 parole.

9. Usa un formato discorsivo senza esagerare con le indicizzazione e le liste, se strettamente necessario puoi usare alcune liste per migliorare la comprensione del tuo utente. 

Ricorda: evita errori, imprecisioni o supposizioni non supportate dai dati. Se qualche informazione sembra mancare o essere incongruente, menzionalo nel tuo commento.
"""

# Make a request to the Claude model
response = client.messages.create(
    model="claude-3-5-sonnet-20240620",  # Specify the model you want to use
    max_tokens=1000,    # Adjust max tokens as needed
    system=PROMPT,
    messages=[{"role": "user", "content": PROMPT}]
)

# Print and parse the response content
response_content = response.content
print("Response from API:", response_content)

