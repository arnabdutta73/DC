import re
import fnmatch
import constants


def split_address(input_address):
    """
    :Process: Split the input address and remove any special characters if present.
    :type input_address: basestring
    :return: split address :type: list
    """
    split_address_2 = re.split(r"[:;,-/#@$&?*\\ ]", input_address)
    return split_address_2


def search_matching(array):
    """
    :Process: build a pattern out of each word and search it in the data dictionary
    :param array: word from the input address string
    :return: nothing
    """
    pattern = ''
    for characters in array.lower():
        pattern += characters + '*'
    matching = fnmatch.filter(DICTIONARY, pattern)
    if matching and len(array) > 2:
        ADDRESS.append(matching[0])
    else:
        ADDRESS.append(array)


def form_address(address_string):
    """
    :process: converts list to a string
    :param address_string:
    :return:
    """
    final_address = " ".join(list(filter(None, address_string)))
    return final_address


def main():
    """
    :main function
    :return: nothing
    """
    global ADDRESS
    ADDRESS = []
    while True:
        input_address = input("Enter Address: ")
        address_array = split_address(input_address)
        for word in address_array:
            search_matching(word)
        final_string = form_address(ADDRESS)
        print(final_string, "\n")
        ADDRESS = []


if __name__ == '__main__':
    DICTIONARY = constants.DICTIONARY
    main()
