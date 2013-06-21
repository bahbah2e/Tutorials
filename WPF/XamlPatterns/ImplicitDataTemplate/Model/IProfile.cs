namespace ImplicitDataTemplate.Model
{
    using System;

    public interface IProfile
    {
        string ProfileName { get; set; }
        DateTime LastLogin { get; set; }
    }

    public abstract class ProfileAbstract : IProfile
    {
        public string ProfileName { get; set; }

        public DateTime LastLogin { get; set; }

        public ProfileAbstract()
        {
            LastLogin = DateTime.MinValue;
        }
    }
}
