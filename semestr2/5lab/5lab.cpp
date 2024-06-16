#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

struct Apple
{
    double diameter;
    double weight;
    string color;
    string name;
};
struct DLList
{
    
    struct Node
    {
        Apple data;     //information
        Node* next;   //next node position
        Node* prev;   //previous node position
    };

    Node* F=NULL;     //first node
    Node* L=NULL;     //last node
    Node* C=NULL;     //current node
    int Count;        //node count

    void Out();
    void Info();
    void Clear();

    bool MoveNext();
    bool MovePrev();
    bool MoveFirst();
    bool MoveLast();

    bool Init(Apple);
    bool AddNext(Apple);
    bool AddPrev(Apple);
    bool AddFirst(Apple);
    bool AddLast(Apple);

    bool Del(Apple&);
    bool DelNext(Apple&);
    bool DelPrev(Apple&);
    bool DelFirst(Apple&);
    bool DelLast(Apple&);
};

bool DLList::MoveNext()
{
    if(!F)       return false;
    if(!C)       {C=F; return true;}
    if(C==L) return false;
    C=C->next;
    return true;
}

bool DLList::MovePrev()
{
    if(!F)       return false;
    if(!C)       {C=F; return true;}
    if(!C->prev) return false;
    C=C->prev;
    return true;
}
bool DLList::MoveFirst()
{
    if(!F) return false;
    C=F;
    return true;
}

bool DLList::MoveLast()
{
    if(!L) return false;
    C=L;
    return true;
}

bool DLList::Init(Apple data)
{
   if(!F)
   {
        F=new Node;
        L=F;
        C=F;
        F->prev=NULL;
        F->next=NULL;
        F->data = data;
        Count=1;
        return true;
   }
   else
        return false;
}

bool DLList::AddNext(Apple data)
{
	if(!F) return Init(data);

	Node* temp=C->next;
	C->next=new Node;
	C->next->next=temp;
	C->next->prev=C;

	if(!temp)
        L=C->next;
	else
        temp->prev=C->next;

    C=C->next;
    C->data=data;
    Count++;
    return true;

}

bool DLList::AddPrev(Apple data)
{
	if(!F) return Init(data);

	Node* temp=C->prev;
	C->prev=new Node;
	C->prev->next=C;
	C->prev->prev=temp;

	if(!temp)
        F=C->prev;
	else
        temp->next=C->prev;

    C=C->prev;
    C->data=data;
    Count++;
    return true;
}

bool DLList::AddFirst(Apple data)
{
    if (MoveFirst())return AddPrev(data);
    else return false;
}

bool DLList::AddLast(Apple data)
{
    if (MoveLast())return AddNext(data);
    else return false;
}

void DLList::Out()
{
    if(!F)  {
                cout<<"List is empty"<<endl;
                return;
            }

    Node* temp=F;
    cout<<"List: "<<endl;
    do
    {
        cout<<endl;
        cout<<"--------------"<<endl;
        cout<<endl;
       cout<<"diameter - "<<temp->data.diameter<<endl;
       cout<<"weight - "<<temp->data.weight<<endl;
       cout<<"color - "<<temp->data.color<<endl;
       cout<<"name - "<<temp->data.name<<endl;
        temp=temp->next;
    }
    while(temp);
    cout<<endl;
}

void DLList::Info()
{

cout<<endl;
cout<<endl;
    if(Count)
        cout<<"List node count: "<<Count<<endl;
    else
        cout<<"List is empty"<<endl;
   bool flag = true;
    if(!C)
    {
        flag=MoveFirst();
    }
    Node* temp=C;
    cout<<endl;
    if(flag==true)
    {
        cout<<"Current node data = "<<endl;
        cout<<endl;
        cout<<"diameter - "<<temp->data.diameter<<endl;
       cout<<"weight - "<<temp->data.weight<<endl;
       cout<<"color - "<<temp->data.color<<endl;
       cout<<"name - "<<temp->data.name<<endl;
        temp=temp->next;
    }
cout<<endl;
cout<<endl;

}

