def digit_match(apples, oranges):
    # Base cases:
    # If both apples and oranges are 0 return 1
    if apples == 0 and oranges == 0:
        return 1
    # If one or both are 1-digit numbers
    elif apples < 10 or oranges < 10:
        if apples % 10 == oranges % 10:
            return 1
        
        return 0
    
    # Recursive Cases
    if apples % 10 == oranges % 10:
        return 1 + digit_match(apples // 10, oranges // 10)
        
    return digit_match(apples // 10, oranges // 10)



# def digit_match(num_1, num_2):
#     if num_1 == 0 and num_2 == 0:
#         return 1
#     return digit_match_helper(num_1, num_2)

# def digit_match_helper(num_1, num_2):
#     if num_1 == 0 or num_2 == 0:
#         return 0
#     if num_1 % 10 == num_2 % 10:
#         return 1 + digit_match_helper(num_1 // 10, num_2 // 10)
#     else:
#         return digit_match_helper(num_1 // 10, num_2 // 10)