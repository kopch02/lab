#include <stdio.h>
#include "iostream"
#include "windows.h"
#include "include/mpi.h"
#include <cmath>

using namespace std;

int main(int argc, char *argv[])
{
    int n;
    double t1, t2;
    MPI_Init(&argc, &argv);
    for (int x = 3; x < 9; x++)
    {

        n = pow(10, x);

        double *v1 = new double[n];
        for (int i = 0; i < n; i++)
        {
            v1[i] = (1.0 / (1 + i));
        }
        double *v2 = new double[n];
        for (int i = 0; i < n; i++)
        {
            v2[i] = i / (1.0 + i);
        }

        double res = 0;
        t1 = MPI_Wtime();
        for (int i = 0; i < n; i++)
        {
            res += v1[i] * v2[i];
        }
        t2 = MPI_Wtime();
        double td = t2 - t1;
        printf("10^%d = %f\n", x, res);
        printf("time for 10^%d : %f\n", x, td);
    }
    MPI_Finalize();
    return 0;
}
