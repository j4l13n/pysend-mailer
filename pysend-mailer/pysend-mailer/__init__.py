#! python3
# This package is allowing users to send email using a package
# This file will provide all send mailer needs to in the system

class SendMailer:
    def __init__(self):
        return None

    '''
    Send method will all a user to send an email

    Attributes:
        - sender: Email of the sender
        - receiver: Email of the receiver
        - text: Contain of the message from the user
    '''
    def send(self, sender, receiver, text):
        return None

    '''
    Send by date method will all a user to send an email
    Scheduled to a specific date

    Attributes:
        - sender: Email of the sender
        - receiver: Email of the receiver
        - text: Contain of the message from the user
        - sdate(schedule_date): Schedule date will set a time to send the email 
    '''
    def send_by_date(self, sender, receiver, text, sdate):
        return None