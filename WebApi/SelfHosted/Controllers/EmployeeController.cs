namespace SelfHosted.Controllers
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Net;
    using System.Net.Http;
    using System.Web.Http;

    using HttpClient.Model;

    public class EmployeeController : ApiController
    {
        static List<Employee> employees = InitEmployees();

        public IEnumerable<Employee>  Get()
        {
            return employees;
        }

        public Employee Get(int id)
        {
            var employee = (from e in employees where e.Id == id select e).FirstOrDefault();

            if (employee == null)
            {
                
            }

            return employee;
        }

        public void Post(Employee newHire)
        {
            employees.Add(newHire);
        }

        public HttpResponseMessage Put(int id, Employee employeeUpdate)
        {
            if (employeeUpdate == null)
            {
                return this.Request.CreateErrorResponse(HttpStatusCode.NotAcceptable, "");
            }

            var employee = (from e in employees where e.Id == id select e).FirstOrDefault();

            if (employee == null)
            {
                return this.Request.CreateErrorResponse(HttpStatusCode.NotFound, string.Format("Employee {0} not found.", id));
            }

            Console.WriteLine(string.Format("Employee: {0}", employeeUpdate.Id));
            return this.Request.CreateResponse(HttpStatusCode.OK, employeeUpdate);
        }

        private static List<Employee> InitEmployees()
        {
            var ret = new List<Employee>();
            ret.Add(new Employee { Id = 1, Name = "Don", Title = "Marketing Director" });
            return ret;
        }
    }
}