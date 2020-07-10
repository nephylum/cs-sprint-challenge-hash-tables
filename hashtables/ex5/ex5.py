import os

def finder(files, queries):

    # will work but is o(n^2) time complex
    # result = []
    # for item in files:
    #     for q in queries:
    #         if q in item:
    #             result.append(item)

    #get files from paths, set file as key and path as value in cache
    cache = {}
    result = []
    for path in files:
        filename = os.path.basename(path)
        if filename not in cache:
            cache[filename] = [path]
        elif filename in cache:
            cache[filename].append(path)

    #check if query is in cache, if so append value to result
    for q in queries:
        if q in cache:
            if len(cache[q]) == 1:
                result.append(cache[q][0])
            elif len(cache[q]) > 1:
                for x in cache[q]:
                    result.append(x)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
