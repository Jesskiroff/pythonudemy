# import math

# def paint_calc(height, width, cover):
#     num_cans = math.ceil((height * width)/ cover)
#     # round_cans = math.ceil(num_cans)
#     print (f"You'll need {num_cans} cans of paint. ")
# # Define a function called paint_calc() above
# test_h = 4 #int(input()) # Height of wall (m)
# test_w = 5 #int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

import math
num_height = int(input("What is the height?"))
num_width = int(input("What is the width? "))
cover = 5

def paint_calc (height=num_height, width=num_width, cover=cover):
    number_of_cans = math.ceil((height*width)/ cover)
    print(f"You'll need {number_of_cans} cans of paint")
paint_calc()