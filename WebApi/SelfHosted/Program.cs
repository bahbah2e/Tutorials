namespace SelfHosted
{
    using System;
    using System.Web;
    using System.Web.Http;
    using System.Web.Http.SelfHost;

    internal class Program : HttpApplication
    {
        private static void Main(string[] args)
        {
            var config = new HttpSelfHostConfiguration("http://127.0.0.1:8001");

            config.Routes.MapHttpRoute(
                "DefaultControllers", "Services/{controller}/{id}",
                new { id = RouteParameter.Optional });

            using (HttpSelfHostServer server = new HttpSelfHostServer(config))
            {
                server.OpenAsync().Wait();
                Console.WriteLine("Press Enter to quit.");
                Console.ReadLine();
            }
        }
    }
}