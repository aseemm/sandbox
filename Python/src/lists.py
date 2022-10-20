# Lists
# Source: https://emre.me/data-structures/lists/

# create
list_empty = [] 
list_ints = [1, 2, 3] 
list_range1 = [*range(10, 20, 1)] # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], remember to unpack
list_range2 = [x for x in range(10, 20)]

# read
# start from [0, len-1], or [-len, -1]

# [start:stop]  # items start through stop
# [start:]      # items start through the rest of the list
# [:stop]       # items from the beginning through stop
# [:]           # a copy of the whole list

# [-1]    # last item in the list
# [-2:]   # last two items in the list
# [:-2]   # everything except the last two items

# [::-1]    # all items in the list, reversed
# [1::-1]   # the first two items, reversed
# [:-3:-1]  # the last two items, reversed
# [-3::-1]  # everything except the last two items, reversed

# update

# use index to change
# use append() for one item, extend() for multiple items
# + to combine multiple lists
# * to repeat a list multiople times
# insert() at an index
list.insert(2, 'r')
list[3:3] = ['e', '.', 'm']

# delete
del list_emre[4]
# remove() for an element
# pop() to remove item at an given index
# clear() to empty a list

# misc
# index() to return index of element
# count()
# sort() - in place list.sort() or list.sort(reverse=True)
list.sort(key=len) # use the function len to sort
# use sorted() if we want to preserve the original list
copy()
reverse()

# check if an element exists use 'in'
print('e' in list)
