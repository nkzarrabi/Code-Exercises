// Coin Sums 

#include <stdio.h>

#define MOD 1000000007
#define MAXN 100000
int main() {
    int T;
    scanf("%d", &T);

    // Precompute the number of ways for all possible N up to the maximum value in the input range.
    // This is more efficient than recalculating for each test case.
    int maxN = 100000; // Maximum N based on problem constraints
    long long ways[MAXN + 1]; // Declare the array without initializing

    // Initialize the ways array to 0
    for (int i = 0; i <= maxN; i++) {
        ways[i] = 0;
    }
    ways[0] = 1; // There is 1 way to make 0 pence - use no coins.


    int coins[] = {1, 2, 5, 10, 20, 50, 100, 200};
    int numCoins = sizeof(coins) / sizeof(coins[0]);

    for (int i = 0; i < numCoins; i++) {
        for (int j = coins[i]; j <= maxN; j++) {
            ways[j] = (ways[j] + ways[j - coins[i]]) % MOD;
        }
    }

    // Handle test cases
    for (int i = 0; i < T; i++) {
        int N;
        scanf("%d", &N);
        printf("%lld\n", ways[N]);
    }

    return 0;
}
