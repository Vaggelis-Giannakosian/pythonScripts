import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# read html as a string Template
html = Template(Path('index.html').read_text())

# instantiate email object
email = EmailMessage()
email['from'] = 'Vangelis Giannakosian'
email['to'] = 'e.giannakosian@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

# add html to email
email.set_content(html.substitute(name='Vangelis'), 'html')

# set up email server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # enter google credentials
    username = 'username@gmail.com'
    password = 'supersecretpassword'
    # login to email provider
    smtp.login(username, password)
    # send email
    smtp.send_message(email)
    print('email was sent successfully')


exit()