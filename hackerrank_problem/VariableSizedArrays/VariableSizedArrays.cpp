#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  vector<vector<int>> arr2d;
  int n, q, k = 0, qIndex, qPos, v;
  cin >> n >> q;
  for(int i=0; i<n; i++) {
    cin >> k;
    vector<int> arr;
    for(int j=0; j<k; j++) {
      cin >> v;
      arr.push_back(v);
    }
    arr2d.push_back(arr);
    // for(int j=0; j<k; j++) {
    //   cout << arr2d[i][j] << " ";
    // }
    // cout << "\n";
  }
  for(int i=0; i<q; i++) {
    cin >> qIndex >> qPos;
    cout << arr2d[qIndex][qPos] << endl;
  }
  return 0;
}