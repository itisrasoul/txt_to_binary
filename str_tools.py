def str_to_bin(str_in):
    str_ascii = ord(str_in)
    return bin(str_ascii).replace("0b", "")

def bin_to_str(bin_in):
    bin_ascii = int(str(bin_in).strip(), 2)
    return chr(bin_ascii)
