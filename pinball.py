import requests

base = "https://api.telegram.org/bot"
token = "921903489:AAHoGRwVcOuWfi7QG9EIOTo9c05fF33Q3ss"
method = "sendMessage"
jin_id = "592357679"
jae_id = "776307592"
text = "새로운 일정이 생겼어요"
url1 = base + token + "/" + method + "?" + "chat_id=" + jin_id + "&" + "text=" + text
url2 = base + token + "/" + method + "?" + "chat_id=" + jae_id + "&" + "text=" + text
response1 = requests.get(url1)
response2 = requests.get(url2)
# print(response1)
# print(response2)