#include <iostream>
#include "assert.h"

using namespace std;

/*
 Implement a vector (mutable array with automatic resizing)
	* size(), resize(), capacity(), is_empty()
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
    // cout << "isPowerOfTwo = " << n << endl;
    
    if (n == 0)
      return 0;
    while (n != 1) {
      if (n%2 != 0)
	return 0;
      n = n/2;
    }
    return 1;
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
    if (!is_empty()) {
      for (int i = 0; i < count; i++) {
	cout << p[i] << " ";
      }
      cout << endl;
    } else {
      cout << "Vector is empty" << endl;
    }
  }

  int is_empty() {
    if (count == 0)
      return 1;
    else
      return 0;
  }
  
  int size() {
    return count;
  }

  int push(int item) {
    // check to see if we need to allocate more memory
    if (is_empty()) {
      p = new int(1);
      cout << "Inserting " << item << " at location " << count << endl;	      
      p[count++] = item;
      capacity = 1;
    } else {
      // if we are at capacity, then double the size of the memory
      int *p_saved = p;
      if (isPowerOfTwo(count)) {
	assert(capacity == count);
	cout << "Increasing capacity from " << capacity << " to " << capacity*2 << endl;
	p = new int[capacity*2];
	for (int i = 0; i < count; i++) {
	  // copy over the old data
	  p[i] = p_saved[i];
	}
	capacity = capacity * 2;
	cout << "Inserting " << item << " at location " << count << endl;	
	p[count++] = item;
	delete p_saved;
      } else {
	cout << "Inserting " << item << " at location " << count << endl;
	p[count++] = item;
      }
    }
  }
  
  int resize() {
  }
};

int main()
{
  myVector vector;

  for (int i = 0; i < 10; i++) {
    vector.push(i);
    vector.printVector();
  }

  return 0;
}