bool DLList::DelFirst(Apple& data)
{
    if(!F)      return false;
    if(C!=F)    MoveFirst();

    Node* temp = C->next;
    data = C->data;

    if(temp) temp->prev=NULL;
    delete C;

    C=temp;
    F=temp;
    Count--;
    if(!temp) {L=NULL; return false;}
    return true;
}

bool DLList::DelLast(Apple& data)
{
    if(!F)      return false;
    if(C!=L)    MoveLast();

    Node* temp = C->prev;
    data = C->data;

    if(temp) temp->next=NULL;
    delete C;

    C=temp;
    L=temp;
    Count--;

    if(!temp) {F=NULL; return false;}
    return true;
}

bool DLList::Del(Apple& data)
{
    if(!F) return false;
	if(!C) return false;

	if(C==F) return DelFirst(data);
    if(C==L) return DelLast(data);

    Node* temp = C->next;
	data=C->data;

	C->prev->next=C->next;
	C->next->prev=C->prev;

	delete C;
	C=temp;
	Count--;
	return true;
}

bool DLList::DelNext(Apple& data)
{
    if(!F) return false;
	if(!C) return false;
	if (MoveNext()) return Del(data);
    return false;
}
bool DLList::DelPrev(Apple& data)
{
    if(!F) return false;
	if(!C) return false;
	if (MovePrev()) return Del(data);
    return false;
}

void DLList::Clear()
{
   if(!MoveFirst())
   {
       cout<<"List is empty"<<endl;
       return;
   }
   Apple k;
   while(Del(k));
}

