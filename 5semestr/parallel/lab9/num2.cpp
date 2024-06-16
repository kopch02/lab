#include <stdio.h>
#include "iostream"
#include "include/mpi.h"
#include "windows.h"

using namespace std;

int main(int argc, char *argv[])
{
    int rank;
    int size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    int *bl = new int[size];
    int *ds = new int[size];

    for (int i = 0; i < size; i++)
    {
        bl[i] = size - i;
    }

    ds[0] = 0;
    for (int i = 1; i < size; i++)
    {
        ds[i]=ds[i-1] + (size - (i - 1));
    }


    int *a = new int[(size * (size + 1)) / 2];
    int *b = new int[size - rank];
    for (int i = 0; i < size - rank; i++)
    {
        b[i] = rank;
    }
    for (int i = 0; i < size; i++)
    {
        a[i] = 0;
    }

    MPI_Gatherv(b, size - rank, MPI_INT, a, bl, ds, MPI_INT, 0, MPI_COMM_WORLD);

    Sleep(10 * rank);

    if (rank == 0)
    {
        printf("rank = %d a: \n", rank);
        for (int i = 0; i < (size * (size + 1)) / 2; i++)
        {
            printf("%d", a[i]);
        }
    }
    MPI_Finalize();

    return 0;
}
