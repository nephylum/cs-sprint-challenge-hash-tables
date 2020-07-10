def has_negatives(a):
# create a hash tables for positive values
    result = []
    pos = {}
    # iterate through hash adding positive values
    for x in a:
        #if positive add to pos hash
        if x > 0:
            #check it's not a duplicate
            if x not in pos:
                pos[x] = None
    for x in a:
        #if negative check pos hash
        if x < 0:
            if abs(x) in pos:
                result.append(abs(x))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
