#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'counterGame' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts LONG_INTEGER n as parameter.
 */

string counterGame(long n)
{
  cout << n << "-> " << bitset<64>(n) << "\n";
  int p = 0;
  while (n > 1)
  {
    long double a = log2(n);
    long double b = floor(a);
    cout << a << "::" << b << "\n";
    if (a == b)
    {
      n /= 2;
    }
    else
    {
      n = n - pow(2, b);
    }
    p = 1 - p;
    // cout << p << " : " << n << "\n";
  }
  string t = (p == 0 ? "Richard" : "Louise");
  cout << t << "\n";
  return t;
}

int main()
{
  ofstream fout("o");

  string t_temp;
  getline(cin, t_temp);

  int t = stoi(ltrim(rtrim(t_temp)));

  for (int t_itr = 0; t_itr < t; t_itr++)
  {
    string n_temp;
    getline(cin, n_temp);

    long n = stol(ltrim(rtrim(n_temp)));

    string result = counterGame(n);

    fout << result << "\n";
  }

  fout.close();

  return 0;
}

string ltrim(const string &str)
{
  string s(str);

  s.erase(
      s.begin(),
      find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace))));

  return s;
}

string rtrim(const string &str)
{
  string s(str);

  s.erase(
      find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
      s.end());

  return s;
}
