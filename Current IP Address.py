from urllib.request import urlopen
import re
import smtplib

# Login credentials for email
from_address = 'MartinIPAddress@gmail.com'
to_address = 'MartinIPAddress@gmail.com'
subject = 'Current IP'
username = 'MartinIPAddress'
password = 'MZIP1208!'

# Website to get IP address
url = 'http://checkip.dyndns.com/'

# Open up the url listed above, read contents of page, and extract IP
request = urlopen(url).read().decode('utf-8')
currentIP = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", request)
currentIP = str(currentIP)
print ("IP address is: ", currentIP)

def send_email(currentIP):
    # Body of email
    body_text = currentIP
    msg = '\r\n'.join(['To: %s' % to_address,
                       'From: %s' % from_address,
                       'Subject: %s' % subject,
                       '', body_text])

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(from_address, to_address, msg)
    server.quit()

# Open up last_ip.txt and extract the contents
with open('last_ip.txt', 'rt') as last_ip:
    last_ip = last_ip.read()

# Check if IP has changed
if last_ip == currentIP:
    print("No change in IP address.")
else:
    print("There is a new IP address.")
    with open('last_ip.txt', 'wt') as last_ip:
        last_ip.write(currentIP)
    print("New IP written to text file.")
    send_email(currentIP)
    

