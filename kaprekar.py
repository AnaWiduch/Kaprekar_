def kaprekar_step(L):

    a = sorted(L) # Sort the list of numbers in ascending order

    b = ''  # Initialize an empty string to concatenate the sorted numbers


    for i in a:     # Concatenate the sorted numbers into a single string
        b += str(i)


    c = b[::-1]    # Reverse the string to get the number in descending order

    # Convert the strings to integers and calculate the difference between the reversed and original numbers
    return int(c) - int(b)
