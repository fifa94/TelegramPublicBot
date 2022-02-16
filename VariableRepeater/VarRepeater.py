class WrongPath(Exception):
    pass


def multiplication_of_var(dictionary, num_of_multiplication=1, path='') -> str:

    """ Function which can generate var file from dictionary.
    First parameter must be in format of dictionary (Key = variable name, Value = data type),
    second is number of multiplication(must be at least 1),
    third parameter is path where var file will be generated
    """

    # if path is not string raise an error
    if not isinstance(path, str):
        error = 'Path must be string or empty'
        raise WrongPath(error)

    # Creating list of keys and values from dictionary.
    list_keys = list(dictionary.keys())
    list_values = list(dictionary.values())

    # Preparing of variables which are necessary for generating
    list_expanded_keys = []
    list_expanded_values = []
    str_base_mem = ''

    for i in range(len(list_keys)):
        # Converting list of keys and values to string.
        str_base = str(list_keys[i])
        str_base_value = str(list_values[i])

        # Checking if variable name is not the same as previous one. If it is not, it will add new variable to list.
        if str_base != str_base_mem:

            str_base_mem = str_base

            for x in range(num_of_multiplication):
                if x > 0:
                    exp_string_key = str_base + str(x)
                else:
                    exp_string_key = str_base

                exp_string_value = str_base_value

                # add elements to lists
                list_expanded_keys.append(exp_string_key)
                list_expanded_values.append(exp_string_value)

    # File name generator
    if len(path) > 0:
        file_name = path + '/' + '{}_to_{}.txt'.format(list_keys[0], list_keys[-1])
    else:
        file_name = '{}_to_{}.txt'.format(list_keys[0], list_keys[-1])

    # Creating file with name of `file_name` and writing content to it.
    #     `f.write('VAR\n')` - writing `VAR` to file
    #     `f.write('END_VAR')` - writing `END_VAR` to file
    #     `f.close()` - closing file
    #     `message = 'File successfully generated'` - message which will be returned
    #     `return message` - returning message

    f = open(file_name, 'w+')
    f.write('VAR\n')

    for i in range(len(list_expanded_keys)):
        content_str = '\t{} : {}\n'.format(list_expanded_keys[i], list_expanded_values[i])
        f.write(content_str)

    f.write('END_VAR')
    f.close()
    message = 'File successfully generated'
    return message


dict_in = {'Something': 'BOOL', 'Some': 'USINT'}

num_of_multiplication_in = 6

# Error = multiplication_of_var(dict_in, num_of_multiplication_in, 'C:/Users/Filip/Desktop')

msg = multiplication_of_var(dict_in, num_of_multiplication_in,)
