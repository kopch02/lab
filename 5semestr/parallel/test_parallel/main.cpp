#include <stdio.h>
#include "iostream"
#include "include/mpi.h"

using namespace std;

int main(int argc, char *argv[])
{
int rank;
int size;
int a=0,s=0;
MPI_Status stat;
MPI_Init(&argc, &argv);
MPI_Comm_rank(MPI_COMM_WORLD, &rank);
MPI_Comm_size(MPI_COMM_WORLD, &size);

if (rank==0)
{
    MPI_Send(&a,1,MPI_INT,rank+1,777,MPI_COMM_WORLD);
    MPI_Recv(&a,1,MPI_INT,size-1,777,MPI_COMM_WORLD,&stat);
}
else
{
    MPI_Recv(&a,1,MPI_INT,rank-1,777,MPI_COMM_WORLD,&stat);
    a++;
    cout<<"a="<<a<<"rank="<<rank<<endl;

}

if (rank==size-1)
{
    MPI_Send(&a,1,MPI_INT,0,777,MPI_COMM_WORLD);
}
else
{
    MPI_Send(&a,1,MPI_INT,rank+1,777,MPI_COMM_WORLD);
}

MPI_Finalize();

return 0;
}

