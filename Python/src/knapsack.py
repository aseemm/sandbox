items = ['clock', 'picture', 'radio', 'vase', 'book', 'computer']
price = [175, 90, 20, 50, 10, 200]
weight = [10, 9, 4, 2, 1, 20]
price_per_weight = [17.5, 10, 5, 25, 10, 10]

max_weight = 20

indata = zip(items, price, weight)
# sorteddata = sorted(indata, key=lambda x: x[1], reverse=True) # max value
# sorteddata = sorted(indata, key=lambda x: x[2]) # min weight
sorteddata = sorted(indata, key=lambda x: x[1]/x[2], reverse=True) # max value/weight ratio

print('Sorted list...')
for idx, val in enumerate(sorteddata):
    print(idx, val)

print('Contents of knapsack...')
totalWeight = 0
for idx, val in enumerate(sorteddata):
    totalWeight = totalWeight + sorteddata[idx][2]
    if totalWeight <= max_weight:
        print(idx, val)

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

#for item in powerSet([1, 2, 4]):
#    print(item)

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    for item1 in powerSet(items):
        remaining_items = list(set(items) - set(item1))
        for item2 in powerSet(remaining_items):
            yield item1, item2

count = 0
for item in yieldAllCombos([1, 2, 4, 7]):
    count = count + 1
    print(count, item)
