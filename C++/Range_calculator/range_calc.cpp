#include <iostream>
#include <iomanip>

using namespace std;

//Function declaration

double eydsla(double x, double y);
double kostnadur(double x, double y);
double margfalda(double x, double y);
double deila(double x, double y);


int main() {
    double Kwh, length, kostnadurPerKwh;
    char val;
    double utkoma;

    cout << "Hve stórt er batteríið í Kwh? ";
    cin >> Kwh;
    cout << "Hve langt kemstu á fullri hleðslu? ";
    cin >> length;
    cout << " " << endl;
    cout << "Veldu aðgerð:" << endl;
    cout << " " << endl;
    cout << "1. Fyrir kwh/100km útreikning. " << endl;
    cout << "2. Fyrir kostnaðarútreikning fyrir hleðslu. " << endl;
    cin >> val;


    switch (val) {
        case '1':
            utkoma = eydsla(Kwh, length);
            cout << "Meðaleyðsla: " << utkoma;
            cout << "Kwh/100km" << endl;
            break;
        case '2':
            cout << "Sláðu inn verð per Kwh. ";
            cin >> kostnadurPerKwh;
            utkoma = kostnadur(Kwh, kostnadurPerKwh);
            cout << "Heildarkostnaður fyrir 0-100% hleðslu: " << utkoma;
            cout << "kr" << endl;
            break;

        default:
            cout << "Röng aðgerð valin." << endl;
            return 1; // Loka forriti með villukóða 1
    }

    //cout << "Útkoma: " << utkoma << endl;
    return 0; // Success
}

// Function definitions
double eydsla(double x, double y) {
    return x / y * 100;     //Kwh / length * 100
}

double kostnadur(double x, double y) {
    return x * y;
}