import os, sys, fileinput, time, math

buf = []
disp = []
tilt = 0
m = 0
PI = 3.14159265359
PL = '\033[1A'
NL = '\033[1B'
CLL = ''

def resetter():
    global PL
    global CLL
    for l in buf:
        CLL += PL


def padnadd():
    for i in range(len(buf)):
        s = buf.pop(0)
        buf.append(s.ljust(m))


def flipper():
    global tilt
    global PI
    global CLL
    disp.clear()

    theta = math.cos(tilt * PI / 180)
    for l in buf:
        if theta > 0:
            i = round(len(l)*(1-theta)/2)
            disp.append(l[i:len(l)-i].ljust(m).center(5*m))
        else:
            i = round(len(l)*(1-theta)/2)
            disp.append(l[i:-i:-1].rjust(m).center(3*m))
    tilt += 8
    tilt %= 360


if __name__ == '__main__':
    m = 0
    xf = input()
    for line in fileinput.input(files=xf + '.txt'):
        buf.append(line[:-1])
        if m < len(line):
            m = len(line)

    resetter()
    #padnadd()
    os.system('cls')
    sys.stdout.write('\n\n\n')
    while 1:
        flipper()
        [sys.stdout.write(l+'\n') for l in disp]
        sys.stdout.flush()
        #For best visual use 0.04
        time.sleep(0.05)
        sys.stdout.write(CLL)
        sys.stdout.flush()