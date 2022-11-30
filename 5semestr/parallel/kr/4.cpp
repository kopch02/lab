#include <stdio.h>
#include "iostream"
#include "include/mpi.h"
#include "windows.h"

using namespace std;

int main(int argc, char *argv[])
{
    int rank;
    int size;
    int n = 20, i, s = 0;
    MPI_Status stat;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Datatype mt;

    MPI_Type_vector(7, 1, 3, MPI_INT, &mt);
    MPI_Type_commit(&mt);

    if (rank == 0)
    {
        int *a = new int[n];
        for (int i = 0; i < n; i++)
        {
            a[i] = i;
        }
        MPI_Send(&a[1], 1, mt, 1, 777, MPI_COMM_WORLD);
    }
    if (rank == 1)
    {   
        int *b = new int[7];
        MPI_Recv(&b[0], 7, MPI_INT, 0, 777, MPI_COMM_WORLD, &stat);
        printf("rank= %d b: ", rank);
        for (int i = 0; i < 7; i++)
        {
            printf(" %d ", b[i]);
        }
    }

    MPI_Finalize();
    return 0;
}
