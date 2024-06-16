#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <ctime>
using namespace std;
struct datetime
{
    int second;
    int minute;
    int hour;
    int day;
    int month;
    int year;
};

void find_n(int& n)
{
    ifstream file;
    datetime a;
    file.open("file.txt");
    if(!file)
    {
        cout<<"file not found"<<endl;
        return;
    }
    while(file >> a.second>>a.minute>>a.hour>>a.day>>a.month>>a.year)
    {
        n++;
    }
    file.close();
}
void in(datetime* array,int n)
{
    ifstream file;
    file.open("file.txt");
    for (int i=0;i<n;i++)
    {
    file>>array[i].second>>array[i].minute>>array[i].hour>>array[i].day>>array[i].month>>array[i].year;
    }
    file.close();
}
void out(datetime* array,int i)
{
    //for(int i=0;i<1;i++)
    
        cout<<"second"<<setw(7)<<"minute"<<setw(5)<<"hour"<<setw(5)<<"day"<<setw(8)<<"month"<<setw(7)<<"year"<<setw(5)<<endl;
        cout<<array[i].second<<setw(7)<<array[i].minute<<setw(5)<<array[i].hour<<setw(5)<<array[i].day<<setw(7)<<array[i].month<<setw(8)<<array[i].year;
        cout<<endl;
    
}
void nextdate(datetime* array,int i)
{
    
    if ((array[i].month==4)||(array[i].month==6)||(array[i].month==9)||(array[i].month==11))
    {
        if (array[i].day==30)
        {
            array[i].day=1;
            array[i].month+=1;
            if(array[i].month==13)
            {
                array[i].month=1;
                array[i].year+=1;
            }
        }
        else{
            array[i].day+=1;
        }
        return;
    }
    if(array[i].month==2)
    {
        if((array[i].year%4==0) ||(array[i].year%4000!=0) || ((array[i].year%100!=0)||(array[i].year%400==0)))
        {
            if(array[i].day==29)
            {
                array[i].day=1;
                array[i].month+=1;
            }
            else{
                array[i].day+=1;
            }
        }
        else{
            if(array[i].day==28)
            {
                array[i].day=1;
                array[i].month+=1;
            }
            else{
                array[i].day+=1;
            }
        }
        return;
    }
    if((array[i].month==1)||(array[i].month==3)||(array[i].month==5)||(array[i].month==7)||(array[i].month==8)||(array[i].month==10)||(array[i].month==12))
    {    
        if (array[i].day==31)
        {
            array[i].day=1;
            array[i].month+=1;
            if(array[i].month==13)
            {
                array[i].month=1;
                array[i].year+=1;
            }
        }
        else{
            array[i].day+=1;
        }
        return;
    }
}
void prevdate(datetime* arrayPrev,int i)
{
    arrayPrev[i].day-=1;
    if(arrayPrev[i].day==0)
    {
        arrayPrev[i].month-=1;
        if(arrayPrev[i].month==2)
        {
            if((arrayPrev[i].year%4==0) ||(arrayPrev[i].year%4000!=0) || ((arrayPrev[i].year%100!=0)||(arrayPrev[i].year%400==0)))
            {
                arrayPrev[i].day=29;
            }
            else {
                arrayPrev[i].day=28;
            }
            return;
        }
        if((arrayPrev[i].month==1)||(arrayPrev[i].month==3)||(arrayPrev[i].month==5)||(arrayPrev[i].month==7)||(arrayPrev[i].month==8)||(arrayPrev[i].month==10)||(arrayPrev[i].month==12))
        {
            arrayPrev[i].day=31;
            return;
        }
        if(arrayPrev[i].month==0)
        {
            arrayPrev[i].month=12;
            arrayPrev[i].year-=1;
            arrayPrev[i].day=31;
            return;
        }
        else 
        {
            arrayPrev[i].day=30;
            return;
        }
    }
}
void sistem()
{
    int a,b;
    int year,month,day,hour,minute,second;
 time_t rawtime;
  struct tm * timeinfo;
  time( &rawtime ); 
  a=time(&rawtime);
  a+=25200;
  year=a/31536000;
  a-=31536000*year;
  year+=2;
  b=year/4;
  year-=2;
  a-=b*86400;
  year+=1970;
  cout<<endl<<"year"<<endl<<year;
  day=a/86400;
  a-=86400*day;
  month=day/31;
  day-=month*31;
  month+=1;
  cout<<endl<<"month"<<endl<<month;
  if((month==2)||(month==3))
  {
      day+=3;
  }
  if((month==4)||(month==5))
  {
      day+=4;
  }
  if((month==6)||(month==7)||(month==8))
  {
      day+=5;
  }
  if((month==9)||(month==10))
  {
      day+=6;
  }
  if((month==11)||(month==12))
  {
      day+=7;
  }
  cout<<endl<<"day"<<endl<<day;
  hour=a/3600;
  a-=3600*hour;
  cout<<endl<<"hour"<<endl<<hour;
  minute=a/60;
  a-=60*minute;
  cout<<endl<<"minute"<<endl<<minute;
  cout<<endl<<"second"<<endl<<a;
}

main()
{
    int n=8;
    datetime date;
    find_n(n);
    datetime* array = new datetime[n];
    datetime* arrayPrev = new datetime[n];
    datetime* arrayCurrent = new datetime[n];
    in(array,n);
    in(arrayPrev,n);
    in(arrayCurrent,n);
    for(int i=0;i<n;i++)
    {
        cout<<endl<<"current"<<endl;
        out(array,i);
        cout<<endl<<"next"<<endl;
        nextdate(array,i);
        out(array,i);
        cout<<endl<<"prev"<<endl;
        prevdate(arrayPrev,i);
        out(arrayPrev,i);
     
    }
    arrayPrev=arrayCurrent;
    cout<<endl<<endl<<endl<<"dates for variant"<<endl<<endl<<endl;
    for(int i=0;i<n;i++)
    {
        if(arrayCurrent[i].day==1)
        {
            cout<<endl<<"current"<<endl;
            out(arrayCurrent,i);
            cout<<endl<<"prev"<<endl;
            prevdate(arrayPrev,i);
            out(arrayPrev,i);
        }
    }
    cout<<endl<<"date of sistem:"<<endl;
    sistem();
    return 0;
}