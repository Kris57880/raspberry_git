import requests
  
def line_message(msg):
    token = "6TRvFcSuN4A8jsnHn5eUqjk9efXcq8OTur1HRFD7VBB"
    token2 = "zle1Bi1MvdQEW390Vf5WqM6tLdb0SaOksYONslBh3tM"
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
   }
    headers2 =  {
        "Authorization": "Bearer " + token2, 
        "Content-Type" : "application/x-www-form-urlencoded"
   }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers2, params = payload)
    return r.status_code
