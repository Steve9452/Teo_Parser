/*
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
*/

#include <iostream>
#include <vector>
using namespace std;

//Estructura de pasatiempo
struct TPasatiempo{
    string nombre;
    string tipo;
    string genero;
};
typedef struct TPasatiempo Pasatiempo;

//Funcion de crear un nuevo pasatiempo
Pasatiempo solicitarPasatiempo(){
    Pasatiempo p;
    cout << "Nombre: "; cin >> p.nombre;
    cout << "Tipo: ";   cin >> p.tipo;
    cout << "Genero: "; cin >> p.genero;
    return p;
}

//Funcion de mostrar un pasatiempo
void mostrarPasatiempo(Pasatiempo p){
    cout << "Nombre: " << p.nombre << endl;
    cout << "Tipo: " << p.tipo << endl;
    cout << "Genero: " << p.genero << endl;
    cout << endl;
}

//Crear lista de pasatiempos
vector<Pasatiempo> lista;

//Agregar un pasatiempo a la lista
void agregarPasatiempo(){
    Pasatiempo p = solicitarPasatiempo();
    bool continuar = true;
    do{
        int opcion = 0;
        cout << "\t1) Al principio\n\t2) Al final"
            << "\n\tOpcion elegida: ";
        cin >> opcion;
        switch(opcion){
            case 1: lista.insert(lista.begin(), p);
                continuar = false;
            break;
            case 2: lista.push_back(p);
                continuar = false;
            break;
            default: cout << "Opcion erronea!" << endl;
            break;
        }
    }while(continuar);
}

//Mostrar la  lista en consola
void mostrarLista() {
    for (int i = 0; i < lista.size(); i++) 
        mostrarPasatiempo(lista[i]);
}

int main(){
    cout << "Inicializando..." << endl;
    
    bool continuar = true;
    //Menu principal
    do{
        int opcion = 0;
        cout << "Menu: \n\t1) Agregar Pasatiempo\n\t2) Ver pasatiempos"
            << "\n\t3) Salir\n\tOpcion elegida: ";
        cin >> opcion;
        switch(opcion){
            case 1: cout << "Agregando..." << endl;
                agregarPasatiempo();
            break;
            case 2: cout << "Listando..." << endl;
                mostrarLista();
            break;
            case 3: continuar = false;
            break;
            default: cout << "Opcion erronea!" << endl;
            break;
        }
    }while(continuar);

    return 0;
}