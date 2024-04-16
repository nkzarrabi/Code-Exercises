// https://projecteuler.net/problem=36
// https://www.hackerrank.com/contests/projecteuler/challenges/euler036/problem

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

// Function to check if a number is a palindrome 
int isPalindrome(int n,int base) {
    int rev = 0;
    int num = n;
    while (num > 0) {
        rev = rev * base + num % base;
        num /= base;
    }
    return rev == n;
}

int main() {
    int N, K;
    scanf("%d %d", &N, &K); // Read N and the choice for condition
    int sum = 0;
    for (int i = 1; i < N; i++) {
        if (isPalindrome(i,10) && isPalindrome(i,K)) {
            sum += i;
        }
    }
    printf("%d\n", sum);
    return 0;
}