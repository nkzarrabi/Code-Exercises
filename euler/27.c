// Quadratic Primes 

#include <stdio.h>
#include <stdlib.h>
#include <math.h>


// Quadratic formula function
int quadratic(int n, int a, int b) {
    return n*n + a*n + b;
}

// Improved prime checking function
int isprime(int n) {
    if (n < 2) return 0; // Numbers less than 2 are not prime
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return 0;
    }
    return 1; // Number is prime
}

int main() {
    int max = 0;
    int product = 0;
    for (int a = -999; a < 1000; a++) {
        for (int b = -1000; b <= 1000; b++) {
            int n = 0;
            // Ensure the result of quadratic is positive and check if it's prime
            while (isprime(quadratic(n, a, b))) {
                n++;
            }
            if (n > max) {
                max = n;
                product = a * b;
            }
        }
    }
    printf("The product of coefficients a and b that produce the maximum number of primes is: %d\n", product);
    return 0;
}
