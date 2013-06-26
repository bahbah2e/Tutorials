namespace HttpClient.Test
{
    using Microsoft.VisualStudio.TestTools.UnitTesting;

    [TestClass]
    public class TestSimulator
    {
        [TestMethod]
        public void test_simulator()
        {
            EmploymentSimulator simulator = new EmploymentSimulator();
            simulator.PutEmployee();
        }
    }
}