def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    hash = {}
    for x in range(length):
    #check if already added to hash
        if weights[x] in hash:
        #check if the key and value add to goal, if so return
            if limit-weights[x] in hash:
                print(hash[weights[x]], x)
                return x, hash[weights[x]]
        hash[weights[x]] = x
    #check every item in hash
    for x in hash:
        weight = x
        to_limit = limit - weight
        if to_limit in hash:
            return hash[to_limit], hash[weight]

    return None
