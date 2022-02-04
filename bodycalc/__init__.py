import math

def get_all(height, weight, bust, cup, waist, hip):
    results = dict()

    bmi = get_bmi(weight, height)
    results['bmi'] = bmi
    bmi_type = get_bmi_type(bmi)
    results['bmi_type'] = bmi_type

    body_shape = None
    if bust and waist and hip:
        body_shape = get_body_shape(bust, waist, hip)
    results['body_shape'] = body_shape

    body_type = None
    if bmi_type and body_shape:
        body_type = get_body_type(bmi_type, body_shape)
    results['body_type'] = body_type

    butt_type = None
    if hip:
        butt_type = get_butt_type(hip)
    results['butt_type'] = butt_type

    bust_scale = None
    if bust:
      bust_scale = get_bust_scale(bust)
    results['bust_scale'] = bust_scale

    tits_scale = None
    if bust_scale and cup:
        tits_scale = get_tits_scale(bust_scale, cup)
    results['tits_scale'] = tits_scale

    tits_type = None
    if tits_scale:
        tits_type = get_tits_type(tits_scale)
    results['tits_type'] = tits_type

    waist_hip_ratio = None
    results['waist_hip_type'] = None
    if waist and hip:
        waist_hip_ratio = waist / hip
        #mean 0.718 sd 0.0563
        if waist_hip_ratio > 0.80 :
            results['waist_hip_type'] = 'wide'
        elif waist_hip_ratio < 0.64 :
            results['waist_hip_type'] = 'narrow'
        else:
            results['waist_hip_type'] = 'normal'
    results['waist_hip_ratio'] = waist_hip_ratio

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
        return 1 if bust > 34 else -1
    except ValueError:
        return None

def get_tits_scale(bust_scale, cup):
    if cup in [''] and bust_scale == None:
        return 99
    elif cup in ['AA', 'A'] and bust_scale < 0:
        return 1
    elif cup in ['AA', 'A'] and bust_scale > 0:
        return 2
    elif cup in ['B', 'C'] and bust_scale < 0:
        return 3
    elif cup in ['D'] and bust_scale < 0:
        return 4
    elif cup in ['B', 'C', 'D'] and bust_scale > 0:
        return 3
    elif cup in ['DD', 'DDD', 'E', 'EE', 'EEE', 'F', 'FF', 'G'] and bust_scale < 0:
        return 4
    elif cup in ['DD', 'DDD', 'E', 'EE', 'EEE', 'F', 'FF', 'G'] and bust_scale > 0:
        return 3
    elif cup in ['FFF', 'GG', 'GGG', 'H', 'HH', 'I'] and bust_scale < 0:
        return 5
    elif cup in ['FFF', 'GG', 'GGG', 'H', 'HH', 'I'] and bust_scale > 0:
        return 4
    elif cup in ['HHH', 'II', 'III', 'J', 'JJ', 'K'] and bust_scale < 0:
        return 6
    elif cup in ['HHH', 'II', 'III', 'J', 'JJ', 'K'] and bust_scale > 0:
        return 5
    else:
        return 0

def get_tits_type(tits_scale):
    if tits_scale == 1:
        return 'tiny'
    elif tits_scale == 2:
        return 'small'
    elif tits_scale == 3:
        return 'medium'
    elif tits_scale == 4:
        return 'large'
    elif tits_scale == 5:
        return 'huge'
    elif tits_scale == 6:
        return 'massive'
    elif tits_scale == 99 or tits_scale == 0:
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

        # calculator.net
        if bust - hip <= 1 and hip - bust <= 3.6 and bust - waist >= 9 or hip - waist >= 10:
            return "hourglass"

        # calculator.net
        elif hip - bust >= 3.6 and hip - bust < 10 and hip - waist >= 9:
            return "lower-hourglass"

        # calculator.net
        elif bust - hip > 1 and bust - hip < 10 and bust - waist >= 9:
            return "upper-hourglass"

        # ORIG Waist is at least 25 percent smaller than Hip AND Bust measurement.
        elif float(waist) * float(1.25) <= bust and float(waist) * float(1.25) <= hip:
            return 'hourglass'

        # calculator.net
        elif hip - bust > 2 and hip - waist >= 7:
            return "spoon"

        # calculator.net
        elif hip - bust >= 3.6 and hip - waist < 9:
            return "triangle"

        # ORIG Hip measurement is more than 5 percent bigger than Bust measurement.
        elif float(hip) * float(1.05) > bust:
            return 'pear'

        # calculator.net
        elif bust - hip >= 3.6 and bust - waist < 9:
            return "inverted-triangle"

        # calculator.net
        elif hip - bust < 3.6 and bust - hip < 3.6 and bust - waist < 9 and hip - waist < 10:
            return "rectangle"

        # ORIG Hip measurement is more than 5 percent smaller than Bust measurement.
        elif float(hip) * float(1.05) < bust:
            return 'apple'

        # Bust, Waist and Hip measurements are within close range.
        high = max(bust, waist, hip)
        low = min(bust, waist, hip)
        difference = high - low

        if difference <= 5:
            return 'banana'
    except ValueError:
        return None

def get_bmi_type(bmi):
    bmi = int(bmi)
    if bmi == 0:
        return None
    if bmi in range(1, 18):
        return 'underweight'
    elif bmi in range(18, 23):
        return 'healthy'
    elif bmi in range(23, 29):
        return 'overweight'
    elif bmi in range(29, 55):
        return 'obese'
    elif bmi >= 55:
        return 'extremely-obese'
    return None

def get_body_type(bmi_type, shape):
    try:
        if shape == None:
            return None
        elif bmi_type == 'underweight':
            return 'skinny'
        elif bmi_type == 'healthy':
            return 'petite'
        elif bmi_type == 'overweight' and shape != 'hourglass':
            return 'average'
        elif bmi_type == 'overweight' and shape == 'hourglass':
            return 'curvy'
        elif bmi_type == 'obese' and shape == 'banana':
            return 'BBW'
        elif bmi_type == 'obese' and shape == 'hourglass':
            return 'BBW - curvy'
        elif bmi_type == 'obese' and shape == 'pear':
            return 'BBW - bottom heavy'
        elif bmi_type == 'obese' and shape == 'apple':
            return 'BBW - top heavy'
        elif bmi_type == 'extremely-obese' and (shape == 'banana' or shape == 'hourglass'):
            return 'SSBBW'
        elif bmi_type == 'extremely-obese' and shape == 'apple':
            return 'SSBBW - top heavy'
        elif bmi_type == 'extremely-obese' and shape == 'pear':
            return 'SSBBW - bottom heavy'
        else:
            return None
    except ValueError:
        return None
