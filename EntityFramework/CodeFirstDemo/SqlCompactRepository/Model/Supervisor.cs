namespace SqlCompactRepository.Model
{
    using System.Collections.Generic;

    public class Supervisor : Employee
    {
        public Supervisor()
        {
            this.Subordinates = new List<Employee>();
        }

        public List<Employee> Subordinates { get; set; }
    }
}
