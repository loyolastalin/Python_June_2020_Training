def multi(name, age =10, *arg):
    print("name {} age {}".format(name, age))
    for var in arg:
        print(var)


