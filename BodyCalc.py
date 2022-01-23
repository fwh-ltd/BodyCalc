import getopt
import json
import sys
import math
import os

opt = dict()

def usage():
    print("-W [--weight] : weight in kilograms")
    print("-C [--height] : height in centimeters")
    print("-b [--bust]   : bust in inches")
    print("-c [--cup]    : cup size, one of: AA A B C D DD DDD E EE EEE F FF G GGG H HH I III J JJ K")
    print("-w [--waist]  : waist in inches")
    print("-h [--hip]    : hip in inches")

def run(opt=None):
    weight = 0
    height = 0.001
    bust   = 0
    cup    = ''
    waist  = 0
    hip    = 0

    if '-K' in opt:
        weight = int(opt['-K'])
    if '-C' in opt:
        height = int(opt['-C']) / 100
    if '-b' in opt:
        bust = int(opt['-b'])
    if '-c' in opt:
        cup = str(opt['-c']).upper()
    if '-w' in opt:
        waist = int(opt['-w'])
    if '-h' in opt:
        hip = int(opt['-h'])
    
    bmi = get_bmi(weight, height)
    body_shape = get_body_shape(bust, waist, hip)
    body_type = get_body_type(bmi, body_shape)
    butt_desc = get_butt_desc(hip)
    tits_multiplier = get_breast_multiplier(bust, cup)
    tits_desc = get_breast_desc(tits_multiplier)

    results = dict()
    results['bmi'] = bmi
    results['body_shape'] = body_shape
    results['body_description'] = body_type
    results['butt_description'] = butt_desc
    results['tits_description'] = tits_desc
    results['tits_multiplier'] = tits_multiplier

    print(json.dumps(results))

def get_bmi(weight, height):
    if not (weight and height):
        return 0
    else:
        return math.floor(weight / (height * height))

def get_breast_multiplier(bust, cup):
    breast_multiplier = None
    bust_scale = None
    try:
        bust = int(bust)
        bust_scale = 'below average' if bust < 34 else 'above average'
    except ValueError:
        bust_scale = None

    if cup in [''] and bust_scale == None:
        breast_multiplier = 99
    elif cup in ['AA', 'A'] and bust_scale == 'below average':
        breast_multiplier = 1
    elif cup in ['AA', 'A'] and bust_scale == 'above average':
        breast_multiplier = 2
    elif cup in ['B', 'C'] and bust_scale == 'below average':
        breast_multiplier = 2
    elif cup in ['D'] and bust_scale == 'below average':
        breast_multiplier = 3
    elif cup in ['B', 'C', 'D'] and bust_scale == 'above bverage':
        breast_multiplier = 3
    elif cup in ['DD', 'DDD', 'E', 'EE', 'EEE', 'F', 'FF', 'G'] and bust_scale == 'below average':
        breast_multiplier = 3
    elif cup in ['DD', 'DDD', 'E', 'EE', 'EEE', 'F', 'FF', 'G'] and bust_scale == 'above average':
        breast_multiplier = 4
    elif cup in ['FFF', 'GG', 'GGG', 'H', 'HH', 'I'] and bust_scale == 'below average':
        breast_multiplier = 4
    elif cup in ['FFF', 'GG', 'GGG', 'H', 'HH', 'I'] and bust_scale == 'above average':
        breast_multiplier = 5
    elif cup in ['HHH', 'II', 'III', 'J', 'JJ', 'K'] and bust_scale == 'below average':
        breast_multiplier = 5
    elif cup in ['HHH', 'II', 'III', 'J', 'JJ', 'K'] and bust_scale == 'above average':
        breast_multiplier = 6
    else:
        breast_multiplier = 0
    return breast_multiplier

def get_breast_desc(multiplier):
    breast_desc = None
    if multiplier == 1:
        breast_desc = 'tiny'
    elif multiplier == 2:
        breast_desc = 'small'
    elif multiplier == 3:
        breast_desc = 'medium'
    elif multiplier == 4:
        breast_desc = 'large'
    elif multiplier == 5:
        breast_desc = 'huge'
    elif multiplier == 6:
        breast_desc = 'massive'
    elif multiplier == 99 or multiplier == 0:
        breast_desc = None
    return breast_desc

def get_butt_desc(hip):
    butt_desc = None
    try:
        hip = int(hip)
        if hip <= 32:
            butt_desc = 'small'
        elif hip in range(33, 40):
            butt_desc = 'medium'
        elif hip in range(40, 44):
            butt_desc = 'large'
        elif hip in range(44, 48):
            butt_desc = 'huge'
        elif hip >= 48:
            butt_desc = 'massive'
    except ValueError:
        butt_desc = None
    return butt_desc

def get_body_shape(bust, waist, hip):
    body_shape = None
    try:
        bust = int(bust)
        waist = int(waist)
        hip = int(hip)

        # Waist is at least 25 percent smaller than Hip AND Bust measurement.
        if float(waist) * float(1.25) <= bust & hip:
            body_shape = 'hourglass'

        # Hip measurement is more than 5 percent bigger than Bust measurement.
        elif float(hip) * float(1.05) > bust:
            body_shape = 'pear'

        # Hip measurement is more than 5 percent smaller than Bust measurement.
        elif float(hip) * float(1.05) < bust:
            body_shape = 'apple'

        # Bust, Waist and Hip measurements are within close range.
        high = max(bust, waist, hip)
        low = min(bust, waist, hip)
        difference = high - low

        # Debugging purposes only!
        #print(high, low, difference)

        if difference <= 5:
            body_shape = 'banana'
    except ValueError:
        body_shape = None
    return body_shape

def get_body_type(bmi, shape):
    body_type = None
    type_descriptor = None
    try:
        bmi = int(bmi)
        if bmi == 0:
            return None

        if bmi in range(1, 18):
            type_descriptor = 'A'
        elif bmi in range(18, 23):
            type_descriptor = 'B'
        elif bmi in range(23, 29):
            type_descriptor = 'C'
        elif bmi in range(29, 55):
            type_descriptor = 'D'
        elif bmi >= 55:
            type_descriptor = 'E'

        if shape == None:
            body_type = None
        elif type_descriptor == 'A':
            body_type = 'skinny'
        elif type_descriptor == 'B':
            body_type = 'petite'
        elif type_descriptor == 'C' and shape != 'hourglass':
            body_type = 'average'
        elif type_descriptor == 'C' and shape == 'hourglass':
            body_type = 'curvy'
        elif type_descriptor == 'D' and shape == 'banana':
            body_type = 'BBW'
        elif type_descriptor == 'D' and shape == 'hourglass':
            body_type = 'BBW - curvy'
        elif type_descriptor == 'D' and shape == 'pear':
            body_type = 'BBW - bottom heavy'
        elif type_descriptor == 'D' and shape == 'apple':
            body_type = 'BBW - top heavy'
        elif type_descriptor == 'E' and shape == 'banana' or shape == 'hourglass':
            body_type = 'SSBBW'
        elif type_descriptor == 'E' and shape == 'apple':
            body_type = 'SSBBW - top heavy'
        elif type_descriptor == 'E' and shape == 'pear':
            body_type = 'SSBBW - bottom heavy'
    except ValueError:
        body_type = None
    return body_type

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "C:K:b:c:w:h:", ["height=","weight=","bust=","cup=","waist=","hip="])
        for o, a in opts:
            opt[o] = a
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    run(opt)

if __name__ == "__main__":
    main()

