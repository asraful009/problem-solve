#include <iostream>
#include <cstdlib>
using namespace std;

class GridNode {
  
  public:
    string val = "";
    int color = -1;
    
    GridNode() {}

    GridNode(string val) {
      this->val = val;
    }

    ~GridNode() {}
    
    void setColor(int color) {
      this->color = color;
    }
    string to_string() {
      return this->val + "[" + std::to_string(this->color) +"]";
    }
};

class Grid {
  private:
    GridNode** nodes;
    int weight, height;

    void travel(int index, string c, int color) {
      // cout<<index<< " >> " <<(index < this->size * this->size) << " "<< (index >=0)<<endl;
      if(index < this->weight * this->height && index >=0) {
        if(this->nodes[index]->color == -1 && this->nodes[index]->val.compare(c) == 0 ) {
          this->nodes[index]->color = color;
          // cout<< "travel: "<<(index+1) << " " << (index-1) <<" " << (index+this->size)<<" " << (index-this->size)<< endl;
          // cout << "edge : "<< index << " right "<< ((index+1) % this->weight)<<endl;
          // cout << "edge : "<< index << " left "<< ((index) % this->weight)<<endl;
          if(((index+1) % this->weight)) travel((index+1) , c, color);
          if(((index) % this->weight)) travel((index-1) , c, color);
          travel((index + this->weight) , c, color);
          travel((index - this->weight) , c, color);
        }

      }
    }

  public:
    Grid() {}

    ~Grid() {
      delete [] this->nodes;
    }


    void InputGrid() {
      string t = "";
      cin>>this->weight>> this->height;
      this->nodes = new GridNode*[this->weight*this->height];
      for(int i=0; i<this->weight*this->height; i++) {
        cin>>t;
        this->nodes[i] = new GridNode(t);
      }
    }

    void print() {
      for(int i=0; i<this->weight*this->height; i++) {
        cout<< "("<<i<<")"<<this->nodes[i]->to_string() << " ";
        if((i+1)%this->weight ==0)
          cout << endl;
      }
    }

    int travel() {
      int color = 0;
      for(int i=0; i<this->weight*this->height; i++) {
        if(this->nodes[i]->color == -1) {
          travel(i, this->nodes[i]->val, ++color);
        }
      }
      return color;
    }


};

int main(int argc, char *argv[]) {
  Grid *grid = new Grid();
  grid->InputGrid();
  grid->print();
  cout<<"------------------------------------\n";
  cout<< grid->travel()<<endl;
  cout<<"------------------------------------\n";
  grid->print();

  return 0;
}
