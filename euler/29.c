// Distinct Powers

#include <stdio.h>
#include <stdlib.h>

int main() {
    unsigned int maxExponent;
    scanf("%u", &maxExponent);

    const unsigned int MaxBasePower = 16;
    unsigned int* minExponent = calloc((maxExponent+1) * MaxBasePower, sizeof(unsigned int));
    for (unsigned int i = 1; i <= MaxBasePower; i++) {
        for (unsigned int j = 1; j <= maxExponent; j++) {
            if (minExponent[i*j] == 0)
                minExponent[i*j] = i;
        }
    }

    unsigned int* base = calloc(maxExponent + 1, sizeof(unsigned int));
    unsigned int repeated = 0;

    for (unsigned int x = 2; x <= maxExponent; x++) {
        unsigned int parent = base[x];
        if (parent == 0) {
            unsigned int power = x * x;
            while (power <= maxExponent) {
                base[power] = x;
                power *= x;
            }
            continue;
        }

        unsigned int exponent = 0, reduce = x;
        while (reduce > 1) {
            reduce /= parent;
            exponent++;
        }

        for (unsigned int y = 2; y <= maxExponent; y++) {
            if (minExponent[y * exponent] < exponent)
                repeated++;
        }
    }

    unsigned long long all = maxExponent - 1;
    unsigned long long result = all*all - repeated;
    printf("%llu\n", result);

    free(minExponent);
    free(base);
    return 0;
}
