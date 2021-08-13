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
    int size;

    void travel(int index, string c, int color) {
      if(index == this->size * this->size)
      try {
        if(this->nodes[index]->color == -1 && this->nodes[index]->val.compare(c) == 0 ) {
          this->nodes[index]->color = color;

          travel((index+1) , c, color);
        }
      } catch(const std::exception& e) {
        std::cerr << e.what() << '\n';
      }
    }

  public:
    Grid() {}

    ~Grid() {
      delete [] this->nodes;
    }


    void InputGrid() {
      string t = "";
      cin>>this->size;
      this->nodes = new GridNode*[this->size*this->size];
      for(int i=0; i<this->size*this->size; i++) {
        cin>>t;
        this->nodes[i] = new GridNode(t);
      }
    }

    void print() {
      for(int i=0; i<this->size*this->size; i++) {
        cout<< this->nodes[i]->to_string() << " ";
        if((i+1)%this->size ==0)
          cout << endl;
      }
    }

    void travel() {
      for(int i=0; i<this->size*this->size; i++) {
        travel(i, this->nodes[i]->val, 1);
      }
    }


};

int main(int argc, char *argv[]) {
  Grid *grid = new Grid();
  grid->InputGrid();
  grid->print();
  cout<<"------------------------------------\n";
  grid->travel();
  cout<<"------------------------------------\n";
  grid->print();

  return 0;
}
