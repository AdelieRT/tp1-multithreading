#include <cpr/cpr.h>
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
#include <chrono>
#include <string>
#include <Eigen/Dense>

// requete get pour recupérer notre requete json avec a, b et x
// ensuite il faut parser ça dans des eigens
// puis resoudre a*x=b avec eigen à la place de numpy comme précéddemment
// refaire une class cpp pour Task
// pour voir le res du proxy aller à l'adresse http://localhost:8000/
class Task {
public:
  int identifier;
  int size;
  std::chrono::time_point<std::chrono::steady_clock> end;
  std::chrono::time_point<std::chrono::steady_clock> start;
  //duration in nanoseconds
  std::chrono::duration<long int, std::ratio<1, 1000000000>> duration;
  //use matrixxf with eigen lib
  Eigen::MatrixXf a;
  Eigen::MatrixXf b;
  Eigen::MatrixXf x;

  Task(int identifier=0, int size=0) {
    std::srand((std::time(0)));
    this->identifier = identifier;
    if(size==0){
      this->size = std::rand() % 2700 + 300; // Random size between 300 and 3000
    }
    //initialisation de a et b avec des randoms
    this->a = Eigen::MatrixXf::Random(this->size, this->size);
    this->b = Eigen::MatrixXf::Random(this->size, 1);
    //initialisation de x en matrice[size, 1]=[0....0]
    this->x = Eigen::MatrixXf::Zero(this->size, 1);
  }

  void work() {
    this->start = std::chrono::steady_clock::now();
    this->x = this->b * this->a.inverse();
    this->end = std::chrono::steady_clock::now();
    this->duration = this->end - start;
  }

  std::string to_json() {

    return 0;
  }

  Task from_json(std::string text) {

    return 0;
  }

  Task operator=(Task const& obj) {
    return 0;
  }
};

int main(int argc, char **argv) {
  Task t = Task();
  //std::cout << t.x << std::endl;
  t.work();
  //std::cout << (t.duration.count())/1e9 << " sec" << std::endl;


  cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/"});
  r.status_code;            // 200
  r.header["content-type"]; // application/json; charset=utf-8
  r.text;                   // JSON text string
  return 0;
}
