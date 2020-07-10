def intersection(arrays):
    hash ={}
    # create a list to start checking for duplicate values
    for x in arrays[0]:
        hash[x] = 0
    for x in range(1, len(arrays)):
        for y in arrays[x]:
            if y in hash:
                hash[y] += 1
        todrop = []
        for item in hash:
            if hash[item] == 0:
                todrop.append(item)
                #hash.pop(item, None)
        for x in todrop:
            hash.pop(x, None)
    result = []
    for x in hash:
        result.append(x)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
