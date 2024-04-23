#include <iostream>

using namespace std;

//Function declaration

double samlagning(double x, double y);
double fradrattur(double x, double y);
double margfalda(double x, double y);
double deila(double x, double y);


int main() {
    double num1, num2;
    char adgerd;
    double utkoma;

    cout << "Skrifaðu fyrstu töluna: ";
    cin >> num1;
    cout << "Skrifaðu seinni töluna: ";
    cin >> num2;
    cout << "Veldu aðgerð (+, -, *, /)";
    cin >> adgerd;

    switch (adgerd) {
        case '+':
            utkoma = samlagning(num1, num2);
            break;
        case '-':
            utkoma = fradrattur(num1, num2);
            break;
        case '*':
            utkoma = margfalda(num1, num2);
            break;
        case '/':
            if (num2 != 0) {
                utkoma = deila(num1, num2);
            } else {
                cout << "Error: Ekki hægt að deila með 0." << endl;
                return 1; // Loka forriti með villukóða 1
            }
            break;
        default:
            cout << "Röng aðgerð valin." << endl;
            return 1; // Loka forriti með villukóða 1
    }

    cout << "Útkoma: " << utkoma << endl;
    return 0; // Success
}

// Function definitions
double samlagning(double x, double y) {
    return x + y;
}

double fradrattur(double x, double y) {
    return x - y;
}

double margfalda(double x, double y) {
    return x * y;
}

double deila(double x, double y) {
    return x / y;
}