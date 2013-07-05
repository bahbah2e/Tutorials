<Query Kind="Statements">
  <Namespace>System.Security.Cryptography</Namespace>
</Query>

var rsa = new RSACryptoServiceProvider();
var privateParameters = rsa.ExportParameters(true);
var publicParametes = rsa.ExportParameters(false);

Debug.WriteLine(rsa.ToXmlString(true));
Debug.WriteLine(rsa.ToXmlString(false));