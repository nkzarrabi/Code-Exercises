// Digit Factorials 
// 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
// Find the sum of all numbers which are equal to the sum of the factiorial of their digits.
// Note: as 1! = 1 and 2! = 2 are not sums they are not included.

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

//factorials of 0-9

const int factorials[10] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};

// Function to check if sum is divisible by i
int isDivisible(int sum, int i) {
    return sum % i == 0;
}

// Function to check if sum is equal to i
int isEqual(int sum, int i) {
    return sum == i;
}

int main() {
    int N, choice;
    scanf("%d %d", &N, &choice); // Read N and the choice for condition
    int res = 0;

    // Choose the condition based on user input
    int (*condition)(int, int) = (choice == 1) ? isEqual : isDivisible;

    for (int i = 10; i < N; i++) {
        int sum = 0;
        int num = i;
        while (num > 0) {
            sum += factorials[num % 10];
            num /= 10;
        }
        
        if (condition(sum, i)) {
            res += i;
        }
    }
    printf("%d\n", res);
    return 0;
}
