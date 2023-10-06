#include <iostream>
#include <cmath>

using namespace std;

int main () {
    //Declarar variables
    int a = 0, b = 0, c = 0;
    int respuesta [2];

    //Usuario ingresa variables
    cout << "Ingrese el valor de a: ";
    cin >> a;
    cout << "Ingrese el valor de b: ";
    cin >> b;
    cout << "Ingrese el valor de c: ";
    cin >> b;

    //Formula general de la ecuacion cuadratica
    respuesta[0] = (-b + sqrt((b^2) - 4*a*c))/2*a;
    respuesta[1] = (-b - sqrt((b^2) - 4*a*c))/2*a;

    //Imprimir respuesta
    cout << "La respuesta 1 es: " << respuesta[0] << endl;
    cout << "La respuesta 2 es: " << respuesta[1] << endl;

    return 0;
}