#include <stdio.h>
#include "iostream"
#include "include/mpi.h"

using namespace std;

int main(int argc, char *argv[])
{
    int rank;
    int size;
    int i, j, s = 0;
    int n;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int *a = new int [size * (size + 1)];
    
    if (rank == 0)
    {
        for (int i = 0; i < size * (size + 1); i++)
        {
            a[i] = i;
        }
    }
    int *b = new int [rank * 2 + 2];

    int *sc = new int[size];
    int *ds = new int[size];

    for (int i = 0; i < size; i++)
    {
        sc[i] = i * 2 + 2;
    }
    ds[0] = 0;
    for (int i = 1; i < size ; i++)
    {
        ds[i] = ds[i - 1] + i * 2;
    }

    MPI_Scatterv(a, sc, ds,MPI_INT, b, rank * 2 + 2, MPI_INT, 0, MPI_COMM_WORLD);

    printf("rank= %d a: \n", rank);
    for (i = 0; i < rank * 2 + 2; i++)
    {
        printf(" %d ", b[i]);

    }
    printf("\n");
    MPI_Finalize();

    return 0;
}
