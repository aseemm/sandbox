import unittest
import math

# Chapter 01 - Strings & Arrays
# # Implement an algorithm to determine if a string has all unique characters. What if you
# # can not use additional data structures?
# def is_unique_chars_using_dict(string: str) -> bool:
#     my_dict = {}
#     for char in string:
#         if char in my_dict:
#             return False
#         my_dict[char] = 1
#     return True

# def is_unique_chars_pythonic(string: str) -> bool:
#     return len(set(string)) == len(string)

# class Test(unittest.TestCase):
#     testcases = [
#         ("abcd", True),
#         ("", True),
#         ("hello", False),        
#         ]

#     def test_dict(self):
#         for text, expected in self.testcases:
#             assert(is_unique_chars_using_dict(text) == expected), f"Failed for value: {text}"

#     def test_pythonic(self):
#         for text, expected in self.testcases:
#             assert(is_unique_chars_pythonic(text) == expected), f"Failed for value: {text}"            

# # Write code to reverse a C-Style String. (C-String means that “abcd” is represented as
# # five characters, including the null character.)
# def reverse_string(string: str) -> str:
#     string_len = len(string)
#     my_list = list(string) # since strings are immutable
#     for idx in range(math.floor(string_len/2)):
#         temp = my_list[idx]
#         my_list[idx] = my_list[string_len-1-idx]
#         my_list[string_len-1-idx] = temp

#     return "".join(my_list)

# Alternate solutions - string[::01] or do a p = char + p

# class Test(unittest.TestCase):
#     testcases = [
#         ("abcd", "dcba"),
#         ("", ""),
#         ("hello", "olleh"),        
#         ]

#     def test(self):
#         for text, expected in self.testcases:
#             assert(reverse_string(text) == expected), f"Failed for value: {text}"

# Design an algorithm and write code to remove the duplicate characters in a string
# without using any additional buffer. NOTE: One or two additional variables are fine.
# An extra copy of the array is not.
# FOLLOW UP
# Write the test cases for this method.            
# def remove_duplicates(string: str) -> str:
#     p = ""
#     for char in string:
#         if char not in p:
#             p = p + char
#     return p
      
# class Test(unittest.TestCase):
#     testcases = [
#         ("hello", "helo"),
#         ("", ""),
#         ("helloe", "helo"),        
#         ("llll", "l")                
#         ]

#     def test(self):
#         for text, expected in self.testcases:
#             assert(remove_duplicates(text) == expected), f"Failed for value {text}"

# # Write a method to decide if two strings are anagrams or not.
# def is_anagram(string1: str, string2: str) -> bool:
#       return sorted(string1) == sorted(string2)

# # Alternate solution is to use bitmaps, and use ord(char) to increment after processing the first
# # string, and decrement after second string for non-zero values
# class Test(unittest.TestCase):
#     testcases = [
#         ("cinema", "iceman", True),
#         ("", "", True),
#         ("hello", "helo", False),
#         ("dot", "DOT", False)        
#         ]

#     def test(self):
#         for text1, text2, expected in self.testcases:
#             assert(is_anagram(text1, text2) == expected), f"Failed for value {text1}, {text2}"
            
# # Write a method to replace all spaces in a string with ‘%20’.
# def modify_string(string: str) -> str:
#     p = ""
#     for char in string:
#         if char == " ":
#             p = p + "%20"
#         else:
#             p = p + char
#     return p

# # Alternate solution is to use bitmaps
# class Test(unittest.TestCase):
#     testcases = [
#         (" cinema", "%20cinema"),
#         ("  cinema", "%20%20cinema"),        
#         ("", ""),
#         ("hello ", "hello%20"),
#         ("hello  ", "hello%20%20"),
#         ("dot", "dot")        
#         ]

#     def test(self):
#         for text, expected in self.testcases:
#             assert(modify_string(text) == expected), f"Failed for value {text}"

# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
def rotate_image(image: list) -> list:
    n = len(image)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # left -> top(save)
            top = image[layer][i]
            image[layer][i] = image[-i - 1][layer]
            # top -> right
            image[-i - 1][layer] = image[-layer - 1][-i - 1]
            # right -> bottom
            image[-layer - 1][-i - 1] = image[i][-layer - 1]
            # bottom -> left(top)
            image[i][-layer - 1] = top

    return image

# Alternate solutions - https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_01/p07_rotate_matrix.py
class Test(unittest.TestCase):
    testcases = [
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),        
        ]

    def test(self):
        for text, expected in self.testcases:
            assert(rotate_image(text) == expected), f"Failed for value {text}"

# # Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# # column is set to 0.
# def clear_row_col(matrix: list) -> list:
#     # save dimensions of the matrix (m x n)
#     m = len(matrix)
#     n = len(matrix[0])
#     # save locations with 0
#     rows = set()
#     cols = set()
#     for ridx in range(m):
#         for cidx in range(n):
#             if matrix[ridx][cidx] == 0:
#                 rows.add(ridx)
#                 cols.add(cidx)
                
#     # clear rows and cols
#     for ridx in range(m):
#         for cidx in range(n):
#             if ridx in rows or cidx in cols:
#                 matrix[ridx][cidx] = 0

#     return matrix

# class Test(unittest.TestCase):
#     testcases = [
#         (
#             [
#                 [1, 2, 3, 4, 0],
#                 [6, 0, 8, 9, 10],
#                 [11, 12, 13, 14, 15],
#                 [16, 0, 18, 19, 20],
#                 [21, 22, 23, 24, 25],
#             ],
#             [
#                 [0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0],
#                 [11, 0, 13, 14, 0],
#                 [0, 0, 0, 0, 0],
#                 [21, 0, 23, 24, 0],
#             ],
#         )
#     ]    

#     def test(self):
#         for text, expected in self.testcases:
#             assert(clear_row_col(text) == expected), f"Failed for value {text}"

# # Assume you have a method isSubstring which checks if one word is a substring of
# # another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
# # only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).
# def isSubstring(s1: str, s2: str) -> bool:
#     return s1 in s2;

# def isRotatedString(s1: str, s2: str) -> bool:
#     if len(s1) == len(s2) != 0:
#         return s2 in s1*2 # concatenate string with itself
#     return False

# class Test(unittest.TestCase):
#     testcases1 = [
#         ("waterbottle", "erbottlewat", False),
#         ("foo", "bar", False),
#         ("foo", "foofoo", True),
#         ]
#     testcases2 = [
#         ("waterbottle", "erbottlewat", True),
#         ("foo", "bar", False),
#         ("foo", "foofoo", False),
#         ]    

#     def test_issubstring(self):
#         for text1, text2, expected in self.testcases1:
#             assert(isSubstring(text1, text2) == expected), f'Failed for value {text1}, {text2}'

#     def test_isrotatedstring(self):
#         for text1, text2, expected in self.testcases2:
#             assert(isRotatedString(text1, text2) == expected), f'Failed for value {text1}, {text2}'            



# Chapter 2 - LinkedList
class LinkedListNode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __str__(self):
        values = [str(x) for x in self]
        return " -> ".join(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def add_multiple(self, values):
        for v in values:
            self.add(v)

class DoublyLinkedList(LinkedList):
    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value, None, self.tail)
            self.tail = self.tail.next

# # Write code to remove duplicates from an unsorted linked list.
# # FOLLOW UP
# # How would you solve this problem if a temporary buffer is not allowed?
# def remove_duplicates(my_list: object) -> object:
#     unique_values = set()
#     curr = my_list.head
#     prev = None

#     while curr:
#         if curr.value in unique_values:
#             # remove
#             prev.next = curr.next
#         else:
#             unique_values.add(curr.value)
#             prev = curr
#         curr = curr.next
#     my_list.tail = prev

#     return my_list

# class Test(unittest.TestCase):
#     testcases = (
#         ([], []),
#         ([1, 1, 1, 1, 1, 1], [1]),
#         ([1, 2, 3, 2], [1, 2, 3]),
#         ([1, 2, 2, 3], [1, 2, 3]),
#         ([1, 1, 2, 3], [1, 2, 3]),
#         ([1, 2, 3], [1, 2, 3]),
#     )
#     def test(self):
#         for text, expected in self.testcases:
#             # create a linked list
#             ll1 = LinkedList(text)
#             ll2 = LinkedList(expected)
#             assert(str(LinkedList(remove_duplicates(ll1))) == str(ll2)), f"Failed for value: {text}"

# # Implement an algorithm to find the nth to last element of a singly linked list.
# def find_element(ll: object, n: int) -> int:
#     # # get length of linked list
#     # len = ll.__len__();
#     # # remove len - n element
#     # curr = ll.head
#     # prev = None
#     # count = 0
#     # while curr:
#     #     if count == len - n:
#     #         print(curr.value)
#     #         return curr.value
#     #     count += 1
#     #     prev = curr
#     #     curr = curr.next
#     prev = ll.head
#     curr = ll.head
#     count = 0
#     while curr:
#         if count >= n:
#             prev = prev.next
#         count += 1
#         curr = curr.next

