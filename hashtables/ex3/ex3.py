def intersection(arrays):
    result = []
    hashtable = {}
    for i in range(len(arrays)):
        for j in range(len(arrays[i])):
            if i == 0:
                hashtable[arrays[i][j]] = 1
            elif arrays[i][j] in hashtable:
                hashtable[arrays[i][j]] += 1

    # add keys to array for values that equal array length
    result = [key for key, value in hashtable.items() if value == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
