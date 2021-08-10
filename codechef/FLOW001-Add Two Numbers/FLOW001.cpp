#include<stdio.h>

int main() {
  long long int i, t, a, b;
  scanf("%lld", &t);
  for(i=0; i<t; i++) {
    scanf("%lld %lld", &a, &b);
    printf("%lld\n", (a+b));
  }
  return 0;
}