#     return prev.value

# class Test(unittest.TestCase):
#     testcases = [
#         ([1, 2, 3], 2, 2),
#         ([1, 2, 3], 1, 3),               
#         ([1, 2, 3], 3, 1),
#         ]

#     def test(self):
#         for input_array, n, expected_array in self.testcases:
#             assert(find_element(LinkedList(input_array), n) == expected_array), f'Failed for {input_array}, {n}'

# # Implement an algorithm to delete a node in the middle of a single linked list, given
# # only access to that node.
# def delete_node(ll:object, node:int) -> object:
#     prev = None
#     curr = ll.head
#     while curr:
#         if curr.value == node:
#             if curr == ll.head:
#                 # first element
#                 ll.head = curr.next
#             else:
#                 prev.next = curr.next
#             break
#         prev = curr
#         curr = curr.next
#     return ll

# # of if you are given the node directly, you can just do something like
# # node.value = node.next.value
# # node.next = node.next.next

# class Test(unittest.TestCase):
#     testcases = [
#         ([1, 2, 3], 2, [1, 3]),
#         ([1, 2, 3], 1, [2, 3]),
#         ([1, 2, 3], 3, [1, 2]),       
#         ]

#     def test(self):
#         for in_array, node, out_array in self.testcases:
#             assert(str(delete_node(LinkedList(in_array), node)) == str(LinkedList(out_array))), f'Failed for {in_array}, {node}'

# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1’s digit is at the head of
# the list. Write a function that adds the two numbers and returns the sum as a linked list.

# def convert_list_to_num(ll: object) -> int:
#     curr = ll.head
#     placevalue = 1
#     sum = 0

#     while curr:
#         sum = sum + placevalue*curr.value
#         placevalue *= 10
#         curr = curr.next
#     return sum

# def convert_num_to_list(num: int) -> object:
#     ll = LinkedList([])
#     while num != 0:
#         ll.add(num % 10)
#         num = num // 10
#     return ll

# def add_numbers(ll1: object, ll2:object) -> object:
#     num1 = convert_list_to_num(ll1)
#     num2 = convert_list_to_num(ll2)
#     return convert_num_to_list(num1 + num2)

# # or try to do both together
# def sum_lists(ll_a, ll_b):
#     n1, n2 = ll_a.head, ll_b.head
#     ll = LinkedList([])
#     carry = 0
#     while n1 or n2:
#         result = carry
#         if n1:
#             result += n1.value
#             n1 = n1.next
#         if n2:
#             result += n2.value
#             n2 = n2.next

#         ll.add(result % 10)
#         carry = result // 10

#     if carry:
#         ll.add(carry)

#     return ll

# class Test(unittest.TestCase):
#     testcases = [
#         ([3, 1, 5], [5, 9, 2], [8, 0, 8])
#     ]

#     def test(self):
#         for in1, in2, sum in self.testcases:
#             assert(str(sum_lists(LinkedList(in1), LinkedList(in2))) == str(LinkedList(sum))), f'Failed for {in1}, {in2}'

# # Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.
# def check_list(ll: object) -> object:
#     fast = slow = ll.head

#     while fast and fast.next:
#         fast = fast.next.next
#         slow = slow.next
#         if fast is slow:
#             break

#     if fast is None or fast.next is None:
#         return None

#     slow = ll.head
#     while fast is not slow:
#         fast = fast.next
#         slow = slow.next

#     return fast

# class Test(unittest.TestCase):
#     looped_list = LinkedList([1, 2, 3, 4, 3])
#     loop_start_node = looped_list.head.next.next
#     looped_list.tail.next = loop_start_node
    
#     testcases = [
#         (LinkedList([1, 2, 3, 4, 5]), None),
#         (looped_list, loop_start_node),        
#         ]

#     def test(self):
#         for input, node in self.testcases:
#             assert(check_list(input) == node), f'Failed for {input}'

# Chapter 3 - Stacks & Queues
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]
        return None
    
    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return bool(self.items)

# Describe how you could use a single array to implement three stacks.
# for stack 1, we will use [0, n/3)
# for stack 2, we will use [n/3, 2n/3)
# for stack 3, we will use [2n/3, n)

