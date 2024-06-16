#define _USE_MATH_DEFINES //задание 1
#include <cmath>
#include<iostream>
using namespace std;

int q()
{
    double y, x1, x2;
    cout << "x1=";
    cin >> x1;
    cout << "x2=";
    cin >> x2;
    y = ((pow(M_E, -x1)) + (pow(M_E, -x2))) / 2;
    cout << "y=" << y;
    system("pause");
    return 0;
}

int w()
{
    float a, b, c, p, s;
    cout << "a=";
    cin >> a;
    cout << "b=";
    cin >> b;
    cout << "c=";
    cin >> c;
    p = (a + b + c) / 2;
    s = sqrt(p * (p - a) * (p - b) * (p - c));
    cout << "p=" << p;
    cout << " s=" << s;
    return 0;
}


int e()
{
    double a, b, c, p, s, A, B, C;
    cout << "a=";
    cin >> a;
    cout << "b=";
    cin >> b;
    cout << "c=";
    cin >> c;
    p = (a + b + c) / 2;
    s = sqrt(p * (p - a) * (p - b) * (p - c));
    A = 2 * s / a;
    B = 2 * s / b;
    C = 2 * s / c;
    cout << "A=" << A;
    cout << " B=" << B;
    cout << " C=" << C;
    system("pause");
    return 0;
}

int r()
{

    double s, R, r, l, v, h;
    cout << "R=";
    cin >> R;
    cout << "r=";
    cin >> r;
    cout << "l=";
    cin >> l;
    cout << "h=";
    cin >> h;
    s = M_PI * (R + r) * l + M_PI * pow(R, 2) + M_PI * pow(r, 2);
    v = (1 / 3) * pow(R, 2) + pow(r, 2) + R * r * h * M_PI;
    cout << "s=" << s;
    cout << " v=" << v;
    return (0);
}
int t()
{
    double a, f, w, y, x;
    cout << "a=";
    cin >> a;
    cout << "f=";
    cin >> f;
    cout << "w=";
    cin >> w;
    x = M_PI_2 - f;
    y = a * pow(M_E, -a * w * x) * sin(w * x);
    cout << "y=" << y;
    return (0);
}

int y()
{
    int x, b;
    cout << "x(>=100)=";
    cin >> x;
    x = x / 10;
    x = x / 10;
    b = x % 10;
    cout << "b=" << b;
    return (0);

}
int u()
{
    double a;
    int b;
    cout << "a(0.xxx)=";
    cin >> a;
    b = a * 10.0;
    b = b % 10;
    cout << "b=" << b;
    return (0);

}

int i()
{
    double a, b, c, d;
    cout << "c=";
    cin >> c;
    cout << "d=";
    cin >> d;
    a = c - d;
    b =c * d* 3;
    cout << "a=" << a;
    cout << "\nb=" << b;
    return (0);

}
int main()
{
    q();
    w();
    e();
    r();
    t();
    y();
    u();
    i();
    return 0;
}