#include <iostream>
#include <string>
#include <fstream>
#include <time.h>
#include <cmath>
#include <cstdlib>

using namespace std;

int random(int range_min, int range_max) {
	return rand() % (range_max - range_min + 1) + range_min;
	srand(static_cast<unsigned int>(time(NULL)));
}
void massivC(int n)
{
	//заполняю массив С рандомными числами
	int* massiv = new int[10000];
	for (unsigned int i = 0; i < n; i++)
	{
		massiv[i] = random(0, 10000);
	}
	ofstream massivC;
	massivC.open("C:/Users/iskan/Desktop/сестровая яп/massivC.txt"); //добавить после путя ofstream::app чтобы  не стриала страрые данные
	for (int i = 0; i < n; i++)
	{
		massivC << massiv[i] << " ";
	}
	massivC.close();
}
void massivB(int n)
{
	int a=n;
	int* massiv = new int[10000];
	for (int i = 0; i < n; i++)
	{
		massiv[i] = a;
		a -= 1;
	}
	ofstream massivB;
	massivB.open("C:/Users/iskan/Desktop/сестровая яп/massivB.txt"); //добавить после путя ofstream::app чтобы  не стриала страрые данные
	for (int i = 0; i < n; i++)
	{
		massivB << massiv[i] << " ";
	}
	massivB.close();
}
void massivA(int n)
{
	int a = 1;
	int* massiv = new int[10000];
	for (int i = 0; i < n; i++)
	{
		massiv[i] = a;
		a += 1;
	}
	for (int i = 1;i < n; i += 3)
	{
		massiv[i] = random(1, 10000);
	}
	ofstream massivA;
	massivA.open("C:/Users/iskan/Desktop/сестровая яп/massivA.txt"); //добавить после путя ofstream::app чтобы  не стриала страрые данные
	for (int i = 0; i < n; i++)
	{
		massivA << massiv[i]<<" ";
	}
	massivA.close();
}
void bubble(int* num, int size)
{
	// Для всех элементов
	for (int i = 0; i < size - 1; i++)
	{
		for (int j = (size - 1); j > i; j--) // для всех элементов после i-ого
		{
			if (num[j - 1] > num[j]) // если текущий элемент меньше предыдущего
			{
				int temp = num[j - 1]; // меняем их местами
				num[j - 1] = num[j];
				num[j] = temp;
			}
		}
	}
}
void bubblemassivA(int n)
{
	//для массива A
	ifstream massiv1;
	massiv1.open("C:/Users/iskan/Desktop/сестровая яп/massivA.txt");
	int massiv[10000];
	for (int i = 0; i < n; i++)
	{
		massiv1.eof();
		massiv1 >> massiv[i];
	}
	bubble(massiv, n);  // сортировка
	ofstream massivA_bubble;
	massivA_bubble.open("C:/Users/iskan/Desktop/сестровая яп/massivA_bubble.txt");
	for (int i = 0; i < n; i++)
	{
		massivA_bubble << massiv[i] << " ";
	}
	massivA_bubble.close();
}
void bubblemassivB(int n)
{
	// для массива B
	ifstream massiv2;
	massiv2.open("C:/Users/iskan/Desktop/сестровая яп/massivB.txt");
	int massivB[10000];
	for (int i = 0; i < n; i++)
	{
		massiv2.eof();
		massiv2 >> massivB[i];
	}
	bubble(massivB, n);  // сортировка
	ofstream massivB_bubble;
	massivB_bubble.open("C:/Users/iskan/Desktop/сестровая яп/massivB_bubble.txt");
	for (int i = 0; i < n; i++)
	{
		massivB_bubble << massivB[i] << " ";
	}
	massivB_bubble.close();
}
void bubblemassivC(int n)
{
	// для массива C
	ifstream massiv3;
	massiv3.open("C:/Users/iskan/Desktop/сестровая яп/massivC.txt");
	int massivC[10000];
	for (int i = 0; i < n; i++)
	{
		massiv3.eof();
		massiv3 >> massivC[i];
	}
	bubble(massivC, n);  // сортировка
	ofstream massivC_bubble;
	massivC_bubble.open("C:/Users/iskan/Desktop/сестровая яп/massivC_bubble.txt");
	for (int i = 0; i < n; i++)
	{
		massivC_bubble << massivC[i] << " ";
	}
	massivC_bubble.close();
}
void shell(int n, int mass[])
{
	int i, j, step;
	int tmp;
	for (step = n / 2; step > 0; step /= 2)
		for (i = step; i < n; i++)
		{
			tmp = mass[i];
			for (j = i; j >= step; j -= step)
			{
				if (tmp < mass[j - step])
					mass[j] = mass[j - step];
				else
					break;
			}
			mass[j] = tmp;
		}
}
void shellmassivA(int n)
{
	ifstream massiv1;
	massiv1.open("C:/Users/iskan/Desktop/сестровая яп/massivA.txt");
	int massiv[10000];
	for (int i = 0; i < n; i++)
	{
		massiv1.eof();
		massiv1 >> massiv[i];
	}
	shell(n, massiv);
	ofstream massivA_shell;
	massivA_shell.open("C:/Users/iskan/Desktop/сестровая яп/massivA_shell.txt");
	for (int i = 0; i < n; i++)
	{
		massivA_shell << massiv[i] << " ";
	}
	massivA_shell.close();
}
void shellmassivB(int n)
{
	ifstream massiv2;
	massiv2.open("C:/Users/iskan/Desktop/сестровая яп/massivB.txt");
	int massiv[10000];
	for (int i = 0; i < n; i++)
	{
		massiv2.eof();
		massiv2 >> massiv[i];
	}
	shell(n, massiv);
	ofstream massivB_shell;
	massivB_shell.open("C:/Users/iskan/Desktop/сестровая яп/massivB_shell.txt");
	for (int i = 0; i < n; i++)
	{
		massivB_shell << massiv[i] << " ";
	}
	massivB_shell.close();
}
void shellmassivC(int n)
{
	ifstream massiv3;
	massiv3.open("C:/Users/iskan/Desktop/сестровая яп/massivC.txt");
	int massiv[10000];
	for (int i = 0; i < n; i++)
	{
		massiv3.eof();
		massiv3 >> massiv[i];
	}
	shell(n, massiv);
	ofstream massivC_shell;
	massivC_shell.open("C:/Users/iskan/Desktop/сестровая яп/massivC_shell.txt");
	for (int i = 0; i < n; i++)
	{
		massivC_shell << massiv[i] << " ";
	}
	massivC_shell.close();
}

