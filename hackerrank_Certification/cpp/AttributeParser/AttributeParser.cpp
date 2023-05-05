#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

void getInput(int lineCount, vector<string> &ref)
{
  for (int i = 0; i < lineCount; i++)
  {
    string temp;
    getline(cin, temp);
    ref.push_back(temp);
  }
  for (vector<string>::iterator it = ref.begin(); it != ref.end(); it++)
    cout << *it << '\n';
  cout << endl;
}
void split(const char *str)
{
  char *ptr;
  ptr = strtok(*str, " ");
  while (ptr != NULL)
  {
    cout << ptr << endl; // print the string token
    ptr = strtoq(NULL, ' ');
  }
}

void htmlParsing(const string &htmlLine)
{
  string rowLine = htmlLine.substr(1, htmlLine.size() - 2);
  cout << rowLine << "\n";
}

int main()
{
  int htmlCount, queryCount;
  cin >> htmlCount >> queryCount;
  cout << htmlCount << " " << queryCount << "\n";
  vector<string> htmls;
  vector<string> queries;
  cin.ignore();
  getInput(htmlCount, htmls);
  getInput(queryCount, queries);

  for (vector<string>::iterator it = htmls.begin(); it != htmls.end(); it++)
    htmlParsing(*it);
  cout << endl;
  return 0;
}
