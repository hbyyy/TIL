
fizzbuzz_list = [
        'fizz' 
        if i % 3 == 0 else 
        'buzz' 
        if i % 5 == 0 else
        i for i in range(1, 100 +1)]
    
print(fizzbuzz_list)
