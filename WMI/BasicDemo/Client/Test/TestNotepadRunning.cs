namespace Client.Test
{
    using System.Diagnostics;
    using System.Threading;

    using Microsoft.VisualStudio.TestTools.UnitTesting;

    [TestClass]
    public class TestNotepadRunning
    {
        [TestMethod]
        public void test_launch_and_query_notepad()
        {
            Process.Start("notepad.exe");

            // Sleep long enough to allow the application to start
            Thread.Sleep(2000);

            WmiProcessClient query = new WmiProcessClient("notepad.exe");
            Assert.IsTrue(query.Exists);
        }
    }
}