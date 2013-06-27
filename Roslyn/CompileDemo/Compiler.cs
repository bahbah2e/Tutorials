using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CompileDemo
{
    using System.IO;

    public class Compiler
    {
        private string ExtractSource(string path)
        {
            string source;

            using (StreamReader sr = new StreamReader(path))
            {
                source = sr.ReadToEnd();
            }

            return source;
        }
    }
}
