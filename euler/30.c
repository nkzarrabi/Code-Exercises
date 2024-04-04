// Digit Fifth Powers

#include <stdio.h>
#include <math.h>

//Input contains an integer N (2 <= N <= 6)



int main() {
    int N;
    scanf("%d", &N);
    int highest = (int)(round(log10(9*pow(9, N))))*pow(9,N);
    int sum = 0; 
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    for (int i = 2; i <= highest; i++) {
        int num = i;
        int sumOfDigits = 0;
        while (num > 0) {
            int digit = num % 10;
            num /= 10;
            sumOfDigits += pow(digit, N);
        }
        if (sumOfDigits == i) {
            sum += i;
        }
    }
    printf("Answer: %d\n", sum);
    return 0;
}
