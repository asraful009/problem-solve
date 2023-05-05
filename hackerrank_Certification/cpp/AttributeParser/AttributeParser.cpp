#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
#include <sstream>
#include <map>
#include <regex>
using namespace std;

class HtmlObj
{
public:
  string tag;
  map<string, string> attributes;
  vector<HtmlObj> childTags;
  HtmlObj(const string tag, const map<string, string> attributes)
  {
    this->tag = tag;
    this->attributes = attributes;
  }
};

void splitAttributes(const string &attributes, map<string, string> &attributeMap)
{
  std::regex regex("\\s*([^=\\s]+)\\s*=\\s*\"([^\"]*)\"\\s*");
  std::smatch match;

  std::string::const_iterator searchStart(attributes.cbegin());
  while (std::regex_search(searchStart, attributes.cend(), match, regex))
  {
    attributeMap[match[1].str()] = match[2].str();
    searchStart = match.suffix().first;
  }
}

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

vector<string> findTagAndAttributes(const string &rowLine)
{
  vector<string> tagAndAttr;
  size_t pos = rowLine.find(' ');
  if (pos != string::npos)
  {
    tagAndAttr.push_back(rowLine.substr(0, pos));
    tagAndAttr.push_back(rowLine.substr(pos));
  }
  else
  {
    tagAndAttr.push_back(rowLine);
  }
  return tagAndAttr;
}

void htmlParser(const int index, const vector<string> &htmls, map<string, HtmlObj *> &mapHtml)
{
  string htmlLine = htmls[index];
  string rowLine = htmlLine.substr(1, htmlLine.length() - 2);
  cout << "[" << index << "] line: " << rowLine << "\n";
  vector<string> tagAndAttrs = findTagAndAttributes(rowLine);
  string tag = tagAndAttrs[0];
  map<string, string> attributeMap;
  if (tagAndAttrs.size() == 2)
  {
    splitAttributes(tagAndAttrs[1], attributeMap);
  };
  mapHtml["df"] = new HtmlObj(tag, attributeMap);

  if (htmls.size() > index + 1)
  {
    htmlParser(index + 1, htmls, mapHtml);
  }
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
  map<string, HtmlObj *> mapHtml;
  htmlParser(0, htmls, mapHtml);
  return 0;
}
