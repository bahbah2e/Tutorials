namespace BasicDemo
{
    using System.Speech.Synthesis;

    public class Talker
    {
        public void Say(string words)
        {
            SpeechSynthesizer synth = new SpeechSynthesizer();
            synth.SetOutputToDefaultAudioDevice();
            synth.Speak(words);
        }
    }
}