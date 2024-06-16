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
        int s = sizeof(int) * n + sizeof(double) * n + n * sizeof(char);
        char *buf = new char[s];
        int pos = 0;
        int *a = new int[n];
        double *b = new double[n];
        double t1, t2;
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

            MPI_Pack(a, n, MPI_INT, buf, s, &pos, MPI_COMM_WORLD);
            MPI_Pack(b, n, MPI_DOUBLE, buf, s, &pos, MPI_COMM_WORLD);
            MPI_Pack(c, n, MPI_CHAR, buf, s, &pos, MPI_COMM_WORLD);
            MPI_Send(buf, s, MPI_PACKED, 1, 777, MPI_COMM_WORLD);

            int q;
            MPI_Recv(&q, 1, MPI_INT, 1, 777, MPI_COMM_WORLD, &stat);
            t2 = MPI_Wtime();

            printf("\ntime: %f\nn: %d", t2 - t1, n);
        }
        if (rank == 1)
        {

            MPI_Recv(buf, s, MPI_PACKED, 0, 777, MPI_COMM_WORLD, &stat);
            MPI_Unpack(buf, s, &pos, a, n, MPI_INT, MPI_COMM_WORLD);
            MPI_Unpack(buf, s, &pos, b, n, MPI_DOUBLE, MPI_COMM_WORLD);
            MPI_Unpack(buf, s, &pos, &c, n, MPI_CHAR, MPI_COMM_WORLD);

            int q = 0;
            MPI_Send(&q, 1, MPI_INT, 0, 777, MPI_COMM_WORLD);
            /*
            printf("a= \n");
            for (int i = 0;i < n;i++)
            {
                printf(" %d ", a[i]);
            }
            printf("\n");
            printf("b= \n");
            for (int i = 0;i < n;i++)
            {
                printf(" %f ", b[i]);
            }
            printf("\n");
            printf("c= %s \n", c);
            for (int i = 0; i < n; i++)
                cout << c[i];
            */
        }
    }
    MPI_Finalize();
    return 0;
}
