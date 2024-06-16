#include <stdio.h>
#include "include/mpi.h"
#include <iostream>
#include "time.h"

using std::cin;
using std::cout;
using std::endl;

int main(int argc, char *argv[])
{
    int rank;
    int size;
    int s = 0;
    int n;
    MPI_Status stat;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    for (int n = 1e3; n < 1e9; n *= 10)
    {
        int *a = new int[n];
        int *b = new int[n / 2];
        if (rank == 0)
        {
            double t1, t2;
            t1 = MPI_Wtime();
            for (int i = 0, j = 0; i < n; i++)
            {
                a[i] = i;
                if (a[i] % 2 == 0)
                {
                    b[j] = a[i];
                    j++;
                }
            }
            MPI_Send(&b[0], n / 2, MPI_INT, 1, 777, MPI_COMM_WORLD);
            t2 = MPI_Wtime();

            cout << "n = " << n << " time = " << t2 - t1 << endl;
        }

        if (rank == 1)
        {
            MPI_Recv(&a[0], n / 2, MPI_INT, 0, 777, MPI_COMM_WORLD, &stat);
        }
        delete[] a;
        delete[] b;
    }

    MPI_Finalize();
    return 0;
}
