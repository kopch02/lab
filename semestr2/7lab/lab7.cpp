#include <iostream>
#include <fstream>

using namespace std;
void newmatr(int**& mas, int n)
{
    mas = new int *[n];
    for (int i = 0; i < n; i++)
        mas[i] = new int[n];
}
void readfile(int** mas, int n)
{
    ifstream file;
    file.open("file.txt");
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            file >> mas[i][j];
        }
    }
    file.close();
    
}
void outmatr(int **mas, int n, int *d, int* ver,int& k,int end)
{
    ofstream res;
    res.open("res.txt");

    cout<<"matr:"<<endl;
    res << "matr:" << endl;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%5d ", mas[i][j]);
            res << mas[i][j]<<" ";
        }
        cout << endl;
        res << endl;
    }
    cout<<endl<<"The shortest distance to the vertices:"<<endl;
    res << endl << "The shortest distance to the vertices:" << endl;

    for(int i=0;i<n;i++)
    {
        cout<<"Path out of 1 in "<<i+1<<" = "<<d[i]<<endl;
        res << "Path out of 1 in " << i + 1 << " = " << d[i] << endl;
    }
    cout<<endl;
    res << endl;
    res << endl<< "shortest way"<< endl;
    cout << endl<< "shortest way"<<endl;
    for (int i = k - 1; i >= 0; i--)
    {
        cout << ver[i];
        res << ver[i];
    }
    cout << endl;
    res.close();
}
void dextra(int n,int temp,int* v,int* d,int** mas,int* ver,int& k,int end)
{
    for (int i = 0; i < n; i++)
    {
        d[i] = 10000;
        v[i] = 1;
    }
    d[0] = 0;
    int minindex;
    int min;
    do
    {
        minindex = 10000;
        min = 10000;
        for (int i = 0; i < n; i++)
        {
            if ((v[i] == 1) && (d[i] < min))
            {
                min = d[i];
                minindex = i;
            }
        }
        if (minindex != 10000)
        {
            for (int i = 0; i < n; i++)
            {
                if (mas[minindex][i] > 0)
                {
                    temp = min + mas[minindex][i];
                    if (temp < d[i])
                    {
                        d[i] = temp;
                    }
                }
            }
            v[minindex] = 0;
        }
    } while (minindex < 10000);
    // поиск пути
    cout<<"Finite top--";
    cin>>end;
    end--;
    ver[0] = end + 1;  
    int weight = d[end];

    while (end != 0) 
    {
        for (int i = 0; i < n; i++) 
            if (mas[i][end] != 0)      
            {
                int temp = weight - mas[i][end]; 
                if (temp == d[i])             
                {                              
                    weight = temp;            
                    end = i;                   
                    ver[k] = i + 1;           
                    k++;
                }
            }
    }
    
}
int main()
{
    int n=6;
    int temp;
    int end;
    int** mas;
    int* d=new int [n];
    int *v = new int[n];
    int ver[6];
    int k = 1;  
    newmatr(mas,n);
    readfile(mas,n);
    dextra(n,temp,v,d,mas,ver,k,end);
    outmatr(mas,n,d,ver,k,end);
    return 0;
}