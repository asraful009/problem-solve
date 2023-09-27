#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'equalizeArray' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */
bool sortByValue(const pair<int, int> &a, const pair<int, int> &b)
{
  return a.second > b.second;
}

int equalizeArray(vector<int> arr)
{
  map<int, int> feq;
  for (int v : arr)
  {
    map<int, int>::iterator it = feq.find(v);

    if (it != feq.end())
    {
      feq[v]++;
    }
    else
    {
      feq[v] = 1;
    }
  }
  // for (const auto &pair : feq)
  // {
  //   int v = pair.first;
  //   int f = pair.second;
  //   std::cout << "v: " << v << ", feq: " << f << std::endl;
  // }

  vector<pair<int, int>> vectorOfPairs(feq.begin(), feq.end());

  // Sort the vector by values using the custom comparator
  sort(vectorOfPairs.begin(), vectorOfPairs.end(), sortByValue);

  // Display the sorted elements
  // for (const auto &pair : vectorOfPairs)
  // {
  //   std::cout << "Key: " << pair.first << ", Value: " << pair.second << std::endl;
  // }

  return arr.size() - vectorOfPairs[0].second;
}

int main()
{
  ofstream fout("o");

  string n_temp;
  getline(cin, n_temp);

  int n = stoi(ltrim(rtrim(n_temp)));

  string arr_temp_temp;
  getline(cin, arr_temp_temp);

  vector<string> arr_temp = split(rtrim(arr_temp_temp));

  vector<int> arr(n);

  for (int i = 0; i < n; i++)
  {
    int arr_item = stoi(arr_temp[i]);

    arr[i] = arr_item;
  }

  int result = equalizeArray(arr);

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
