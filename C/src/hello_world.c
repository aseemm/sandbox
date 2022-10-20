#include <stdio.h>

int main() {
  FILE *fp;
  char buf[256];

  fp = fopen("hello_world.txt", "r");
  fscanf(fp, "%s", buf);

  printf("Hello, %s World!\n", buf);
  return 0;
}

