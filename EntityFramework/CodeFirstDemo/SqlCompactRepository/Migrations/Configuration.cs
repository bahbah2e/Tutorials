namespace SqlCompactRepository.Migrations
{
    using System;
    using System.Data.Entity.Migrations;

    using SqlCompactRepository.Model;

    internal sealed class Configuration : DbMigrationsConfiguration<CompanyContext>
    {
        public Configuration()
        {
            this.AutomaticMigrationsEnabled = true;
        }

        protected override void Seed(CompanyContext context)
        {
            var don = new Employee
                          {
                              Id = 1,
                              Name = "Don",
                              Title = "Marketing Director",
                              HireDate = new DateTime(1958, 3, 29)
                          };

            var peggy = new Employee
                            {
                                Id = 2,
                                Name = "Peggy",
                                Title = "Secretary",
                                HireDate = new DateTime(1964, 7, 20)
                            };

            context.Employees.Add(don);
            context.Employees.Add(peggy);
        }
    }
}