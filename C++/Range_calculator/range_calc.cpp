#include <iostream>
#include <iomanip>
#include <limits> 

using namespace std;

//Declarations
double eydsla(double x, double y);
double kostnadur(double x, double y);

int main() {
    double Kwh, drægni, kostnadurPerKwh;
    char val;
    double utkoma;

    do {
        cout << "Hve stórt er batteríið í Kwh? ";
        while (!(cin >> Kwh)) {
            cin.clear(); // Clear error flag
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Ignore wrong input
            cout << "Invalid input. Please enter a valid number for Kwh: ";
        }
        if (Kwh <= 0) {
            cout << "Please enter a positive number for Kwh.\n";
        }
     } while (Kwh <= 0);

    do {
        cout << "Hve langt kemstu á fullri hleðslu? ";
        while (!(cin >> drægni)) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Invalid input. Please enter a valid number for range: ";
        }
        if (drægni <= 0) {
            cout << "Please enter a positive number for range.\n";
        }
    } while (drægni <= 0);

    cout << endl;
    cout << "Veldu aðgerð:" << endl;
    cout << endl;
    cout << "1. Fyrir kwh/100km útreikning. " << endl;
    cout << "2. Fyrir kostnaðarútreikning fyrir hleðslu. " << endl;
    cin >> val;

    switch (val) {
        case '1':
            utkoma = eydsla(Kwh, drægni);
            cout << "Meðaleyðsla: " << utkoma;
            cout << "Kwh/100km" << endl;
            break;
        case '2':
            cout << "Sláðu inn verð per Kwh. ";
            while (!(cin >> kostnadurPerKwh)) {
                cin.clear(); // Clear error flag
                cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Ignore wrong input
                cout << "Invalid input. Please enter a valid number for cost per Kwh: ";
                
            }
            utkoma = kostnadur(Kwh, kostnadurPerKwh);
            cout << "Heildarkostnaður fyrir 0-100% hleðslu: " << utkoma;
            cout << "kr" << endl;
            break;

        default:
            cout << "Röng aðgerð valin." << endl;
            return 1; // Loka forriti með villukóða 1
    }
    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    cout << "Press ENTER to continue...";
    cin.get();
    return 0;
}

// Definitions
double eydsla(double x, double y) {
    return x / y * 100;     //Kwh / length * 100
}

double kostnadur(double x, double y) {
    return x * y;           //Kwh * kostnaðurPerKwh
}