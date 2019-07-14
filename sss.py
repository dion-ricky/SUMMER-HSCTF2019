#!/usr/bin/python3
import telnetlib
import re

def guess(msg_hex, connection, current = 'hsctf{'):
    d = 'abcdefghijklmnopqrstuvwxyz_{}0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ()[]!?+-=:;@#$%^&*\\/.,><"\'~`|'
    while True:
        for a in d:
            tc = current
            tc += a
            print('Testing %s' % tc)
            connection.read_until(b'\n')
            connection.write(tc.encode('ascii'))
            connection.read_until(b'\n')
            raw = connection.read_until(b'\n').decode('utf-8')
            enc = get_encrypted(raw)
            if compare(enc, msg_hex):
                current = tc
                print("Found match: %s" % current)
                break
            if len(enc) > len(msg_hex):
                return

def get_message(raw):
    return re.search('message: (.*)\n', raw).group(1)

def get_encrypted(raw):
    return re.search('Encrypted: (.*)\n', raw).group(1)

def compare(enc, msg):
    if len(enc) > len(msg):
        return None
    l = len(enc)
    return enc == msg[:l]

def main():
    t = telnetlib.Telnet('crypto.hsctf.com', 8111)
    _raw = t.read_until(b'encrypt: ').decode('utf-8') # this contains the encrypted message
    msg = get_message(_raw)

    t.write('hsctf{'.encode('ascii')) # verify

    t.read_until(b'\n')

    if compare(get_encrypted(t.read_until(b'\n').decode('utf-8')), msg):
        guess(msg, t, 'hsctf{h0w_d3d_y3u_de3cryP4_th3_s1p3R_s3cuR3_m355a9e')

if __name__ == '__main__':
    main()
