namespace WindowsDemo
{
    using System;
    using System.Security.Principal;

    class Program
    {
        static void Main(string[] args)
        {
            var id = WindowsIdentity.GetCurrent();
            Console.WriteLine(id.Name);

            var account = new NTAccount(id.Name);
            var sid = account.Translate(typeof(SecurityIdentifier));
            Console.WriteLine(sid.Value);

            foreach (var group in id.Groups.Translate(typeof(NTAccount)))
            {
                Console.WriteLine(group.Value);
            }

            var principle = new WindowsPrincipal(id);

            var localAdmins = new SecurityIdentifier(
                WellKnownSidType.BuiltinAdministratorsSid, 
                id.User.AccountDomainSid);
        }
    }
}
