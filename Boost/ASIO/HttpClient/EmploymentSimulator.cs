namespace HttpClient
{
    using System;
    using System.Net.Http;
    using System.Net.Http.Formatting;

    using HttpClient.Model;

    public class EmploymentSimulator
    {
        public async void PutEmployee()
        {
            var client = new HttpClient();
            var don = new Employee { Id = 1, Name = "Don", Title = "Marketing Director" };

            MediaTypeFormatter jsonFormatter = new JsonMediaTypeFormatter();

            try
            {
                HttpResponseMessage response = await client.PutAsync("http://localhost.:8001/employees", don, jsonFormatter);
                response.EnsureSuccessStatusCode();
            }
            catch (Exception e)
            {
                string mes = e.Message;
                throw;
            }
            
        }
    }
}