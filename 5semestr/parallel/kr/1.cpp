#include <stdio.h>
#include "include/mpi.h"
#include <iostream>
#include "time.h"

using std::cin;
using std::cout;
using std::endl;

int main(int argc, char *argv[])
{
    int rank;
    int size;
    int n = 100;
    double t1,t2,t;
    MPI_Status stat;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (rank == 0)
    {
        t1 = MPI_Wtime();
        MPI_Send(&n,1,MPI_INT,3,777,MPI_COMM_WORLD);
        MPI_Recv(&n,1,MPI_INT,3,777,MPI_COMM_WORLD,&stat);
        t2 = MPI_Wtime();
        cout << "n = " << n << " time = " << t2 - t1 << endl;
    }

    if (rank == 3)
    {
        MPI_Recv(&n,1,MPI_INT,0,777,MPI_COMM_WORLD,&stat);
        MPI_Send(&n,1,MPI_INT,0,777,MPI_COMM_WORLD);

    }


    MPI_Finalize();
    return 0;
}
