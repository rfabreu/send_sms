# # How to write a python script to send automatic sms?   
# from flask import Flask, request
# from twilio import twiml

# app = Flask(__name__)

# @app.route('/sms', methods=['POST']) 
# def sms():
#     number = request.form['From']
#     message_body = request.form['Body']

#     resp = twiml.Response()
#     resp.message('Hello {}, you said: {}'.format(number, message_body))
#     return str(resp)   

# if __name__ == '__main__':
#     app.run()

# print('Hello World!')


import requests

resp = requests.post('https://textbelt.com/text', {
  'phone': '4169853788',
  'message': 'Daily test SMS.\nConfirm delivey!',
  'key': 'textbelt',
})
print(resp.json())