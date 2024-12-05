#include <cpr/cpr.h>
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>

// requete get pour recupérer notre requete json avec a, b et x
// ensuite il faut parser ça dans des eigens
// puis resoudre a*x=b avec eigen à la place de numpy comme précéddemment
// refaire une class cpp pour Task
// pour voir le res du proxy aller à l'adresse http://localhost:8000/
class Task {
public:
  int identifier;
  int size;
  float time;

  Task() {}

  void work() {}

  string to_json() {}

  Task from_json(text) {}

  static void operator=() {}
};

int main(int argc, char **argv) {
  cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/"});
  r.status_code;            // 200
  r.header["content-type"]; // application/json; charset=utf-8
  r.text;                   // JSON text string
  return 0;
}
