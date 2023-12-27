def char_to_bin(char_in):
    char_ascii = ord(char_in)
    return bin(char_ascii).replace("0b", "")

def str_to_bin(str_in):
    return "    ".join([char_to_bin(each) for each in str_in])

def bin_to_str(bin_in):
    bin_ascii = int(str(bin_in).strip(), 2)
    return chr(bin_ascii)
