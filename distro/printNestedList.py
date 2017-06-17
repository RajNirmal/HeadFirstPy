"""This is a small function that will get a nested list as an input
    and prints the nested list in a proper manner"""
def printList (theList):
    """The list is got and iterated and the isinstance() BIF is used"""
    for details in theList:
        if isinstance(details,list):
            printList(details)
        else:
            print(details)
