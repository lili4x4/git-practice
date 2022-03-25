def most_common_value(number_list):
    """ returns the most common element of the list
    """
    frequency_index = {}
    max_frequency = -1
    most_common_value = None
    for num in number_list:
        if frequency_index.get(num):
            frequency_index[num] += 1
        else:
            frequency_index[num] = 1

        if max_frequency < frequency_index[num]:
            max_frequency = frequency_index[num]
            most_common_value = num
    

    return most_common_value

<<<<<<< HEAD
<<<<<<< HEAD
def tyrah_print_num(most_common_value):
    printing = (most_common_value *3)

    return printing

    tyrah_print_num(most_common_value)

=======
=======
def intro(name, state):
    print(f"Hello, my name is {name} annd I live in {state}!")
    
def lili_rulez():
    print("Lili rulez!")

lili_rulez()
>>>>>>> 53d5b58b36fc5eea1946ad749415c560430d3f06
def print_mochi():
    print("Mmmm, mochi!")
>>>>>>> f8432be7af36f61f9837fad9c0766df5ee67db30

if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
