#include <fstream>
#include <iostream>
#include <time.h>
using namespace std;

double* enterMassiv(int); //создание массива
int open(); //открыл файл и посчитал количество элементов 
void zapis(int, double*);//запись данных из файла в массив
void Add(int& n, double*& a,double y,int k)
{
	
    if (k<1 || k>n + 2)
        cout << "error" << endl;
    else {
        double* t = enterMassiv(n + 1);
        n++;
        for (int i = 0; i < k - 1; i++)
        {
            t[i] = a[i];
        }
        t[k - 1] = y;
        for (int i = k; i < n; i++)
        {
            t[i] = a[i - 1];
        }
        delete[] a;
        a = t;
    }

}
void out(int,double*); //вывод массива
bool delet_k_number(double*& a, int &n, int k)
{
    if (k > n || k < 1)
    {
        cout << "Error!" << endl;
        return false;
    }

    for (int ix = k - 1; ix < n - 1; ix++)
    {
        a[ix] = a[ix + 1];
    }
    n--;
    return true;
}
int main()
{	
	
	int n,k;
	double x,y,t;
	n=open();
	double *a = enterMassiv(n);
	zapis(n,a);
	out(n,a);
	/*cout<<"enter the number that appears at the beginning of the array-->";
	cin>>y;
	k=1;
	Add(n, a, y,k);
	out(n,a);*/
	cout<<"on which position to put the number?-->";
	cin>>k;
	cout<<"what number?-->";
	cin>>y;
	Add(n, a, y,k);
	out(n,a);
	srand (time(0));
	y=rand();
	cout<<"to which position to add a random number?-->";
	cin>>k;
	Add(n, a, y,k);
	out(n,a);
	/*cout<<"enter the number that will be in last place-->";
	cin>>y;
	k=n+1;
	Add(n, a, y,k);
	out(n,a);*/
	cout<<"which number do you want to delete?-->";
	cin>>k;
	delet_k_number(a,n,k);
	out(n,a);
	cout<<"after which element to add a new value?-->";
	cin>>x;
	bool h=0,v=0;
	for(int i=0;i<n;i++)
	{
		if (a[i]==x)
		{
			cout<<"What element add?-->";
			cin>>y;
			k=i+2;
			Add(n, a, y,k);
			h=1;
			break;
		}
	}
	if(h==0){
	cout<<"no such element"<<endl;
	}
	out(n,a);
	cout<<"what elements to remove?-->";
	cin>>t;
	for(int i=0;i<n;i++)
	{
		if (a[i]==t)
		{
			k=i+1;
			delet_k_number(a,n,k);
			//h=1;
			i-=1;
			v=1;
		}
	}
	if(v==0){
		cout<<"no such elements"<<endl;
	}
	
	out(n,a);
	return 0;
}
int open(){
	int g = 0;
	double s;
	ifstream massiv;
	massiv.open("file.txt");
	if (!massiv)
	{
		cout << "error, file not found" << endl;
		return 0;
	}
	while (massiv >> s)
		g++;
	massiv.close();
	return g;
}
double* enterMassiv(int n){
	double* a = new double[n];
	return a;
}
void zapis(int n, double*a){
	ifstream massiv;
	massiv.open("file.txt");
	if (!massiv)
	{
		cout << "error, file not found" << endl;
		return;
	}
	for (int i = 0; i < n; i++)
	{
		massiv >> a[i];
	}
	massiv.close();
}
void out(int n,double*a){
	for(int i=0;i<n;i++)
	{
		cout<<"["<<i<<"]"<<"="<<a[i]<<endl;
	}
}