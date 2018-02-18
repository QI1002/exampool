
#basic type operation => 
#string,list(stack, queue),dict,orderdict,heap,tree,linked list

import sys

def del1(x,i): del x[i]
def del2(x,i,j): del x[i:j]

def cmd(s, t):
    print("{0}:{1}".format(s, t()))

def demostr(data):
    cmd("data.lower()", lambda: data.lower()) 
    cmd("data.upper()", lambda: data.upper()) 
    cmd("data.capitalize()", lambda: data.capitalize()) 
    cmd("data.title()", lambda: data.title())
    cmd("data.swapcase()", lambda: data.swapcase())

    cmd("data+data", lambda: data+data)
    cmd("data*3", lambda: data*3)

    cmd("data.split(' ', 2)", lambda: data.split(' ', 2)) 
    cmd("data.rsplit(' ', 2)", lambda: data.rsplit(' ',2)) 
    cmd("''.join(data.split())", lambda: ''.join(data.split())) 
    cmd("data.partition('is')", lambda: data.partition('is')) 
    cmd("data.rpartition('is')", lambda: data.rpartition('is')) 

    cmd("'-9801'.zfill(7)", lambda: '-9801'.zfill(7))
    cmd("data.index('a')", lambda: data.index('a'))
    cmd("data.rindex('a')", lambda: data.rindex('a'))
    cmd("data.find('is')", lambda: data.find('is'))
    cmd("data.rfind('is')", lambda: data.rfind('is'))
    cmd("data.replace('a','b')", lambda: data.replace('a','b'))
    cmd("data.count(' ', 5)", lambda: data.count(' ', 5))

    cmd("data.center(20,'_')", lambda: data.center(20,'_'))
    cmd("data.center(20,' ').strip()", lambda: data.center(20,' ').strip())
    cmd("data.ljust(20,'_')", lambda: data.ljust(20,'_')) 
    cmd("data.rjust(20,' ').lstrip()", lambda: data.rjust(20,' ').lstrip()) 
    cmd("data.rjust(20,'_')", lambda: data.rjust(20,'_')) 
    cmd("data.ljust(20,' ').rstrip()", lambda: data.ljust(20,' ').rstrip())

    cmd("data.startswith('this')", lambda: data.startswith('this')) 
    cmd("data.endswith('racle')", lambda: data.endswith('racle')) 
    
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
    cmd("del data[3]", lambda: del1(data, 3) or data)
    cmd("data.copy()", lambda: data.copy())
    cmd("data.clear()", lambda: data.clear())

def main():
    argv = sys.argv
    print(sys.argv)

    if (len(argv) != 2):
        print("Usage: {0} [string|stringhelp|list|listhelp|dict|dicthelp]".format(argv[0]))
        sys.exit(0)

    if (argv[1] == "str"): demostr("This is a Miracle")
    if (argv[1] == "strhelp"): help(str)

    if (argv[1] == "list"): demolist(list("cab"))
    if (argv[1] == "listhelp"): help(list)

    if (argv[1] == "dict"): demodict({x:y for x,y in enumerate("abcdefg")})
    if (argv[1] == "dicthelp"): help(dict)

if __name__== "__main__":
   main()

