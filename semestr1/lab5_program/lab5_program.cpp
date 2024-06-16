#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
using namespace std;

int one()// не работает
{
	int a, b, n;
	cout << "Введите диапозон [a;b]" << endl << "a=";
	cin >> a;
	cout << "b=";
	cin >> b;
	cout << "простые числа в промежутке [" << a << ":" << b << "]= ";
	while (a<=b)
	{
		for (n = 2; a % n == 0; n++)
			if (n = a)
			{
				cout << n << ", ";
				
			}
		n = 2;
				
		a += 1;
	}
	return 0;
}
int two()//не работает
{
	int a, b, c,n=2;
	cout << "a=";
	cin >> a;
	cout << "b=";
	cin >> b;
	cout << "c=";
	cin >> c;
	while ((a % n == 0) && (b % n == 0) && (c % n == 0))
		n += 1;
		cout << "наименьшее общее кратное =" << n;
	return 0;
}

int three()// работает
{
	double a,s,S;
	cout << "a=";
	cin >> a;
	s = (a * a * sqrt(3)) / 4;
	S = s * 6;
	cout << "площадь шестиугольника=" << S;
	return 0;
}

int four()//работает, но некоторые дроби не сокрощает
{
	double n, a, b, c, d, f, e;
	cout << "1=поделить дроби\n2=умножить дроби\n3=сложить дроби\nдействие=";
	cin >> n;
	cout << "a/b and c/d" << endl;
	cout << "a=";
	cin >> a;
	cout << "b=";
	cin >> b;
	cout << "c=";
	cin >> c;
	cout << "d=";
	cin >> d;
	if (n == 1)
	{
		f = (a * d);
		e = (b * c);
		cout << "(a/b) / (c/d)=" << f << "/" << e;
		return 0;
	}
	if (n == 2)
	{
		f = (a * c);
		e = (b * d);
		cout << "(a/b) * (c/d)=" << f << "/" << e;
		return 0;
	}
	if (n == 3)
	{
		f = a * d + c * b;
		e = b * d;
		cout << "(a/b) + (c/d)=" << f << "/" << e;
		return 0;
	}
	else
		cout << "error";
	return 0;
}

int five()// работает
{
	double n, nf=0, mf=1,i=1;
	int m;
	cout << "m=";
	cin >> m;
	cout << "n=";
	cin >> n;
	for (m; m <= n; m++)
	{
		if (m % 2 == 0)
		{
			for (i; i <= m; i++)
			{
				mf = mf * i;
				//cout << "mf=" << mf << endl;
			}
			//cout << "чётность=" << m << endl;
			//cout << "факториал=" << mf << endl;
			nf += mf;
		}
		mf = 1;
		i = 1;
	}
	cout << "ответ=" << nf<<endl;
	return 0;
}
int six()//работает
{
	int n, max=0, min=99999999, a,min1=0,e=0,b=0,v;
	cout << "количество чисел=";
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cout << "введите число = ";
		cin >> a;
		v = a;
		while (a >= 10)
		{
			b += a % 10;
			a /= 10;
		} 
		b += a % 10;
		a /= 10;
		if (b > max)
		{
			max = b;
			e = v;
		}
		if (b < min)
		{
			min = b;
			min1 = v;
		}
		b = 0;
	}
	cout << "число с наибольшей суммой цифр=" << e << endl;
	cout << "число с наименьшей суммой цифр=" << min1 << endl;
	return 0;
}
int seven()//работает
{
	double a, b, c=0, d=0,q,w;
	cout << "введите 1е число=";
	cin >> a;
	cout << "введите 2е число=";
	cin >> b;
	q = a;
	w = b;
	if (a < 0)
	{
		a *= -1;
	}
	if (b < 0)
	{
		b *= -1;
	}
	do
	{
		c += 1;
		a /= 10;
	} while (a >= 10);
	do
	{
		d += 1;
		b /= 10;
	} while (b >= 10);
	if (c > d)
	{
		cout << "число в котором больше цифр=" << q;
		return 0;
	}
	else
		cout << "число в котором больше цифр=" << w;
	return 0;
}
int eight()//работает
{
	double n, S;
	do
	{
		cout << "Выберете действие:\nВычислить площадь круга-1\nВычислить площадь прямоугольника-2\nВычислить площадь прямоугольного триугольника-3\nдля выхода нажмите 0" << endl;
		cin >> n;
		if (n == 1)
		{
			double r;
			cout << "Введите радиус r=";
			cin >> r;
			S = r * r * M_PI;
			cout << "площадь круга=" << S << endl;
		}
		if (n == 2)
		{
			double a, b;
			cout << "введите длинну a=";
			cin >> a;
			cout << "введите ширину b=";
			cin >> b;
			S = a * b;
			cout << "площадь прямоугольника= " << S << endl;
		}
		if (n == 3)
		{
			double f, r;
			cout << "введите катет a=";
			cin >> f;
			cout << "введите катет b=";
			cin >> r;
			S = f * r / 2;
			cout << "площадь прямоугольного триугольника= " << S << endl;
		}
	} while (n != 0);
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
		case 7: {seven(); }break;
		case 8: {eight(); }break;
		//case 9: {nine(); }break;
		//case 10: {ten(); }break;
		//case 11: {eleven(); }break;
			//case 12: {twelve(); }break;
		}
		cin.get();
	} while (x != 0);
	return 0;
}