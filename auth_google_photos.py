
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/photoslibrary.readonly"]

flow = InstalledAppFlow.from_client_secrets_file(
    "credentials.json", SCOPES)
creds = flow.run_local_server(port=0)

# Save credentials
with open("google_credentials.json", "w") as token:
    token.write(creds.to_json())
