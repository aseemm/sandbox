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
  int _count;
  int _capacity;

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

  int resize(int new_Capacity) {
      int *p_saved = p;
      p = new int[new_Capacity];
      for (int i = 0; i < _count; i++) {
	// copy over the old data
	p[i] = p_saved[i];
      }
      _capacity = new_Capacity;
      delete p_saved;    
  }

public:
  // constuctor
  myVector() {
    _count = 0;
    _capacity = 0;    
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
      for (int i = 0; i < _count; i++) {
	cout << at(i) << " ";
      }
      cout << endl;
    } else {
      cout << __LINE__ << ": " << "Vector is empty" << endl;
    }
  }
  
  int size() {
    return _count;
  }
  
  int isEmpty() {
    if (_count == 0)
      return 1;
    else
      return 0;
  }

    int capacity() {
    return _capacity;
  }
    
  int at(int index) {
    return p[index];
  }

  void push(int item) {
    if (isEmpty()) {
      // check to see if we need to allocate more memory
      resize(1);
      cout << __LINE__ << ": " << "Pushing " << item << " at location " << _count << endl;
      p[_count++] = item;
    } else {
      // if we are at _capacity, then double the size of the memory
      if (isPowerOfTwo(_count)) {
	assert(_capacity == _count);
	cout << __LINE__ << ": " << "Increasing _capacity from " << _capacity << " to " << _capacity*2 << endl;
	resize(_capacity*2);
	cout << __LINE__ << ": " << "Pushing " << item << " at location " << _count << endl;	
	p[_count++] = item;
      } else {
	cout << __LINE__ << ": " << "Pushing " << item << " at location " << _count << endl;
	p[_count++] = item;
      }
    }
  }

  int pop() {
    int item;
    assert (_count != 0);

    item = p[--_count];
    cout << __LINE__ << ": " << "Popping " << item << " at location " << _count << endl;    

    // if size is 1/4 _capacity, resize to half
    if (_count == _capacity/2) {
      cout << __LINE__ << ": " << "Decreasing _capacity from " << _capacity << " to " << _capacity/2 << endl;      
      resize(_capacity/2);
    }
    return item;
  }

  void insert(int index, int item) {
    assert(index <= _count);
    cout << __LINE__ << ": " << "Inserting " << item << " at location " << index << endl;

    // resize as needed
    if (isPowerOfTwo(_count)) {
      cout << __LINE__ << ": " << "Increasing _capacity from " << _capacity << " to " << _capacity*2 << endl;
      resize(_capacity*2);
    }

    for (int i = _count; i >= 0; i--) {
      // copy over the old fields
      if (index == i) {	
	p[i] = item;
	_count++;
	break;
      } else {
	p[i] = p[i-1];
      }
    }
  }

  void _delete(int index) {
    assert(index <= _count);
    cout << __LINE__ << ": " << "Deleting " << p[index] << " at location " << index << endl;
    
    for (int i = 0; i < _count; i++) {
      if (i <= index) {
	// don't change anything
      } else {
	p[i-1] = p[i];
      }
    }
    _count--;
    
    // if size is 1/4 _capacity, resize to half
    if (_count == _capacity/2) {
      cout << __LINE__ << ": " << "Decreasing _capacity from " << _capacity << " to " << _capacity/2 << endl;      
      resize(_capacity/2);
    }
  }

  int find(int item) {
    // return the first index
    for (int i = 0; i < _count; i++) {
      if (p[i] == item) {
	return i;
      }
    }
    return -1;
  }

  void remove(int item) {
    int index = find(item);
    while (index != -1) {
      _delete(index);
      index = find(item);      
    }
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

  for (int i = 0; i < vector.size(); i++) {  
    cout << "Element at location " << i << " = " << vector.at(i) << endl;
  }

  vector.printVector();            
  vector.insert(0, 4);
  vector.printVector();          
  vector.insert(4, 5);
  vector.printVector();
  vector.insert(2, 5);
  vector.printVector();

  vector._delete(0);
  vector.printVector();
  vector._delete(4);
  vector.printVector();

  vector.insert(2, 5);
  vector.push(5);
  cout << "Element 5 is at location " << vector.find(5) << endl;  
  vector.printVector();  

  cout << "Removing element 5" << endl;    
  vector.remove(5);
  vector.printVector();
  return 0;
}
