#include <iostream>
#include <string>
#include <fstream>
using namespace std;


void readfile()
{
    string a;
    double b;
    ifstream f;
    f.open("file.txt");
    if (!f) {
        cout << "ERROR! No file" << endl;
        return;
    }
    while (f >> a >> b)
    {
        cout << a << " " << b << endl;

    }
    f.close();
}
struct product
{
    int quantity;//количество
    double price;//Цена
    void out();
};
void product::out()
{
    cout<<"quantity="<<quantity<<" "<<"price="<<price<<endl;
}
struct node { product data; node* next; };
struct myqueue
{
    
    node* first = NULL;
    int count = 0, rest=0;//rest-остаток товара на складе в штуках
    double money=0;//прибыль
    double fullprice=0;
    bool push(product);
    bool pop(product&);
    void info();

};
bool myqueue::push(product data)
{
    if (!first)
    {
        first = new node;
        first->next = NULL;
        first->data = data;
        count = 1;
        rest=first->data.quantity;
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
        temp->next->data = data;
        temp->next->next = NULL;
        count++;
        fullprice += data.price * data.quantity;
        rest += data.quantity;
    }
    return true;
}
bool myqueue::pop(product& data)
{
    if (!first) return false;
    node* temp = first->next;
    data = first->data;
    delete first;
    first =temp;
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
        cout<< "\trest = "<<rest<<endl;
        cout<< "\tmoney = "<<money<<endl;
        cout << "\tQueue size = " << count << endl;
        first->data.out();
        //cout << "\tfirst data = " << first->data << endl << endl;
    }
}
int main()
{
    int n = 10;
    product k;
    product r;
    myqueue q;
    int x;

    do
    {
    cout<<"1-Add item to queue"<<endl;
    cout<<"2-Clear Queu"<<endl;
    cout<<"3-report"<<endl;
    cout<<"4-Sell goods"<<endl<<"x=";
    cin>>x;
    
    switch (x)
    {
    case 1:
        cout<<"Enter the number=";
        cin>>k.quantity;
        cout<<"enter price=";
        cin>>k.price;
        q.push(k);
        q.info();
        break;
    case 2:
    q.rest = 0;
    while (q.count) q.pop(k);
    break;
    case 3:
    q.info();
    cout << "fullquantity:" << q.rest << endl;
    cout << "fullprice:" << q.fullprice << endl;
    cout << "PLUSmoney:" << q.money << endl;
    break;
    case 4:
    cout << "Enter data:" << endl;
            k = q.first->data;

                cout << "quantity=";cin >> r.quantity;
                cout << "price=";cin >> r.price;

                if (r.quantity > q.rest || r.price < k.price) {
                  

                    cout << "There are not enough items or selected price is too low!" << endl;
                    break;
                }
                else{

                    q.rest -= r.quantity;

                        while (r.quantity) {
                            if (r.quantity < k.quantity || r.quantity == k.quantity) {
                                q.money += r.quantity * (r.price - k.price);
                                q.fullprice -= k.price * r.quantity;
                                k.quantity -= r.quantity;
                                r.quantity = 0;
                                q.first->data.quantity = k.quantity;

                            }
                            else {
                                q.money += k.quantity * (r.price - k.price);
                                q.fullprice -= k.price * k.quantity;
                                r.quantity -= k.quantity;
                                k.quantity = 0;

                            }
                            if (k.quantity == 0) 
                            {
                                q.pop(k);
                                if(q.count!=0)
                                k = q.first->data;
                            }
                        }
                    
            }
            break;
    default:
        break;
    }
    }while (x!=0);
    q.rest = 0;
    while (q.count) q.pop(k);
    return 0;
}
