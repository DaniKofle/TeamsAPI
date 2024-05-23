"""
import requests


response = requests.get("https://graph.microsoft.com/v1.0/me")
        
connection = response.status_code
print(connection)
"""
"""
Client Secret: Geheime ID: ffa023a2-86d5-496f-92a3-d6d63f5fa4ae
               Wert: kHJ8Q~etqAu4LBEaycmRDY1GNXFRKhS6FRqGndpL
"""
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
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'resource': resource
}

# Zugriffstoken abrufen
response = requests.post(token_url, data=data)
access_token = response.json()['access_token']

# Beispielanfrage an die Microsoft Graph API (hier: Benutzerprofil)
api_endpoint = 'https://graph.microsoft.com/v1.0//me/planner/tasks'
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Accept': 'application/json'
}
response = requests.get(api_endpoint, headers=headers)

# Antwort verarbeiten
if response.status_code == 200:
    user_profile = response.json()
    print("Benutzerprofil:")
    print(user_profile)
else:
    print(f"Fehler bei der Anfrage an die Microsoft Graph API: {response.text}")
