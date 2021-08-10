#include<stdio.h>

int main() {
  long long int i, n, k, t, c;
  scanf("%lld %lld", &n, &k);
  c = 0;
  for(i=0; i<n; i++) {
    scanf("%lld", &t);
    if(t%k == 0) {
      c++;
    }
  }
  printf("%lld\n", c);
  return 0;
}