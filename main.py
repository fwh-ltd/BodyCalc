import getopt
import json
import sys
import bodycalc

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

    results = bodycalc.get_all(height, weight, bust, cup, waist, hip)    
    print(json.dumps(results))

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
