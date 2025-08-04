def MaximumPairWise(n,numbers):
    '''
    Adds two numbers
    '''
    if n >= 2 and n <= 200000:
        current_number = 0
        for n in numbers:
            if n > current_number:
                current_number = n
        first_num_index = numbers.index(current_number)

        current_number = 0
        for n in numbers:
            if numbers.index(n) != first_num_index and n > current_number:
                current_number = n
        
        second_num_index = numbers.index(current_number)

        return numbers[first_num_index] * numbers[second_num_index]
    
    else:
        print("Input list is not within valid range")
