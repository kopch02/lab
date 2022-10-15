#include <stdio.h>
#include "iostream"
#include "windows.h"
#include "include/mpi.h"
#include "ctime"

using namespace std;

int main(int argc, char *argv[])
{
    int rank;
    int size;
    int n=0, count, i, j;
    MPI_Status stat;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if(rank==0)
    {
        n=size;
        int **a=new int *[n];
        a[0]=new int [n*n];
        for(i=1; i<n; i++)
        {
            a[i]=a[i-1]+n;
        }
        for(i=0; i<n; i++)
        {
            for(j=0; j<n; j++)
            {
                a[i][j]=0;
            }
        }
        
        for (i=1;i<size;i++)
        {
            MPI_Probe(MPI_ANY_SOURCE,MPI_ANY_TAG,MPI_COMM_WORLD,&stat);
            MPI_Get_count(&stat,MPI_INT,&count);
            MPI_Recv(a[stat.MPI_SOURCE],count,MPI_INT,stat.MPI_SOURCE,777,MPI_COMM_WORLD,&stat);
            printf("source= %d \n",stat.MPI_SOURCE);
        }
        for(i=0; i<n; i++)
        {
            for(j=0; j<n; j++)
            printf(" %d ",a[i][j]);
            printf("\n ");
        }
    }
    else
    {   
        srand(rank* time(0) );
        n = rand() % size +1;
        int *a = new int[n];
        for (i=0;i<n;i++)
        a[i]=rank;
        MPI_Send(a,n,MPI_INT,0,777,MPI_COMM_WORLD);
        cout<<"rank = "<<rank<<" :";
        for(i=0; i<n; i++)
        {
            printf(" %d ",a[i]);
        }
        cout<<endl;
    }
    MPI_Finalize();
    return 0;
}


/*
if (rank==1)
{   
    cout<<"rank = "<<rank<<endl;

    for (int i = 0;i<n;i++)
    {
        for (int j=0;j<n;j++)
        {
            a[i][j]=0;
        }
    }

    MPI_Recv(&a[0][0],2*n,MPI_INT,0,777,MPI_COMM_WORLD,&stat);
}


for (int i =0;i<n;i++){
    for (int j=0;j<n;j++)
    {
        cout<<a[i][j]<<" ";
    }
    cout<<endl;
}
*/
//delete a[0];
//delete a;



//Sleep(rank);

