namespace SqlCompactRepository
{
    using System.Data.Entity;

    using SqlCompactRepository.Model;

    public class CompanyContext : DbContext
    {
        public CompanyContext() : base("Company")
        {
        }

        public DbSet<Employee> Employees { get; set; }
    }
}