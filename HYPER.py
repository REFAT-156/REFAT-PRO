import os, platform, time, sys
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)
xoss('\n\x1b[1;37m[●] Checking Update........✔️✔️');time.sleep(0.5)
def Update():
    exit('\033[1;31m[●] Commands On Update Please Wait For Update ❤ ')
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            xoss("\x1b[1;92m[●] Congratulations ! Your Device Support this Tools 🍼🙂")
            xoss('\x1b[1;94m[●] Follow My Github First 🎈')
            os.system('xdg-open https://github.com/REFAT-156')
            from HYPER import refat
            refat()
        elif bit == '32bit':
            xoss("\n\x1b[1;92m[●] Congratulations ! Your Device Support this Tools 🍼🙂")
            xoss('\x1b[1;94m[●] Follow My Github First 🎈')
            os.system('xdg-open https://github.com/REFAT-156')
            from HYPER import refat
            refat()
        else:
            exit('\033[1;31m[●] Connection & Network Error 🤕')
Run()
