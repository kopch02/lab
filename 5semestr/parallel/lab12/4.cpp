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

        MPI_Datatype mt;
        MPI_Type_vector(n / 2, 1, 2, MPI_INT, &mt);
        MPI_Type_commit(&mt);

        if (rank == 0)
        {
            double t1, t2;
            for (int i = 0; i < n; i++)
                a[i] = i;
            t1 = MPI_Wtime();
            MPI_Send(&a[0], 1, mt, 1, 777, MPI_COMM_WORLD);
            t2 = MPI_Wtime();

            cout << "n = " << n << " time = " << t2 - t1 << endl;
        }

        if (rank == 1)
        {
            MPI_Recv(&a[0], n / 2, MPI_INT, 0, 777, MPI_COMM_WORLD, &stat);
        }
        MPI_Type_free(&mt);
        delete[] a;
    }

    MPI_Finalize();
    return 0;
}
