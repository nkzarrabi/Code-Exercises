// 197 is a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
// Find the sum of circular primes below N.

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

// Function to check if a number is prime
// Improved prime checking function
int isprime(int n) {
    if (n < 2) return 0; // Numbers less than 2 are not prime
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return 0;
    }
    return 1; // Number is prime
}

int isCircularPrime(int n) {
    int len = floor(log10(n)) + 1;
    int pow10 = pow(10, len - 1);
    for (int i = 0; i < len; i++) {
        if (!isprime(n)) return 0;
        n = n / 10 + (n % 10) * pow10;
    }
    return 1;
} 


int main() {
    int N, choice;
    scanf("%d %d", &N, &choice); // Read N and the choice for condition
    int sum = 0;
    for (int i = 2; i < N; i++) {
        if (isCircularPrime(i)) {
            sum += (choice == 0) ? 1 : i;
        }
    }
    printf("%d\n", sum);
    return 0;
}