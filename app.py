from chatbot import _predict_class,_get_response

from flask import Flask, render_template, request

app = Flask(__name__)

class chats:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

conversation = []
conversation.append(chats("bot","Hi, how may I help you?"))
@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method =="POST":
        message = request.form['inputField']
        if message != "":
            conversation.append(chats("human",message))
            ints = _predict_class(message)
            res = _get_response(ints)
            conversation.append(chats("bot",res))
        elif message == "":
            conversation.clear()
            conversation.append(chats("bot","Hi, how may I help you?"))
    return render_template('home.html',conversation=conversation)

# if __name__ == "__main__":
#     app.run(debug=False,port=8000)