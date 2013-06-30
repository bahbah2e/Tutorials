namespace Client
{
    using System;
    using System.Management;

    public class WmiProcessClient
    {
        private const string QueryFindProcess = "SELECT * from Win32_Process where Caption='";

        private string queryProcess = "Notepad.exe";

        public WmiProcessClient(string target)
        {
            this.queryProcess = target;
        }

        public bool Exists
        {
            get { return this.IsProcessRunning; }
        }

        protected virtual void ProcessQueryException(Exception e)
        {
        }

        private bool IsProcessRunning
        {
            get
            {
                try
                {
                    using (var searchProcess = new ManagementObjectSearcher(this.QueryProcess))
                    {
                        using (ManagementObjectCollection searchResults = searchProcess.Get())
                        {
                            if (searchResults.Count > 0)
                            {
                                return true;
                            }
                        }
                    }
                }
                catch (Exception e)
                {
                    this.ProcessQueryException(e);
                    throw;
                }

                return false;
            }
        }

        private string QueryProcess
        {
            get { return QueryFindProcess + this.queryProcess + "'"; }
        }
    }
}