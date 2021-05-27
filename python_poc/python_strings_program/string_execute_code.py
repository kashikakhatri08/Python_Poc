def exec_method():
    string_container = """
def sum(a,b):
    print("first number: {} , second number: {}".format(a,b))
    c= a +b
    print("sum of first and second number : {}".format(c))
        
sum(1,2)
    """
    exec(string_container)

exec_method()