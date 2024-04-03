// Number Spiral Diagonals 
// Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
/*
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
*/

#include <stdio.h>

void spiral(int n) {
    int sum = 1;
    for (int i = 3; i <= n; i += 2) {
        sum += 4*i*i - 6*i + 6;
    }
    printf("%d\n", sum);
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    /* The first line contains an integer T */
    /* The next T lines each contain an integer N */
    int t, n;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        scanf("%d", &n);
        spiral(n);
    }
}


