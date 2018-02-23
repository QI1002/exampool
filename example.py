
#basic type operation => 
#string,list(stack, queue),dict,orderdict,heap,tree,linked list

import sys
from heapq import *
from bisect import *
from itertools import *

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

def demoheapq(data):
    cmd("heapify(data)", lambda: heapify(data) or data)
    cmd("heappush(data, -1)", lambda: heappush(data,-1) or data)
    cmd("heappop(data)", lambda: heappop(data))
    cmd("heappushpop(data, 9)", lambda: heappushpop(data, 9))
    cmd("heapreplace(data, 2)", lambda: heapreplace(data, 2))
    cmd("heapify(data)", lambda: heapify(data) or data)

    cmd("list(merge(data, [3,4,6,8])))", lambda: list(merge(data, [3,4,6,8])))
    cmd("nlargest(3, data)", lambda: nlargest(3, data))
    cmd("nsmallest(3, data)", lambda: nsmallest(3, data))
    
def demobisect(data):
    cmd("bisect_left(data,1)", lambda: bisect_left(data, 1))
    cmd("bisect_right(data,1)", lambda: bisect_right(data, 1))
    cmd("bisect_left(data,7)", lambda: bisect_left(data, 7))
    cmd("bisect_right(data,7)", lambda: bisect_right(data, 7))
    cmd("bisect_left(data,0)", lambda: bisect_left(data, 0))
    cmd("bisect_right(data,0)", lambda: bisect_right(data, 0))
    cmd("bisect_left(data,2)", lambda: bisect_left(data, 2))
    cmd("bisect_right(data,2)", lambda: bisect_right(data, 2))
    cmd("bisect_left(data,4)", lambda: bisect_left(data, 4))
    cmd("bisect_right(data,4)", lambda: bisect_right(data, 4))
    cmd("bisect_left(data,6)", lambda: bisect_left(data, 6))
    cmd("bisect_right(data,6)", lambda: bisect_right(data, 6))
    cmd("bisect_left(data,8)", lambda: bisect_left(data, 8))
    cmd("bisect_right(data,8)", lambda: bisect_right(data, 8))
     
    data2 = list(data) 
    cmd("insort_left(data,8)", lambda: insort_left(data, 8) or data)
    cmd("insort_right(data2,8)", lambda: insort_right(data2, 8) or data2)
    cmd("insort_left(data,6)", lambda: insort_left(data, 6) or data)
    cmd("insort_right(data2,6)", lambda: insort_right(data2, 6) or data2)
    cmd("insort_left(data,4)", lambda: insort_left(data, 4) or data)
    cmd("insort_right(data2,4)", lambda: insort_right(data2, 4) or data2)
    cmd("insort_left(data,2)", lambda: insort_left(data, 2) or data)
    cmd("insort_right(data2,2)", lambda: insort_right(data2, 2) or data2)
    cmd("insort_left(data,0)", lambda: insort_left(data, 0) or data)
    cmd("insort_right(data2,0)", lambda: insort_right(data2, 0) or data2)

def demoitertools(data):
    cmd("[ count(10).next() for x in range(5) ]", lambda c = count(10): [ c.next() for i in range(5) ])
    cmd("[ cycle('ABC').next() for x in range(5) ]", lambda c = cycle('ABC'): [ c.next() for i in range(5) ])
    cmd("[ repeat('AB').next() for x in range(5) ]", lambda c = repeat('AB'): [ c.next() for i in range(5) ])

    cmd("list(chain('ABC', 'DEF'))", lambda: list(chain('ABC', 'DEF')))
    cmd("list(compress('ABC', [0,1,1]))", lambda: list(compress('ABC', [0,1,1])))
    cmd("list(dropwhile( lambda x: x < 5, [2,4,7,4,2,7]))", lambda: list(dropwhile( lambda x: x < 5, [2,4,7,4,2,7])))
    cmd("list(takewhile( lambda x: x < 5, [2,4,7,4,2,7]))", lambda: list(takewhile( lambda x: x < 5, [2,4,7,4,2,7])))
    cmd("[ k, list(g) for k,g in groupby('AAABBA') ]", lambda: [ (k,list(g)) for k,g in groupby('AAABBA')])
    cmd("list(ifilter(lambda x: x%3, range(10)))", lambda: list(ifilter(lambda x: x%3, range(10))))
    cmd("list(ifilterfalse(lambda x: x%3, range(10)))", lambda: list(ifilterfalse(lambda x: x%3, range(10))))
    cmd("list(imap(lambda a,b: a*b, ['D', 2 , [1]], [3, 4, 2]))", lambda: list(imap(lambda a,b: a*b, ['D', 2, [1]], [3, 4, 2])))
    cmd("list(starmap(lambda a,b: a*b, [('D',3), (2,4) , ([1],2)]))", lambda: list(starmap(lambda a,b: a*b,[('D',3), (2,4) , ([1],2)])))
    cmd("list(izip('ABCD', 'xy'))", lambda: list(izip('ABCD', 'xy')))

    cmd("list(product('ABCD', 'xy'))", lambda: list(product('ABCD', 'xy')))
    cmd("list(permutations(range(4), 2))", lambda: list(permutations(range(4), 2)))
    cmd("list(combinations(range(4), 2))", lambda: list(combinations(range(4), 2)))
    cmd("list(combinations_with_replacement(range(4), 2))", lambda: list(combinations_with_replacement(range(4), 2)))

    cmd("[ cycle('AB').next() for x in range(5) ]", lambda c = cycle('AB'): not c.next() or [ c.next() for i in range(5) ])

def main():
    argv = sys.argv
    #print(sys.argv)

    if (len(argv) != 2):
        print("Usage: {0} [string|stringhelp|list|listhelp|dict|dicthelp|heapq|heapqhelp|bisect|bisecthelp|itertools|itertoolshelp]]".format(argv[0]))
        sys.exit(0)

    if (argv[1] == "str"): demostr("This is a Miracle")
    if (argv[1] == "strhelp"): help(str)

    if (argv[1] == "list"): demolist(list("cab"))
    if (argv[1] == "listhelp"): help(list)

    if (argv[1] == "dict"): demodict({x:y for x,y in enumerate("abcdefg")})
    if (argv[1] == "dicthelp"): help(dict)

    if (argv[1] == "heapq"): demoheapq([5,1,7,3])
    if (argv[1] == "heapqhelp"): help(heapq)

    if (argv[1] == "bisect"): demobisect([1,3,5,7])
    if (argv[1] == "bisecthelp"): help(bisect)

    if (argv[1] == "itertools"): demoitertools({x:y for x,y in enumerate("abcdefg")})
    if (argv[1] == "itertoolshelp"): help(itertools)

if __name__== "__main__":
   main()

