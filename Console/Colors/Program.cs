namespace Colors
{
    using System;
    using System.Reflection;

    internal class Program
    {
        private static Version AssemblyVersion
        {
            get { return Assembly.GetCallingAssembly().GetName().Version; }
        }

        private static void EchoColor(string echo, ConsoleColor color)
        {
            ConsoleColor begin = Console.ForegroundColor;
            Console.ForegroundColor = color;
            Console.WriteLine(echo);
            Console.ForegroundColor = begin;
        }

        private static void EchoGreen(string echo)
        {
            EchoColor(echo, ConsoleColor.Green);
        }

        private static void EchoRed(string echo)
        {
            EchoColor(echo, ConsoleColor.Red);
        }

        private static void EchoUsage()
        {
            Console.WriteLine();

            EchoGreen(string.Format("Calling Application Version: {0}", AssemblyVersion));
            Console.WriteLine("Copyright (C) 2013 Company");
            Console.WriteLine();

            Console.WriteLine("Usage: language [options]");
        }

        private static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                EchoUsage();
            }

            for (int i = 0; i < args.Length; i++)
            {
                switch (args[i])
                {
                    case "-?":
                    case "-help":
                        EchoUsage();
                        i = args.Length;
                        break;
                    case "-i":
                        string input = args[++i];
                        EchoGreen(input);
                        break;

                    case "-o":
                        string output = args[++i];
                        EchoRed(output);
                        break;
                }
            }
        }
    }
}