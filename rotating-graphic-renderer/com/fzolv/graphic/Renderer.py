import os
import sys
import fileinput
import time
import math

CURRENT = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(CURRENT)
sys.path.append(PARENT)

buf = []
disp = []
tilt = 0
m = 0
PI = 3.14159265359
PL = '\033[1A'
NL = '\033[1B'
CLL = ''


def findmax():
    global m
    for line in buf:
        if m < len(line):
            m = len(line)

def resetter():
    global PL
    global CLL
    for i in range(len(buf)):
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
            disp.append(' '*m + rep(l).ljust(m))
        else:
            disp.append(rep(l).rjust(m))
    tilt += 4
    tilt %= 360


def rep(str):
    rp = ''
    p = -100000
    theta = math.cos(tilt * PI / 180)
    n = len(str)
    for i in range(n):
        i_t = i if theta > 0 else n-i-1
        t = round(i_t*theta)
        if p == t:
            continue
        p = t
        rp += str[i_t]
    return rp


def render(buffer):
    global buf
    buf = buffer
    findmax()
    resetter()
    padnadd()
    os.system('cls')
    sys.stdout.write('\n\n\n')
    while 1:
        flipper()
        [sys.stdout.write(l + ' '*10 + '\n') for l in disp]
        sys.stdout.flush()
        #For best visual use 0.04
        time.sleep(0.06)
        sys.stdout.write(CLL)
        sys.stdout.flush()


if __name__ == '__main__':
    m = 0
    xf = input()
    for line in fileinput.input(files=PARENT + '\\' + xf + '.txt'):
        buf.append(line[:-1])

    render(buf)