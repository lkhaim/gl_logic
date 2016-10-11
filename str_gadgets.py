def chunker(input_str, m):
    '''
    chunker() takes a string "input_str" and a positive integer "m"
    and returns a list of strings, each of which is of length "m",
    with an exception of the last element,
    which contains the remaining characters
    and is of the length (len(input_str) % m).
    '''
    # checking value of m and returning 0, if it's not positive
    if m <= 0:
        print("Value of m is %d, but should be more than 0." % m)
        return 0

    # initiating variables
    chunks = [] # list to hold chunks of "m" characters
    start = 0   # index of input_str, where a chunk begins

    str_len = len(input_str)
    # splitting input_str into chunks
    while start < str_len:
        end = start + m
        chunks.append(input_str[start:end])
        start += m

    # returning list of chunks
    return chunks