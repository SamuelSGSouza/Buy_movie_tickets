from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# definindo forma de contato por email


def envia_email(filme, cinema):
    msg = MIMEMultipart()
    msg["from"] = 'samuels.g.desouza@gmail.com'
    msg["to"] = 'samuels.g.desouza@gmail.com'
    msg["subject"] = f'o filme {filme} está com vendas iniciadas no cinema {cinema}'
    corpo = MIMEText(
        f'o filme {filme} está com vendas iniciadas no cinema {cinema}')
    msg.attach(corpo)

    server = smtplib.SMTP(host='smtp.gmail.com', port='587')
    server.ehlo()
    server.starttls()
    server.login('samuels.g.desouza@gmail.com', "chronotriggerA1")
    server.sendmail(msg["from"], msg["to"], msg.as_string())

    server.quit()

    def __str__(self):
        return 'tudo ok!'
