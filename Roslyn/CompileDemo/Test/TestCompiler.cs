namespace CompileDemo.Test
{
    using System;

    using Microsoft.VisualStudio.TestTools.UnitTesting;

    [TestClass]
    public class TestCompiler
    {
        [TestMethod]
        public void test_compile_file()
        {
            for (int i = 0; i < 100; i++)
            {
                using (var compiler = new Compiler())
                {
                    Type[] types = compiler.Build("Test\\adder.cs");
                    Assert.AreEqual(types.Length, 1);
                    Assert.AreEqual(types[0].Name, "Adder");
                    Assert.AreEqual(types[0].FullName, "Math.Adder");
                }
            }
        }
    }
}