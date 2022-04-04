def func_0(start_num):
    start_num +=1
    return func_1(start_num)

def func_1(start_num):
    start_num +=1
    return start_num
    
start_num = 1 #Int are inmutable values
print(f"start num\t-> {start_num}")
finish_num = func_0(start_num)
print(f"calc'd num\t-> {finish_num}")
print(f"start num\t-> {start_num}")

    