
#include <bits/stdc++.h>
#pragma once
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
