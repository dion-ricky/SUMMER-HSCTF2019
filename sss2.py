#!/usr/bin/python3
import telnetlib
import re

def get_message(raw):
    return re.search('message: (.*)\n', raw).group(1)

def find(msg):
    while True:
        t = telnetlib.Telnet('crypto.hsctf.com', 8111)
        raw = t.read_until(b'encrypt: ').decode('utf-8')
        _msg = get_message(raw)
        print("Got: %s" % _msg)
        if _msg == msg:
            print("Found: %s" % _msg)
            return

def main():
    t = telnetlib.Telnet('crypto.hsctf.com', 8111)
    _raw = t.read_until(b'encrypt: ').decode('utf-8') # this contains the encrypted message
    msg = get_message(_raw)
    print("Finding: %s" % msg)
    find(msg)

if __name__ == '__main__':
    main()
