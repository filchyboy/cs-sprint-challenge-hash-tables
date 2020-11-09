def finder(files, queries):
    result = []
    table = {}
    for i in range(len(queries)):
        table[queries[i]] = True

    for member in files:
        split_files = member.split("/")
        if split_files[-1] in table:
            result.append(member)
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
