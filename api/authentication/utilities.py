from django.core.mail import EmailMessage


def send_activation_email(to, url):
    subject = '<< Reset password >>'
    body = """
    Hello,

    To reset your password please follow this link: {}
    """.format(url)
    sent_from = 'admin@localhost'

    email = EmailMessage(subject, body, sent_from, to)
    email.send()
