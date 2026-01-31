"""
NOT CHECKED YET
BECAUSE I CAN NOT CREATE AZURE ACCOUNT FOR CREDIT CARD
"""
import os
import imaplib
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("MICROSOFT_MAIL")
ACCESS_TOKEN = os.getenv("MICROSOFT_ACCESS_TOKEN")


def generate_oauth2_string(email, token):
    return f"user={email}\x01auth=Bearer {token}\x01\x01".encode()

imap = imaplib.IMAP4_SSL("outlook.office365.com")  # Outlook IMAP server
imap.authenticate("XOAUTH2", lambda x: generate_oauth2_string(EMAIL, ACCESS_TOKEN))

imap.select("INBOX")

status, messages = imap.search(None, "ALL")
mail_ids = messages[0].split()

print("Total emails:", len(mail_ids))

for mail_id in mail_ids[-5:]:
    _, msg_data = imap.fetch(mail_id, "(BODY[HEADER.FIELDS (SUBJECT FROM DATE)])")
    print(msg_data[0][1].decode())

imap.logout()
