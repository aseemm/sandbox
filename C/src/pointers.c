#include <stdio.h>
     
int main() {
  int **ipp;
  int *ip1, *ip2;
  int i, j, k;

  i = 5; j = 6; k = 7;
  ip1 = &i; ip2 = &j;

  printf("i=%d, j=%d, k=%d\n", i, j, k);
  printf("ip1=%p, ip2=%p, *ip1=%d, *ip2=%d\n", ip1, ip2, *ip1, *ip2);

  ipp = &ip1;
  printf("ipp=%p, *ipp=%p, **ipp=%d\n", ipp, *ipp, **ipp);  

  return 0;
}