int main()
{
	setlocale(LC_ALL, "ru");
	int n,num,sort;
	cout << "веберите массив:" << endl << "1)Почти отсортированный массив" << endl << "2)Массив в обратном порядке" << endl << "3)массив с рандомными числами" << endl<<"=>";
	cin >> num;
	cout << "выберите метод сортировки" << endl << "1)пузырьком" << endl << "2)шелла" << endl<<"=>";
	cin >> sort;
	cout << "введите размерность массива = ";
	cin >> n;
	if (num == 1)
	{
		massivA(n);//заполняю почти упорядочный массив
		if (sort == 1)
		{
			bubblemassivA(n);//сортировка массива А пузырьком
		}
		if (sort == 2)
		{
			shellmassivA(n);//сортировка массива А методом шелла
		}
		
	}
	if (num == 2)
	{
		massivB(n);//заполняю массив в обратном порядке
		if (sort == 1)
		{
			bubblemassivB(n);//сортировка массива B пузырьком
		}
		if (sort == 2)
		{
			shellmassivB(n);//сортировка массива B методом шелла
		}
		
	}
	if (num == 3)
	{
		massivC(n);//заполняю массив рандомными числами
		if (sort == 1)
		{
			bubblemassivC(n);//сортировка массива C пузырьком
		}
		if (sort == 2)
		{
			shellmassivC(n);//сортировка массива C методом шелла
		}
		
	}
	/*
	massivC(n);//заполняю массив С рандомными
	massivB(n);//заполняю B в обратном порядке
	massivA(n);//заполняю почти упорядочный массив
	bubblemassivA(n);//сортировка массива А пузырьком 
	bubblemassivB(n);//сортировка массива B пузырьком
	bubblemassivC(n);//сортировка массива С пузырьком
	shellmassivA(n);//сортировка массива А методом шелла
	shellmassivB(n);//сортировка массива B методом шелла
	shellmassivC(n);//сортировка массива C методом шелла
	cout << "были созданны 3 разных массива и отсортированны метом шелла и пузырьком"<<endl;
	*/
	return 0;
}
