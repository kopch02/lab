#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

struct flesh
{
	double speed;
	double memory;
	string name;
	string color;
};
struct Tree
{
	flesh data;
	Tree* left;
	Tree* right;

};

int GetTreeSize(Tree* T)
{
	if (!T) 
	{
		return 0;
	}
	if (!T->left && !T->right)
	{
		return 1;
	}
	int left = 0, right = 0;
	if (T->left)
	{
		left = GetTreeSize(T->left);
	}
	if (T->right)
	{
		right = GetTreeSize(T->right);
	}
	return left + right + 1;
}
void Addspeed(Tree*& T, flesh data)
{
	if (!T) 
	{
		T = new Tree;
		T->data = data;
		T->left = NULL;
		T->right = NULL;
		return;
	}
	if (data.speed < T->data.speed)
		Addspeed(T->left, data);
	else
		Addspeed(T->right, data);
}
void Addmemory(Tree *&T, flesh data)
{
	if (!T)
	{
		T = new Tree;
		T->data = data;
		T->left = NULL;
		T->right = NULL;
		return;
	}
	if (data.memory < T->data.memory)
		Addmemory(T->left, data);
	else
		Addmemory(T->right, data);
}
void Addname(Tree*& T, flesh data)
{
	if (!T) 
	{
		T = new Tree;
		T->data = data;
		T->left = NULL;
		T->right = NULL;
		return;
	}
	if (data.name < T->data.name)
		Addname(T->left, data);
	else
		Addname(T->right, data);
}
void Addcolor(Tree *&T, flesh data)
{
	if (!T)
	{
		T = new Tree;
		T->data = data;
		T->left = NULL;
		T->right = NULL;
		return;
	}
	if (data.color < T->data.color)
		Addcolor(T->left, data);
	else
		Addcolor(T->right, data);
}
void PrintLRR(Tree* T)
{
	if (!T) 
	{
		return;
	}
	PrintLRR(T->left);
	cout << T->data.speed << " " << T->data.memory << " " << T->data.name << " " << T->data.color<<endl;
	PrintLRR(T->right);

}
Tree* Searchspeed(Tree*& T, flesh data,double z)
{
	if (!T) 
	{
		return NULL;
	}

	while (T->data.speed != z) 
	{
		if (data.speed < T->data.speed)
		{
			T = T->left;
		}
		else 
		{
			T = T->right;
		}
		if (!T) break;
	}
		return T;
	
}
Tree* Searchmemory(Tree*& T, flesh data)
{
	if (!T) 
	{
		return NULL;
	}

	while (T->data.memory != data.memory)
	{
		if (data.memory < T->data.memory)
		{
			T = T->left;
		}
		else 
		{
			T = T->right;
		}
		if (!T) break;
	}
		return T;
	
}
Tree* Searchname(Tree*& T, flesh data)
{
	if (!T) 
	{
		return NULL;
	}

	while (T->data.name != data.name)
	{
		if (data.name < T->data.name)
		{
			T = T->left;
		}
		else 
		{
			T = T->right;
		}
		if (!T) break;
	}
		return T;
	
}
Tree *Searchcolor(Tree *&T, flesh data)
{
	if (!T)
	{
		return NULL;
	}

	while (T->data.color != data.color)
	{
		if (data.color < T->data.color)
		{
			T = T->left;
		}
		else
		{
			T = T->right;
		}
		if (!T)
			break;
	}
	return T;
}
void Delete(Tree*& T)
{
	if (T) 
	{
		if (T->left) Delete(T->left);
		if (T->right) Delete(T->right);
		delete T; 
		T = NULL;
	}
	else
		cout << "Tree is empty" << endl;
}
/*void ss(double z,Tree*& T, flesh data)
{
	if(z>T->data.speed)
	{
		
	}
}*/
int main()
{
	ifstream file;
	flesh f;
	Tree* T=NULL;
	int x;
	double z;
	file.open("file.txt");
	cout << "x=1 --Sort by speed" << endl
		 << "x=2 --Sort by memory" << endl
		 << "x=3 --Sort by name" << endl
		 << "x=4 --Sort by color"<<endl<<"x -- ";

	cin>>x;
	switch (x)
	{
	case 1:
		for (int i = 0; i < 3; i++)
		{
			file >> f.speed >> f.memory >> f.name >> f.color;
			Addspeed(T, f);
		}
		break;
	case 2:
		for (int i = 0; i < 3; i++)
		{
			file >> f.speed >> f.memory >> f.name >> f.color;
			Addmemory(T, f);
		}
	break;
	case 3:
		for (int i = 0; i < 3; i++)
		{
			file >> f.speed >> f.memory >> f.name >> f.color;
			Addname(T, f);
		}
	break;
	case 4:
		for (int i = 0; i < 3; i++)
		{
			file >> f.speed >> f.memory >> f.name >> f.color;
			Addcolor(T, f);
		}
	break;
	default:
		break;
	}
	

	cout<<"size tree="<<GetTreeSize(T)<<endl;
	PrintLRR(T);
	Delete(T);
	return 0;
}