
#basic type operation => 
#string,list,dict,orderdict,stack,queue,heap,tree,linked list

import sys

def del1(x,i): del x[i]
def del2(x,i,j): del x[i:j]

def cmd(s, t):
    print("{0}:{1}".format(s, t()))

def demolist(data):
    cmd("data.append('f')", lambda: data.append('f') or data) 
    cmd("data+data", lambda: data+data) 
    cmd("data*3", lambda: data*3 ) 
    cmd("(data*3).count('a')", lambda: (data*3).count('a') or data*3) 

    cmd("data.extend(list('xyz'))", lambda: data.extend(list('xyz')) or data) 
    cmd("data.reverse()", lambda: data.reverse() or data) 
    cmd("data.remove('y')", lambda: data.remove('y') or data) 
    cmd("data.index('x')", lambda: data.index('x')) 
    cmd("data.sort()", lambda: data.sort() or data) 
    cmd("data.pop()", lambda: data.pop()) 

    cmd("del(data[-2])", lambda: del1(data, -2) or data) 
    cmd("del(data[1:3])", lambda: del2(data, 1, 3) or data) 

def demodict(data):
    cmd("data.keys()", lambda: data.keys())
    cmd("data.values()", lambda: data.values())
    cmd("data.items()", lambda: data.items())

    cmd("data.viewkeys()", lambda: data.viewkeys())
    cmd("data.viewvalues()", lambda: data.viewvalues())
    cmd("data.viewitems()", lambda: data.viewitems())

    cmd("[ for x in data.iterkeys() ]", lambda: [ x for x in data.iterkeys() ] )
    cmd("[ for x in data.itervalues() ]", lambda: [ x for x in data.itervalues() ] )
    cmd("[ for x in data.iteritems() ]", lambda: [ x for x in data.iteritems() ] )

    cmd("data.has_key(10)", lambda: data.has_key(10))
    cmd("data.fromkeys([1,2,3], 11)", lambda: dict.fromkeys([1,2,3],11))
    cmd("data.get(5,[])", lambda: data.get(5,[]))
    cmd("data.setdefault(10,[])", lambda: data.setdefault(10, []))

    cmd("data.pop(6)", lambda: data.pop(6))
    cmd("data.popitem()", lambda: data.popitem())
    cmd("data.copy()", lambda: data.copy())
    cmd("data.clear()", lambda: data.clear())

def main():
    argv = sys.argv
    print(sys.argv)

    if (len(argv) != 2):
        print("Usage: {0} [list|listhelp]".format(argv[0]))
        sys.exit(0)

    if (argv[1] == "list"): demolist(list("cab"))
    if (argv[1] == "listhelp"): help([])

    if (argv[1] == "dict"): demodict({x:y for x,y in enumerate("abcdefg")})
    if (argv[1] == "dicthelp"): help({})

if __name__== "__main__":
   main()

