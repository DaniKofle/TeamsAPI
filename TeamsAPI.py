import requests
from msal import ConfidentialClientApplication

# Deine Azure AD App-Registrierung Details
CLIENT_ID = '8d569605-f732-4dae-a941-613a57540d61'
CLIENT_SECRET = 'kHJ8Q~etqAu4LBEaycmRDY1GNXFRKhS6FRqGndpL'
TENANT_ID = '7a60a9cc-0250-4d36-8c3f-ab33f485862d'

# Endpoint für die Authentifizierung
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]
GRAPH_API_ENDPOINT = "https://graph.microsoft.com/v1.0"

# Erstellen der MSAL Anwendung
app = ConfidentialClientApplication(
    CLIENT_ID,
    authority=AUTHORITY,
    client_credential=CLIENT_SECRET,
)

# Holen des Tokens
result = app.acquire_token_for_client(scopes=SCOPE)

if "access_token" in result:
    access_token = result["access_token"]
    print("Access Token erhalten.")
    print(access_token)
    
    # Anfrage an die Graph API um alle Assignments zu bekommen
    assignments_endpoint = f"{GRAPH_API_ENDPOINT}/education/me/assignments"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(assignments_endpoint, headers=headers)
    if response.status_code == 200:
        assignments = response.json()
        print("Assignments:")
        print(assignments)
    else:
        print(f"Fehler beim Abrufen der Assignments: {response.status_code}")
        print(response.json())
else:
    print("Fehler beim Abrufen des Access Tokens:")
    print(result.get("error"))
    print(result.get("error_description"))
