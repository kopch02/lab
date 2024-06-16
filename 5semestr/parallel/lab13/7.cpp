#include <stdio.h>
#include "iostream"
#include "include/mpi.h"

using namespace std;

int main(int argc, char *argv[])
{
    int rank;
    int size;

    MPI_Status stat;
    MPI_Request req;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Datatype mt, mt1;

    int n = 9;

    MPI_Type_vector(n, 1, n, MPI_INT, &mt);
    MPI_Type_commit(&mt);

    int count = (n % 2 != 0) ? (n / 2 + 1) : (n / 2);
    MPI_Type_hvector(count, 1, 8, mt, &mt1);
    MPI_Type_commit(&mt1);

    int **a = new int *[n];

    a[0] = new int[n * n];
    for (int i = 1; i < n; i++)
    {
        a[i] = a[i - 1] + n;
    }

    if (rank == 0)
    {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                a[i][j] = 10 * (i + 1) + j + 1;

        MPI_Send(a[0], 1, mt1, 1, 777, MPI_COMM_WORLD);
    }

    if (rank == 1)
    {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                a[i][j] = 0;

        MPI_Recv(&a[0][0], 1, mt1, 0, 777, MPI_COMM_WORLD, &stat);
    }

    printf("rank=%d arr : \n", rank);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf(" %d ", a[i][j]);
        }
        printf("\n");
    }
    printf("]\n");

    MPI_Finalize();

    return 0;
}
