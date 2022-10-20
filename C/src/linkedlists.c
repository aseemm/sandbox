#include <stdio.h>
#include <malloc.h>
#include <iostream>

using namespace std;

// When looping over a linked list, figure out how you will use the last element
// c->next != NULL => last element hasn't been processed
// c != NULL       => all elements have been processed
#define DEBUG 1

struct Node {
    int data;
    struct Node *next;
};

// Add a node to the top of the list
void insertList(struct Node **head, int data) {
  struct Node *node = (struct Node *) malloc (sizeof(struct Node));
  node->data = data;
  node->next = *head;
  *head = node;
}

// Print
void printList(struct Node **head) {
  struct Node *c = *head;  
#ifdef DEBUG
  int count = 0;
#endif
  
  while (c != NULL) { 
#ifdef DEBUG
    count++;
    if (count > 10) return;
#endif    
    printf("%d -> ", c->data);
    c = c->next;
  }
  printf("NULL\n", c);
  cout << "hello" << endl;
}

// Adding a node to the end of the list
void appendList(struct Node **head, int d) {
    struct Node *c = *head;
    
    // create the end node
    struct Node *node = (struct Node *) malloc (sizeof(struct Node));
    node->data = d;
    node->next = NULL;

    // walk through the list until the end
    while (c != NULL) {
      if (c->next->next == NULL) {
	c->next->next = node;
	return;
      }
      c = c->next;
    }
}

void deleteList(struct Node **head, int d) {
  struct Node *c = *head;
  struct Node *tail; // points to the last entry we're sure of
  
  /*
    If the first node is the one to be deleted
    A -> B -> C -> D -> NULL
    c
  */
  if (c->data == d) {
    *head = c->next;
    return;
  }
  /*
    Not the first node
    A -> B -> C -> D -> NULL
         c
  */
  while (c != NULL) { 
    if (c->data == d) {
      // remove node
      tail->next = c->next;
      return;
    } else {
      // move the chains
      tail = c;
      c = c->next;
    }
  }
  return;
}

void mergeLists(struct Node **n1, struct Node **n2) {
    // plan to return n1, as the final list
  /*
    n1 -> 4 -> 8 -> 15 -> 19 -> NULL
          c1   
          tail
    n2 -> 7 -> 9 -> 10 -> 16 -> NULL
          c2   t2
  */	
  // pointer to keep track of where we are
#ifdef DEBUG  
  int count = 0;
#endif  
  struct Node *c1 = *n1;
  struct Node *c2 = *n2;
  struct Node *t2;
  struct Node *tail; // points to the last entry we've merged correctly  

  // if one of the lists is empty
  if (n1 == NULL) {
    n1 = n2;
    return;
  }
  if (n2 == NULL) {
    return;
  }

  while (c1 != NULL && c2 != NULL) {
#ifdef DEBUG
    count++;
    if (count > 10) return;
#endif
    
    // if one of the lists is about to go empty
    if (c1 == NULL) {
      tail->next = c2;
    }
    if (c2 == NULL) {
      return;
    }      
    
    if (c1->data <= c2->data) {
      tail = c1;
      c1 = c1->next;
    } else {
      t2 = c2->next;
      tail->next = c2;
      c2->next = c1;
      tail = c2; // don't go too far ahead and start pointing to c1
      c2 = t2;
    }
  }
  return;	
}

void reverseList(struct Node **head) {
  struct Node *p = NULL;
  struct Node *c = *head;
  struct Node *n = *head;

  while (c != NULL) {
    n = c->next;
    c->next = p;
    p = c;
    c = n;
  }
  *head = p;
}

void reverseRecursiveList(struct Node **head) {
  struct Node *f = *head;
  struct Node *r = (*head)->next;  


  /*
    A -> B -> C -> D -> NULL
    f    r    

        (NULL)
         ^
	 |
    A -> B <- C <- D 
    f              r    
  */
  
  if (r == NULL) {
    // only one element in the list
    *head = f;
    return;
  }	
  reverseRecursiveList(&r);
  f->next->next = f;
  f->next = NULL;
  *head = r;
}

int main() {
  struct Node *list = NULL;
  struct Node *list1 = NULL;
  struct Node *list2 = NULL;  

  // create a simple linked list
  /* insertList(&list, 1); */
  /* insertList(&list, 2); */
  /* insertList(&list, 3); */
  /* printList(&list); */

  /* appendList(&list, 0); */
  /* appendList(&list, -1); */
  /* printList(&list); */

  /* deleteList(&list, 1); */
  /* printList(&list); */
  /* deleteList(&list, -1); */
  /* printList(&list); */

  /* reverseList(&list); */
  /* printList(&list); */

  insertList(&list1, 1);
  insertList(&list1, 2);
  insertList(&list1, 3);    
  printList(&list1);    
  reverseRecursiveList(&list1);
  printf("final output --\n");
  printList(&list1);  
  
  /* // merge linked lists   */
  /* insertList(&list1, 19); */
  /* insertList(&list1, 15); */
  /* insertList(&list1, 8); */
  /* insertList(&list1, 4); */
  /* printList(&list1); */
  
  /* insertList(&list2, 16); */
  /* insertList(&list2, 10); */
  /* insertList(&list2, 9); */
  /* insertList(&list2, 7);   */
  /* printList(&list2); */

  /* mergeLists(&list1, &list2); */
  /* printList(&list1); */
  
  return 0;
}
