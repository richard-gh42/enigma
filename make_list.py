def make_list_from_str(str:str):
    str_l = []
    for letter in str:
        str_l.append(letter)
    return str_l

def make_dict_from_lists(list1:list, list2:list):
    dictionary = {}
    for i in range(len(list1)):
        dictionary[list1[i]] = list2[i]
    return dictionary

def make_dict_from_strings(string1:str, string2:str):
    string1_l = make_list_from_str(string1)
    string2_l = make_list_from_str(string2)
    dictionary = make_dict_from_lists(string1_l, string2_l)
    return dictionary

def make_dict_list_to_str(list:list, str:str):
    str_l = make_list_from_str(str)
    dictionary = make_dict_from_lists(list, str_l)
    return dictionary

def make_dict_str_to_list(str:str, list:list):
    str_l = make_list_from_str(str)
    dictionary = make_dict_from_lists(str_l, list)
    return dictionary

def let_list_to_num_list(list:list=[str,str,...]):
    let_to_num = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, 
        "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, 
        "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, 
        "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, 
        "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, 
        "Z": 26,
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 
        'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 
        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 
        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 
        'z': 26}
    temp = []
    for i in range(len(list)):
        temp.append(let_to_num[list[i]])
    return temp

def num_list_to_let_list(list:list=[int,int,...]):
    num_to_let = {
            1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 
            6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 
            11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 
            16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 
            21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 
            26: "Z"}
    temp = []
    for i in range(len(list)):
        temp.append(num_to_let[list[i]])
    return temp