namespace HttpClient.Test
{
    using System;
    using System.Collections.Generic;
    using System.Net.Http;
    using System.Net.Http.Formatting;
    using System.Threading.Tasks;

    using HttpClient.Model;

    using Microsoft.VisualStudio.TestTools.UnitTesting;

    [TestClass]
    public class TestSimulator
    {
        [TestMethod]
        public void test_simulator()
        {
            this.PutEmployee();
        }

        public async void PutEmployee()
        {
            var client = new HttpClient();
            var peggy = new Employee { Id = 2, Name = "Peggy", Title = "Marketing" };

            HttpResponseMessage response = await client.GetAsync("http://E6400:8001/services/employee");
            response.EnsureSuccessStatusCode();
            IEnumerable<Employee> confirm = await response.Content.ReadAsAsync<IEnumerable<Employee>>();
            int n = 0;

        }
    }
}