#include <iostream>
#include <string>
using namespace std;

string string_prime(string a, string b)
{
  if (a.length() > 0 && b.length() > 0)
  {
    return b.substr(0, 1) + a.substr(1, a.length()) + " " +
           a.substr(0, 1) + b.substr(1, b.length());
  }
  else if (a.length() == 0 && b.length() > 0)
  {
    return b.substr(0, 1) + " " +
           b.substr(1, b.length());
  }
  else if (a.length() > 0 && b.length() == 0)
  {
    return a.substr(1, a.length()) + " " + a.substr(1, a.length());
  }
  else
  {
    return " ";
  }
}
int main()
{
  // Complete the program
  string a, b;
  cin >> a >> b;
  cout << a.length() << " " << b.length() << "\n"
       << (a + b) << "\n"
       << string_prime(a, b) << "\n";
  return 0;
}