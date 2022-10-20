/*
  Hashmap
 */

#include <stdio.h>
#include <stdlib.h>

// insert
// _delete
// find
// display
// hash - map key to array index, SHA2-family or Mod (for strings, convert to an integer)
// collisions - store both records in a single array location, or move one of the records to a new location that we acn find later
// chaining - each array location is a pointer to a linked list, need to keep the load factor (size of the linked list down)
// open addressing - store extra elements in unused array locations, using scheme like linear probing (keep walking through the array until we find an empty location)

#define SIZE 16

struct dataItem {
  int key;
  int value;
};
struct dataItem *hashArray[SIZE];

// use a simple modulo function
int getHash(int key) {
  return key % SIZE;
}

void display() {
  for (int i = 0; i < SIZE; i++) {
    if (hashArray[i] != NULL) {
      printf(" (%d %d)", hashArray[i]->key, hashArray[i]->value);
    } else {
      printf(" (- -)");
    }
  }
  printf("\n");
}

void insert(int key, int value) {
  struct dataItem *item = (struct dataItem *) malloc(sizeof(struct dataItem));
  item->key = key;
  item->value = value;

  int hashIndex = getHash(key);

  // move in array until an empty or deleted cell
  while ((hashArray[hashIndex] != NULL) && hashArray[hashIndex]->key != -1) {
    hashIndex++;
    hashIndex %= SIZE;
  }
  hashArray[hashIndex] = item;
}

int _delete(int key) {
  int hashIndex = getHash(key);

  // move in array until an empty or deleted cell
  while (hashArray[hashIndex] != NULL) {
    if (hashArray[hashIndex]->key == key) {
      hashArray[hashIndex]->key = -1;
      hashArray[hashIndex]->value = -1;      
      hashIndex++;
      hashIndex %= SIZE;
      return 1;
    }
  }
    return -1;
}

int find(int key) {
  int hashIndex = getHash(key);

  // move in array until an empty or deleted cell
  while (hashArray[hashIndex] != NULL) {
    if (hashArray[hashIndex]->key == key)
      return hashArray[hashIndex]->value;
    hashIndex++;
    hashIndex %= SIZE;
  }
  return -1;
}

/* int main() { */
/*   printf("Inserting entries...\n"); */
/*   insert(1, 10); */
/*   insert(10, 20); */
/*   insert(1, 30); */
/*   display(); */

/*   printf("find(1) = %d\n", find(1)); */
/*   printf("find(2) = %d\n", find(2)); */
/*   printf("find(10) = %d\n", find(10)); */

/*   printf("Deleting entries...\n"); */
/*   printf("delete(1) = %d\n", _delete(1)); */
/*   display(); */

/*   printf("delete(10) = %d\n", _delete(10)); */
/*   display(); */

/*   printf("find(1) = %d\n", find(1)); */
/*   printf("find(2) = %d\n", find(2)); */
/*   printf("find(10) = %d\n", find(10));   */
/* } */
