#include <stdio.h>
#include "iostream"
#include "windows.h"
#include "include/mpi.h"
#include "ctime"
#include <cmath>

using namespace std;

void broad(void* n,int start, int count, MPI_Datatype datatype)
{
    int rank, size;
    MPI_Status stat;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank != start)
    {
        MPI_Recv(n, count, datatype, MPI_ANY_SOURCE, 777, MPI_COMM_WORLD, &stat);
    }
    for (int i = 0;i < ceil(log2(size));i++)
    {   
        if ( rank < pow(2, i))
        {
            MPI_Send(n, count, datatype, int(ceil(rank + pow(2,i))) % size , 777, MPI_COMM_WORLD);
        }
    }
}

int main(int argc, char *argv[])
{
    int rank;
    int a = 22;
    double t1, t2, td;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    if (rank == 0)
    {
        t1 = MPI_Wtime();
        broad(&a,0,1,MPI_INT);
        t2 = MPI_Wtime();
        td = t2 - t1;
        cout<<" time = "<<td<<endl;
    }
    else
    {
        broad(&a,0,1,MPI_INT);
    }

    MPI_Finalize();

    return 0;
}