
#include <iostream> //задание 1
#include <cmath>
using namespace std;

int one()
{
    int h, m, k;
    cout << "k=";
    cin >> k;
    h = k / 3600 * M_PI;
    k %= 3600;
    m = k / 60;
    cout << "hh.mm=" << h << "." << m;
    return(0);
    
}
int two()
{
    setlocale(LC_ALL, "Russian");
    double x, y, z, f;
    cout << "x(-2<=x<=4)=";
    cin >> x;
    if (x < -2) // проверка подходит ли х условию
    {
        cout << "x не подходит";
        return(0);
    }
    else if (x > 4)
    {
        cout << "x не подходит";
        return(0);
    }
    else if (x > 0) // выбираю f
        f = x;
    else if (x < -1)
        f = x * x;
    else
        f = 0;
    z = 7 * pow(x, 3) + 5 * x * x + x;
    y = f + 0.75 * z;
    cout << "y=" << y;
    return(0);    
}

int three()
{
    setlocale(LC_ALL, "Russian");
    double x,x1, x2, D,a,b,c;
    bool t;
    cout << "a=";
    cin >> a;
    cout << "b=";
    cin >> b;
    cout << "c=";
    cin >>c;
    D = b * b - 4 * a * c;
        if (D < 0)
        {
            t = false;
            cout << "нет вещественных корней";
            return 0;
        }
        else if (D == 0)
        {
            x = -b / 2 * a;
            t = true;
            cout << "x=" << x;
                return 0;
        }
        else
            x1 = (-b + sqrt(D)) / (2 * a);
            x2 = (-b - sqrt(D)) / (2 * a);
            t = true;
            cout << "\nx1=" << x1;
            cout << "\nx2=" << x2;
            return 0;

}

int four()
{
    setlocale(LC_ALL, "Russian");
    int x1A, x2B, x3C, y1A, y2B, y3C, AB, BC, AC;
    cout << "x1A=";
    cin >> x1A;
    cout << "y1A=";
    cin >> y1A;
    cout << "x2B=";
    cin >> x2B;
    cout << "y2B=";
    cin >> y2B;
    cout << "x3C=";
    cin >> x3C;
    cout << "y3C=";
    cin >> y3C;
    AB = sqrt(pow(x2B - x1A, 2) + pow(y2B - y1A, 2));
    AC = sqrt(pow(x3C - x1A, 2) + pow(y3C - y1A, 2));
    BC = sqrt(pow(x3C - x2B, 2) + pow(y3C - y2B, 2));
    if ((AB + AC) < BC)
    {
        cout << "такого треуголька не существует";
        return 0;
    }
    else if ((AB + BC) < AC)
    {
        cout << "такого треуголька не существует";
        return 0;
    }
    else if ((AC + BC) < AB)
    {
        cout << "такого треуголька не существует";
        return 0;
    }
    else if ((AB == AC) && (AB == BC))
        cout << "треугольник равносторонний";
    else if ((AB == BC) || (AB == AC) || (BC == AC))
        cout << "треугольник равнобедренный";
    else
        cout << "треугольник разносторонний";

    return 0;
}

int five()
{
    double x, y, z, a, b, T,min, max;
    cout << "a=";
    cin >> a;
    cout << "b=";
    cin >> b;
    x = a * a - 1;
    y = b * b - a * a;
    z = sqrt(abs(a + b));
    if (x > y)
        max = x;
    else
        max = y;
    if ((x < y) && (x < z))
        min = x;
    else if ((y < x) && (y < z))
        min = y;
    else
        min = z;
    T = (abs(x) + min) / (abs(y) + max);
    cout << "T=" << T;
    return 0;
}

