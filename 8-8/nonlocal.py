#!/usr/bim/python


def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested


F = tester(0)
F('CALI')
F("SANLE")
F("wangtao")
F("LIQIANG")
