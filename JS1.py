from math import sqrt
from copy import copy

final_number = 30

#this is the initial list
initial_list = list(range(2, final_number+1))
prime_list = []

#get and store all prime factors till final nnumber in prime_list
for i in initial_list:
    prime = True
    for div in range(2, int(sqrt(i)+1)):
        if i%div == 0:
            prime = False
    if(prime):
        prime_list.append(i)

#based on the idea that for all numbers whose second multiple is greater than the largest number
#need to be in the final list as they cannot be included in any combination
def return_intermediate_lists(prime_list, max_number):
    final_list = []
    intermediate_list = []
    for number in prime_list:
        if number*2 > max_number:
            final_list.append(number)
        else:
            intermediate_list.append(number)
    return intermediate_list, final_list


inter_list, final_list = return_intermediate_lists(prime_list, final_number)
print(inter_list)
print(final_list)
max_sum = 0
output_list = []

def include_number_and_maximize(inter_list, number, max_num, final_list):
    new_list = copy(inter_list)
    my_dict = {x:0 for x in inter_list}
    key_sets = 0
    for key in my_dict:
        if number % key == 0:
            my_dict[key] += 1
            key_sets += 1
            new_list.remove(key)
    new_list.append(number)
    sum1 = sum(new_list)
    max_sum_with_number = sum1
    for factor in reversed(range(2, max_num+1)):
        if factor == number or factor in final_list:
            continue
        add = True
        for key in my_dict:
            if factor % key == 0:
                if my_dict[key] > 0:
                    add = False
                    break
        if(add):
            new_list.append(factor)
            for key in my_dict:
                if factor % key == 0:
                    my_dict[key] += 1
                    key_sets += 1
                    new_list.remove(key)
            max_sum_with_number = max(sum(new_list), max_sum_with_number)
        if key_sets == len(my_dict):
            break
    new_list += final_list
    max_sum_with_number = sum(new_list)
    return new_list, max_sum_with_number

for number in range(2, final_number+1):
    if number in final_list:
        continue
    op_list, inter_sum = include_number_and_maximize(inter_list, number, 30, final_list)

    if inter_sum > max_sum:
        max_sum = inter_sum
        output_list = op_list
        print("---------------")
        print("maximizing for {}".format(number))
        print("list: {} sum: {}".format(output_list, inter_sum))

print("\n")
print("final list is ", output_list)
print("final sum is", max_sum)

