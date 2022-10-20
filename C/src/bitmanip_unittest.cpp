#include "bitmanip.c"
#include <gtest/gtest.h>
 
TEST(testUpdateBits, Sanity) {
  ASSERT_EQ(0x454, updateBits(0x400, 0x15, 2, 6));
}

TEST(testConvertToBinary, Sanity) {
  ASSERT_EQ("2", convertToBinary("2"));
}
 
int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
