
#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <time.h>

using namespace std;

int random(int range_min, int range_max) {
    return rand() % (range_max - range_min + 1) + range_min;
}
int main()
{
    srand(static_cast<unsigned int>(time(NULL)));
    setlocale(0, "Russian");
    int n,minr,maxr,max,min,a,nummax=0,nummin=0,proizvedenie=1;
    cout << "Введите размерность массива=";
    cin >> n;
    cout << "Введите область для рандомных чисел" << endl << "от ";
    cin >> minr;
    cout << "до ";
    cin >> maxr;
    int* massiv = new int[n];
    // заполняю массив рандомными значениями
    for (int i = 0; i < n; i++)
    {
        massiv[i] = random(minr, maxr);
    }
    
    // вывод значений массива
    cout << "\nВаш массив: " << endl;
    for (int i = 0; i < n; ++i) {
        cout << "[" << i << "]=" << massiv[i] << " " << endl;
    }
    
    max = massiv[0];
    min = massiv[0];
    for (int i = 0; i < n; i++)
    {
        if (massiv[i] > max)
        {
            max = massiv[i];
            nummax = i;
        }
        if (massiv[i] < min)
        {
            min = massiv[i];
            nummin = i;
        }
    }
    for (int i = 0; i < n; i++)
    {
        if (massiv[i] == 0)
        {
            i += 1;
            while (massiv[i] != 0)
            {
                proizvedenie *= massiv[i];
                i += 1;
            }
            break;
        }
    }
    cout << "номер максимального элемента массива = " << nummax << endl;
    cout << "номер минимальногл элемента массива = " << nummin << endl;
    cout << "максимальный элемент массива = " << max << endl;
    cout << "минимальный элемент массива = " << min << endl;
    if (proizvedenie == 1)
    {
        cout << "нет двух нулевых элементов"<<endl;
    }
    else
    cout << "произведение элементов массива, расположенных между первым и вторым нулевыми элементами = " << proizvedenie << endl;
    massiv[nummax] = min;
    massiv[nummin] = max;
    // вывод значений массива
    cout << "максимальный элемент массива (поменяный местами) = " << massiv[nummax] << endl;
    cout << "минимальный элемент массива (поменяный местами) = " << massiv[nummin] << endl;
    a = nummax;
    nummax = nummin;
    nummin = a;
    cout << "номер максимального элемента массива (поменяного местами) =" << nummax<<endl;
    cout << "номер минимального элемента массива (поменяного местами) =" << nummin<<endl;
    cout << "\nВаш массив: "<<endl;
    for (int i = 0; i < n; ++i) {
        cout << "[" << i << "]=" << massiv[i] << " " << endl;
    }
    return 0;
}
