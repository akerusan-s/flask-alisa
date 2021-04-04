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

s = requests.post("http://127.0.0.1:5000/post", json=params)
print(s.json())
