import enchant
from scapy.all import *
from scapy.layers.inet import TCP, IP

i = 1  # index for the packet's number


def check_fuzz(pkt):
    """
     This function will check if "Fuzzing detected" has occurred, we will check if there is incorrect use of the protocol; Flags, package length.
      We will also check if we have received an irrational sequence of letters
    """
    global i
    print("Packet number:", str(i))
    i += 1
    print("Package received, the program will check the SSH protocol...")
    # TCP RST Flag: attempts to hijack a TCP connection from https://ipwithease.com/tcp-rst-flag/
    # RST=4
    print("*The program checks the flag of the package")
    if pkt[TCP].flags == 4:
        fuzzing(pkt)

    # taking the data of the packet after removing the first two characters: b' and the last character: '
    data = str(pkt.getlayer(Raw).load)[2:-1]

    # according to this web: https://datatracker.ietf.org/doc/html/rfc4253#section-4.2:
    # The maximum length of the string is 255 characters, including the Carriage Return and Line Feed.
    print("*The program checks the length of the package")
    if len(data) > 255:
        fuzzing(pkt)
    split_dat = data.split(" ")

    # As for the hint given in the task, we will examine whether a manifestly illogical sequence of letters was conveyed in the package
    print("*The program checks the data of the package")
    if check_Fuzzing_detected(split_dat):
        print("The program found an illogical sequence of letters")
        fuzzing(pkt)
    print("")

def check_Fuzzing_detected(data):
    """
    This function will check the hint given in the task: Was a packet of an unreasonable sequence of letters transmitted in the packet?
    :return: bool
    """
    dictionary = enchant.Dict("en_US")  # Dictionaries are created using a language tag which specifies the language
    # to be checked - in this case, “en_US” signifies American English
    line = 1
    word = 1
    Fuzzingdetected = False
    for line_data in data:
        words = line_data.split()
        for word_line in words:
            # Enchant is a module in python which is used to check the spelling of a word, gives suggestions to correct words.
            # Also, gives antonym and synonym of words. It checks whether a word exists in dictionary or not
            exist = dictionary.suggest(word_line)
            if not exist:
                Fuzzingdetected = True
                return Fuzzingdetected
            print("The function found the following logical sequence:", exist)
            word += 1
        line += 1
        word = 1
    return Fuzzingdetected


def fuzzing(pkt):
    """
    This function is activated when the program has detected an attack and will therefore execute an exit
    """
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("-------------Fuzzing detected-------------")
    print('----- SSH detected from IP: ' + str(pkt[IP].dst) + ' ------')
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    exit(0)


if __name__ == '__main__':
    # based on this web for example of packet sniffing using Scapy
    # https://thepacketgeek.com/scapy/sniffing-custom-actions/part-1/
    pkt = sniff(filter="tcp dst port 22", prn=check_fuzz)

"""
readme:
Install python3-enchant
Installing python3-enchant package on Ubuntu is as easy as running the following command on terminal:

sudo apt-get update
sudo apt-get install python3-enchant
"""
