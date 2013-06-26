namespace HttpClient
{
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

            HttpResponseMessage response = await client.PutAsync("http://E6400:8001", don, jsonFormatter);
            response.EnsureSuccessStatusCode();
        }
    }
}