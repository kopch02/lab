#include <stdio.h>
#include <iostream>
#include "include/mpi.h"


int main(int argc, char *argv[])
{
    int rank;
    int size;
    int n = 0;
    double t1, t2, a = 0, t, fl;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    std::cin >> n;

    t1 = MPI_Wtime();
    for (int i = 0; i < n; i++)
        a = a + 0.000000000001;
    t2 = MPI_Wtime();

    t = (t2 - t1) / (2 * n);

    fl = 1. / t / 1000000;

    printf("n = %d, t2-t1=%g t = %g Mflops=%g\n", n, t2 - t1, t, fl);

    MPI_Finalize();
    
    return 0;
}
