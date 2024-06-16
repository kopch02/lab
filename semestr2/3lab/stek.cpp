#include <iostream>
#include <string>
#include <fstream>
using namespace std;

struct flower
{
    string color;
    string rarity;
    int petal;
    double price;
    void Out();

};
void flower::Out()
{
    cout<<endl;
    cout << "color=" << color << endl;
    cout << "rarity=" << rarity << endl;
    cout << "petal=" << petal << endl;
    cout << "price=" << price << endl;
    
}
void readfile(string &a,string &b,int &c,double &d,int num)
{
    
    ifstream f;
    f.open("file.txt");
    if (!f) {
        cout << "ERROR! No file" << endl;
        return;
    }
    int i=0;
    do
    {
    f>>a;
    f>>b;
    f>>c;
    f>>d;
    i++;
    }while (i<num);
   f.close();
}

struct mystack
{
    struct node { flower data; node* prev; };
    node* top = NULL; //все новые элементы стека будут пустыми
    int count; //отвечает за количетво элементов в стеке
    bool push(flower);//добовление в стек
    bool pop(flower&);//удаление из стека
    void info();
};


int main()
{
    string a,b;
    int c;
    double d;
    int x;
    flower k;
    flower r;
    mystack s;
    mystack s1;
    int n=3;
    n++;
    int t=0;
    int acount=1;
    do
    {
    cout<<"x=0 -- Exit the program" <<endl<<"x=1 -- enter one product";
    cout<<endl<<"x=2 -- product will be entered from the file"<<endl<<"x=3 -- info for stek";
    cout<<endl<<"x=4 -- delete top element"<<endl<<"x=5 -- delete stek";
    cout<<endl<<"x=6 -- Select an element to remove";
    cout<<endl<<"enter x = ";
    cin>>x;
    switch (x)
    {
    case 1:
        cout<<endl<<"Enter color = ";
        cin>>k.color;
        cout<<endl<<"Enter the rarity = ";
        cin>>k.rarity;
        cout<<endl<<"enter the petal = ";
        cin>> k.petal;
        cout<<endl<<"enter the price = ";
        cin>>k.price;
        s.info();
        s.push(k);
        s.info();
        acount++;
        break;
    case 2:
    for(int i=1;i<n;i++)
    {
    readfile(a,b,c,d,i);
    flower ki = { a,b,c,d };
    s.push(ki);
    }
    s.info();
    acount+=3;
    break;
    case 3:
    for(int i=1;i<acount;i++)
    {
    s.pop(k);
    s1.push(k);
    k.Out();
    }
    for(int i=1;i<acount;i++)
    {
    s1.pop(k);
    s.push(k);
    }
    s.info();
    break;
    case 4:
    s.pop(k);
    s.info();
    acount--;
    case 5:
    if(acount==1)
    {
        s.info();
    }
    for(int i=0;i<=acount;i++)
    {
        s.pop(k);
        acount--;
    }
    break;
    case 6:
        
        cout<<endl<<"Enter color = ";
        cin>>r.color;
        cout<<endl<<"Enter the source = ";
        cin>>r.rarity;
        cout<<endl<<"enter the petal = ";
        cin>> r.petal;
        cout<<endl<<"enter the price = ";
        cin>>r.price;
        t=0;
    for(int i=1;i<acount;i++)
    {
        

        s.pop(k);
        if((r.color==k.color)&&(r.petal==k.petal)&&(r.price==k.price)&&(r.rarity==k.rarity) )
        {
            acount--;
         for(int i=1;i<=t;i++)
           {
            s1.pop(k);
            s.push(k);
           }
           
           break;
        }
        else
        {
        t++;
        s1.push(k);
        }
        if(t+1==acount)
        {
            for(int i=1;i<=t;i++)
           {
            s1.pop(k);
            s.push(k);
           }
        }
       
    }
    default:
        break;
    }
    } while (x != 0);
    return 0;
}

bool mystack::push(flower data)
{
    if (!top)
    {
        top = new node;
        top->prev = NULL;
        count = 1;
    }
    else
    {
        node* temp;
        temp = new node;
        temp->prev = top;
        top = temp;
        count++;
    }
    top->data = data;
    return true;
}
bool mystack::pop(flower& data)
{
    if (!top) return false;

    node* temp = top->prev;
    data = top->data;
    delete top;
    top = temp;
    count--;
    return true;
}
void mystack::info()
{
    if (!top)
        cout << "--->stack is empty" << endl;
    else
    {
        cout << endl << "stack info: " << endl;
        cout << "\tstack size = " << count << endl;
       // cout << "\ttop data = " << top->data << endl << endl;
        top->data.Out();
    }
}
