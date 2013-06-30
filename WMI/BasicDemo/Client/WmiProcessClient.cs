using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Client
{
    using System.Management;

    public class WmiProcessClient
    {
        private static ILog logger = LogManager.GetLogger(typeof(ConditionProcess));

        private const string QueryFindProcess = "SELECT * from Win32_Process where Caption='";
        
        private string queryProcess = "XMain.exe";

        public ConditionProcess(string target)
        {
            this.queryProcess = target;
        }

        public bool Exists
        {
            get { return IsProcessRunning; }
        }

        private string QueryProcess
        {
            get { return QueryFindProcess + this.queryProcess + "'"; }
        }
        
        private bool IsProcessRunning
        {
            get
            {
                try
                {
                    using (ManagementObjectSearcher searchHmi = new ManagementObjectSearcher(QueryProcess))
                    {
                        using (ManagementObjectCollection searchResults = searchHmi.Get())
                        {
                            if (searchResults.Count == 1)
                            {
                                logger.InfoFormat("Process {0} found.", this.queryProcess);
                                return true;
                            }
                        }
                    }
                }
                catch (Exception e)
                {
                    logger.Info("Exception testing process status.", e);
                }

                logger.InfoFormat("Process {0} not found.", this.queryProcess);
                return false;
            }
        }
    }
}
