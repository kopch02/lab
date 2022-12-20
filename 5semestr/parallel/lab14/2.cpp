#include <stdio.h>
#include "include/mpi.h"
#include "string.h"
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    const int n = 15;

    int *len = new int[n];
    MPI_Aint *ds = new MPI_Aint[n];
    MPI_Datatype *types = new MPI_Datatype[n];
    MPI_Status *stat = new MPI_Status();
    MPI_Datatype halfMatrix;

    int **intArray = new int*[n];
    intArray[0] = new int[n * n];

    for (int i = 1; i < n; i++)
    {
        intArray[i] = intArray[i - 1] + n;
    }

    for (int i = 0; i < n; i++)
    {
        len[i] = 1;
        ds[i] = 4 * i;

        MPI_Type_vector(n - i, 1, n, MPI_INT, &types[i]);
        MPI_Type_commit(&types[i]);
    }

    MPI_Type_struct(n, len, ds, types, &halfMatrix);
    MPI_Type_commit(&halfMatrix);

    if (rank == 0)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                intArray[i][j] = 10 * (i + 1) + (j + 1);
            }
        }

        MPI_Send(intArray[0], 1, halfMatrix, 1, 777, MPI_COMM_WORLD);
    }

    if (rank == 1)
    {
        MPI_Recv(intArray[0], 1, halfMatrix, 0, 777, MPI_COMM_WORLD, stat);

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cout << setw(4) << intArray[i][j];
            }
            cout << endl;
        }
    }

    MPI_Finalize();
    return 0;
}