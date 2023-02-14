from models.Message import Message
import json
import requests

class LNS:
    def __init__(self, configPath: str):
        with open(configPath) as configFile:
            config = json.load(configFile)
            self.addMessageLambda = config["addMessageLambdaEndpoint"]
            self.listMessageLambda = config["listMessageLambdaEndpoint"]
    
    def addMessage(self, message: Message) -> bool:
        res = requests.post(self.addMessageLambda, json=message.toJson())        
        return res.status_code == 200

    def listMessage(self):
        res = requests.get(self.listMessageLambda)
        
        msgList = []
        for msg in res.json()["messages"]:
            msgList.append(Message.fromJson(msg))

        return msgList
        
