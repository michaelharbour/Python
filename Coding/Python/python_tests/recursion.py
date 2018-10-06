
# A recursive function to invert a string

# pylint: disable=C0103,C0303

def reverseString(someString):

    # 1st, set up the base case
    if someString is None:
        return someString

    # 2nd base case - make sure the length of the string is not 0 or 1
    if (len(someString)) <= 1:
        return someString

    '''The reason we have to do the first case is that we cannot check the length of a 
       string if it doesn't exist (i.e. 'None') and need to check for this condition
       seperately.  it's possible a try/except conditional would eliminate the need for
       this but I need to test'''

    return reverseString(someString[1:]) + someString[0]

    # A string is just a list of characters
    # In a list, to get to all the elements following the first just use [1:]
    # How can we be sure that there is an index at 1?  Because we just checked those two cases above
    # The last bit here is just taking the first character and appending it to the end of the string

myAlph = "abcdefghijklmnopqrstuvwxyz"
myGreet = "Hello world!"
myString = "abc123"

myTest1 = None
myTest2 = "A"


print "\n\nThe reverse of %s is:\n\t%s\n\nThe reverse of %s is:\n\t%s\n\nThe reverse of %s is:\n\t%s\n\n" % \
(myAlph, reverseString(myAlph), myGreet, reverseString(myGreet), myString, reverseString(myString))

print "\n\nThe reverse of %s is:\n\t%s\n\nThe reverse of %s is:\n\t%s\n\n" % \
(myTest1, reverseString(myTest1), myTest2, reverseString(myTest2))

'''But, while demonstrating recursion effectively, there are much easier ways to reverse a string
as in the cases above...  You just have to watch for none values, which you would test for in the 
fuction itself.  Note that Test1 is not recorded here.'''

print "%s\n\n%s\n\n%s\n\n%s" % (myAlph[::-1], myGreet[::-1], myString[::-1], myTest2[::-1])

# pylint: enable=C0103,C0303