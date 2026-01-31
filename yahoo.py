import os
import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("YAHOO_EMAIL")                    # Your Yahoo email
APP_PASSWORD = os.getenv("YAHOO_APP_PASSWORD")      # Your App Password

imap_host = "imap.mail.yahoo.com"
imap_port = 993

# Connect and login
imap = imaplib.IMAP4_SSL(imap_host, imap_port)
imap.login(EMAIL, APP_PASSWORD)

# Select inbox
imap.select("INBOX")

# Search all emails
status, messages = imap.search(None, "ALL")
email_ids = messages[0].split()

print("Total emails:", len(email_ids))

# Get last 5 emails
for email_id in email_ids[-5:]:
    status, msg_data = imap.fetch(email_id, "(RFC822)")
    
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            
            # Decode subject
            subject = msg.get("Subject")
            if subject:
                decoded_subject = decode_header(subject)[0]
                if isinstance(decoded_subject[0], bytes):
                    subject = decoded_subject[0].decode()
                else:
                    subject = decoded_subject[0]
            
            print(f"From: {msg.get('From')}")
            print(f"Subject: {subject}")
            print(f"Date: {msg.get('Date')}")
            print("---")

imap.close()
imap.logout()