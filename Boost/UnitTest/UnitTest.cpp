// UnitTest.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <boost/test/included/unit_test.hpp>
#include "TestTarget.hpp"

using namespace boost::unit_test;

test_suite* init_unit_test_suite( int argc, char* argv[] ) 
{
    test_suite* test = BOOST_TEST_SUITE("mt::fillhead : generic test suite");

    test->add( BOOST_TEST_CASE( &TestEmployeeDefaultName ));
    test->add( BOOST_TEST_CASE( &TestEmployeeDefaultTitle ));
    
    return test;
}