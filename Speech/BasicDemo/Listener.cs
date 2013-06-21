namespace BasicDemo
{
    using System;
    using System.Speech.Recognition;

    public class Listener
    {
        private readonly string[] keyPhrases = { "build" };

        private readonly SpeechRecognizer listener = new SpeechRecognizer();

        public Listener()
        {
            Console.WriteLine("Listening...");
            var keyChoices = new Choices(this.keyPhrases);
            var keyGrammer = new Grammar(new GrammarBuilder(keyChoices));
            this.listener.LoadGrammar(keyGrammer);
            this.listener.Enabled = true;
            keyGrammer.SpeechRecognized += this.keyGrammer_SpeechRecognized;
        }

        private void keyGrammer_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            Console.WriteLine("Building");
        }
    }
}