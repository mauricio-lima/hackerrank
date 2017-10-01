/*
STL Iterators
http://www.cprogramming.com/tutorial/stl/iterators.html





*/




#include <iostream>
#include <vector>

using namespace std;


class Person{
	protected:
		string firstName;
		string lastName;
		int id;
	public:
		Person(string firstName, string lastName, int identification){
			this->firstName = firstName;
			this->lastName = lastName;
			this->id = identification;
		}
		void printPerson(){
			cout<< "Name: "<< lastName << ", "<< firstName <<"\nID: "<< id << "\n"; 
		}
	
};





class Student :  public Person{
	private:
		vector<int> testScores;
    
	public:
        Student(string firstName, string lastName, int identification, vector<int> scores) : Person(firstName, lastName, identification)
         {
          testScores = scores;   
         }
    
        char calculate()
         {
          vector<int>::iterator iterator;
          int                   average;
            
          average = 0;
          for(iterator = testScores.begin(); iterator != testScores.end(); iterator++)
           {
            average += *iterator;   
           }
          average /= testScores.size();
            
          if (average < 40)
            return 'T';
            
          if (average < 55)
            return 'D';
            
          if (average < 70)
            return 'P';
            
          if (average < 80)
            return 'A';
            
          if (average < 90)
            return 'E';
            
          if (average <= 100)
            return 'O';
            
          return 'U';  
         }
 };





int main() {
	string firstName;
  	string lastName;
	int id;
  	int numScores;
	cin >> firstName >> lastName >> id >> numScores;
  	vector<int> scores;
  	for(int i = 0; i < numScores; i++){
	  	int tmpScore;
	  	cin >> tmpScore;
		scores.push_back(tmpScore);
	}
	Student* s = new Student(firstName, lastName, id, scores);
	s->printPerson();
	cout << "Grade: " << s->calculate() << "\n";
	return 0;
}



