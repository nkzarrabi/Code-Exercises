#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

// convert number to string
char* num2str(unsigned int x, unsigned int digits)
{
  char* result = (char*)malloc(digits + 1);
  result[digits] = '\0';
  // it's faster to generate the digits in reverse order ...
  while (digits-- > 0)
  {
    result[digits] = (char)(x % 10 + '0');
    x /= 10;
  }
  return result;
}

// ... and back
unsigned int str2num(char* str)
{
  unsigned int result = 0;
  for (char* s = str; *s != '\0'; s++)
  {
    result *= 10;
    result += *s - '0';
  }
  return result;
}

// Function to swap values given their pointers
void swap(void* v1, void* v2, size_t size) {
    void* temp = malloc(size);
    memcpy(temp, v1, size);
    memcpy(v1, v2, size);
    memcpy(v2, temp, size);
    free(temp);
}

// Function to reverse a range of elements
void reverse(void* base, size_t num, size_t size) {
    char* lo = base;
    char* hi = lo + (num - 1) * size;
    while (lo < hi) {
        swap(lo, hi, size);
        lo += size;
        hi -= size;
    }
}


int next_permutation(void* base, size_t num, size_t size, int (*compar)(const void*, const void*)) {
    if (num <= 1) return 0;

    char* last = (char*)base + (num - 1) * size;
    char* next = last - size;

    // Step 1
    while (next >= (char*)base && compar(next, next + size) >= 0) {
        next -= size;
    }

    if (next < (char*)base) return 0; // Last permutation

    // Step 2
    char* greater;
    for (greater = last; compar(next, greater) >= 0; greater -= size);

    // Step 3
    swap(next, greater, size);

    // Step 4
    reverse(next + size, (last - next) / size, size);

    return 1;
}


// fill all gaps in mask (marked as '.') with the digits found in str and return result as a number
unsigned int merge(char* strFill, char* mask)
{
  unsigned int result = 0;
  for (char* m = mask; *m != '\0'; m++)
  {
    result *= 10;
    // if placeholder '.' is found, then take next digit from strFill
    if (*m == '.')
      result += *strFill++ - '0';
    else // else take the digit of the mask
      result += *m - '0';
  }
  return result;
}


unsigned int calculateSum(unsigned int digits, unsigned int cancel) {
    const unsigned int Tens[MAX_DIGITS] = {1, 10, 100, 1000, 10000};
    unsigned int sumN = 0, sumD = 0;
    unsigned int keep = digits - cancel;
    unsigned int* used = calloc(10000, sizeof(unsigned int));
    if (!used) return 0; // Error handling for memory allocation

    for (unsigned int d = 1; d < Tens[keep]; d++) {
        for (unsigned int n = 1; n < d; n++) {
            char* strN = num2str(n, keep);
            char* strD = num2str(d, keep);
            for (unsigned int insert = Tens[cancel - 1]; insert < Tens[cancel]; insert++) {
                char* strInsert = num2str(insert, cancel);
                int isAscending = checkAscending(strInsert); // Implement this function based on your logic
                if (!isAscending) continue;

                char* strInsertN = createInsertStr(strInsert, keep); // Implement this based on your description
                do {
                    unsigned int newN = merge(strN, strInsertN);
                    if (newN < Tens[digits - 1]) continue;

                    char* strInsertD = createInsertStr(strInsert, keep); // Similar to strInsertN creation
                    do {
                        unsigned int newD = merge(strD, strInsertD);
                        if (newN * d == newD * n && !used[newN * 10000 + newD]) {
                            sumN += newN;
                            sumD += newD;
                            used[newN * 10000 + newD] = 1;
                        }
                    } while (next_permutation(strInsertD, strInsertD + strlen(strInsertD)));
                    free(strInsertD);
                } while (next_permutation(strInsertN, strInsertN + strlen(strInsertN)));
                free(strInsertN);
                free(strInsert);
            }
            free(strN);
            free(strD);
        }
    }
    free(used);
    return sumN, sumD;
}

int main() {
    unsigned int digits, cancel;
    scanf("%u %u", &digits, &cancel);
    unsigned int sumN, sumD;
    sumN, sumD = calculateSum(digits, cancel);
    printf("%u %u\n", sumN, sumD);
    return 0;
}
