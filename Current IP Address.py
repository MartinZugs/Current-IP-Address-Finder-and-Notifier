from urllib.request import urlopen
from twilio.rest import Client
import re
import smtplib

# Twilio login and info
account_sid = '' #Insert your account SID from Twilio here
auth_token = '' #Insert your auth token from Twilio here

# Setting up Twilio text
client = Client(account_sid, auth_token)

# Login credentials for email
from_address = '' #Insert the email address you wish to send from, I recommend using Gmail
to_address = '' #Insert the email address you wish to send to
subject = 'Current IP' #This is the subject line of the email
username = '' #Insert the username of the email you are sending from
password = '' #Insert the password for the email you are sending from

# Website to get IP address
url = 'http://checkip.dyndns.com/' #Website that provides youre current IP in simple text form

 # Open up the url listed above, read contents of page, and extract IP
request = urlopen(url).read().decode('utf-8')
currentIP = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", request)
currentIP = str(currentIP)
print ("IP address is: ", currentIP)

# Function to send the email
def send_email(currentIP):
    # Body of email
    body_text = currentIP
    msg = '\r\n'.join(['To: %s' % to_address,
                       'From: %s' % from_address,
                       'Subject: %s' % subject,
                       '', body_text])

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com:587') #Only works for gmail
    server.starttls()
    server.login(username, password)
    server.sendmail(from_address, to_address, msg)
    server.quit()

# Function to send the text
def send_text(currentIP):
    message = client.api.account.messages.create(
    to= "", #Insert your personal number here
    from_= "", #Insert the number Twilio gave you here
    body= "Your current IP address is: " + currentIP)

# Open up last_ip.txt and extract the contents
with open('last_ip.txt', 'rt') as last_ip:
    last_ip = last_ip.read()

# Check if IP has changed and send email and text
if last_ip == currentIP:
    print("No change in IP address.")
else:
    print("There is a new IP address.")
    with open('last_ip.txt', 'wt') as last_ip:
        last_ip.write(currentIP)
    print("New IP written to text file.")
    send_email(currentIP)
    send_text(currentIP)
    

