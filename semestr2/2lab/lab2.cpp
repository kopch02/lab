#include <iostream>
#include <iomanip>
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;


int get_number()
{
  float n;
  do
  {
    cout << "Enter number: ";
    cin >> n;
    if (n <= 0 || (n - (int)n))
      cout << " ---Error, try again" << endl;
  } while(n <= 0 || (n - (int)n));
  return n;
}
void newmatr(double**& M, int n, int m)
{
  M = new double*[n];
  for(int i = 0; i < n; i++)
    M[i] = new double [m];
}
void delmatr(double**& M, int n, int m)
{
  for(int i = 0; i < n; i++)
    delete [] M[i];
  delete [] M;
}
void out(double** M, int n, int m)
{
  
  for(int i = 0; i < n; i++)
    {
      for(int j = 0; j < m; j++)
        cout << setw(25) << M[i][j];
      cout << endl;
    }
    cout << endl;
}
void out_vektor(double* x, int n )
{
 
  for(int i = 0; i < n; i++)
    {
      cout << setw(5) << x[i];
      cout << endl;
    }
    cout << endl;
}
void reshuffle(double**& M, int n, int m, int k, double &opred)
{
  for (int i = k + 1; i < n; i++)
  {
    if (M[i][k] != 0)
    {
      double temp;
      for (int i1 = 0; i1 < m; i1++)
      {
        temp = M[k][i1];
        M[k][i1] = M[i][i1];
        M[i][i1] = temp;
      }
      opred *= -1;
      break;
    }
  }
}
bool minor(double**& M, int n, int m, double &opred)
{
  for (int  i = 0; i < n ; i++)
  {
    if (M[i][i] == 0) reshuffle(M, n, m, i, opred);
    if (M[i][i] == 0) return false;
    for (int i1 = i + 1; i1 < n; i1++)
      for (int i2 = i + 1; i2 < m; i2++)
        M[i1][i2] = M[i][i] * M[i1][i2] - M[i][i2] * M[i1][i];
    for (int j = i + 1; j < n; j++)
    {
      M[j][i] = 0;
    }
  }
  return true;
}
bool Solve(double **&M, double *x, int n, int m, double &opred)
{
  double res = 0;
  if (!minor(M, n, m, opred)) return false;
  for(int i = n - 1; i >= 0; i--)
  {
    res = 0;
    for(int j = i + 1; j <= n - 1; j++)
      res = res - x[j] * M[i][j];
    res += M[i][n];
    x[i] = res / M[i][i];
  }
  return true;
}
double opr(double** M, int n, int m)
{
  double opr = 1;
  for(int i = 0; i < n; i++)
  {
    if (M[i][i] == 0) return 0;
    opr *= M[i][i] / pow(M[i][i], n - 1 - i);
  }
  return opr;
}
void test(double**& M, int n, int m)
{
  int k;
  cout << "Enter number test: "; cin >> k;
  switch (k)
  {
    case 1:
    {
      fstream A("data_array.txt", ios::in);
      for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
          A >> M[i][j];
      A.close();
      break;
    }
    case 2:
    {
      double a,b;
      srand(time(0));
      a = -10;
      b = 10;
      for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
          {
            M[i][j] = a + ((double) rand() / RAND_MAX) * (b - a);
          }
      break;
    }
    case 3:
    {
      for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
          if (i == j) M[i][j] = 1;
          else M[i][j] = 0;
      break;
    }
    case 4:
    {
      for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
          M[i][j] = 0;
      break;
    }
    case 5:
    {
      for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
          if (j == (m - 1)) M[i][j] = 1;
          else M[i][j] = 1. / (i + j + 1);
      break;
    }
  }
}
void copy(double**& M, int n, int m, double** M1)
{
  for(int i = 0; i < n; i++)
    for(int j = 0; j < m; j++)
      M1[i][j] = M[i][j];
}
double accuracy(double** M1, int n, int m, double *x)
{
  double epsilon = 0;
  double s;
  for(int i = 0; i < n; i++)
  {
    s = 0;
    for(int k = 0; k < m - 1; k++)
      s += M1[i][k] * x[k];
    if (fabs(M1[i][m - 1] - s) > epsilon) epsilon = fabs(M1[i][m - 1] - s);
  }
  return epsilon;
}
bool obratka(double** M, int n, int m, double &opred, double**& rev)
{
  double *x = new double [n];
  bool tochka = true;
  for(int i = 0; i < n; i++)
  {
    double** buff;
    newmatr(buff, n, m);
    copy(M, n, m, buff);
    for(int j = 0; j < n; j++)
    {
      if (i == j) buff[j][m - 1] = 1;
      else buff[j][m - 1] = 0;
    }
    if (!Solve(buff, x, n, m, opred)) tochka = false;
    for(int j = 0; j < n; j++)
      rev[j][i] = x[j];
    delmatr(buff, n, m);
  }
  delete [] x;
  x = NULL;
  return tochka;
}
void multy(double** M1, double** M2, int n1, int m1, int n2, int m2)
{
  double** buff;
  newmatr(buff, n1, m2);
  double S;
  if(m1 != n2)
  {
    cout << "error" << endl;
    delmatr(buff, n1, m2);
  }
  for(int i = 0; i < n1; i++)
    for(int j = 0; j < m2; j++)
    {
      S = 0;
      for(int k = 0; k < m1; k++)
        S += M1[i][k] * M2[k][j];
      buff[i][j] = S;
    }
  out(buff, n1, m2);
  delmatr(buff, n1, m2);
}
int main()
{
  int n;
  double opred = 1;
  cout << "enter size matrix: "; n = get_number();
  int m = n + 1;
  double **A;
  double **A1;
  double **rev;
  double *x = new double [n];
  newmatr(A, n, m);
  test(A, n, m);
  newmatr(A1, n, m);
  copy(A, n, m, A1);
  newmatr(rev, n, n);
  out(A, n, m);
  if (Solve(A, x, n, m, opred))
  {
    out_vektor(x, n);
    cout << "epsilon = " << accuracy(A1, n, m, x) << endl << endl;
  }
  else cout << "no single solution" << endl;
  cout << "opr = " << opred * opr(A, n, m) << endl;
  if (obratka(A1, n, m, opred, rev))
  {
    out(rev, n, n);
    multy(A1, rev, n, m - 1, n, n);
  }
  else cout << "no obratka" << endl;
  delmatr(A, n, m);
  delmatr(A1, n, m);
  delmatr(rev, n, n);
  delete [] x;
  x = NULL;
  return 0;
}