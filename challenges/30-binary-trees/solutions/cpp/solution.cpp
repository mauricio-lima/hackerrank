#include <iostream>
#include <cstddef>
#include <queue>
#include <string>
#include <cstdlib>

using namespace std;	
class Node{
    public:
        int data;
        Node *left,*right;
        Node(int d){
            data=d;
            left=right=NULL;
        }
};


class Solution
 {
    public:
  		Node* insert(Node* root, int data){
            if(root==NULL){
                return new Node(data);
            }
            else{
                Node* cur;
                if(data<=root->data){
                    cur=insert(root->left,data);
                    root->left=cur;
                }
                else{
                   cur=insert(root->right,data);
                   root->right=cur;
                 }           
           return root;
           }
        }
        
        
        




    void levelOrder(Node * root)
     {
      queue<Node*> level;
      Node*        node;  
  
        
      if (!root)
        return;
      
      level.push(root);
      while(!level.empty())
       {
        node = level.front();
        
        cout << node->data << ' ';
          
        level.pop();  
        if (node->left)  level.push(node->left);
        if (node->right) level.push(node->right); 
       }
     }




};//End of Solution


int main()
 {
  Solution myTree;
  Node*    root=NULL;
  int      T,data;
  
  
  cin>>T;
  while(T-- > 0)
   {
    cin>>data;
    root= myTree.insert(root,data);
   }
  myTree.levelOrder(root);
    
  return 0;
 }
 