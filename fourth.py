from collections import Counter
test_list = [1,2,3,4,5,6,7,8,9]
input_list = [1,2,8,9,12,46,76,82,15,20,30]
s = [(x) for x in test_list for y in input_list if y%x==0]
print(dict(Counter(s)))