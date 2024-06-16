#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <ctime>

using namespace std;

enum { s2, m2, h2, d2, mon2, y2 };

class datetime
{
    private:
    int second;
    int minute;
    int hour;
    int day;
    int month;
    int year;

    public:
    datetime(int s,int m,int h, int d,int mon,int y)
    {
        if (s >= 0 && s < 60)

			second = s;

		else  second = 0;

		if ((m >= 0) && (m < 60))

			minute = m;

		else minute = 0;

		if (h >= 0 && h < 24)

			hour = h;

		else hour = 0;
		if (d > 0 && d < 32)

			day = d;

		else day = 1;
		if (mon > 0 && mon < 13)

			month = mon;

		else month = 1;

		year = y;
    }
    int Get(int index)
	{
		switch (index)
        {
		case 0: return second;
		case 1: return minute;
		case 2: return hour;
		case 3: return day;
		case 4: return month;
		case 5: return year;
		}
	}
    void nextdate(datetime* ,int );
    void prevdate(datetime* ,int );
    void sistem();
    datetime()
    {

    };
    ~datetime()
    {

    };

};

class run
{
    public:
    void find_n(int& );
    void in(datetime* ,int );
    void out(datetime* , int );
};
class app
{
    public:
    void runmain();
};
void run::find_n(int& n)
{
    ifstream file;
    datetime a;
    int r,b,c,d,e,f;
    file.open("file.txt");
    if(!file)
    {
        cout<<"file not found"<<endl;
        return;
    }
    while(file >> r>>b>>c>>d>>e>>f)
    {
        n++;
    }
    
    file.close();
}
void run::in(datetime* array,int n)
{
    int s,m,h,d,mon,y;
    ifstream file;
    file.open("file.txt");
    for (int i=0;i<n;i++)
    {
        file>>s>>m>>h>>d>>mon>>y;
        array[i]=datetime(s,m,h,d,mon,y);
    }
    file.close();
}
void run::out(datetime* array,int i)
{
 
        cout<<"second"<<setw(7)<<"minute"<<setw(5)<<"hour"<<setw(5)<<"day"<<setw(8)<<"month"<<setw(7)<<"year"<<setw(5)<<endl;
        cout<<array[i].Get(s2)<<setw(7)<<array[i].Get(m2)<<setw(5)<<array[i].Get(h2)<<setw(5)<<array[i].Get(d2)<<setw(7)<<array[i].Get(mon2)<<setw(8)<<array[i].Get(y2);
        cout<<endl;
    
}
void datetime::nextdate(datetime* array,int i)
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
void datetime::prevdate(datetime* arrayPrev,int i)
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
void datetime::sistem()
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

void app::runmain()
{
    int n;
    datetime date;
    run rr;
    rr.find_n(n);
    datetime* array = new datetime[n];
    datetime* arrayPrev = new datetime[n];
    datetime* arrayCurrent = new datetime[n];
    rr.in(array,n);
    rr.in(arrayPrev,n);
    rr.in(arrayCurrent,n);
    for(int i=0;i<n;i++)
    {
        cout<<endl<<"current"<<endl;
        rr.out(array,i);
        cout<<endl<<"next"<<endl;
        date.nextdate(array,i);
        rr.out(array,i);
        cout<<endl<<"prev"<<endl;
        date.prevdate(arrayPrev,i);
        rr.out(arrayPrev,i);
     
    }
    arrayPrev=arrayCurrent;
    cout<<endl<<endl<<endl<<"dates for variant"<<endl<<endl<<endl;
    for(int i=0;i<n;i++)
    {
        if(arrayCurrent[i].Get(d2)==1)
        {
            cout<<endl<<"current"<<endl;
            rr.out(arrayCurrent,i);
            cout<<endl<<"prev"<<endl;
            date.prevdate(arrayPrev,i);
            rr.out(arrayPrev,i);
        }
    }
    cout<<endl<<"date of sistem:"<<endl;
    date.sistem();
    delete[] array;
    delete[] arrayCurrent;
    delete[] arrayPrev;
    
}

int main()
{
    app q;
    q.runmain();

    return 0;
}