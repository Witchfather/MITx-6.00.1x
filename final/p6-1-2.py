class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
    def hasPrevious(self):
        return self.before != None
    def hasNext(self):
        return self.after != None
    def __str__(self):
        return self.name

def insert(frob, newFrob):
    """
    frob: an existing frob
    newFrob: a new frob to be inserted

    Insert a new frob in the correct position in linked list (the list must be
    in alphabetical order).
    """
    if newFrob.myName() <= frob.myName():
        insert_left(frob.getBefore(), frob, newFrob)
    else:
        insert_right(frob, frob.getAfter(), newFrob)

def insert_frob(before, after, newFrob):
    newFrob.setAfter(after)
    newFrob.setBefore(before)
    before.setAfter(newFrob)
    after.setBefore(newFrob)

def insert_left(before, after, newFrob):
    if before == None:
        newFrob.setAfter(after)
        after.setBefore(newFrob)
    elif before.myName() <= newFrob.myName():
        insert_frob(before, after, newFrob)
    else:
        insert_left(before.getBefore(), before, newFrob)

def insert_right(before, after, newFrob):
    if after == None:
        newFrob.setBefore(before)
        before.setAfter(newFrob)
    elif after.myName() >= newFrob.myName():
        insert_frob(before, after, newFrob)
    else:
        insert_right(after, after.getAfter(), newFrob)

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list
    """
    if start == None:
        return None
    elif start.getBefore() == None:
        return start
    else:
        return findFront(start.getBefore())

# Test case 1
eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

def assertFrob(frob, before, after):
    print 'Testing ' + str(frob) + '...',
    if frob.getBefore() != before:
        raise Exception('expected: ' + str(before) + '; got: ' + str(frob.getBefore()))
    if frob.getAfter() != after:
        raise Exception('expected: ' + str(after) + '; got: ' + str(frob.getAfter()))
    print 'ok'

assertFrob(andrew, None, eric)
assertFrob(eric, andrew, fred)
assertFrob(fred, eric, martha)
assertFrob(martha, fred, ruth)
assertFrob(ruth, martha, None)

# Test case 2
print 'Finding frob starting in ' + str(martha) + '...',
frob = findFront(martha)
if frob != andrew:
    raise Exception('expected: ' + str(andrew) + '; got: ' + str(frob))
print 'ok'

print 'Finding frob starting in ' + str(andrew) + '...',
frob = findFront(andrew)
if frob != andrew:
    raise Exception('expected: ' + str(andrew) + '; got: ' + str(frob))
print 'ok'

print 'Finding frob starting in None...',
frob = findFront(None)
if frob != None:
    raise Exception('expected: None; got: ' + str(frob))
print 'ok'

# Helper functions to print double linked list
def back(node):
    return node.getBefore()

def forward(node):
    return node.getAfter()

def print_list(node, fcn):
    while node != None:
        print node,
        node = fcn(node)
        if node != None:
            print '=>',

print_list(andrew, forward)
print
print_list(ruth, back)
