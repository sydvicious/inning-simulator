#!/usr/bin/env python

# Author: Syd Polk

import argparse
import sys

parser = argparse.ArgumentParser(description="inning-simmulator.py - print out state of the bases, outs, and runs after a sequence of offense.")
parser.add_argument('files', type=str, nargs='*', help="Files to be parsed. No file implies <stdin>.")

args = parser.parse_args()


class Inning():

    def __init__(self, first_base = False, second_base = False, third_base = False, outs = 0, runs = 0):
        self.first_base = first_base
        self.second_base = second_base
        self.third_base = third_base
        self.outs = outs
        self.runs = runs

    def __unicode__(self):
        bases = 0
        if self.first_base:
            bases += 1
        if self.second_base:
            bases += 10
        if self.third_base:
            bases += 100
        return "Bases: %3d, Outs: %d, Runs: %d" % (bases, self.outs, self.runs)

    def __str__(self):
        bases = 0
        if self.first_base:
            bases += 1
        if self.second_base:
            bases += 10
        if self.third_base:
            bases += 100
        return "Bases: %03d, Outs: %d, Runs: %d" % (bases, self.outs, self.runs)

    def incr_outs(self):
        self.outs += 1
        if self.outs == 3:
            self.first_base = False
            self.second_base = False
            self.third_base = False

    def advance_runners(self):
        if self.third_base:
            self.runs += 1
        if self.second_base:
            self.third_base = True
        else:
            self.third_base = False
        if self.first_base:
            self.second_base = True
        else:
            self.second_base = False
        self.first_base = False

    def batter_to_first_non_forcing(self):
        self.advance_runners()
        self.first_base = True

    def batter_to_first_forcing(self):
        if self.first_base:
            if self.second_base:
                if self.third_base:
                    self.runs += 1
                self.third_base = True
            self.second_base = True
        self.first_base = True


# batter is out. If there are less than three outs, runners advance one base
def out(inning):
    inning.incr_outs()
    if inning.outs < 3:
        inning.advance_runners()


def k(inning):
    inning.incr_outs()


def single(inning):
    inning.batter_to_first_non_forcing()


def double(inning):
    single(inning)
    inning.advance_runners()


def triple(inning):
    double(inning)
    inning.advance_runners()


def hr(inning):
    triple(inning)
    inning.advance_runners()


# batter safe at first; all runners advance one base
def e(inning):
    single(inning)


def bb(inning):
    inning.batter_to_first_forcing()


def hbp(inning):
    inning.batter_to_first_forcing()


actions = {
    'out': out,
    'k': k,
    '1b': single,
    '2b': double,
    '3b': triple,
    'hr': hr,
    'e': e,
    'bb': bb,
    'hbp': hbp
}

def process_file(event_file):
    for line in event_file:
        line = line.strip()

        # Adding comments and blank lines to specification so that test files are easier to write
        if line == '':
            continue
        if line[0] == '#':
            continue

        events = line.split(',')
        inning = Inning()

        for event in events:
            actions[event](inning)

        print(inning)

if __name__ == '__main__':

    files = list()
    if args.files is not None:
        files = args.files

    if len(files) == 0:
        process_file(sys.stdin)
    else:
        for file in files:
            f = open(file, 'r')
            process_file(f)
            f.close()



