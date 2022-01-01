DIGIT_MAP = {
    "zero" : '0',
    "one" : '1',
    "two" : '2',
    "three" : '3',
    "four" : '4',
    "five" :'5',
    "six" : '6',
    "seven" : '7'
}



def convert(s):

    try:
        number = ' '
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"conversion succeeded! x = {x}")
    #except KeyError:
     #   print("conversion failed")
      #  x = -1
    #except TypeError:
      #  print("conversion failed")
      #  x = -2
    #return x
    except(KeyError, TypeError):
        print("conversion failed")
        x = -1
    print(x)

convert("one three three seven".split())

convert("one three double".split())

convert(512)