
import poplib
import email
import time


class MailHelper:

    def __init__(self, app):
        self.app = app

    def get_mail(self, username, password, subject):
        for i in range(5):
            pop = poplib.POP3(self.app.config['james']['host'])
            pop.user(username)
            pop.pass_(password)

            emails_received = pop.stat()[0]

            if emails_received > 0:
                for n in range(emails_received):
                    msg_lines = pop.retr(n+1)[1]
                    msg_text = "\n".join(map(lambda l: l.decode('utf-8'),
                                             msg_lines)
                                         )
                    msg_parsed = email.message_from_string(msg_text)

                    if msg_parsed.get("Subject") == subject:
                        pop.dele(n+1)
                        pop.quit()
                        return msg_parsed.get_payload()
            pop.quit()
            time.sleep(3)
