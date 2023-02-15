import os
import requests
# import smtplib
# from email.mime.text import MIMEText

# SET UP API URL AND PARAMETERS TO SEND SMS
# url = 'https://textbelt.com/text' # UPDATE THIS TO USE ENV VARIABLE
# API_KEY = os.getenv('TEXT_API_KEY') or os.getenv('secrets.TEXT_API_KEY') # 'textbelt'
# phone = os.getenv('PHONE_NUMBER') or os.getenv('secrets.PHONE_NUMBER')

# RETRIEVE EMAIL SETTINGS FOR CONFIRMATION
# smtp_server = os.environ.get('SMPT_SERVER') or os.environ.get('secrets.SMPT_SERVER')
# smtp_port = os.environ.get('SMTP_PORT') or os.environ.get('secrets.SMTP_PORT')
# smtp_username = os.environ.get('SMTP_USERNAME') or os.environ.get('secrets.SMTP_USERNAME')
# smtp_password = os.environ.get('SMTP_PASSWORD') or os.environ.get('secrets.SMTP_PASSWORD')
# from_email = os.environ.get('FROM_EMAIL') or os.environ.get('secrets.FROM_EMAIL')
# to_email = os.environ.get('TO_EMAIL') or os.environ.get('secrets.TO_EMAIL')

# SEND SMS USING THE TEXTBELT API

# resp = requests.post('https://textbelt.com/text', {
#   'phone': '4169853788',
#   'message': 'Daily SMS check.\nConfirm delivey!',
#   'key': 'textbelt',
#   })
# if resp.json()['success']:
  # print('SMS sent successfully!\nCheck the email.')

  # SEND EMAIL CONFIRMATION
  # message = MIMEText('SMS was sent successfully to live system.\nCheck to confirm delivery!')
  # message['From'] = from_email
  # message['To'] = to_email
  # message['Subject'] = 'SMS system check'

  # with smtplib.SMTP(smtp_server, smtp_port) as server:
  #   server.connect(smtp_server, smtp_port)
  #   server.starttls()
  #   server.login(smtp_username, smtp_password)
  #   server.sendmail(from_email, to_email, message.as_string())

#   print('Success check message sent!')
# else:
  # SEND EMAIL SMS DELIVERY FAILURE
  # message = MIMEText('Auto SMS failed.\nCheck working conditions!')
  # message['From'] = from_email
  # message['To'] = to_email
  # message['Subject'] = 'SMS system check'

  # with smtplib.SMTP(smtp_server, smtp_port) as server:
  #   server.connect(smtp_server, smtp_port)
  #   server.starttls()
  #   server.login(smtp_username, smtp_password)
  #   server.sendmail(from_email, to_email, message.as_string())

  # print('SMS failure message sent!')


# FROM THIS POINT ONWARDS THIS IS A TEMP TEST VERSION
resp = requests.post('https://textbelt.com/text', {
  'phone': '4169853788',
  'message': 'Daily SMS check.\nConfirm delivey!',
  'key': 'textbelt',
})
print(resp.json())