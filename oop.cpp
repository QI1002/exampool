

#include <iostream>
#include <string.h>
#include <malloc.h>

using namespace std;

#define VIRTUAL_FUNC
#define VIRTUAL_DEMO

template <class T>
class SmartPtr
{
public:	
    SmartPtr(T* ptr)
    {
	ref_count = (unsigned int*)malloc(sizeof(unsigned int));
	*ref_count = 1;
        this->ptr = ptr;
    }

    SmartPtr(SmartPtr<T>& src)
    {
        ref_count = src.ref_count;
	ptr = src.ptr;
	*ref_count++;
    }

    SmartPtr<T>& operator= (SmartPtr<T>& src)
    {
        if (&src != this)
	{
            ref_count = src.ref_count;
	    ptr = src.ptr;
	    *ref_count++;
	}
	
	return *this;
    }

    ~SmartPtr()
    {
	*ref_count--;
	if (*ref_count == 0)
        {
            free(ref_count);
	    delete ptr;
	    ptr = NULL;
	    ref_count = NULL;
	}
    }

protected:
    T* ptr;
    unsigned int* ref_count;
};

class Employee
{

public:
    static const bool debug = true;
    
    Employee(const char* name):
    name(NULL),	    
    rank(-1)
    {
	if (debug) cout << "employee init" << endl;    
        this->name = strdup(name);
    }

    ~Employee()
    {
	if (debug) cout << "employee uninit" << endl;    
        if (name != NULL) free(name);
    }

    char* getName(void)
    {
        return name;
    }

#ifdef VIRTUAL_FUNC
    virtual int getRank(void) = 0;
#else    
#ifdef VIRTUAL_DEMO    
    virtual int getRank(void)
#else
    int getRank(void)
#endif	    
    {
        return -1;
    }
#endif

protected:

    char* name;
    int rank;
};

class Fresher: public Employee
{
public:
    Fresher(const char* name):
    Employee(name)	    
    {
	if (debug) cout << "fresher init" << endl;   
	rank = 0;
    }

    ~Fresher()
    {
	if (debug) cout << "fresher uninit" << endl;    
    }

    int getRank(void)
    {
        return rank;
    }
};

int main(int argc, char* argv[])
{
#ifndef VIRTUAL_FUNC	
    Employee e0("Zero");
    cout << "e0: " << e0.getName() << " : " << e0.getRank() << endl;
#endif

    Fresher e1("One");
    cout << "e1: " << e1.getName() << " : " << e1.getRank() << endl;

    Employee* e1p = new Fresher("Two");
    cout << "e1p: " << e1p->getName() << " : " << e1p->getRank() << endl;

    SmartPtr<Employee> ee(e1p);
    SmartPtr<Employee> ee2(ee);
    SmartPtr<Employee> ee3 = ee2;

    return 0;
}
