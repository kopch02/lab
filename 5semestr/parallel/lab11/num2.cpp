#include <stdio.h>
#include "iostream"
#include "include/mpi.h"

using namespace std;

int main(int argc, char *argv[])
{
    int rank;
    int size;
    int n, i, s = 0;
    MPI_Status stat;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (rank == 0)
    {
        scanf("%d", &n);
    }
    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
    int *a = new int[n * size * 2];
    for (i = 0; i < n * size * 2; i++)
    {
        a[i] = i + rank;
    }
    int *b = new int[n * 2];
    for (i = 0; i < n; i++)
    {
        b[i] = 0;
    }
    int *RC = new int[size];
    for (i = 0; i < size; i++)
    {
        RC[i] = n * 2;
    }
    MPI_Reduce_scatter(a, b, RC, MPI_INT, MPI_SUM, MPI_COMM_WORLD);
    printf("rank= %d b: ", rank);
    for (i = 0; i < n * 2; i++)
    {
        printf(" %d ", b[i]);
    }
    printf("\n ");
    MPI_Finalize();
    return 0;
}
