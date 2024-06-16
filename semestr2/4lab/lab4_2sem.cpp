#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;
struct product//ball
{
    string color;
    double diameter;
    int strip;
    double speed;
};

struct node { int n; char* data; node* next; };

struct myqueue
{
    node* first = NULL;
    int count = 0;
    double fullprice = 0, plusmoney = 0;//цена и прибыль
    int fullquantity = 0;
    bool push(char*, int);
    bool pop(char*&, int&);
    void info();

};
bool myqueue::push(char* data, int n)
{
    if (!first)
    {
        first = new node;
        first->next = NULL;
       // first->data = data;
        count = 1;
        first->n = n;
        first->data = new char[n];
        for (int i = 0;i < n;i++) {
            first->data[i] = data[i];
        }
    }
    else
    {
        node* temp;
        temp = first;
        while (temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = new node;
        temp->next->data = new char[n];

        temp->next->next = NULL;
        temp->next->n = n;
        for (int i = 0;i < n;i++) {
            temp->next->data[i] = data[i];

        }
        count++;
      
    }
    return true;
}
bool myqueue::pop(char*& data, int &n)
{
    if (!first) return false;
    node* temp = first->next;
    n = first->n;
    for (int i = 0;i < n;i++)
    {
        data[i] = first->data[i];

    }
    delete first->data;
    delete first;
    first = temp;
    count--;
    return true;
}
void myqueue::info()
{
    if (!first)
    {
        cout << "--->queue is empty" << endl;
    }
    else
    {
        cout << endl << "queue info: " << endl;
        cout << "\tQueue size = " << count << endl;
    }
}
void GetSeria(char*& data, int& n, product a)
{
    size_t s = a.color.size();

    int n0 = sizeof(size_t);
    int n1 = s;
    int n2 = sizeof(double);
    int n3 = sizeof(int);
    int n4 = n2;

    n = n0 + n1 + n2 + n3 + n4;

    data = new char[n];

    char* d0 = reinterpret_cast<char*>(&s);
    char* d1 = const_cast<char*>(a.color.c_str());
    char* d2 = reinterpret_cast<char*>(&a.diameter);
    char* d3 = reinterpret_cast<char*>(&a.strip);
    char* d4 = reinterpret_cast<char*>(&a.speed);

    for (int i = 0;i < n0;i++) data[i] = d0[i];
    for (int i = 0;i < n1;i++) data[i+n0] = d1[i];
    for (int i = 0;i < n2;i++) data[i+n0+n1] = d2[i];
    for (int i = 0;i < n3;i++) data[i+n0+n1+n2] = d3[i];
    for (int i = 0;i < n4;i++) data[i+n0+n1+n2+n3] = d4[i];

}
void GetDeSeria(char* data, int n, product& riga)
{
    int n0, n1, n2, n3, n4;
    n0 = sizeof(size_t);
    n2 = sizeof(double);
    n3 = sizeof(int);
    n4 = sizeof(double);

    size_t p = *reinterpret_cast<size_t*>(data);
    n1 = p;

    string ss(data + n0, p);
    riga.color = ss;
    riga.diameter = *reinterpret_cast<double*>(data + n0 + n1);
    riga.strip = *reinterpret_cast<int*>(data + n0 + n1 + n2);
    riga.speed = *reinterpret_cast<double*>(data + n0 + n1 + n2 + n3);
}
void show(product b)
{
    cout << "ball:";
    cout << "\t color:" << b.color
        << "\t diameter:" << b.diameter
        << "\t strip:" << b.strip
        << "\t speed:" << b.speed << endl;

}
int enteredfile()
{
    product riga = { "red",1, 1, 1 };
    
    const char* file = "C:/Users/iskan/Desktop/ycheba/lab/2semestr/4lab/file.dat";
    ofstream out(file, ios::binary);         //Ставим режим "бинарный файл"
    out.write((char*)&riga.color, sizeof(riga.color));           
    out.write((char*)&riga.diameter, sizeof(riga.diameter));        
    out.write((char*)&riga.speed, sizeof(riga.speed));            
    out.write((char*)&riga.strip, sizeof(riga.strip));   

    product riga1 = { "green",7, 1, 67 };

    out.write((char*)&riga1.color, sizeof(riga1.color));           
    out.write((char*)&riga1.diameter, sizeof(riga1.diameter));        
    out.write((char*)&riga1.speed, sizeof(riga1.speed));            
    out.write((char*)&riga1.strip, sizeof(riga1.strip)); 

    product riga2 = { "yellow",3, 10, 99 };

    out.write((char*)&riga2.color, sizeof(riga2.color));           
    out.write((char*)&riga2.diameter, sizeof(riga2.diameter));        
    out.write((char*)&riga2.speed, sizeof(riga2.speed));            
    out.write((char*)&riga2.strip, sizeof(riga2.strip));  
    out.close();
    return 0;
}
/*bool In(myqueue &q)
{
    fstream file("file.dat", ios::in | ios::binary);
    if (!file) {
        cout << "Error! file not found" << endl;
        return false;
    }
    int i = 1, n;
    product c;
    while (!file.eof()) {
        if (file.read((char*)&n, sizeof(int))) {
            cout << "\t - " << i << " - " << "seria length: " << n << endl;
            char* data = new char[n];
            file.read(data, n);
            i++;
            //GetDeSeria(data, n, c);
            //delete[]data;
            //GetSeria(data, n, c);
            q.push(data, n);
            delete[]data;
        }
        file.close();
        return true;
    }
}*/
int main()
{
    product riga, latvia;
    myqueue q;
    bool metka = false;
    char *data;
    q.info();
    int n = 0, x;
    do
    {
        cout<<"x=1 - add element"<<endl;
        cout<<"x=2 - delete element"<<endl;
        cout<<"x=3 - delete all"<<endl;
        cout<<"x=4 - info"<<endl;
        cout<<"x=";
        cin>>x;
        switch(x)
        {
            case 1:
            cout << "Enter product data:" << endl;
            cout << "color - "; cin >> riga.color;
            cout << "diameter - "; cin >> riga.diameter;
            cout << "speed - "; cin >> riga.speed;
            cout << "strip - "; cin >> riga.strip;
            GetSeria(data, n, riga);
            q.push(data, n);
            break;
            case 2:
            {
            cout << "Enter product data:" << endl;
            cout << "color - "; cin >> latvia.color;
            cout << "diameter - "; cin >> latvia.diameter;
            cout << "speed - "; cin >> latvia.speed;
            cout << "strip - "; cin >> latvia.strip;
            for(int i=0;i<q.count;i++)
            {
                q.pop(data,n);
                GetDeSeria(data, n, riga);

                if(riga.color!=latvia.color || riga.diameter!=latvia.diameter || riga.speed!=latvia.speed || riga.strip!=latvia.strip)
                {
                    GetSeria(data,n,riga);
                    q.push(data,n);                   
                }
                else
                {
                    metka=true;
                    break;
                }
                
            }
            if(!metka)
            {
                cout<<"There is no such element"<<endl;
            }
            break;
        }
            case 3:
            while(q.count)
            {
            q.pop(data, n);
            GetDeSeria(data,n, riga);
            show(riga);
            }
            break;
            case 4:
            q.info();
            break;
            default:
            break;
        }
    }while (x!=0);
     while (q.count) 
     {
        q.pop(data, n);
        delete[]data;
     }
    return 0;
}