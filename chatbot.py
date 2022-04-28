import random

hellow = ["hi","is anyone there?","hello","good day","hello there"]
bye = ["tata","see you later","bye","goodbye","i am leaving","have a good day"]
hoare = ["how are you","whats up","how you doing"]
name = ["whats your name","what is your name","do you have any name","what should i call you","name"]
menu = ["whats is on menu","i want to buy something","what do you recommend","could i get you something"]
hours = ["when are you guys open","what are your hours", "hours of operation","time",]

print("***************__**********\n")

while True:
    a = input('User Said -')

    if a.lower() in hellow:
        botans = ["Hello !","hi","hi there","welcome"]
        print('Bot Said - '+random.choice(botans)+'\n')

    elif a.lower() in bye:
        botans = ["sad to see you go:(","bye","miss you"]
        print('Bot said - '+random.choice(botans)+'\n')

    elif a.lower() in hoare:
        botans = ["i am fine","happy","i am excited","good"]
        print('Bot said - '+random.choice(botans)+'\n')

    elif a.lower() in name:
        botans = ["my name is abc","you can call me abd","myself priy"]
        print('Bot said - '+random.choice(botans)+'\n')

    elif a.lower() in menu:
        botans = ["everything that you want","lunch","breakfast","dinner"]
        print('Bot said - '+random.choice(botans)+'\n')

    elif a.lower() in hours:
        botans = ["we are open till 3pm","24x7","8pm to 3am"]
        print('Bot said - '+random.choice(botans)+'\n')

    else:
        print('Bot said - Sorry what?''\n')
