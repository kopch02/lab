#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include <iomanip>
#include <Windows.h>
#include <Wingdi.h>
#include <string.h>
#include <process.h> 
#include <windowsx.h>
#include <objidl.h>
#include <gdiplus.h>

using namespace std;

const double PI=3.14159265359;
enum {A,B};

//глобальные переменные для рисования окна
HINSTANCE hInstance; HINSTANCE hPrevInst;
LPSTR lpszArgs; int nWinMode;
HPEN MyPen;
HBRUSH MyBrush;
HDC dc;
double AE,ACI,AR,AS,AT;
double BE,BCI,BR,BS,HT;

/*Прототип используемой в программе оконной функции */
LRESULT CALLBACK WindowFuncEllipse(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK WindowFuncSquaCircle(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK WindowFuncSquaRectangle(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK WindowFuncSquare(HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK WindowFuncTriangle(HWND, UINT, WPARAM, LPARAM);

class Exc {

public:
	string message;
	Exc( string b)
	{
		message = b;
	}
	void show()
	{
		cout << endl;
		cout << "\t" << message << endl;
	}
	~Exc()  {};
};

class shape
{   
    public:
    void draw();
    virtual void move()=0;
    virtual double area()=0;

    shape()
    {

    }
};

template<typename T>
class cylinder
{
    public:
    double V;
    T* m;
    double h;
    cylinder(T* f, double height)
    {
       h=height;
       m=f;
    }
    double volume()
    {
        V=m->area()*h;
        cout<<endl<<"figure volume="<<V<<endl;   
    }
};

class exemple : public shape
{
    public:
        int  WINAPI WinMainEllipse(  HINSTANCE hInstance, HINSTANCE hPrevInst,LPSTR lpszArgs, int nWinMode) 
        {
        char szWinName[ ]="MyWindow";      //Произвольное имя класса главного окна
        char szTitle[ ]="Ellipse";               //Произвольный заголовок окна
        MSG msg;                    //Структура msg типа MSG для получения сообщений Windows
        WNDCLASS wc;                                  //Структура wc типа WNDCLASS для задания
                                    //характеристик окна
        /*Заполнение структуры wc типа WNDCLASS для описания класса главного окна*/
        ZeroMemory(&wc,sizeof(wc));                             //Обнуление всех членов структуры wc
        wc.hInstance= hInstance;                                       // Дескриптор приложения
        wc.lpszClassName=szWinName;                           // Имя класса окна
        wc.lpfnWndProc=WindowFuncEllipse;                           // Определение оконной функции
        wc.style=0;                                                            // Стиль по умолчанию
        wc.hIcon=LoadIcon(NULL,IDI_APPLICATION);           //Стандартная пиктограмма
        wc.hCursor=LoadCursor(NULL,IDC_ARROW);              //Стандартный курсор мыши
        wc.hbrBackground=GetStockBrush(BLACK_BRUSH);         // Белый фон окна
        wc.lpszMenuName=NULL;                                  // Без меню
        wc.cbClsExtra=0;                                                  // Без дополнительной информации
        wc.cbWndExtra=0;                                                // Без дополнительной информации
        /*Регистрация класса главного окна*/
        if(!RegisterClass (&wc))                                         //Если класс окна не регистрируется
        {                                    // выводим сообщение и заканчиваем выполнение программы
        MessageBox (NULL,"don't reg","Error",MB_OK);
        return 1;}                                                           // возвращаем код ошибки
        /*Создание главного окна и отображение его на мониторе*/
        HWND hwnd = CreateWindow (                           //Вызов функции API для создания ок-на
        szWinName,                                             // имя класса главного окна
                        szTitle,                                                       // заголовок окна
                        WS_OVERLAPPEDWINDOW,               // Стиль окна
                        100,                                                            // x-координата левого угла окна
                        100,                                                            // y-координата левого угла окна
                        500,                                                            // Ширина окна
                        500,                                                            // Высота окна
                        HWND_DESKTOP,                                  // Без родительского окна
                        NULL,                                                       // Без меню
                        hInstance,                                                  // Дескриптор приложения
                        NULL);                                                     // Без дополнительных аргументов
        ShowWindow (hwnd, SW_SHOWNORMAL);       //  Вызов функции API
       
                                            // для отображения окна
        /*Организация цикла обнаружения сообщений*/
        while(GetMessage(&msg,NULL,0,0))               // Если есть сообщение, передать его
                    // нашему приложению
        DispatchMessage(&msg);
                                //и вызвать оконную функцию WindowFunc
        
        return 0;                                                     //После выхода из цикла вернуться в Windows
        }
        int  WINAPI WinMainCircle(  HINSTANCE hInstance, HINSTANCE hPrevInst,LPSTR lpszArgs, int nWinMode) 
        {
        char szWinName[ ]="CIRC";      //Произвольное имя класса главного окна
        char szTitle[ ]="Circle";               //Произвольный заголовок окна
        MSG msg;                    //Структура msg типа MSG для получения сообщений Windows
        WNDCLASS CIRC;                                  //Структура wc типа WNDCLASS для задания
                                    //характеристик окна
        /*Заполнение структуры wc типа WNDCLASS для описания класса главного окна*/
        ZeroMemory(&CIRC,sizeof(CIRC));                             //Обнуление всех членов структуры wc
        CIRC.hInstance= hInstance;                                       // Дескриптор приложения
        CIRC.lpszClassName=szWinName;                           // Имя класса окна
        CIRC.lpfnWndProc=WindowFuncSquaCircle;                           // Определение оконной функции
        CIRC.style=0;                                                            // Стиль по умолчанию
        CIRC.hIcon=LoadIcon(NULL,IDI_APPLICATION);           //Стандартная пиктограмма
        CIRC.hCursor=LoadCursor(NULL,IDC_ARROW);              //Стандартный курсор мыши
        CIRC.hbrBackground=GetStockBrush(BLACK_BRUSH);         // Белый фон окна
        CIRC.lpszMenuName=NULL;                                  // Без меню
        CIRC.cbClsExtra=0;                                                  // Без дополнительной информации
        CIRC.cbWndExtra=0;                                                // Без дополнительной информации
        /*Регистрация класса главного окна*/
        if(!RegisterClass (&CIRC))                                         //Если класс окна не регистрируется
        {                                    // выводим сообщение и заканчиваем выполнение программы
        MessageBox (NULL,"don't reg","Error",MB_OK);
        return 1;}                                                           // возвращаем код ошибки
        /*Создание главного окна и отображение его на мониторе*/
        HWND hwnd = CreateWindow (                           //Вызов функции API для создания ок-на
        szWinName,                                             // имя класса главного окна
                        szTitle,                                                       // заголовок окна
                        WS_OVERLAPPEDWINDOW,               // Стиль окна
                        100,                                                            // x-координата левого угла окна
                        100,                                                            // y-координата левого угла окна
                        500,                                                            // Ширина окна
                        500,                                                            // Высота окна
                        HWND_DESKTOP,                                  // Без родительского окна
                        NULL,                                                       // Без меню
                        hInstance,                                                  // Дескриптор приложения
                        NULL);                                                     // Без дополнительных аргументов
        ShowWindow (hwnd, SW_SHOWNORMAL);       //  Вызов функции API
       
                                            // для отображения окна
        /*Организация цикла обнаружения сообщений*/
        while(GetMessage(&msg,NULL,0,0))               // Если есть сообщение, передать его
                    // нашему приложению
        DispatchMessage(&msg);
                                //и вызвать оконную функцию WindowFunc
        
        return 0;                                                     //После выхода из цикла вернуться в Windows
        }
        int  WINAPI WinMainREC(  HINSTANCE hInstance, HINSTANCE hPrevInst,LPSTR lpszArgs, int nWinMode) 
        {
        char szWinName[ ]="REC";      //Произвольное имя класса главного окна
        char szTitle[ ]="rectangle";               //Произвольный заголовок окна
        MSG msg;                    //Структура msg типа MSG для получения сообщений Windows
        WNDCLASS REC;                                  //Структура wc типа WNDCLASS для задания
                                    //характеристик окна
        /*Заполнение структуры wc типа WNDCLASS для описания класса главного окна*/
        ZeroMemory(&REC,sizeof(REC));                             //Обнуление всех членов структуры wc
        REC.hInstance= hInstance;                                       // Дескриптор приложения
        REC.lpszClassName=szWinName;                           // Имя класса окна
        REC.lpfnWndProc=WindowFuncSquaRectangle;                           // Определение оконной функции
        REC.style=0;                                                            // Стиль по умолчанию
        REC.hIcon=LoadIcon(NULL,IDI_APPLICATION);           //Стандартная пиктограмма
        REC.hCursor=LoadCursor(NULL,IDC_ARROW);              //Стандартный курсор мыши
        REC.hbrBackground=GetStockBrush(BLACK_BRUSH);         // Белый фон окна
        REC.lpszMenuName=NULL;                                  // Без меню
        REC.cbClsExtra=0;                                                  // Без дополнительной информации
        REC.cbWndExtra=0;                                                // Без дополнительной информации
        /*Регистрация класса главного окна*/
        if(!RegisterClass (&REC))                                         //Если класс окна не регистрируется
        {                                    // выводим сообщение и заканчиваем выполнение программы
        MessageBox (NULL,"don't reg","Error",MB_OK);
        return 1;}                                                           // возвращаем код ошибки
        /*Создание главного окна и отображение его на мониторе*/
        HWND hwnd = CreateWindow (                           //Вызов функции API для создания ок-на
        szWinName,                                             // имя класса главного окна
                        szTitle,                                                       // заголовок окна
                        WS_OVERLAPPEDWINDOW,               // Стиль окна
                        100,                                                            // x-координата левого угла окна
                        100,                                                            // y-координата левого угла окна
                        500,                                                            // Ширина окна
                        500,                                                            // Высота окна
                        HWND_DESKTOP,                                  // Без родительского окна
                        NULL,                                                       // Без меню
                        hInstance,                                                  // Дескриптор приложения
                        NULL);                                                     // Без дополнительных аргументов
        ShowWindow (hwnd, SW_SHOWNORMAL);       //  Вызов функции API
       
                                            // для отображения окна
        /*Организация цикла обнаружения сообщений*/
        while(GetMessage(&msg,NULL,0,0))               // Если есть сообщение, передать его
                    // нашему приложению
        DispatchMessage(&msg);
                                //и вызвать оконную функцию WindowFunc
        
        return 0;                                                     //После выхода из цикла вернуться в Windows
        }
        int  WINAPI WinMainSQ(  HINSTANCE hInstance, HINSTANCE hPrevInst,LPSTR lpszArgs, int nWinMode) 
        {
        char szWinName[ ]="SQ";      //Произвольное имя класса главного окна
        char szTitle[ ]="sqare";               //Произвольный заголовок окна
        MSG msg;                    //Структура msg типа MSG для получения сообщений Windows
        WNDCLASS SQ;                                  //Структура wc типа WNDCLASS для задания
                                    //характеристик окна
        /*Заполнение структуры wc типа WNDCLASS для описания класса главного окна*/
        ZeroMemory(&SQ,sizeof(SQ));                             //Обнуление всех членов структуры wc
        SQ.hInstance= hInstance;                                       // Дескриптор приложения
        SQ.lpszClassName=szWinName;                           // Имя класса окна
        SQ.lpfnWndProc=WindowFuncSquare;                           // Определение оконной функции
        SQ.style=0;                                                            // Стиль по умолчанию
        SQ.hIcon=LoadIcon(NULL,IDI_APPLICATION);           //Стандартная пиктограмма
        SQ.hCursor=LoadCursor(NULL,IDC_ARROW);              //Стандартный курсор мыши
        SQ.hbrBackground=GetStockBrush(BLACK_BRUSH);         // Белый фон окна
        SQ.lpszMenuName=NULL;                                  // Без меню
        SQ.cbClsExtra=0;                                                  // Без дополнительной информации
        SQ.cbWndExtra=0;                                                // Без дополнительной информации
        /*Регистрация класса главного окна*/
        if(!RegisterClass (&SQ))                                         //Если класс окна не регистрируется
        {                                    // выводим сообщение и заканчиваем выполнение программы
        MessageBox (NULL,"don't reg","Error",MB_OK);
        return 1;}                                                           // возвращаем код ошибки
        /*Создание главного окна и отображение его на мониторе*/
        HWND hwnd = CreateWindow (                           //Вызов функции API для создания ок-на
        szWinName,                                             // имя класса главного окна
                        szTitle,                                                       // заголовок окна
                        WS_OVERLAPPEDWINDOW,               // Стиль окна
                        100,                                                            // x-координата левого угла окна
                        100,                                                            // y-координата левого угла окна
                        500,                                                            // Ширина окна
                        500,                                                            // Высота окна
                        HWND_DESKTOP,                                  // Без родительского окна
                        NULL,                                                       // Без меню
                        hInstance,                                                  // Дескриптор приложения
                        NULL);                                                     // Без дополнительных аргументов
        ShowWindow (hwnd, SW_SHOWNORMAL);       //  Вызов функции API
       
                                            // для отображения окна
        /*Организация цикла обнаружения сообщений*/
        while(GetMessage(&msg,NULL,0,0))               // Если есть сообщение, передать его
                    // нашему приложению
        DispatchMessage(&msg);
                                //и вызвать оконную функцию WindowFunc
        
        return 0;                                                     //После выхода из цикла вернуться в Windows
        }
        int  WINAPI WinMainTriangle(  HINSTANCE hInstance, HINSTANCE hPrevInst,LPSTR lpszArgs, int nWinMode) 
        {
        char szWinName[ ]="TR";      //Произвольное имя класса главного окна
        char szTitle[ ]="Triangle";               //Произвольный заголовок окна
        MSG msg;                    //Структура msg типа MSG для получения сообщений Windows
        WNDCLASS TR;                                  //Структура wc типа WNDCLASS для задания
                                    //характеристик окна
        /*Заполнение структуры wc типа WNDCLASS для описания класса главного окна*/
        ZeroMemory(&TR,sizeof(TR));                             //Обнуление всех членов структуры wc
        TR.hInstance= hInstance;                                       // Дескриптор приложения
        TR.lpszClassName=szWinName;                           // Имя класса окна
        TR.lpfnWndProc=WindowFuncTriangle;                           // Определение оконной функции
        TR.style=0;                                                            // Стиль по умолчанию
        TR.hIcon=LoadIcon(NULL,IDI_APPLICATION);           //Стандартная пиктограмма
        TR.hCursor=LoadCursor(NULL,IDC_ARROW);              //Стандартный курсор мыши
        TR.hbrBackground=GetStockBrush(BLACK_BRUSH);         // Белый фон окна
        TR.lpszMenuName=NULL;                                  // Без меню
        TR.cbClsExtra=0;                                                  // Без дополнительной информации
        TR.cbWndExtra=0;                                                // Без дополнительной информации
        /*Регистрация класса главного окна*/
        if(!RegisterClass (&TR))                                         //Если класс окна не регистрируется
        {                                    // выводим сообщение и заканчиваем выполнение программы
        MessageBox (NULL,"don't reg","Error",MB_OK);
        return 1;}                                                           // возвращаем код ошибки
        /*Создание главного окна и отображение его на мониторе*/
        HWND hwnd = CreateWindow (                           //Вызов функции API для создания ок-на
        szWinName,                                             // имя класса главного окна
                        szTitle,                                                       // заголовок окна
                        WS_OVERLAPPEDWINDOW,               // Стиль окна
                        100,                                                            // x-координата левого угла окна
                        100,                                                            // y-координата левого угла окна
                        500,                                                            // Ширина окна
                        500,                                                            // Высота окна
                        HWND_DESKTOP,                                  // Без родительского окна
                        NULL,                                                       // Без меню
                        hInstance,                                                  // Дескриптор приложения
                        NULL);                                                     // Без дополнительных аргументов
        ShowWindow (hwnd, SW_SHOWNORMAL);       //  Вызов функции API
       
                                            // для отображения окна
        /*Организация цикла обнаружения сообщений*/
        while(GetMessage(&msg,NULL,0,0))               // Если есть сообщение, передать его
                    // нашему приложению
        DispatchMessage(&msg);
                                //и вызвать оконную функцию WindowFunc
        
        return 0;                                                     //После выхода из цикла вернуться в Windows
        }
};



class eleps : public exemple
{
    protected:
    double A;
    double B;
    public:
    eleps(double ae, double be):exemple()
    {
        if ((ae>=0)&&(be>=0))
        {
            A=ae;
            B=be;
            
        }
       else throw Exc("eleps error");
    }
    double area()
    {
        return (A*B*PI);
    }
    void draw()
    {  
        AE=A;
        BE=B;
        WinMainEllipse(hInstance,  hPrevInst, lpszArgs,  nWinMode);
    }
    void move()
    {

    }
};
class circle : public eleps
{
private:
    double R;
    public:
    circle(double r):eleps(A, B)
    {
        if (r>0)
        {
            R=r;
            A=r;
            B=r;
        }
       else throw Exc("circle error");
    }
    
    double area()
    {
        return (PI*R*R);
    }

    void draw()
    {
        ACI=R;
        BCI=R;
        WinMainCircle(hInstance,  hPrevInst, lpszArgs,  nWinMode);
    }
    void move()
    {

    }

};

class triangle : public exemple
{
    private:
    double A;
    double H;
    public:
    triangle(double a, double h):exemple()
    {
        if ((a>0)&&(h>0))
        {
            A=a;
            H=h;
        }
       else throw Exc("triangle error");
    }
    double area()
    {
        return (0.5*A*H);
    }
        void draw()
    {
        AT=A;
        HT=H;
        WinMainTriangle(hInstance,  hPrevInst, lpszArgs,  nWinMode);
    }
    void move()
    {

    }
};

class rectangle : public exemple
{
    protected:
    double A;
    double B;
    public:
    rectangle(double a, double b):exemple()
    {
        if ((a>=0)&&(b>=0))
        {
            A=a;
            B=b;
        }
       else throw Exc("rectangle error");
    }
    
    double area()
    {
        return (A*B);
    }
     
    void draw()
    {
        AR=A;
        BR=B;
        WinMainREC(hInstance,  hPrevInst, lpszArgs,  nWinMode);
    }
    void move()
    {

    }
};

class square : public rectangle
{
    private:
    public:
    square(double a):rectangle(A,B)
    {
        if (a>0)
        {
            A=a;
            B=a;
        }
    }
    double area()
    {
        return (A*A);
    }
     
    void draw()
    {
        AS=B;
        BS=B;
        WinMainSQ(hInstance,  hPrevInst, lpszArgs,  nWinMode);
    }
    void move()
    {

    }
};

class run
{
    public:
    void runmain()
    {
        double a,b,r,h,base, ae, be, S, heightc,heightt,heightr,heights,heighte;
        
        try
        {
        cout<<endl<<"enter radius for circle(r)->";
        cin>>r;
        cout<<"enter the height of the circle for the volume->";
        cin>>heightc;

        cout<<endl<<"enter height for triangle(h)->";
        cin>>h;
        cout<<endl<<"endter base of triangle(base)->";
        cin>>base;
        cout<<"enter the height of the triangle for the volume->";
        cin>>heightt;

        cout<<endl<<"enter a,b sides of the rectangle(side a will be used for the square) a->";
        cin>>a; cout<<"b->"; cin>>b;
        cout<<"enter the height of the square for the volume->";
        cin>>heights;
        cout<<"enter the height of the rectangle for the volume->";
        cin>>heightr;

        cout<<endl<<"endter a and b for eleps a->";
        cin>>ae; cout<<"b->"; cin>>be;
        cout<<"enter the height of the eleps for the volume->";
        cin>>heighte;

        eleps* x=new eleps(ae,be);
        circle* c=new circle(r);
        triangle* v=new triangle(base,h);
        rectangle* n=new rectangle(a,b);
        square* z=new square(a);

        cylinder<eleps> EL=cylinder(x,heighte);
        cylinder<circle> CI=cylinder(c,heightr);
        cylinder<triangle> TR=cylinder(v,heightt);
        cylinder<rectangle> RE=cylinder(n,heightr);
        cylinder<square> SQ=cylinder(z,heightr);

        S=c->area();
        cout<<endl<<"circle S ="<<S<<endl;
        CI.volume();
        c->draw();
        
        S=v->area();
        cout<<endl<<"triangle S ="<<S<<endl;
        TR.volume();
        v->draw();
        
        S=n->area();
        cout<<endl<<"rectangle S ="<<S<<endl;
        RE.volume();
        n->draw();

        S=z->area();
        cout<<endl<<"square S ="<<S<<endl;
        SQ.volume();
        z->draw();
        
        S=x->area();
        cout<<endl<<"eleps S ="<<S<<endl;
        EL.volume();
        x->draw();
        }

        catch(Exc exc) 
        {
			exc.show();
		}
        catch (...) 
        {
			cout << "Some unknown error" << endl;
		}
    }
};


int main()
{
    run l;
    l.runmain();
    system("pause");

    return 0;
}  

LRESULT CALLBACK WindowFuncEllipse(HWND hwnd, UINT message,WPARAM wParam, LPARAM lParam)  
{
                                 // выбор по значению сообщения (message)
    switch(message) 
    {            
        case WM_DESTROY:                           //При завершении приложения пользователем
        PostQuitMessage (0);                           //вызвать функцию API завершения приложения
        break;
        case WM_PAINT:
        {
        HDC hdc = GetDC(hwnd);
        Ellipse(hdc,AE,BE,1,1);
        ReleaseDC(hwnd, hdc);
        }
        break;
        default:                                    // Все сообщения, не обрабатываемые данной функцией,
                                                    // направляются на обработку по умолчанию
        return DefWindowProc (hwnd,message,wParam,lParam);
    }                                                           //Конец оператора switch
}
LRESULT CALLBACK WindowFuncSquaCircle(HWND hwnd, UINT message,WPARAM wParam, LPARAM lParam)  
{  
                                 // выбор по значению сообщения (message)
    switch(message) 
    {            
        case WM_DESTROY:                           //При завершении приложения пользователем
        PostQuitMessage (0);                           //вызвать функцию API завершения приложения
        break;
        case WM_PAINT:
        {
        HDC hdc = GetDC(hwnd);
        Ellipse(hdc,ACI,BCI,1,1);
        ReleaseDC(hwnd, hdc);
        }
        break;
        default:                                    // Все сообщения, не обрабатываемые данной функцией,
                                                    // направляются на обработку по умолчанию
        return DefWindowProc (hwnd,message,wParam,lParam);
    }                                                           //Конец оператора switch
}
LRESULT CALLBACK WindowFuncSquaRectangle(HWND hwnd, UINT message,WPARAM wParam, LPARAM lParam)  
{  
                                 // выбор по значению сообщения (message)
    switch(message) 
    {            
        case WM_DESTROY:                           //При завершении приложения пользователем
        PostQuitMessage (0);                           //вызвать функцию API завершения приложения
        break;
        case WM_PAINT:
        {
        HDC hdc = GetDC(hwnd);
        Rectangle(hdc,AR,BR,1,1);
        ReleaseDC(hwnd, hdc);
        }
        break;
        default:                                    // Все сообщения, не обрабатываемые данной функцией,
                                                    // направляются на обработку по умолчанию
        return DefWindowProc (hwnd,message,wParam,lParam);
    }                                                           //Конец оператора switch
}
LRESULT CALLBACK WindowFuncSquare(HWND hwnd, UINT message,WPARAM wParam, LPARAM lParam)  
{
    // выбор по значению сообщения (message)
    switch(message) 
    {            
        case WM_DESTROY:                           //При завершении приложения пользователем
        PostQuitMessage (0);                           //вызвать функцию API завершения приложения
        break;
        case WM_PAINT:
        {
        HDC hdc = GetDC(hwnd);
        Rectangle(hdc,AS,BS,1,1);
        ReleaseDC(hwnd, hdc);
        }
        break;
        default:                                    // Все сообщения, не обрабатываемые данной функцией,
                                                    // направляются на обработку по умолчанию
        return DefWindowProc (hwnd,message,wParam,lParam);
    }                                                           //Конец оператора switch
}
LRESULT CALLBACK WindowFuncTriangle(HWND hwnd, UINT message,WPARAM wParam, LPARAM lParam)  
{
                                 // выбор по значению сообщения (message)
    switch(message) 
    {            
    PAINTSTRUCT ps; 
    LOGBRUSH lb; 
    RECT rc; 
    HDC hdc; 
    HPEN hPen;
    HGDIOBJ  hPenOld; 

        case WM_DESTROY:                           //При завершении приложения пользователем
        PostQuitMessage (0);                           //вызвать функцию API завершения приложения
        break;
        case WM_PAINT:
        {
        GetClientRect(hwnd, &rc);
        lb.lbStyle = BS_SOLID; 
        lb.lbColor = RGB(255,0,0); 
        lb.lbHatch = 0;
        hdc = BeginPaint(hwnd, &ps);
        hPen = ExtCreatePen(PS_COSMETIC | PS_SOLID, 1, &lb, 0, NULL);
        hPenOld = SelectObject(hdc, hPen);
        LineTo(hdc,1,1);
        LineTo(hdc,AT,1);
        LineTo(hdc,AT*0.5,HT);
        LineTo(hdc,1,1);
        DeleteObject(hPen); 
        ReleaseDC(hwnd, hdc);
        EndPaint(hwnd, &ps);
        }
        break;
        default:                                    // Все сообщения, не обрабатываемые данной функцией,
                                                    // направляются на обработку по умолчанию
        return DefWindowProc (hwnd,message,wParam,lParam);
    }                                                           //Конец оператора switch
}