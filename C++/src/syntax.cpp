#include <iostream>
using namespace std;

#define NAME_SIZE 50 // macro

class Person {
  // all data members/methods private by default
  int id;
  char name[NAME_SIZE];

public:
  Person() {
    // empty
  }
  
  Person(int a) : id(a) {
    id = a;
  }

  // destructor
  ~Person() {
    // empty
  }

  void aboutMe() {
    cout << "I am a person" << endl;
  }
};

class Student: public Person {
public:
  void aboutMe() {
    cout << "I am a student" << endl;
  }
};    

int main() {
  Student *pStudent = new Student();

  pStudent->aboutMe(); // prints "I am a student"
  delete pStudent; // delete allocated memory

  return 0;
}
