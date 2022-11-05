#include <stdio.h>
#include "iostream"
#include "include/mpi.h"
#include "windows.h"

using namespace std;


int main(int argc, char *argv[])
{
    int rank;
    int size;
    int n = 9;
    MPI_Status stat;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0)
        cin >> n;

    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);

    int **a = new int *[2];
    a[0] = new int[2 * n];
    for (int i = 1; i < 2; i++)
        a[i] = a[i - 1] + n;

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < n; j++)
        {
            a[i][j] = rank;
        }
    }

    int **b = new int *[2 * size];
    b[0] = new int[2 * size * n];
    for (int i = 1; i < 2 * size; i++)
        b[i] = b[i - 1] + n;

	MPI_Gather(*a, 2 * n, MPI_INT, *b, 2 * n, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank == 0)
    {

        printf("rank = %d, a: \n", rank);
        for (int i = 0; i < 2 * size; i++)
        {
            for (int j = 0; j < n; j++)
                cout << b[i][j] << " ";
            cout << endl;
        }
    }
    delete[] b[0];
    delete[] b;
    delete[] a[0];
    delete[] a;

    MPI_Finalize();
    return 0;
}
