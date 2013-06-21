using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BasicDemo.Test
{
    using NUnit.Framework;

    [TestFixture]
    public class TestTalker
    {
        [Test]
        public void test_say_hello()
        {
            Talker talk = new Talker();
            talk.Say("say hello to my little friend");
        }
    }
}
