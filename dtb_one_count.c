#include <stdio.h>
#include<string.h>
int main() {
    int num;
    printf("Enter a decimal number: ");
    scanf("%d", &num);
    int flag = 0,c = 0;
    for(int i = 31; i >= 0; i--){
        int bit = (num >> i) & 1;
        if(bit == 1){
            flag = 1;
            c++;
        }
        if(flag){
            printf("%d", bit);
        }
        
    }
    if(flag == 0){
        printf("0");
    }
    printf("\nCount of 1's: %d\n", c);
    return 0;
}
