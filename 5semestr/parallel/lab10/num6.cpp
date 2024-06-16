#include <stdio.h>
#include "iostream"
#include "include/mpi.h"
#include "windows.h"

using namespace std;

int main(int argc, char *argv[])
{
    int rank;
    int size;
    int i, s = 0, j;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    int **a = new int *[size];
    a[0] = new int[size * size];
    for (i = 1; i < size; i++)
    {
        a[i] = a[i - 1] + size;
    }
    if (rank == 0)
    {
        for (i = 0; i < size; i++)
        {
            for (j = 0; j < size; j++)
            {
                a[i][j] = i;
            }
        }
    }
    int *RC = new int[size];
    int *ds = new int[size];
    for (int i = 0; i < size; i++)
    {
        RC[i] = size - i;
        ds[i] = i * size;
    }
    int *b = new int[size - rank];
    MPI_Scatterv(*a, RC, ds, MPI_INT, b, size - rank, MPI_INT, 0, MPI_COMM_WORLD);
    printf("rank= %d b: ", rank);
    for (i = 0; i < size - rank; i++)
    {
        printf(" %d ", b[i]);
    }
    printf("\n ");
    MPI_Finalize();
    return 0;
}
