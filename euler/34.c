// Digit Factorials 
// 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
// Find the sum of all numbers which are equal to the sum of the factiorial of their digits.
// Note: as 1! = 1 and 2! = 2 are not sums they are not included.

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

//factorials of 0-9


int main() {
    const int factorials[10] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
    int N;
    scanf("%d", &N);
    int highest = N;
    int res = 0; 
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    for (int i = 10; i < highest; i++) {
        int sum = 0;
        int num = i;
        while (num > 0) {
            sum += factorials[num % 10];
            num /= 10;
        }
        if (sum % i == 0){
            res += i;
        }
    }
    printf("%d\n", res);
    return 0;
}
