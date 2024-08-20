def josephus_problem(n, k):
    people = list(range(1, n + 1))
    result = []
    index = 0

    while len(people) > 0:
        index = (index + k - 1) % len(people)
        result.append(people.pop(index))

    return result


n, k = map(int, input().split())


result = josephus_problem(n, k)


print("<" + ", ".join(map(str, result)) + ">")

