# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    input_int = None
    sum = 0

    while input_int != 0:
        input_int = int(input("Please enter a number (enter 0 to stop): "))
        sum += input_int
        if sum >= 1000:
            break5
    
    return sum

if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
