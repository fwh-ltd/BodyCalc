# BodyCalc

## Description
---

**BodyCalc** is a simple application for women to calculate things like BMI (Body Mass Index) and Body Shape, and 
can also be used to approximate things like Breast Size, Butt Size and Body Type.

It is _not_ designed to be 100% accurate, and probably _never_ will be, though it strives to be as accurate as is possible.

All measurements must be entered to get complete results. However, you can calculate some items individually.

## How to use
```
#python3 BodyCalc.py
-W [--weight] : weight in kilograms
-C [--height] : height in centimeters
-b [--bust]   : bust in inches
-c [--cup]    : cup size, one of: AA A B C D DD DDD E EE EEE F FF G GGG H HH I III J JJ K
-w [--waist]  : waist in inches
-h [--hip]    : hip in inches
```

```
# python3 BodyCalc.py -b 36 -w 24 -C 170 -K 52 -c DD
{"bmi": 17, "body_shape": "apple", "body_description": "skinny", "butt_description": "small", "tits_description": "large", "tits_multiplier": 4}
```

