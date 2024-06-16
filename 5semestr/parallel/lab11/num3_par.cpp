#include <stdio.h>
#include "iostream"
#include "windows.h"
#include "include/mpi.h"
#include <cmath>

using namespace std;

int main(int argc, char *argv[])
{

    int n, rank, size;
    double t1, t2;
    MPI_Init(&argc, &argv);
    MPI_Status stat;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

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

        int t = n / size;
        double *b1 = new double[t];
        double *b2 = new double[t];
        double res = 0;
        MPI_Scatter(v1, t, MPI_DOUBLE, b1, t, MPI_DOUBLE, 0, MPI_COMM_WORLD);
        MPI_Scatter(v2, t, MPI_DOUBLE, b2, t, MPI_DOUBLE, 0, MPI_COMM_WORLD);
        double s = 0;
        if (rank == 0)
        {
            t1 = MPI_Wtime();
        }
        for (int i = 0; i < t; i++)
        {
            s += b1[i] * b2[i];
        }
        MPI_Reduce(&s, &res, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);
        if (rank == 0)
        {
            t2 = MPI_Wtime();
            double td = t2 - t1;
            printf("10^%d = %f\n", x, res);
            printf("time for 10^%d : %f\n", x, td);
        }
    }
    MPI_Finalize();
    return 0;
}
