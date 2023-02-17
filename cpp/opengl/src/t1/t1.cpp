#include <iostream>
#include <string>
#include <cmath>
#include <bits/stdc++.h>

struct Vertex {
  double x, y, z;
};

std::ostream& operator<<(std::ostream& stream, const Vertex& vertex) {
  stream << "{ \"x\": "<< vertex.x << ", \"y\": "<< vertex.y << ", \"z\":" << vertex.z << " }";
  return stream;
}

std::ostream& operator<<(std::ostream& stream, const std::vector<double>& arr) {
  stream << "[";
  std::cout.precision(32);
  for (double d: arr) {
    stream << " "<< std::fixed << d << ",";
  }
  stream << "]\n";
  return stream;
}

std::ostream& operator<<(std::ostream& stream, const std::vector<Vertex* >& vertices) {
  stream << "[\n";
  std::size_t size = vertices.size();
  for (std::size_t i = 0; i < size-1; i++) {
    stream << "  "<< *vertices[i] << ",\n";
  }
  stream << "  "<< *vertices[size-1] << "\n]\n";
  return stream;
}

void fileRead(std::vector<Vertex* >& vertices) {
    std::ifstream ifile("i", std::ios::in);

    if (!ifile.is_open()) {
      std::cerr << "There was a problem opening the input file!\n";
      exit(1);
    }

    double x, y, z;
    while (ifile >> x >> y >> z) {
      vertices.push_back(new Vertex({x, y, z}));
    }
    ifile.close();

    //verify that the scores were stored correctly:
    
      // std::cout<<vertices;

    return;
}

double binomialCoefficients(int n, int k) {
   double C[k+1];
   memset(C, 0, sizeof(C));
   C[0] = 1;
   for (int i = 1; i <= n; i++) {
      for (int j = std::min(i, k); j > 0; j--)
         C[j] = C[j] + C[j-1];
   }
   return C[k];
}

void bezierCurves(const std::vector<Vertex*>& vertices, const double rate) {
  if(rate <=0.0f) return;
  std::vector<Vertex*> bcPoints;
  std::vector<double> coeff;
  const int vertexSize = vertices.size();
  for (int index = 0; index < vertexSize; index++) {
    coeff.push_back(binomialCoefficients(vertexSize - 1, index));
  }
  // std::cout<<coeff;
  for (double t = 0.0; t <= 1.0; t += rate) {
    Vertex* bcPoint = new Vertex({.0f, .0f ,.0f});
    for (int index = 0; index < vertexSize; index++) {
      double p1t = std::pow((1.0 - t), (double)(vertexSize - index - 1));
      double pt = std::pow(t, (double)(index));
      bcPoint->x += coeff[index] * p1t * pt * vertices[index]->x;
      bcPoint->y += coeff[index] * p1t * pt * vertices[index]->y;
      //std::cout<< *bcPoint<< std::endl;
    }
    bcPoints.push_back(bcPoint);
  }
  std::cout<< bcPoints;
//   console.log({ bCValues });
};


int main() {
  std::vector<Vertex*> vertices;
  fileRead(vertices);
  bezierCurves(vertices, .0001321f);
}