import string


def isOrdered():
    string_container = "abbcg"
    string_alpha = string.ascii_lowercase
    flag = False
    for i in range(0,len(string_container)):
        count = string_alpha.find(string_container[i])


        for j in range(i+1,len(string_container)):

            for k in range(count+1, len(string_alpha)):

                if string_container[j] == string_alpha[k]:
                    flag = True
                    break
                else:
                    flag = False

    if flag == True:
        print("yes")
    else:
        print("no")




isOrdered()