int main()
{
    DLList MyList;

    Apple a;
    Apple buff;

    ifstream file;
    ofstream ff;
    
    file.open("file.txt");
    for(int i=0;i<3;i++)
    {
    file>>a.diameter>>a.weight>>a.color>>a.name;
    MyList.AddNext(a);
    }
    file.close();

    int x;
    int z;
    do
    {
        cout<<"x=0 -- exit"<<endl;
        cout<<"x=1 -- add element"<<endl;
        cout<<"x=2 -- info"<<endl;
        cout<<"x=3 -- del element"<<endl;
        cout<<"x=4 -- move corrent element"<<endl;
        cout<<"x=5 -- Clear list"<<endl;
        cout<<"x=6 -- copy list for file(data.txt)"<<endl;
        cout<<"x=7 -- Sort"<<endl;
        cout<<"x=";
        cin>>x;
    switch (x)
    {
    case 1:                 //добавить элемент
    cout<<"z=1 -- add first"<<endl;
    cout<<"z=2 -- add last"<<endl;
    cout<<"z=3 -- add next"<<endl;
    cout<<"z=4 -- add prev"<<endl;
    cout<<"z=";
    cin>>z;
    switch (z)
    {
    case 1:
    cout<<endl<<"diameter-";
    cin>>a.diameter;
    cout<<endl<<"weight-";
    cin>>a.weight;
    cout<<endl<<"color-";
    cin>>a.color;
    cout<<endl<<"name-";
    cin>>a.name;
    MyList.AddFirst(a);
    break;
    case 2:
    cout<<endl<<"diameter-";
    cin>>a.diameter;
    cout<<endl<<"weight-";
    cin>>a.weight;
    cout<<endl<<"color-";
    cin>>a.color;
    cout<<endl<<"name-";
    cin>>a.name;
    MyList.AddLast(a);
    break;
    case 3:
    cout<<endl<<"diameter-";
    cin>>a.diameter;
    cout<<endl<<"weight-";
    cin>>a.weight;
    cout<<endl<<"color-";
    cin>>a.color;
    cout<<endl<<"name-";
    cin>>a.name;
    MyList.AddNext(a);
    break;
    case 4:
    cout<<endl<<"diameter-";
    cin>>a.diameter;
    cout<<endl<<"weight-";
    cin>>a.weight;
    cout<<endl<<"color-";
    cin>>a.color;
    cout<<endl<<"name-";
    cin>>a.name;
    MyList.AddPrev(a);
    break;
    default:
        break;
    }
    
    MyList.Info();
    break;
    case 2:                 //информация 
    MyList.Info();
    MyList.Out();
    break;
    case 3:                 //удалить элемент
    cout<<"z=1 -- del first"<<endl;
    cout<<"z=2 -- del last"<<endl;
    cout<<"z=3 -- del next"<<endl;
    cout<<"z=4 -- del prev"<<endl;
    cout<<"z=5 -- del current"<<endl;
    cout<<"z=";
    cin>>z;
    switch (z)
    {
    case 1:
        MyList.DelFirst(a);
        break;
    case 2:
    MyList.DelLast(a);
    break;
    case 3:
    MyList.DelNext(a);
    break;
    case 4:
    MyList.DelPrev(a);
    break;
    case 5:
    MyList.Del(a);
    default:
        break;
    }
    break;
    case 4:                 //передвигать текущий элемент
    cout<<"z=1 -- move first"<<endl;
    cout<<"z=2 -- move last"<<endl;
    cout<<"z=3 -- move next"<<endl;
    cout<<"z=4 -- move prev"<<endl;
    cout<<"z=";
    cin>>z;
    switch (z)
    {
    case 1:
    MyList.MoveFirst();
    MyList.Info();
        break;
    case 2:
    MyList.MoveLast();
    MyList.Info();
    break;
    case 3:
    MyList.MoveNext();
    MyList.Info();
    break;
    case 4:
    MyList.MovePrev();
    MyList.Info();
    break;
    default:
        break;
    }
    break;
    case 5:             //очистить лист
    while (MyList.Count)
    {
        MyList.Del(a);
    }
    break;
    case 6:             //выгрузка в файл
    ff.open("data.txt");
    MyList.MoveFirst();
    for(int i=0;i<MyList.Count;i++)
    {
        ff<<MyList.C->data.diameter<<" "<<MyList.C->data.weight<<" "<<MyList.C->data.color<<" "<<MyList.C->data.name<<endl;
        MyList.MoveNext();
    }
    ff.close();
    break;
    case 7:             //сортировка
    cout<<"z=1 -- sort by diametr"<<endl;
    cout<<"z=2 -- sort by weight"<<endl;
    cout<<"z=3 -- sort by color"<<endl;
    cout<<"z=4 -- sort by name"<<endl;
    cout<<"z=";
    cin>>z;
    switch (z)
    {
    case 1:
        for (int i = 0; i < MyList.Count - 1; i++)
	{
        MyList.MoveLast();
		for (int j = (MyList.Count - 1); j > i; j--) 
		{
			if ((MyList.C->prev->data.diameter) > (MyList.C->data.diameter)) 
			{
				buff=MyList.C->data;
				MyList.C->data=MyList.C->prev->data;
				MyList.C->prev->data=buff;
			}
        MyList.MovePrev();

		}
	}
        break;
        case 2:
        for (int i = 0; i < MyList.Count - 1; i++)
	{
        MyList.MoveLast();
		for (int j = (MyList.Count - 1); j > i; j--) 
		{
			if ((MyList.C->prev->data.weight) > (MyList.C->data.weight)) 
			{
				buff=MyList.C->data;
				MyList.C->data=MyList.C->prev->data;
				MyList.C->prev->data=buff;
			}
        MyList.MovePrev();

		}
	}
        break;
    case 3:
    for (int i = 0; i < MyList.Count - 1; i++)
	{
        MyList.MoveLast();
		for (int j = (MyList.Count - 1); j > i; j--) 
		{
			if ((MyList.C->prev->data.color) > (MyList.C->data.color)) 
			{
				buff=MyList.C->data;
				MyList.C->data=MyList.C->prev->data;
				MyList.C->prev->data=buff;
			}
        MyList.MovePrev();

		}
	}
    break;
    case 4:
    for (int i = 0; i < MyList.Count - 1; i++)
	{
        MyList.MoveLast();
		for (int j = (MyList.Count - 1); j > i; j--) 
		{
			if ((MyList.C->prev->data.name) > (MyList.C->data.name)) 
			{
				buff=MyList.C->data;
				MyList.C->data=MyList.C->prev->data;
				MyList.C->prev->data=buff;
			}
        MyList.MovePrev();

		}
	}
    break;
    default:
        break;
    }
    
    break;
    default:
        break;
    }
    }while (x!=0);
    return 0;
}
