#!/usr/bin/env python

import re
import sys

BYR = 'byr'
IYR = 'iyr'
EYR = 'eyr'
HGT = 'hgt'
HCL = 'hcl'
ECL = 'ecl'
ECL_ACCEPTED = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
PID = 'pid'
CID = 'cid'


def read(in_file):
    ''' Reads data for day 04. '''
    with open(in_file) as f:
        data = [x.strip() for x in f.readlines()]

    passports = []
    passport = {}
    for line in data:
        if not line:
            passports.append(passport)
            passport = {}
        else:
            fields = line.split()
            for field in fields:
                key, value = field.split(':')
                passport[key] = value
    passports.append(passport)
    return passports


def valid_passport_1(passport):
    ''' Checks one passport to be valid for part 1. '''
    return len(passport) == 8 or (len(passport) == 7 and CID not in passport)


def valid_passport_2(passport):
    ''' Checks one passport to be valid for part 2. '''
    if not valid_passport_1(passport):
        return False

    byr = int(passport[BYR])
    if byr < 1920 or byr > 2002:
        return False

    iyr = int(passport[IYR])
    if iyr < 2010 or iyr > 2020:
        return False

    eyr = int(passport[EYR])
    if eyr < 2020 or eyr > 2030:
        return False

    hgt = passport[HGT]
    unit = hgt[-2:]
    try:
        val = int(hgt[:-2])
    except ValueError:
        return False
    if unit not in ['in', 'cm']:
        return False
    if unit == 'cm' and (val < 150 or val > 193):
        return False
    if unit == 'in' and (val < 59 or val > 76):
        return False

    r_hcl = re.compile('^#[0-9a-f]{6}$')
    if not r_hcl.match(passport[HCL]):
        return False

    if passport[ECL] not in ECL_ACCEPTED:
        return False

    r_pid = re.compile('^[0-9]{9}$')
    if not r_pid.match(passport[PID]):
        return False

    return True


def solve(in_file, valid_passport_function):
    ''' Solves day 04. '''
    passports = read(in_file)
    return sum(map(valid_passport_function, passports))


if __name__ == '__main__':
    print("part 1")
    print(solve('04test.in', valid_passport_1))
    print(solve('04.in', valid_passport_1))

    print("part 2")
    print(solve('04test.in', valid_passport_2))
    print(solve('04.in', valid_passport_2))

    sys.exit(0)