# An array is monotonic if it is either monotone increasing or monotone decreasing.

# logic1
def is_monotonic():
    array_container = [6, 5, 4, 4]
    print("The array is :",array_container)
    result1 = [None] * (len(array_container) - 1)
    result2 = [None] * (len(array_container) - 1)
    reply1 = True
    reply2 = True
    for i in range(0, len(array_container) - 1):
        result1[i] = array_container[i] <= array_container[i + 1]
        result2[i] = array_container[i] >= array_container[i + 1]
    for i in range(0, len(array_container) - 1):
        if not result1[i]:
            reply1 = False

        if not result2[i]:
            reply2 = False

    return reply1, reply2


# logic2
def is_monotonic2():
    array_container = [5,15,20,10]
    print("The array is :", array_container)
    return (all(array_container[i] <= array_container[i + 1] for i in range(len(array_container) - 1)) or
            all(array_container[i] >= array_container[i + 1] for i in range(len(array_container) - 1)))


reply1, reply2 = is_monotonic()


if not reply1:
    print("not monotonic_increasing")
else:
    print("monotonic_increasing")
if not reply2:
    print("not monotonic_decreasing")
else:
    print("monotonic_decreasing")
print("----------------------------------")
reply_logic2 = is_monotonic2()
print("array is monotonic:{} ".format(reply_logic2))
