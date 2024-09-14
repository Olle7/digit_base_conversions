def g():
    #if False:
    #    yield None
    yield 1
    yield 2
    yield 3
    #return
    #return "33w"


print(list(g()))

#print(g())
#for x in g():
#    print(x)