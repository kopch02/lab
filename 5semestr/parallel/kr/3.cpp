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
    
    n = rank;

    MPI_Reduce(&n, &s, 1, MPI_INT, MPI_SUM, 0,MPI_COMM_WORLD);
    printf("rank= %d n: %d", rank,n);
    
    if (rank == 0)
    {
        printf("\nrank= %d sum: %d", rank,s);
    }
    
    printf("\n ");
    MPI_Finalize();
    return 0;
}
