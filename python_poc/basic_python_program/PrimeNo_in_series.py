def prime_number():
    for i in range(11, 21):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


prime_number()
