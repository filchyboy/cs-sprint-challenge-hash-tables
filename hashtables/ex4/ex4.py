def has_negatives(a):
    result = []
    table = {}
    for i in range(len(a)):
        if (a[i] < 0 and abs(a[i]) in table) or (a[i] > 0 and -a[i] in table):
            result.append(abs(a[i]))
        table[a[i]] = True

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -3, -2, 1, 2, 3, 4, -4]))
