#include <stdio.h>
#include "iostream"
#include "windows.h"
#include "include/mpi.h"

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
    {
        int **s = new int *[size - 1];
        s[0] = new int[(size - 1) * n];
        for (int i = 1; i < size - 1; i++)
        {
            s[i] = s[i - 1] + n;
        }

        for (int i = 1; i < size ; i++)
        {
            MPI_Recv(&s[i - 1][0], n, MPI_INT, i, 777, MPI_COMM_WORLD, &stat);
        }
        cout << "s=" << endl;
        for (int i = 0; i < size - 1; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cout << s[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl;
        delete[] s[0];
        delete[] s;
    }
    else
    {
        int *a = new int[n];
        for (int i = 0; i < n; i++)
        {
            a[i] = rank;
        }

        MPI_Send(&a[0], n, MPI_INT, 0, 777, MPI_COMM_WORLD);
        delete[] a;
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
// delete a[0];
// delete a;

// Sleep(rank);
