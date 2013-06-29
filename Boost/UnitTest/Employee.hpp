namespace company {
namespace employees {

#ifndef interface
#define interface struct
#endif

interface IEmployee
{
    virtual ~IEmployee() {}
    virtual int GetId() = 0;
	virtual const char* GetName() = 0;
	virtual const char* GetTitle() = 0;
};

class EmployeeNull : public IEmployee
{
public:
	int GetId() { return -1; }
    const char* GetName() { return "Unknown Name"; }
	const char* GetTitle() { return "Unknown Title"; }
};

}}