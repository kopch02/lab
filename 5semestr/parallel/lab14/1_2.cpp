#include <stdio.h>
#include "include/mpi.h"
#include "string.h"
#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char *argv[])
{
    int rank, size;
    int n;

    MPI_Status stat;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    for (int x = 1; x < 7; x++)
    {
        n = pow(11, x);
        char c[n];
        int *a = new int[n];
        double *b = new double[n];
        double t1, t2;

        int bl[] = {n, n, n};

        MPI_Datatype mt;
        MPI_Datatype dt[] = {MPI_INT, MPI_DOUBLE, MPI_CHAR};

        MPI_Aint ds[3], aa, ab, ac;
        MPI_Get_address(a, &aa);
        MPI_Get_address(b, &ab);
        MPI_Get_address(c, &ac);

        ds[0] = 0;
        ds[1] = ab - aa;
        ds[2] = ac - aa;

        MPI_Type_struct(3, bl, ds, dt, &mt);
        MPI_Type_commit(&mt);

        if (rank == 0)
        {   
            t1 = MPI_Wtime();
            for (int i = 0; i < n; i++)
            {
                a[i] = i;
                b[i] = i / (i + 1.);
            }

            string s4(n, 'h');
            char *h = s4.data();
            strcpy(c, h);

            MPI_Send(a, 1, mt, 1, 777, MPI_COMM_WORLD);

            int q;
            MPI_Recv(&q, 1, MPI_INT, 1, 777, MPI_COMM_WORLD, &stat);
            t2 = MPI_Wtime();

            printf("\ntime: %f\nn: %d", t2 - t1, n);
        }

        if (rank == 1)
        {
            MPI_Recv(a, 1, mt, 0, 777, MPI_COMM_WORLD, &stat);

            int q = 0;
            MPI_Send(&q, 1, MPI_INT, 0, 777, MPI_COMM_WORLD);
            /*
            printf("a= \n");
            for (int i = 0; i < n; i++)
            {
                printf(" %d ", a[i]);
            }
            printf("\n");
            printf("b= \n");
            for (int i = 0; i < n; i++)
            {
                printf(" %f ", b[i]);
            }
            printf("\n");
            printf("c=  \n");
            for (int i = 0; i < n; i++)
                cout << c[i];
            */
        }
    }
    MPI_Finalize();
    return 0;
}
