#include <vector>
#include <iostream>
using namespace std;

class Student
{
  const static int __N = 5;

public:
  int scores[__N];
  void input()
  {
    for (int i = 0; i < __N; i++)
    {
      cin >> scores[i];
    }
  }
  int calculateTotalScore()
  {
    int score = 0;
    for (int i = 0; i < __N; i++)
    {
      score += scores[i];
    }
    return score;
  }
};

int main()
{
  int n; // number of students
  cin >> n;
  Student *s = new Student[n]; // an array of n students

  for (int i = 0; i < n; i++)
  {
    s[i].input();
  }

  // calculate kristen's score
  int kristen_score = s[0].calculateTotalScore();

  // determine how many students scored higher than kristen
  int count = 0;
  for (int i = 1; i < n; i++)
  {
    int total = s[i].calculateTotalScore();
    if (total > kristen_score)
    {
      count++;
    }
  }

  // print result
  cout << count;

  return 0;
}
