#include <stdio.h>
#include "iostream"
#include "include/mpi.h"
#include "windows.h"

using namespace std;

int main(int argc, char *argv[])
{
    int rank;
    int size;
    int n = 10, i, s = 0;
    MPI_Status stat;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Datatype mt;
    MPI_Datatype mt1;
    MPI_Datatype mt2;
    MPI_Type_contiguous(n, MPI_INT, &mt1);
    MPI_Type_commit(&mt1);
    MPI_Type_vector(n/2, 1, 2, mt1, &mt);
    MPI_Type_commit(&mt);
    MPI_Type_contiguous(2, mt, &mt1);
    MPI_Type_commit(&mt1);
    MPI_Type_vector(2, 1, 2, mt1, &mt2);
    MPI_Type_commit(&mt2);
    int **a = new int *[n];
    a[0] = new int[n * n];
    for (int i = 1; i < n; i++)
    {
        a[i] = a[i - 1] + n;
    }
    if (rank == 0)
    {
        for (int i = 0; i < n; i++)
        {   
            for(int j =0;j<n;j++)
            {
                a[i][j] = i;
            }
        }
        MPI_Send(*a , 1, mt, 1, 777, MPI_COMM_WORLD);
    }
    if (rank == 1)
    {
        MPI_Recv(*a, 1, mt, 0, 777, MPI_COMM_WORLD, &stat);
        printf("rank= %d a: ", rank);
        for (int i = 0; i < n; i++)
        {   
            for(int j =0;j<n;j++)
            {
                printf(" %d ", a[i][j]);
            }
            printf("\n ");
        }
    }

    MPI_Finalize();
    return 0;
}
