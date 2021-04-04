import requests

params = {
  "request": {
    "command": "ладно",
    "original_utterance": "ладно",
    "payload": {},

  },
  "session": {
    "message_id": 2,
    "user_id": "1",
    "new": False
  },
  "version": "1.0"
}

s = requests.post("https://flask-alisa-yandex.herokuapp.com/post", json=params)
print(s.json())
