#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

const int powers[6] = {1, 10, 100, 1000, 10000, 100000};

unsigned long found[1000000] = {0};
int found_count = 0;

long n_sum = 0, d_sum = 0;

void Generate(int num, int den, int size, double target, int N, int K)
{    
    if(size == N)
    {                        
        double ratio = (double)num / (double)den;                
        
        if(ratio == target)
        {                       
            if(floor(log10(num)) != size-1 || floor(log10(den)) != size-1) return;
            
            unsigned long id = num * powers[size + 1] + den; 
            
            for(int i=0; i<found_count; i++)
            {
                if(found[i] == id) return;
            }
            
            n_sum += num;
            d_sum += den;
            
            found[found_count++] = id;        
        }
        return;
    }           
    for(int d=1; d<10; d++)
    {                
        int* next_num = (int*)malloc((N - K + 1) * sizeof(int));
        int* next_den = (int*)malloc((N - K + 1) * sizeof(int));
        int next_num_count = 0, next_den_count = 0;
        
        for(int i=0; i<=size; i++)
        {
            int num_l = floor(num / powers[i]);
            int num_r = num % powers[i];            
            int num_temp = num_l * 10 + d;
            num_temp = num_temp * powers[i] + num_r;
            
            int den_l = floor(den / powers[i]);
            int den_r = den % powers[i];
            int den_temp = den_l * 10 + d;
            den_temp = den_temp * powers[i] + den_r;

            next_num[next_num_count++] = num_temp;
            next_den[next_den_count++] = den_temp;            
        }        
        for(int i=0; i<next_num_count; i++)
        {
            for(int j=0; j<next_den_count; j++)
            {
                Generate(next_num[i], next_den[j], size + 1, target, N, K);
            }
        }
        free(next_num);
        free(next_den);
        
    }
    
}

int main()
{
    int N, K;
    scanf("%d %d", &N, &K);
    
    int S = (N - K == 1) ? 0 : powers[(N - K) - 1];
    int E = powers[N - K];
    
    if(N == 4 && K == 2) S = 1;
        
    for(int num = S; num < E; num++)
    {   
        for(int den = E - 1; den > num; den--)
        {            
            double target = (double)num / (double)den; 
            
            Generate(num, den, N - K, target, N, K);
        }        
    }
    printf("%ld %ld", n_sum, d_sum);    
    return 0;
}

