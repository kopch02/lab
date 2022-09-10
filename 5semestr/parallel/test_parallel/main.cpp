#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include "include/mpi.h"
using namespace std;

int main(int argc, char *argv[])
{
    double start,end;
    long lim = 1e9;
    double sum = 0;
    MPI_Init(&argc, &argv);
    start = MPI_Wtime ();
    for (int i=0;i<lim;i++)
    {
        sum+=(1/(1+i));
    }
    end = MPI_Wtime ();
    cout << "limit: " << lim << endl;
    cout << "sum: " << sum << endl;
    cout << "time: " << end-start << endl;
    MPI_Finalize();
    return 0;
}
