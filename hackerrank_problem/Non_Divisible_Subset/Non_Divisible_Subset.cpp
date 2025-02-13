#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'nonDivisibleSubset' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY s
 * not finish
 */

int nonDivisibleSubset(int k, vector<int> s)
{
  set<int> taken;
  for (size_t i = 0; i < s.size(); i++)
  {
    int firstSelectedCandidate = s[i];
    // std::set<int>::iterator fit = taken.find(firstSelectedCandidate);
    // if (fit != taken.end())
    //   continue;
    for (size_t j = 0; j < s.size(); j++)
    {
      if (i == j)
        continue;
      int secondSelectedCandidate = s[j];
      // std::set<int>::iterator sit = taken.find(secondSelectedCandidate);
      // if (sit != taken.end())
      //   continue;
      int m = (firstSelectedCandidate + secondSelectedCandidate) % k;
      std::cout
          << firstSelectedCandidate << " + " << secondSelectedCandidate
          << " = " << (firstSelectedCandidate + secondSelectedCandidate) << " % " << k << " == " << m << endl;

      if (m != 0)
      {
        taken.insert(firstSelectedCandidate);
        taken.insert(secondSelectedCandidate);
      }
      for (int element : taken)
      {
        cout << element << " ";
      }
      cout << "\n";
    }
  }
  for (int element : taken)
  {
    cout << element << " ";
  }
  cout << "\n"
       << taken.size() << endl;

  return taken.size();
}

int main()
{
  ofstream fout("o");

  string first_multiple_input_temp;
  getline(cin, first_multiple_input_temp);

  vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

  int n = stoi(first_multiple_input[0]);

  int k = stoi(first_multiple_input[1]);

  string s_temp_temp;
  getline(cin, s_temp_temp);

  vector<string> s_temp = split(rtrim(s_temp_temp));

  vector<int> s(n);

  for (int i = 0; i < n; i++)
  {
    int s_item = stoi(s_temp[i]);

    s[i] = s_item;
  }

  int result = nonDivisibleSubset(k, s);

  fout << result << "\n";

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

vector<string> split(const string &str)
{
  vector<string> tokens;

  string::size_type start = 0;
  string::size_type end = 0;

  while ((end = str.find(" ", start)) != string::npos)
  {
    tokens.push_back(str.substr(start, end - start));

    start = end + 1;
  }

  tokens.push_back(str.substr(start));

  return tokens;
}
