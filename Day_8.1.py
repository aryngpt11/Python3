import math
def paint_calc(height,width,cover):
    area=height*width
    num_of_cans=math.ceil(area/cover)
    print(f"u need {num_of_cans} no. of cans")
test_h=int(input("Enter height: "))
test_w=int(input("Enter width: "))
coverage=5
paint_calc(height=test_h,width=test_w,cover=coverage)