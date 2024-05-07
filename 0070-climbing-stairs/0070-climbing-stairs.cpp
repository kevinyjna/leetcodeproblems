class Solution {
public:
    int climbStairs(int n) {
        int res = 0;
        int one = 1;
        int two = 2;
        if (n == 1) {
            return one;
        }
        if (n == 2){
            return two;
        } 
        for (int i = 2; i < n; i++) {
            
            res = one + two;
            one = two;
            two = res;
 
        }
        
        return res;
    }
};