#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

void getInput(int lineCount, vector<string> &ref)
{
  for (int i = 0; i < lineCount; i++)
  {
    string temp;
    getline(cin, temp);
    ref.push_back(temp);
  }
  // for (vector<string>::iterator it = ref.begin(); it != ref.end(); it++)
  //   cout << *it << '\n';
  // cout << endl;
}
vector<string> split(const string &input, char delimiter)
{
  vector<std::string> result;
  stringstream ss(input);
  string item;

  while (getline(ss, item, delimiter))
  {
    result.push_back(item);
  }

  return result;
}
void htmlParsing(const string &htmlLine)
{
  string rowLine = htmlLine.substr(1, htmlLine.length() - 2);
  cout << rowLine << "\n";
}

int main()
{
  int htmlCount, queryCount;
  cin >> htmlCount >> queryCount;
  vector<string> htmls;
  vector<string> queries;
  cin.ignore();
  getInput(htmlCount, htmls);
  getInput(queryCount, queries);

  for (vector<string>::iterator it = htmls.begin(); it != htmls.end(); it++)
  {
    htmlParsing(*it);
  }

  return 0;
}
