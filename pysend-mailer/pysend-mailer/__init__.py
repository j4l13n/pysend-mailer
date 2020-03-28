#! python3
# This package is allowing users to send email using a package
# This file will provide all send mailer needs to in the system
import smtplib, re


class SendMailer:
    def __init__(self, sender, password, receiver, message):
        self.sender = sender
        self.password = password
        self.receiver = receiver
        self.message = message
        self.provider = None

    '''
    Send method will all a user to send an email

    Attributes:
        - sender: Email of the sender
        - receiver: Email of the receiver
        - text: Contain of the message from the user
    '''
    def send(self, sender, password, receiver, message):
        # Check email server
        emailRegex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+
            @
            ([a-zA-Z0-9.-]+)
            \.[a-zA-Z]{2,4}
        )''', re.VERBOSE)

        search_sender = emailRegex.search(sender)

        if search_sender == None:
            raise Exception('Sender email was not found')

        search_receiver = emailRegex.search(receiver)

        if search_receiver == None:
            raise Exception('Receiver email was not found')

        self.sender = search_sender.group()
        self.receiver = search_receiver.group()
        self.provider = search_receiver.group(2)
        self.password = password
        self.message = message
        
        # Setup SMTP server using the given server name
        
        if self.provider == 'gmail':
            # Connecting to GMAIL SMTP Server
            smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            # Establish a connection to the server
            smtpObj.ehlo()
            # Login to sender account
            smtpObj.login(self.sender, self.password)
            # Send the email
            smtpObj.sendmail(self.sender, self.receiver, self.message)
            print('Message sent successfully')
            # Quit
            smtpObj.quit()
        elif self.provider == 'yahoo':
            # Connecting to GMAIL SMTP Server
            smtpObj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
            import pdb; pdb.set_trace()
            # Establish a connection to the server
            smtpObj.ehlo()
            smtpObj.starttls()
            # Login to sender account
            smtpObj.login(self.sender, self.password)
            # Send the email
            smtpObj.sendmail(self.sender, self.receiver, self.message)
            print('Message sent successfully')
            # Quit
            smtpObj.quit()
        else:
            print('Server provider was not found')

    '''
    Send by date method will all a user to send an email
    Scheduled to a specific date

    Attributes:
        - sender: Email of the sender
        - receiver: Email of the receiver
        - text: Contain of the message from the user
        - sdate(schedule_date): Schedule date will set a time to send the email 
    '''
    def send_by_date(self, sender, receiver, message, sdate):
        return None

send_mailer = SendMailer('juliushirwa@yahoo.fr', '0788562619', 'juliushirwa@yahoo.fr', 'Get out man')

send_mailer.send('juliushirwa@yahoo.fr', '0788562619', 'juliushirwa@yahoo.fr', 'Get out man')