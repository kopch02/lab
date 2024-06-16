#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    setlocale(LC_ALL, "Russian");
    int x;
    cout << "Номер задания=";
    cin >> x;
    switch (x)
    {
    case (1):
    {

        double x;
        cout << "Введите x=";
        cin >> x;
        double S, b = ((x - 1) / (x + 1)), eps = 1e-7;
        S = b;
        for (int i = 1; fabs(b / (i * 2. + 1)) > eps; i++)
        {
            b *= ((x - 1) * (x - 1)) / ((x + 1) * (x + 1));
            S += b / (i * 2. + 1);
        }
        cout << "Cумма числового ряда S=" << S * 2 << endl;
    }
    break;
    case(2):
    {
        double x;
        cout << "Введите x=";
        cin >> x;
        double S, b = (x - 1), eps = 1e-7;
        S = b;
        for (int i = 2; fabs(b / i) > eps; i++)
        {
            b *= -(x - 1);
            S += b / i;
        }
        cout << "Сумма числового ряда S=" << S << endl;
    }
    break;
    case(3):
    {
        double x;
        cout << "Введите x=";
        cin >> x;
        double S, b = (x - 1) / x, eps = 1e-7;
        S = b;
        for (int i = 2; fabs(b / i) > eps; i++)
        {
            b *= (x - 1) / x;
            S += b / i;
        }
        cout << "Сумма числового ряда S=" << S << endl;
    }
    }
}