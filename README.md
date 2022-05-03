# Fuzzing
Identify communications with meaningless content on the SSH protocol
Programming, Fuzzing and Thinking
## Writing language:
Python 3.8
## introduction:
In this task we were asked to identify a validity that produces full communication in meaningless content on the SSH protocol. The goal was to build a Peyton script that detects this attack, and prints to the screen: "Fuzzing detected". I used the scape library for Peyton to listen to the above media and identify the attack.
Details of the plans:
# Fuzzing.py:
In this program I wrote my solution to the task, the program will use the sniff function to "branch" into packages and provide information about them. Once the packages are captured they will be sent to a function that will analyze and check if the contents of the package are meaningful and use the SSH protocol correctly, if the program does not know how to decrypt it, print to the user: "Fuzzing detected", and perform an exit by exit.
# server.py:
To test the program I wrote Fuzzing.py I wrote another program in which I created scapy packages with ssh protocol and sent packages that would be caught by the "branch" of the program Fuzzing.py for packages of the above type. .


## Using important libraries in the task:

# scapy:
Scapy is a Python software that allows the user to send, sniff and analyze and forge network packets. This capability enables the construction of tools that can investigate, scan or attack networks. In other words, Scapy is a powerful interactive packet manipulation program.
Purpose of use: To listen to the media and that I can stop the program if there is an attack. In addition, the function allows access to the different layers of the package and I used this to decrypt the sent package and check what I was asked for.
# Enchant:
Enchant is a module in python that is used to check the spelling of a word, giving suggestions for correcting words. It also gives contrast and synonyms of words. It checks if there is a word in the dictionary or not

Purpose of use: To check if the content of the word contains an illogical sequence of letters, if what is sent is probably an attack, then the program will be closed.

## Run (in Linux):
Make sure you have python3-enchant
If you have not run the following commands in the terminal:
sudo apt-get update
sudo apt-get install python3-enchant
Activate the Fuzzing.py program by typing the following line in the terminal:
sudo python3 ./Fuzzing.py
To test the program and see that it does detect meaningless communication, type the following line of code from another terminal to run server.py:
sudo python3 ./server.py
