import math

def get_all(height, weight, bust, cup, waist, hip):
    results = dict()

    bmi = get_bmi(weight, height)
    results['bmi'] = bmi
    bmi_type = get_bmi_type(bmi)
    results['bmi_type'] = bmi_type

    body_shape = get_body_shape(bust, waist, hip)
    results['body_shape'] = body_shape

    body_type = get_body_type(bmi_type, body_shape)
    results['body_type'] = body_type

    butt_type = get_butt_type(hip)
    results['butt_type'] = butt_type

    bust_scale = get_bust_scale(bust)
    results['bust_scale'] = bust_scale

    tits_scale = get_tits_scale(bust_scale, cup)
    results['tits_scale'] = tits_scale

    tits_type = get_tits_type(tits_scale)
    results['tits_type'] = tits_type

    return results


def get_bmi(weight, height):
    if not (weight and height):
        return 0
    else:
        bmi = weight / (height * height)
        floored = math.floor(bmi)
        return floored
       
def get_bust_scale(bust):
    try:
        bust = int(bust)
        return 'small' if bust < 34 else 'large'
    except ValueError:
        return None

def get_tits_scale(bust_scale, cup):
    if cup in [''] and bust_scale == None:
        return 99
    elif cup in ['AA', 'A'] and bust_scale == 'small':
        return 1
    elif cup in ['AA', 'A'] and bust_scale == 'large':
        return 2
    elif cup in ['B', 'C'] and bust_scale == 'small':
        return 2
    elif cup in ['D'] and bust_scale == 'small':
        return 3
    elif cup in ['B', 'C', 'D'] and bust_scale == 'large':
        return 3
    elif cup in ['DD', 'DDD', 'E', 'EE', 'EEE', 'F', 'FF', 'G'] and bust_scale == 'small':
        return 3
    elif cup in ['DD', 'DDD', 'E', 'EE', 'EEE', 'F', 'FF', 'G'] and bust_scale == 'large':
        return 4
    elif cup in ['FFF', 'GG', 'GGG', 'H', 'HH', 'I'] and bust_scale == 'small':
        return 4
    elif cup in ['FFF', 'GG', 'GGG', 'H', 'HH', 'I'] and bust_scale == 'large':
        return 5
    elif cup in ['HHH', 'II', 'III', 'J', 'JJ', 'K'] and bust_scale == 'small':
        return 5
    elif cup in ['HHH', 'II', 'III', 'J', 'JJ', 'K'] and bust_scale == 'large':
        return 6
    else:
        return 0

def get_tits_type(scale):
    if scale == 1:
        return 'tiny'
    elif scale == 2:
        return 'small'
    elif scale == 3:
        return 'medium'
    elif scale == 4:
        return 'large'
    elif scale == 5:
        return 'huge'
    elif scale == 6:
        return 'massive'
    elif scale == 99 or scale == 0:
        return None
    else:
        return None

def get_butt_type(hip):
    try:
        hip = int(hip)
        if hip <= 32:
            return 'small'
        elif hip in range(33, 40):
            return 'medium'
        elif hip in range(40, 44):
            return 'large'
        elif hip in range(44, 48):
            return 'huge'
        elif hip >= 48:
            return 'massive'
    except ValueError:
        return None
    return None

def get_body_shape(bust, waist, hip):
    try:
        bust = int(bust)
        waist = int(waist)
        hip = int(hip)

        # Waist is at least 25 percent smaller than Hip AND Bust measurement.
        if float(waist) * float(1.25) <= bust & hip:
            return 'hourglass'

        # Hip measurement is more than 5 percent bigger than Bust measurement.
        elif float(hip) * float(1.05) > bust:
            return 'pear'

        # Hip measurement is more than 5 percent smaller than Bust measurement.
        elif float(hip) * float(1.05) < bust:
            return 'apple'

        # Bust, Waist and Hip measurements are within close range.
        high = max(bust, waist, hip)
        low = min(bust, waist, hip)
        difference = high - low

        # Debugging purposes only!
        #print(high, low, difference)

        if difference <= 5:
            return 'banana'
    except ValueError:
        return None

def get_bmi_type(bmi):
    bmi = int(bmi)
    if bmi == 0:
        return None
    if bmi in range(1, 18):
        return 'A'
    elif bmi in range(18, 23):
        return 'B'
    elif bmi in range(23, 29):
        return 'C'
    elif bmi in range(29, 55):
        return 'D'
    elif bmi >= 55:
        return 'E'
    return None

def get_body_type(bmi_type, shape):
    try:
        if shape == None:
            return None
        elif bmi_type == 'A':
            return 'skinny'
        elif bmi_type == 'B':
            return 'petite'
        elif bmi_type == 'C' and shape != 'hourglass':
            return 'average'
        elif bmi_type == 'C' and shape == 'hourglass':
            return 'curvy'
        elif bmi_type == 'D' and shape == 'banana':
            return 'BBW'
        elif bmi_type == 'D' and shape == 'hourglass':
            return 'BBW - curvy'
        elif bmi_type == 'D' and shape == 'pear':
            return 'BBW - bottom heavy'
        elif bmi_type == 'D' and shape == 'apple':
            return 'BBW - top heavy'
        elif bmi_type == 'E' and (shape == 'banana' or shape == 'hourglass'):
            return 'SSBBW'
        elif bmi_type == 'E' and shape == 'apple':
            return 'SSBBW - top heavy'
        elif bmi_type == 'E' and shape == 'pear':
            return 'SSBBW - bottom heavy'
        else:
            return None
    except ValueError:
        return None
