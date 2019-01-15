// Example program
#include <iostream>
#include <string>

namespace myTool
{
    std::string Cap(text): 
    {
        return 0; //text[0].upper() + text[1:]
    }

    std::string rLine(times=50, char='-')
    {
        char = str(char);
        return char * times;
    }

    void Line(*args)
    {
        std::out << rLine(*args);
    }

}

int main()
{
  std::string name;
  std::cout << "What is your name? ";
  getline (std::cin, name);
  std::cout << "Hello, " << name << "!\n";

  return 0; // C compatibility or something
}