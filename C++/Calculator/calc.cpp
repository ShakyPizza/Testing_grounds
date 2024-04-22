#include <iostream>


//Function declaration
double plus(double x, double y);
double minus(double x, double y);
double margfalda(double x, double y);
double deila(double x, double y);


int main() {
    double num1, num2;
    char adgerd;
    double utkoma;

    std::cout << "Skrifaðu fyrstu töluna: ";
    std::cin >> num1;
    std::cout << "Skrifaðu seinni töluna: ";
    std::cin >> num2;
    std::cout << "Veldu aðgerð (+, -, *, /)";
    std::cin >> adgerd;

    switch (adgerd) {
        case '+':
            utkoma = plus(num1, num2);
            break;
        case '-':
            utkoma = minus(num1, num2);
            break;
        case '*':
            utkoma = margfalda(num1, num2);
            break;
        case '/':
            if (num2 != 0) {
                utkoma = deila(num1, num2);
            } else {
                std::cout << "Error: Ekki hægt að deila með 0." << std::endl;
                return 1; // Loka forriti með villukóða 1
            }
            break;
        default:
            std::cout << "Röng aðgerð valin." << std::endl;
            return 1; // Loka forriti með villukóða 1
    }

    std::cout << "utkoma: " << utkoma << std::endl;
    return 0; // Success
}

// Function definitions
double plus(double x, double y) {
    return x + y;
}

double minus(double x, double y) {
    return x - y;
}

double margfalda(double x, double y) {
    return x * y;
}

double deila(double x, double y) {
    return x / y;
}