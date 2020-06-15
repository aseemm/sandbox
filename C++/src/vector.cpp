#include <iostream>
#include "assert.h"

using namespace std;

/*
 Implement a vector (mutable array with automatic resizing)
	* size(), resize(), capacity(), isEmpty()
	* at(index)
	* push(item), pop(item)
	* insert(index, item), delete(index)
	* find(item), remove(item)
*/
class myVector {
  int *p;
  int count;
  int capacity;

  bool isPowerOfTwo(int n) {
    // cout << __LINE__ << ": " << "isPowerOfTwo = " << n << endl;
    
    if (n == 0)
      return 0;
    while (n != 1) {
      if (n%2 != 0)
	return 0;
      n = n/2;
    }
    return 1;
  }

  int resize(int newCapacity) {
      int *p_saved = p;
      p = new int[newCapacity];
      for (int i = 0; i < count; i++) {
	// copy over the old data
	p[i] = p_saved[i];
      }
      capacity = newCapacity;
      delete p_saved;    
  }
  
public:
  // constuctor
  myVector() {
    count = 0;
    capacity = 0;    
    p = NULL;
  }

  // destructor
  ~myVector() {
    delete p;
  }

  void printVector() {
    // print the contents of the vector
    if (!isEmpty()) {
      cout << __LINE__ << ": ";
      for (int i = 0; i < count; i++) {
	cout << at(i) << " ";
      }
      cout << endl;
    } else {
      cout << __LINE__ << ": " << "Vector is empty" << endl;
    }
  }

  int isEmpty() {
    if (count == 0)
      return 1;
    else
      return 0;
  }
  
  int size() {
    return count;
  }

  void push(int item) {
    if (isEmpty()) {
      // check to see if we need to allocate more memory
      resize(1);
      cout << __LINE__ << ": " << "Pushing " << item << " at location " << count << endl;
      p[count++] = item;
    } else {
      // if we are at capacity, then double the size of the memory
      if (isPowerOfTwo(count)) {
	assert(capacity == count);
	cout << __LINE__ << ": " << "Increasing capacity from " << capacity << " to " << capacity*2 << endl;
	resize(capacity*2);
	cout << __LINE__ << ": " << "Pushing " << item << " at location " << count << endl;	
	p[count++] = item;
      } else {
	cout << __LINE__ << ": " << "Pushing " << item << " at location " << count << endl;
	p[count++] = item;
      }
    }
  }

  int pop() {
    int item;
    assert (count != 0);

    item = p[--count];
    cout << __LINE__ << ": " << "Popping " << item << " at location " << count << endl;    

    // if size is 1/4 capacity, resize to half
    if (count == capacity/2) {
      cout << __LINE__ << ": " << "Decreasing capacity from " << capacity << " to " << capacity/2 << endl;      
      resize(capacity/2);
    }
    return item;
  }

  int at(int index) {
    return p[index];
  }
};

int main()
{
  myVector vector;

  for (int i = 0; i < 10; i++) {
    vector.push(i);
    vector.printVector();
  }

  for (int i = 0; i < 10; i++) {
    vector.pop();
    vector.printVector();    
  }

  for (int i = 0; i < 3; i++) {
    vector.push(i);
    vector.push(i);    
    vector.pop();
    vector.printVector();        
  }  

  return 0;
}
