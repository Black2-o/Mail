"""
NOT CHECKED YET
BECAUSE I CAN NOT CREATE AZURE ACCOUNT FOR CREDIT CARD
"""

import os
from dotenv import load_dotenv
from msal import PublicClientApplication

load_dotenv()

MICROSOFT_CLIENT_ID = os.getenv("MICROSOFT_CLIENT_ID")
MICROSOFT_TENANT_ID =  os.getenv("MICROSOFT_TENANT_ID")

SCOPES = ["https://outlook.office.com/IMAP.AccessAsUser.All", "offline_access"]

app = PublicClientApplication(MICROSOFT_CLIENT_ID, authority=f"https://login.microsoftonline.com/{MICROSOFT_TENANT_ID}")

# Interactive login
result = None
accounts = app.get_accounts()
if accounts:
    result = app.acquire_token_silent(SCOPES, account=accounts[0])

if not result:
    result = app.acquire_token_interactive(SCOPES)

print("ACCESS TOKEN:", result['access_token'])
print("REFRESH TOKEN:", result.get('refresh_token'))
