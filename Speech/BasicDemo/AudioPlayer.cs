namespace BasicDemo
{
    using QuartzTypeLib;

    internal class AudioPlayer
    {
        private string mediaFile;

        public string Source
        {
            get { return this.mediaFile; }
            set { this.mediaFile = value; }
        }

        public void Play()
        {
            // Access the IMediaControl interface.
            var graphManager = new FilgraphManager();
            IMediaControl mc = graphManager;
            // Specify the file.
            mc.RenderFile(this.mediaFile);
            // Start playing the audio asynchronously.
            mc.Run();
        }
    }
}