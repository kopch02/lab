#include <stdio.h>
#include "iostream"
#include "include/mpi.h"
#include "windows.h"

using namespace std;

int main(int argc, char *argv[])
{
    int rank;
    int size;
    int i, s = 0;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int *b = new int[3];
    for (i = 0; i < 3; i++)
        b[i] = rank;

    int *a = new int[3 * (size - 1)];

    int *RC = new int[size];
    RC[0] = 0;
    for (int i = 1; i < size; i++)
        RC[i] = 3;
    int *ds = new int[size];
    ds[0] = 0;
    for (int i = 1; i < size; i++)
        ds[i] = (i - 1) * 3;

    MPI_Gatherv(b, 3, MPI_INT, a, RC, ds, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank == 0)
    {

        printf("rank = %d, a: \n", rank);
        for (int i = 0; i < 3 * (size - 1); i++)
        {
            cout << a[i] << " ";
        }
        cout << endl;
    }
    delete[] a;
    delete[] b;
    delete[] RC;
    delete[] ds;
    MPI_Finalize();
    return 0;
}
