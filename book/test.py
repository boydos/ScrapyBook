def addlist(alist) :
    print "in"
    for i in alist:
        print "hello ",i
        yield i+2
    print "out"
alist=[1,2,3,4]
arr= addlist(alist)
print "begin"
for x in arr:
    print x;
