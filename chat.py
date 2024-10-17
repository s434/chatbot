import random
import json
from gtts import gTTS
import os
import torch

from model import NeuralNet
from chatbot.nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')



with open('pre trained.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


bot_name = "MoviFia"
#print("Let's chat! (type 'quit' to exit)")
def get_response(msg):
    language = "en"
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                x = random.choice(intent['responses'])
                
                myobj = gTTS(text=x, lang=language, slow=False)
                # Saving the converted audio in a mp3 file named
                # welcome 
                myobj.save("welcome.mp3")
                # Playing the converted file
                os.system("start welcome.mp3")
                return x
    else:
        y = "I do not understand"
        myobj = gTTS(text=y, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("start welcome.mp3")
        return "I do not understand..."

def image(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return tag
    







   







