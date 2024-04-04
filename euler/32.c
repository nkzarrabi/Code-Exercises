// Pandigital products
// Problem 32

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MAX_DIGITS 10

int compareUnsignedInt(const void *a, const void *b) {
    return (*(unsigned int *)a - *(unsigned int *)b);
}

void swap(unsigned int *x, unsigned int *y) {
    unsigned int temp = *x;
    *x = *y;
    *y = temp;
}

int nextPermutation(unsigned int *array, int size) {
    // Find the rightmost element which is smaller than its next element
    int i = size - 2;
    while (i >= 0 && array[i] >= array[i + 1])
        i--;
    if (i < 0)
        return 0; // Last permutation reached

    // Find the rightmost element that exceeds the value of element at 'i'
    int j = size - 1;
    while (array[j] <= array[i])
        j--;

    // Swap elements at 'i' and 'j'
    swap(&array[i], &array[j]);

    // Reverse the order of elements after 'i'
    int k = i + 1, l = size - 1;
    while (k < l) {
        swap(&array[k], &array[l]);
        k++;
        l--;
    }
    return 1;
}

int main() {
    unsigned int maxDigit, digits[MAX_DIGITS], valid[MAX_DIGITS * MAX_DIGITS], validCount = 0, sum = 0;
    scanf("%u", &maxDigit);

    if (maxDigit < 1 || maxDigit > 9) {
        printf("Invalid input. Please enter a number between 1 and 9.\n");
        return 1;
    }

    // Initialize digits array
    for (unsigned int i = 0; i < maxDigit; i++) {
        digits[i] = i + 1;
    }

    do {
        for (unsigned int lenA = 1; lenA < maxDigit; lenA++)
            for (unsigned int lenB = 1; lenB < maxDigit - lenA; lenB++) {
                unsigned int lenC = maxDigit - lenA - lenB;
                if (lenC < lenA || lenC < lenB)
                    break;

                unsigned int pos = 0, a = 0, b = 0, c = 0;

                for (unsigned int i = 0; i < lenA; i++, pos++)
                    a = a * 10 + digits[pos];
                for (unsigned int i = 0; i < lenB; i++, pos++)
                    b = b * 10 + digits[pos];
                for (unsigned int i = 0; i < lenC; i++, pos++)
                    c = c * 10 + digits[pos];

                if (a * b == c) {
                    int exists = 0;
                    for (unsigned int i = 0; i < validCount; i++) {
                        if (valid[i] == c) {
                            exists = 1;
                            break;
                        }
                    }
                    if (!exists) {
                        valid[validCount++] = c;
                    }
                }
            }
    } while (nextPermutation(digits, maxDigit));

    for (unsigned int i = 0; i < validCount; i++)
        sum += valid[i];

    printf("%u\n", sum);
    return 0;
}