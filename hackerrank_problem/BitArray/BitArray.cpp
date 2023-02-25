#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  long long int n, s, p, q, m = 0x100000000, i = 0, j=0, pq, t;
  std::vector<long long int*>::iterator it;
  cin >> n >> s >> p >> q;
  p = p % m;
  vector<long long int *> a(n, nullptr);
  
  a[i] = new long long int(s % m );
  for (i = 1; i<n; i++) {
    //a[i-1]*P+Q
    t = ((*a[i-1] * p) % m + q) % m;
    a[i] = new long long int(t);
  }
  it = std::unique(a.begin(), a.begin() + n);
  a.resize(std::distance(a.begin(), it));
  cout<< a.size()<< "\n";
  return 0;
}