# How would you design a stack which, in addition to push and pop, also has a function
# min which returns the minimum element? Push, pop and min should all operate in
# O(1) time.
# You can implement this by having each node in the stack keep track of the minimum beneath itself.
# Then, to find the min, you just look at what the top element thinks is the min.

class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.minstack = Stack()

    def minimum(self):
        return self.minstack.peek()
    
    def push(self, value):
        super().push(value)
        if not self.minstack or value < self.minimum():
            self.minstack.push(value)
        else:
            self.minstack.push(self.minimum())

    def pop(self, value):
        value = super().pop()
        self.minstack.pop()
        return value

class Test(unittest.TestCase):
    def test(self):
        my_stack = MinStack()
        assert my_stack.minimum() is None

        my_stack.push(5)
        assert my_stack.minimum() == 5

# Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds
# some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks, and should create a new stack once
# the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
# behave identically to a single stack (that is, pop() should return the same values as it
# would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific
# sub-stack.

# We know that push() should behave identically to a single stack, which means that we need
# push() to call push on the last stack. We have to be a bit careful here though: if the last stack
# is at capacity, we need to create a new stack. Our code should look something like this:

  # def pop_at(self, index):
  #       return self.left_shift(index, True)

  #   def left_shift(self, index, remove_top):
  #       stack = self.stacks[index]
  #       removed_item = stack.pop() if remove_top else stack.remove_bottom()
  #       if stack.is_empty():
  #           del self.stacks[index]
  #       elif len(self.stacks) > index + 1:
  #           v = self.left_shift(index + 1, False)
  #           stack.push(v)
  #       return removed_item

# Towers of Hanoi
# recursive solution

# Queues using stacks

# Write a program to sort a stack in ascending order. You should not make any assumptions about how the stack is implemented. The following are the only functions that
# should be used to write this program: push | pop | peek | isEmpty.
# def push(self, item):
#         if self.is_empty() or item < self.peek():
#             super().push(item)
#         else:
#             while self.peek() is not None and item > self.peek():
#                 self.temp_stack.push(self.pop())
#             super().push(item)
#             while not self.temp_stack.is_empty():
#                 super().push(self.temp_stack.pop())

# Graphs
class Node:
    def __init__(self):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new = Node(key)

        if self.root is None:
            self.root = new
            return
        
        current = self.root
        while current:
            if current.key > key:
                # left
                if current.left is None:
                    current.left = new
                    new.parent = current
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new
                    new.parent = current
                    return
                current = current.right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, parent):
        new = Node(key)

        if parent is None:
            if self.root is None:
                self.root = new
                return new
            raise Exception('a root already exists')

        if not parent.left:
            parent.left = new
            new.parent = parent
        elif not parent.right:
            parent.right = new
            new.parent = parent
        else:
            raise Exception('cant have more than two parents')

        return new

# Implement a function to check if a tree is balanced. For the purposes of this question,
# a balanced tree is defined to be a tree such that no two leaf nodes differ in distance
# from the root by more than one.
# compute minDepth & maxDepth. Should differ by not more than 1
# recurse down

# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
# graphs are modeled as dictionaries
# def is_route(graph, start, end, visited=None):
#     if visited is None:
#         visited = set()
#     for node in graph[start]:
#         if node not in visited:
#             visited.add(node)
#             if node == end or is_route(graph, node, end, visited):
#                 return True
#     return False

# BFS with a dummy queue
# def is_route_bfs(graph, start, end):
#     if start == end:
#         return True
#     visited = set()
#     queue = deque()
#     queue.append(start)
#     while queue:
#         node = queue.popleft()
#         for adjacent in graph[node]:
#             if adjacent not in visited:
#                 if adjacent == end:
#                     return True
#                 else:
#                     queue.append(adjacent)
#         visited.add(node)
#     return False

# Given a sorted (increasing order) array, write an algorithm to create a binary tree with
# minimal height.
# Algorithm:
# 1. Insert into the tree the middle element of the array.
# 2. Insert (into the left subtree) the left subarray elements
# 3. Insert (into the right subtree) the right subarray elements
# 4. Recurse

# Given a binary search tree, design an algorithm which creates a linked list of all the
# nodes at each depth (eg, if you have a tree with depth D, you’ll have D linked lists).
#

