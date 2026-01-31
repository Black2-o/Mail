import os
import imaplib
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("GMAIL")
ACCESS_TOKEN = os.getenv("GOOGLE_ACCESS_TOKEN")

def generate_oauth2_string(email, token):
    return f"user={email}\1auth=Bearer {token}\1\1".encode()

imap = imaplib.IMAP4_SSL("imap.gmail.com")

imap.authenticate(
    "XOAUTH2",
    lambda x: generate_oauth2_string(EMAIL, ACCESS_TOKEN)
)

imap.select("INBOX")

status, messages = imap.search(None, "ALL")
mail_ids = messages[0].split()

print("Total emails:", len(mail_ids))

for mail_id in mail_ids[-5:]:
    _, msg_data = imap.fetch(
        mail_id,
        "(BODY[HEADER.FIELDS (SUBJECT FROM DATE)])"
    )
    print(msg_data[0][1].decode())

imap.logout()
