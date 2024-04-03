#include <stdio.h>

// Return (base^exponent) % modulo
unsigned int powmod(unsigned long long base, unsigned int exponent, unsigned int modulo) {
    unsigned long long result = 1;
    while (exponent > 0) {
        // Odd exponent?
        if (exponent % 2 == 1) {
            result = (result * base) % modulo;
            exponent--;
        } else {
            base = (base * base) % modulo;
            exponent /= 2;
        }
    }
    return result;
}

// Return modulo multiplicative inverse of a such that (a*inverse(a)) % p = 1
unsigned int modInverse(unsigned int a, unsigned int modulo) {
    // Fermat's little theorem: a^(p-2) is the modular multiplicative inverse of a modulo p
    return powmod(a, modulo - 2, modulo);
}

int main() {
    unsigned int tests;
    scanf("%u", &tests);
    while (tests--) {
        unsigned long long n;
        scanf("%llu", &n);

        // Sum along the diagonals, initially for width = 1
        unsigned long long sum = 1;

        // Direct computation:
        unsigned long long x = n / 2;
        const unsigned int Modulo = 1000000007;

        x %= Modulo;

        // First part: 8 * x * (x + 1) * (2*x + 1) / 3
        unsigned long long sharedTerm = (2*x * (x + 1)) % Modulo;
        unsigned long long sum1 = ((4 * sharedTerm * (2*x + 1)) % Modulo) * modInverse(3, Modulo);

        // Second part: 2 * x * (x + 1) + 4 * x + 1
        unsigned long long sum2 = sharedTerm + 4*x + 1;

        // sum = first part + second part
        sum = (sum1 % Modulo + sum2 % Modulo) % Modulo;

        printf("%llu\n", sum);
    }
    return 0;
}
