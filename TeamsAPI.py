import requests

# Konfigurationsdaten für deine Anwendung in Azure AD
client_id = '8d569605-f732-4dae-a941-613a57540d61'
client_secret = 'kHJ8Q~etqAu4LBEaycmRDY1GNXFRKhS6FRqGndpL'
tenant_id = '7a60a9cc-0250-4d36-8c3f-ab33f485862d'
resource = 'https://graph.microsoft.com'

# Token-Endpunkt
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"

# Daten für die Anforderung des Zugriffstokens
data = {
    'grant_type': 'password',
    'client_id': client_id,
    'client_secret': client_secret,
    'username': 'dkofler@office.htlinn.ac.at',  # Benutzername
    'password': 'Sh4ringan0513',  # Passwort
    'resource': resource
}

# Zugriffstoken abrufen
response = requests.post(token_url, data=data)

# Ausgabe der gesamten Antwort
print("Antwort der Token-Anforderung:")
print(response.json())

# Überprüfen, ob die Anfrage erfolgreich war und das Zugriffstoken extrahieren
if response.status_code == 200:
    access_token = response.json()['access_token']
    
    # Beispielanfrage an die Microsoft Graph API (hier: Aufgaben des Benutzers)
    api_endpoint = 'https://graph.microsoft.com/v1.0/me/todo/lists'
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Accept': 'application/json'
    }
    response = requests.get(api_endpoint, headers=headers)

    # Antwort verarbeiten
    if response.status_code == 200:
        tasks = response.json()
        print("Deine Aufgaben:")
        print(tasks)
    else:
        print(f"Fehler bei der Anfrage an die Microsoft Graph API: {response.text}")
else:
    print(f"Fehler bei der Anfrage zum Abrufen des Zugriffstokens: {response.text}")
