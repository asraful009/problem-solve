#include <iostream>
#include <cmath>
#include <bits/stdc++.h>

struct Vertex {
  double x, y, z;
};

std::ostream& operator<<(std::ostream& stream, const Vertex& vertex) {
  stream << "{ x: "<< vertex.x << ", y: "<< vertex.y << ", z:" << vertex.z << " }";
  return stream;
}

std::ostream& operator<<(std::ostream& stream, const std::vector<double>& arr) {
  stream << "[";
  for (double d: arr) {
    stream << " "<< d << ",";
  }
  stream << "]\n";
  return stream;
}

std::ostream& operator<<(std::ostream& stream, const std::vector<Vertex* >& vertices) {
  stream << "[\n";
  for (Vertex* v: vertices) {
    stream << "  "<< *v << ",\n";
  }
  stream << "]\n";
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
    
      std::cout<<vertices;

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
  std::cout<<coeff;
  for (double t = 0.0; t <= 1.0; t += rate) {
    Vertex* bcPoint = new Vertex({.0f, .0f ,.0f});
    for (int index = 0; index < vertexSize; index++) {
      double p1t = std::pow((1.0 - t), (double)(vertexSize - index + 1));
      double pt = std::pow(t, (double)(vertexSize - index + 1));
      std::cout<< p1t<<", "<< pt <<"\n";
      // bcPoint[pointIndex] += coeff[index] * p1t * pt * arr[index];
    }
  }
//   console.log({ bCValues });
};


int main() {
  std::vector<Vertex*> vertices;
  fileRead(vertices);
  bezierCurves(vertices, .021f);
}