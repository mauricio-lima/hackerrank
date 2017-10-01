#include <string>
#include <iostream>

using namespace std;


int main()
 {
  string s;
  

  cin >> s;
  try
   {
    cout << stoi(s) << endl;
   }
  catch(invalid_argument)
   {
    cout << "Bad String" << endl;   
   }

  return 0;
 }
