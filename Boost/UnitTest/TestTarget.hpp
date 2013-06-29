#include <boost/test/included/unit_test.hpp>
#include "Employee.hpp"

using namespace boost::unit_test;
using namespace company::employees;

void TestEmployeeDefaultName()
{
    const char* DefaultName = "Unknown Name";
    
    IEmployee* employee = new EmployeeNull();

    BOOST_CHECK(employee->GetName() == DefaultName);
    
    delete employee;
}

void TestEmployeeDefaultTitle()
{
    const char* DefaultTitle = "Unknown Title";
    
    IEmployee* employee = new EmployeeNull();

    BOOST_CHECK(employee->GetTitle() == DefaultTitle);
    
    delete employee;
}
