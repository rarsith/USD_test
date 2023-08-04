import re

string_data = "-p 0 0 0 -p 0 0 1 -p 0 9 9 -k 1 2 3 4 5 -s 0 2.345 -2.87986 9.33333 -x 2 3 2 -x 4.124234 -4.332234 -5.1123423"

delimiters = ["-p", "-k", "-s", "-x"]

def parse_string_recursive(string_data, delimiters):
    dictio = {}
    '''Parse a string recursively using a list of delimiters'''
    for delimiter in delimiters:
        '''If the delimiter is in the string, split the string at the first instance of the delimiter and recursively call the function on the second half of the string.'''
        if delimiter in string_data:
            '''The split function returns a list of strings. The first element of the list is the string before the delimiter, and the second element is the string after the delimiter.'''
            split_list = string_data.split(delimiter, 1)
            dictio[delimiter] = split_list
            '''The first element of the split list is the string before the delimiter. The second element of the split list is the string after the delimiter. The first element of the split list is added to the list returned by the recursive call to the function.'''
            return [split_list[0]] + parse_string_recursive(split_list[1], delimiters)
        '''If none of the delimiters are in the string, return the string as a list.'''
    print(dictio)
    return [string_data]


vv=parse_string_recursive(string_data, delimiters)
print(vv)


def split_string_with_delimiters_recursive(input_string, delimiters):
    # Base case: No more delimiters to split with
    if not delimiters:
        return [input_string]

    # Take the first delimiter from the list
    delimiter = delimiters[0]

    # Get the remaining delimiters
    remaining_delimiters = delimiters[1:]

    # Split the input string using the current delimiter
    splits = input_string.split(delimiter)

    # Create a list to store the results of recursive calls
    new_splits = []

    # Iterate through each substring from the split
    for substring in splits:
        # Call the recursive function on each substring with remaining delimiters
        recursive_splits = split_string_with_delimiters_recursive(substring, remaining_delimiters)

        # Extend the new_splits list with the results of the recursive call
        new_splits.extend(recursive_splits)

    # Return the new_splits list
    return new_splits


# Test the recursive function
input_string = "Hello|world;how,are-you"
delimiters = ['|', ';', ',', '-']
result = split_string_with_delimiters_recursive(input_string, delimiters)
print(result)
