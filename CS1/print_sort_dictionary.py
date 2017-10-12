# print the key/value pair of a dictionary sorted on value
def print_sort_dictionary( D ):
    DS = sorted(D.items(), key=lambda x:x[1])               
    for k in DS:
        print k
