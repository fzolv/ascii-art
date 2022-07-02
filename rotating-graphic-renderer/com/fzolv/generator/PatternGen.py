import os
import sys
import fileinput
CURRENT = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(CURRENT)
sys.path.append(PARENT)
from graphic.Renderer import render

appender = []


def readfile(alph):
    buf = []
    m = 0
    for line in fileinput.input(files=PARENT + '\\'+alph+'.txt'):
        buf.append(line[:-1])
        if m < len(line):
            m = len(line)
    #[print(l) for l in buf]
    return [buf, m]


def padnadd(ar):
    global appender
    for i in range(len(ar[0])):
        s = ar[0].pop(0)
        s = s.ljust(ar[1])
        #s += ' '
        if len(appender) <= i:
            appender.append('')
        appender[i] += s


if __name__ == '__main__':
    str = input()
    for c in str:
        padnadd(readfile(c))
    render(appender)
