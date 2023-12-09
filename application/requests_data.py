import time


import requests
import smtplib
from email.message import EmailMessage


class SendEmail:

    def __init__(self, to_email: list = [], subject: str = 'Nivel da agua', message: str = ""):
        self.from_email = 'projetoautomacao788@gmail.com'
        self.send_host = 'smtp.gmail.com'
        self.password = "rbtdysocgphbhcgp"
        self.smtp_port = 587
        self.to_email = to_email
        self.subject = subject
        self.message = message

        try:
            self.server = smtplib.SMTP(self.send_host, self.smtp_port)
            self.server.starttls()
            self.log_in()
            self.create_msg()
            self.server.quit()
            self.status = 'E-mail enviado com sucesso!'
            print(self.status)
        except Exception as e:
            self.status = f'Erro ao enviar o e-mail: {str(e)}'
            print(self.status)

    def log_in(self):
        self.server.login(self.from_email, self.password)

    def create_msg(self):
        body = f"""
        <html>
            <h1>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ALERT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!<h1>
            <h1>{self.message}</h1>
        </html>
        """

        message_mail = EmailMessage()
        message_mail["From"] = self.from_email
        message_mail["To"] = ', '.join(self.to_email)
        message_mail["Subject"] = self.subject

        message_mail.set_content(body, subtype='html')

        self.server.sendmail(self.from_email, self.to_email, message_mail.as_string())


class Levelwater:

    def __init__(self, link: str = 'http://192.168.0.108/'):
        self.link = link

        self.url_request()
        while True:

            if self.url_request() == "Level 1 atingido":
                time.sleep(3)

                SendEmail(to_email=["felipebragabarroso@gmail.com"], message="Level 1 atingido")

            else:
                time.sleep(3)
                print(self.url_request())
                print("ERRO 404")
                Levelwater(self.link)

    def url_request(self):
        url = requests.get(self.link).json()

        if url.get("message") == 'Level 1 atingido':
            return "Level 1 atingido"

