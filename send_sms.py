import requests

resp = requests.post('https://textbelt.com/text', {
  'phone': '4169853788',
  'message': 'Daily SMS check.\nConfirm delivey!',
  'key': 'textbelt',
})
print(resp.json())