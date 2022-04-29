from scapy.all import *
from scapy.layers.inet import TCP, IP

if __name__ == '__main__':
    good_data1="hello Word"
    send(IP(dst='8.8.8.8') / TCP(dport=22, flags='S') / Raw(load=good_data1))
    good_connected_words="hello Word"
    send(IP(dst='8.8.8.8') / TCP(dport=22, flags='S') / Raw(load=good_connected_words))
    bad_data = "helljjjcjnkczdnoword"
    send(IP(dst='8.8.8.8') / TCP(dport=22, flags='S') / Raw(load=bad_data))
