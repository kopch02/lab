#include <iostream>
#include <cmath>
using namespace std;

int one()// 1 из общего
{
	int a, n,b,m,c;
	cout << "n=";
	cin >> n;
	a = 0;
	c = 0;
	m = 0;
	while (n != 0)
	{
		a *= 10;
		a =a+ (n % 2);
		n = n / 2;
	
	}
	
	while (a != 0)
	{
		b = a % 10;
		m = m + (b * pow(2, c));
		c += 1;
		a = a / 10;
	}
	
	cout << "m=" << m;
	return 0;
}


int two()// 2 из общего
{
	int n, div=2;
	cout << "n=";
	cin >> n;
	cout << n << "=1";
	while (n > 1)
	{
		while (n % div == 0)
		{
			cout << "*" << div;
			n /= div;
		}
		div += 1;
	}
	return 0;
}

int three()// 3 из общего
{
	setlocale(0, "Russian");
	int n,sum=0,f=0,m=0,b=0,d;
	//sum-сумма
	//f- первая цифра
	//m- число в обратном порядке
	//b- количиство цифр в числе
	cout << "n=";
	cin >> n;
	d = n;
	while (n!=0)
	{
		
			m = (m * 10) + (n % 10);
			sum = sum + (n % 10);
			b += 1;
			n /= 10;
			
			
	}
	while (d > 10)
	{
		d /= 10;
		f = d;
	}
	cout << "сумма чисел = " << sum << endl;
	cout << "первая цифра = " << f << endl;
	cout << "число в обратном порядке = " << m << endl;
	cout << "количество цифр в числе = " << b << endl;
	return 0;
}

int four()// 4 из общего
{
	setlocale(0, "Russian");
	int n,a=0,b=1,c=0;
	cout << "n=";
	cin >> n;
	n = n*2-1;
	cout << "сумма ничётных чисел = 0";
	while (b != n)
	{
		c = c + b;
		a = c;
		cout << "+" << b;
		b =b + 2;
	} 
	c = c + b;
	a = c;
	cout << "+" << b;
	b = b + 2;
	cout << "\nn^2 как сумма нечётных чисел = " << a;
	return 0;
}
int five()//1е из вариантов(7й)
{
	setlocale(0, "Russian");
	int n, a=0;
	cout << "n=";
	cin >> n;
	while (n != 0)
	{
		a += 1;
		n /= 10;
	}
	cout << "количиство цифр в числе n = " << a;
	return 0;
}
int six()//задание 3 из варианта(7й)
{
	int a=1;
	double n;
	do
	{
		n = (3 + a) / pow((a-4),2);
		cout << "n при a =" << a << " = " << n << endl;
		a += 3;
	} while (a != 22);
	return 0;
}
int seven()// задание 4 из варианта(7й)
{
	int a, b, a1=1, b1=1, i=2;
	// i-количество шагов
	// a,b -текущие слагаемые
	// a1,b1 -предидущие слагаемые
	while (i!=16)
	{
		a = (3 * b1) + (2 * a1);
		b = (2 * a1) + b1;
		cout << "при i = " << i;
		cout << "	a  =   " << a;
		cout << "		b=" << b << endl;
		i += 1;
		a1 = a;
		b1 = b;
	}
	return 0;
}
int eight()// задание 10 из общего
{
	int n, a=0;
	cout << "n=";
	cin >> n;
	while (n != 0)
	{
		a = a * 10 + n % 10;
		n /= 10;
	}
	cout << "перевёрнутое число n=" << a;
	return 0;
}
int nine()//задание 13 из общего
{
	int n = 0, t = 0, d = 1;
	cout << "n=";
	cin >> n;
	while (n)
	{
		t += (n % 2) * d;
		n = n / 2;
		d = d * 10; 
	}
	cout <<"n  двоичном коде = "<<t;
	return 0;
}

int ten()//задание 15 из общего
{
	int n;
	double d = 0, a = 0, f = 0;
	cout << "n=";
	cin >> n;
	while (a != n)
	{
		a += 1;
		f = f + sin(a);
		d = d + 1 / f;
	}
	cout << "S=" << d;
	return 0;
}
int eleven()// 16е из общего 
{
	double sum, s, s1, x = 1;
	int n,i=2;
	//sum- сумма
	//s- текущее слогаемое 
	//s1- предидущее слогаемое
	cout << "n=";
	cin >> n;
	if (n <= 0)
	{
		cout << "ошибка n<=0";
		return 0;
	}
	else
	{
		s1 = sin(x);
		sum = s1;
		cout << "s[1]=" << s1 << endl;
		for (i; i <= n; i++)
		{
			s = sin(s1);
			sum += s;
			s1 = s;
			cout << "s[" << i << "]=" << s << endl;
		}
		cout << "S=" << sum;
	}
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
		case 9: {nine(); }break;
		case 10: {ten(); }break;
		case 11: {eleven(); }break;
		//case 12: {twelve(); }break;
		}
		cin.get();
	} while (x != 0);
	return 0;
}

