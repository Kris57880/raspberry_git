import requests
  
def line_message(msg):
    token = "6TRvFcSuN4A8jsnHn5eUqjk9efXcq8OTur1HRFD7VBB"
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
   }
	
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code
