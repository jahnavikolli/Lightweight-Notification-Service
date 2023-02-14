from LNS import LNS
from models.Message import Message
import pprint

if __name__ == "__main__":
    cfgPath = "Config.json"
    lns = LNS(cfgPath)

    while True:
        op = int(input("""
                Operations:\n
                1: Add a message to db\n
                2: List the messages from db\n
                select an operation:        
                """))
        
        if op == 1:
            id = input("Enter the id: ")
            value = input("Enter the value: ")
            ttl = input("Enter the time to live(in secs): ")

            lns.addMessage(Message(id, value, ttl))
        elif op == 2:
            msgList = lns.listMessage()
            pprint.pprint(msgList)
        else:
            print("Invalid operation!")
            continue
