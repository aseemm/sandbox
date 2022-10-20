#include <stdio.h>
#include <string>
#include <iostream>
#include <bitset>

using namespace std;

/* 
Given two 32-bit numbers, N and M, and two bit positions, i and j. Write a
method to set all bits between i and j in N equal to M (e.g., M becomes a substring of
N located at i and starting at j)

EXAMPLE:
Input: N = 10000000000, M = 10101, i = 2, j = 6
Output: N = 10001010100
*/
int updateBits(int n, int m, int i, int j){
  // create a mask
  unsigned int mask = 0xffffffff;

  // clear out the lower & upper bits
  mask = (mask >> i) << i;
  mask = (mask << (32-j-1)) >> (32-j-1);

  // clear out the appropriate bits in n, and then put m in there
  return (n & ~mask) | ((m << i) & mask);
}

/*
Given a (decimal - e.g. 3.72) number that is passed in as a string, print the binary rep-
resentation. If the number can not be represented accurately in binary, print “ERROR”
*/
string convertToBinary(string num) {
  string retValue = "ERROR";
  
  std::size_t pos = 0;

  pos = num.find(".");
  if (pos != std::string::npos) {
    // extract decimal & integer part
    cout << stoi(num) << endl;
  } else {
    // only integer part
    int temp = stoi(num);
    cout << std::bitset<8>(temp) << endl;
  }

  return retValue;
}
