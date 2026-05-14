class Solution {
public:
    bool isPalindrome(int x) {
        // Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;
        
        int reversedHalf = 0;
        
        // Only reverse half the digits
        while (x > reversedHalf) {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }
        
        // x == reversedHalf        → even digits (e.g. 1221)
        // x == reversedHalf / 10   → odd digits  (e.g. 121, middle digit ignored)
        return x == reversedHalf || x == reversedHalf / 10;
    }
};