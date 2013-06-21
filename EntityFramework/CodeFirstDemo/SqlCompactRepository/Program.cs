namespace SqlCompactRepository
{
    using System.Data.Entity;

    using SqlCompactRepository.Migrations;

    internal class Program
    {
        private static void Main(string[] args)
        {
            Database.SetInitializer(new MigrateDatabaseToLatestVersion<CompanyContext, Configuration>());

            var context = new CompanyContext();
            context.Database.Initialize(true);
            context.SaveChanges();
        }
    }
}