#include <iostream>
using namespace std;
class Test
{
private:
	int mark;
	float spi;
public:
	void SetData()
	{
		mark = 270;
		spi= 6.5;
	}
	void Displaydata()
	{
		cout<< "Mark= " << mark<< endl;
		cout<< "spi= " <<spi;

	}
};



int main()
{
	Test o1;
	o1.SetData();
	o1.DisplayData();
	return 0;
}