int six()
{
    double x, y,x1,y1;
    cout << "x=";
    cin >> x;
    cout << "y=";
    cin >> y;
    if (x == y)
    {
        cout << "ошибка: x=y";
        return 0;
    }
    else if (x < y)
    {
        x1 = (x + y) / 2;
        y1 = x * y * 2;
    }
    else
    {
        y1 = (x + y) / 2;
        x1 = x * y * 2;
    }
    cout << "x=" << x1;
    cout << "y=" << y1;
    return 0;
}
/*#include <iostream>//задание 7 доделать
using namespace std;
int seven()
{
    double x1, x2, x3, y1, y2, y3,a,b,c;
    cout << "x1=";
    cin >> x1;
    cout << "y1=";
    cin >> y1;
    cout << "x2=";
    cin >> x2;
    cout << "y2=";
    cin >> y2;
    cout << "x3=";
    cin >> x3;
    cout << "y3=";
    cin >> y3;
    cout << "a=";
    cin >> a;
    cout << "b=";
    cin >> b;
    cout << "c=";
    cin >> c;
    return 0;
}*/

int eight()
{
    setlocale(LC_ALL, "Russian");
    int n, a, b;
    cout << "n=";
    cin >> n;
    b = n;
    a = 0;
    while (b != 0)
    {
        a = a * 10 + b % 10;
        b /= 10;
    }
    //cout << a ;
    if (a == n)
        cout << "\nданное число является палиндромом";
    else
        cout << "\nданное число не является палиндромом";
    return 0;
}

int nine()
{
    double a,f;
    cout << "a=";
    cin >> a;
    if (a <= 0)
    {
        f = 0;
        cout << "f=" << f;
        return 0;
    }
    else if (a > 0 && a <= 1)
    {
        f = a;
        cout << "f=" << f;
        return 0;
    }
    else
        f = pow(a, 3);
    cout << "f=" << f;
    return 0;
}

int ten()//задание 10(а)
{
    setlocale(0, "Russian");
    double a, b, c;
    cout << "a=";
    cin >> a;
    cout << "b=";
    cin >> b;
    cout << "c=";
    cin >> c;
    if ((a > 0) && (b > 0) && (c > 0))
        if ((a < b) && (a < c))
            if (b < c)
            {
                cout << "числа положительные и образуют возрастающую последовательность";
                cout << "a,b,c=" << a << "," << b << "," << c;
                return 0;
            }
            else
            {
                cout << "последовательность не возрастает";
                return 0;
            }

        else
        {
                cout << "последовательность не возрастает";
                    return 0;
        }
 else
 cout << "введено отрицательное число";
 return 0;
    
}

int eleven() //задание 10(б)
{
    setlocale(0, "Russian");
    double a, b, c;
    cout << "a=";
    cin >> a;
    cout << "b=";
    cin >> b;
    cout << "c=";
    cin >> c;
    if((a!=b)&&(a!=c)&&(b!=c))
        if ((c < a) && (c < b))
        {
            cout << "c наименьшее и = " << c;
            return 0;
        }
        else
        {
            cout << "c не наименьшее";
            return 0;
        }
    else
    {
        cout << "нкоторые числа равны";
    }
    return 0;
}


int twelve() //задание 10(в)
{
    setlocale(0, "Russian");
    double x, y, z;
    cout << "x=";
    cin >> x;
    cout << "y=";
    cin >> y;
    cout << "z=";
    cin >> z;
    if ((x < 0) && (y < 0) && (z < 0))
    {
        cout << "все числа отрицательны";
        return 0;
    }
    else if ((x >= 0) && (x <= 1))
    {
        cout << "x находится в промежутке [0;1]" << endl;
    }
     if ((y >= 0) && (y <= 1))
    {
        cout << "y находится в промежутке [0;1]" << endl;
    }
     if ((z >= 0) && (z <= 1))
    {
         cout << "z находится в промежутке [0;1]" << endl;
    }
    else
        cout << "есть положительное число и не одно из них не находится в промежутке [0;1] ";
    return 0;
}

int main() //меню
{
    setlocale(0, "Russian");
    int x;
    do
    {
        cout << "\nВведите номер задания: " << endl;
        cin >> x;
        switch (x)
        {
        case 1: {one(); }break;
        case 2: {two(); }break;
        case 3: {three(); }break;
        case 4: {four(); }break;
        case 5: {five(); }break;
        case 6: {six(); }break;
            //case 7: {seven(); }break;
        case 8: {eight(); }break;
        case 9: {nine(); }break;
        case 10: {ten(); }break;
        case 11: {eleven(); }break;
        case 12: {twelve(); }break;
        }
        cin.get();
    } while (x != 0);
    return 0;
}