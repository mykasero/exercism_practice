base = [ 8, 16, 12, 32, 28,4, 23]
half1 = []
half2 = []
base.sort()
main = base
iter1 = 0
number_to_find = 23
number_found = False

main_center = main[int((len(main)/2))]

while iter1>len(main)/2:
    if number_to_find == main_center:
        number_found = True
        print("Y")
        break
    elif number_to_find < main_center:
        half1.append(main[main.index(main_center)-iter1])
        iter1+=1
    elif number_to_find > main_center:
        half2.append(main[main.index(main_center)+iter1])
        iter1+=1
#     # main = [0]

print(half1,half2,main_center)