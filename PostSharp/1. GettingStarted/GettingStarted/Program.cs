namespace PostSharp.Tutorial
{
    using System;
    using System.Diagnostics;

    internal static class Program
    {
            private static void Main()
        {
                Trace.Listeners.Add(new TextWriterTraceListener(Console.Out));

                SayHello();
                SayGoodbye();
            }

            [Trace("MyCategory")]
            private static void SayHello()
            {
                Console.WriteLine("Hello, world.");
            }

            [Trace("MyCategory")]
            private static void SayGoodbye()
            {
                Console.WriteLine("Good bye, world.");
        }
    }
}