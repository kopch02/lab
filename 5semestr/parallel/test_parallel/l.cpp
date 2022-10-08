#include <stdio.h>
#include "iostream"
#include "include/mpi.h"

using namespace std;

int main(int argc, char *argv[])
{
int rank;
int size;
MPI_Status stat;
MPI_Init(&argc, &argv);
MPI_Comm_rank(MPI_COMM_WORLD, &rank);
MPI_Comm_size(MPI_COMM_WORLD, &size);

int* a=new int[(size * (size + 1))/2 - 1];
int j=0;

if (rank==0)
{
    for (int i = 1;i<size;i++)
    {
        MPI_Recv(&a[j],i+1,MPI_INT,i,777,MPI_COMM_WORLD,&stat);
        j+=i+1;
    }
    cout<<"a=";
    for (int i =0;i<(size * (size + 1))/2 - 1;i++)
    {
        cout<<a[i]<<"   ";
    }
    cout<<endl;
    delete []a;
}
else
{   
    int* b= new int[rank+1];
    for (int i = 0;i<rank+1;i++)
    {
        b[i]=rank;
    }
    MPI_Send(&b[0],rank+1,MPI_INT,0,777,MPI_COMM_WORLD);

    cout<<"rank="<<rank<<"    "<<"b=";
    for (int i =0;i<rank+1;i++)
    {
        cout<<b[i]<<"   ";
    }
    cout<<endl;
    delete []b;
}

MPI_Finalize();

return 0;
}

