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
//mettre des commentaires de ce que l'on cherche à faire pas de ce que le code fait
class Task {
public:
  int identifier;
  int size;
  std::chrono::time_point<std::chrono::steady_clock> end;
  std::chrono::time_point<std::chrono::steady_clock> start;
  //temps de tache en nanoseconds
  std::chrono::duration<long int, std::ratio<1, 1000000000>> duration;
  float time;
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
    this->time = 0;
  }

  void work() {
    this->start = std::chrono::steady_clock::now();
    this->x = this->b * this->a.inverse();
    this->end = std::chrono::steady_clock::now();
    this->duration = this->end - start;
    this->time = this->duration.count();
  }

  std::string to_json() {
    nlohmann::json task_json;

    nlohmann::json a_array = nlohmann::json::array();
    for(int i=0; i<this->size; i++){
      for(int j=0; j<this->size; j++){
        a_array.push_back(this->a.coeff(i,j));
      }
    }

    nlohmann::json b_array = nlohmann::json::array();
    for(int i=0; i<this->size; i++){
      b_array.push_back(this->b.coeff(i,1));
    }

    nlohmann::json x_array = nlohmann::json::array();
    for(int i=0; i<this->size; i++){
      x_array.push_back(this->x.coeff(i,1));
    }
    

    task_json["identifier"] = this->identifier;
    task_json["size"] = this->size;
    task_json["a"] = a_array;
    task_json["b"] = b_array;
    task_json["x"] = x_array;
    task_json["time"] = this->time;

    return task_json.dump();
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
  t.work();
  //durée de taches en seconde
  std::cout << (t.time)/1e9 << " sec" << std::endl;
  std::string t_to_j = t.to_json();
  //task to json
  std::cout << t_to_j << std::endl;

  //dans l'autre sens il faudra couper à chaque fois qu'on atteindra la size


  cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/"});
  r.status_code;            // 200
  r.header["content-type"]; // application/json; charset=utf-8
  r.text;                   // JSON text string
  return 0;
}
