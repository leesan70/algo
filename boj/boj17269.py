alphabets = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]


def arrange_name(name1, name2):
    arranged_name = ""
    len_name1 = len(name1)
    len_name2 = len(name2)
    shorter_name = name1 if len_name1 < len_name2 else name2
    min_length = min(len_name1, len_name2)
    for i in range(len(name2)):
        arranged_name += name1[i]
        arranged_name += name2[i]

