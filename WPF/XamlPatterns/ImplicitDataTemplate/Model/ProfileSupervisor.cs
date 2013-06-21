namespace ImplicitDataTemplate.Model
{
    using System.Collections.Generic;

    public class ProfileSupervisor : ProfileAbstract
    {
        public ProfileSupervisor()
        {
            this.Subordinates = new List<IProfile>();
        }

        public IEnumerable<IProfile> Subordinates { get; set; }
    }
}
