#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
KeypadRemote F8ASB 2020 // information sur F8ASB.COM
PossibilitĂ© de faire des QSY avec un clavier numerique USB
DeveloppĂ© pour les non-voyants
73 de F8ASB Juan
'''

import keyboard
import time

def main():

    while True:
        key=keyboard.read_key()
        print(key)
        time.sleep(0.5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass

