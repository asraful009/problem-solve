#include <stdio.h>

int main() {
  float wf = 0.00f, init = 0.0f;
  int w = 0;
  scanf("%d %f", &w, &init);
  if(w % 5 == 0) {
    wf = w;
    if(wf + 0.5f<= init) {
      printf("%.2f\n", init-wf-0.5f);
    } else {
      printf("%.2f\n", init);
    }
  } else {
    printf("%.2f\n", init);
  }
  return 0;
}