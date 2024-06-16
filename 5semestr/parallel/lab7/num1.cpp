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
    int a = 22, b = 27;
    int chet, nechet;
    MPI_Status stat;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (size%2 == 0){  //создаю вспомогательныйе переменные в зависимости от того, на чётном или не чётном количестве процессо запущенна программа
        chet = 0;
        nechet = 1;
    }
    else{
        chet = 1;
        nechet = 0;
    }

    if (rank == 0){
        MPI_Sendrecv(&a, 1, MPI_INT, 2, 777, &a, 1, MPI_INT, size - 1 - nechet, 777, MPI_COMM_WORLD, &stat); //если было запущенно на чётном количестве, то принимаю 
                                                                                                                //от предпоследнего процесса, если нет, то от последнего

        cout<<"rank ="<<rank<<" a ="<<a<<endl;
    }
    else if(rank == 1){
        MPI_Sendrecv(&b, 1, MPI_INT, 3, 777, &b, 1, MPI_INT, size - 1 - chet, 777, MPI_COMM_WORLD, &stat); //наоборот от нулевого 
        cout<<"rank ="<<rank<<" b ="<<b<<endl;
    }
    else if (rank == size - 2){
        MPI_Probe(MPI_ANY_SOURCE,MPI_ANY_TAG,MPI_COMM_WORLD,&stat);
        MPI_Sendrecv(&a, 1, MPI_INT, chet, 777, &a, 1, MPI_INT, stat.MPI_SOURCE, 777, MPI_COMM_WORLD, &stat);//это предпоследний процесс, отправляю на 0 или 1 в зависимости от того
                                                                                                            //на скольких процессах была запущенна программа
    }
    else if (rank == size - 1){
        MPI_Probe(MPI_ANY_SOURCE,MPI_ANY_TAG,MPI_COMM_WORLD,&stat);
        MPI_Sendrecv(&b , 1, MPI_INT, nechet, 777, &b, 1, MPI_INT, stat.MPI_SOURCE, 777, MPI_COMM_WORLD, &stat);
    }
    else
    {   
        MPI_Probe(MPI_ANY_SOURCE,MPI_ANY_TAG,MPI_COMM_WORLD,&stat);
        if (stat.MPI_SOURCE % 2 == 0){
            MPI_Sendrecv(&a, 1, MPI_INT, rank + 2, 777, &a, 1, MPI_INT, stat.MPI_SOURCE, 777, MPI_COMM_WORLD, &stat);
        }
        else{
            MPI_Sendrecv(&b, 1, MPI_INT, rank + 2, 777, &b, 1, MPI_INT, stat.MPI_SOURCE, 777, MPI_COMM_WORLD, &stat);
        }
    }
   

    MPI_Finalize();

    return 0;
}