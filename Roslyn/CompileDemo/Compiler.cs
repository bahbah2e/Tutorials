namespace CompileDemo
{
    using System;
    using System.IO;
    using System.Reflection;

    using Roslyn.Compilers;
    using Roslyn.Compilers.CSharp;

    public class Compiler : IDisposable
    {
        private const string TempFileTemplate = "*.tmp.vpr";

        private readonly MetadataReference mscorlib = MetadataReference.CreateAssemblyReference("mscorlib");

        public Type[] Build(string sourcePath)
        {
            this.Cleanup();
            Type[] types = new Type[] { };
            SyntaxTree tree = SyntaxTree.ParseFile(sourcePath);

            Compilation compilation = Compilation.Create(
                                                outputName: "HelloWorld",
                                                options: new CompilationOptions(outputKind: OutputKind.DynamicallyLinkedLibrary),
                                                syntaxTrees: new[] { tree },
                                                references: new[] { mscorlib });

            string outputFileName = Path.Combine(Path.GetTempPath(), Path.GetRandomFileName() + TempFileTemplate).Replace("*", "");
            var result = compilation.Emit(outputFileName);

            try
            {
                Assembly addInAssembly = Assembly.Load(File.ReadAllBytes(outputFileName));
                types = addInAssembly.GetExportedTypes();
                File.Delete(outputFileName);
            }
            catch (BadImageFormatException e)
            {
                throw;
            }

            return types;
        }

        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this);
        }

        protected virtual void Dispose(bool disposing)
        {
            if (disposing)
            {
                this.Cleanup();
            }
        }

        private MetadataReference LocalReference
        {
            get
            {
                return MetadataReference.CreateAssemblyReference(Assembly.GetExecutingAssembly().Location);
            }
        }

        private string LocalReferences
        {
            get
            {
                Assembly vaporizer = Assembly.GetExecutingAssembly();
                string references = string.Empty;
                foreach (AssemblyName reference in vaporizer.GetReferencedAssemblies())
                {
                    references += reference + ",";
                }

                return references;
            }
        }

        private void Cleanup()
        {
            foreach (string vprFile in Directory.EnumerateFiles(Path.GetTempPath(), TempFileTemplate))
            {
                try
                {
                    File.Delete(vprFile);
                }
                catch (Exception e)
                {
                }
            }
        }

        private void EmitStream(Compilation comp, string outputFileName)
        {
            FileStream ilStream = new FileStream(outputFileName, FileMode.Create);
            var result = comp.Emit(ilStream);
            ilStream.Close();
        }

        private string ExtractSource(string path)
        {
            string source;

            using (var sr = new StreamReader(path))
            {
                source = sr.ReadToEnd();
            }

            return source;
        }
    }
}