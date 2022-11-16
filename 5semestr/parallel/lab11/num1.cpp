#include <stdio.h>
#include "iostream"
#include "include/mpi.h"
#include "windows.h"
#include <time.h>

using namespace std;

int main(int argc, char *argv[])
{
    int rank;
    int size;
    int  i, a, b, s = 0;
    MPI_Status stat;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    srand(rank);
    a = rand() % 101;
    
    b = 0;
    MPI_Reduce(&a, &b, 1, MPI_INT, MPI_MAX, 0, MPI_COMM_WORLD);

    if (rank == 0)
    {
        printf("rank= %d b: ", rank);
        printf(" %d ", b);
        printf("\n ");
    }

    printf("rank= %d a: ", rank);
    printf(" %d ", a);
    printf("\n ");

    MPI_Finalize();
    return 0;
}