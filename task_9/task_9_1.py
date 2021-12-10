def swap_quotes(input_string: str) -> str:
    """
    Swap quotes inside input string and returns it.
    :param input_string: string to convert
    :type input_string: str
    :return: converted string
    :rtype: srt
    """
    return input_string.translate(str.maketrans('\'"', '"\''))


# print(swap_quotes('"Let\'s swap quotes"'))