# Write an algorithm to find the ‘next’ node (i.e., in-order successor) of a given node in
# a binary search tree where each node has a link to its parent.
# search from root, or just the right sideIf right subtree of node is not NULL, then succ lies in right subtree. Do the following. 
# Go to right subtree and return the node with minimum key value in the right subtree.
# If right subtree of node is NULL, then succ is one of the ancestors. Do the following. 
# Travel up using the parent pointer until you see a node which is left child of its parent. The parent of such a node is the succ.


#Design an algorithm and write code to find the first common ancestor of two nodes
#in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
#necessarily a binary search tree.
# he idea of this approach is to have two pointers, one on each node. We need to move these pointers towards the root in a way that allows them to meet at the LCA.
# The first thing we can notice is that these pointers should be in the same depth. In addition to that, the deeper pointer can never be the LCA. Therefore, our first step should be to keep moving the deeper pointer to its parent until the two pointers are on the same depth.
# Now, we have two pointers that are on the same depth. We can keep moving both pointers towards the root one step at a time until they meet at one node. Since this node is the deepest node that our pointers can meet at, therefore, it’s the deepest common ancestor of our starting nodes, which is the LCA.
# Sparse tables?

# You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes. Create an algorithm to decide if T2 is a subtree of T1.
# translate to string (inorder, preoder (root, left, rigth)
#


# You are given a binary tree in which each node contains a value. Design an algorithm
#to print all paths which sum up to that value. Note that it can be any path in the tree
#- it does not have to start at the root.
# save paths in buffer


# Heaps (Min, Max)
# Can represent as an array where
# root, i = 0
# parent(i) = (i-1)/2
# left(i) = 2*i+1
# right(i) = 2*i+2

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_left_child(i):
    return 2 * i + 1


def get_right_child(i):
    return 2 * i + 2

def min_heapify(arr, i):
    left = get_left_child(i)
    right = get_right_child(i)
    smallest = i

    if left < len(arr) and arr[i] > arr[left]:
        smallest = left
    if right < len(arr) and arr[smallest] > arr[right]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest)
        
def build_min_heap(arr):
    for i in reversed(range(len(arr)//2)):
        min_heapify(arr, i)


print(arr)
build_min_heap(arr)
print(arr)

# https://www.askpython.com/python-modules/python-heapq-module
# The heap functionalities are in the heapq package, so import it
import heapq 
# we now initialise a list to be converted to heap 
lis = [15, 7, 9, 4, 13] 
 
# converting lis to heap using the heapify function
heapq.heapify(lis) 
print ("The heap looks like: ") 
print(lis)
 
#using the heappop function
print ("The popped item using heappushpop() is : ",end="") 
print (heapq.heappop(lis))
 
print ("After popping, the heap looks like: ")
print(lis)
 
#using the heappush function to push 2
print ("After pushing 2, the heap looks like: ") 
heapq.heappush(lis, 2) 
print(lis)


# Linked List
Node = data, next
LL = head, tail, size

insert(index)
append()
get(index)
delete(index)

# Stacks & Queues
Use collections.deque
Stack - push = append, pop = pop, size, is_empty()
Queue = enqueue = append, dequeue = popleft, size(), is_empty()

# Binary Tree
Node = left, right, root/data
insert_left, insert_right # create a new BinaryTree node, and push down existing item

Traversals -
pre-order, in-order, post-order

# Heap (Priority Queue)
heapify()
build_heap(array

# Hash tables
Use python dict

# Binary Search Trees
Insert
Lookup
Delete

Balanced versus non-balanced

           BinarySearchTree - root, size, length, __len__, put(key, val) & private _put(), _get, _contains, delete
           Node - key, payload, leftChild, rightChild, parent
           https://emre.me/data-structures/binary-search-trees/

           The node to be deleted has no children - is_leaf() = true
The node to be deleted has only one child - promote to take place of parent
The node to be deleted has two children - replace with successor() TBD

           ### Graphs
           Edge list - graph = [[0, 1], [0, 2], [1, 2], [2, 3], [2, 4], [4, 5]]
           Adjacency list -A list where the index represents the node and the value at that index is a list of the node’s neighbors:


           graph = [
    [1, 2],
    [0, 2],
    [0, 1, 3, 4],
    [2],
    [2, 5],
    [4]
]
or a dictionary
           graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 4],
    3: [2],
    4: [2, 5],
    5: [4]
}


           Adjacency Matrix - A matrix of 0 and 1 indicating whether node x connects to node y (0 means no, 1 means yes).
https://emre.me/data-structures/graphs/
           
           
if __name__ == "__main__":
    unittest.main()
