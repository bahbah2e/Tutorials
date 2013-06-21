namespace ImplicitDataTemplate.Service
{
    using System.Collections.Generic;

    using ImplicitDataTemplate.Model;

    public class EmployeeDataSource
    {
        private List<IProfile> employees = new List<IProfile>();

        public EmployeeDataSource()
        {
            IProfile peggy = new ProfileDefault { ProfileName = "Peggy" };

            employees.Add(peggy);
            employees.Add(new ProfileSupervisor { ProfileName = "Don", Subordinates = new List<IProfile>() { peggy } });
        }

        public IEnumerable<IProfile> Employees
        {
            get { return this.employees; }
        }
    }
}
