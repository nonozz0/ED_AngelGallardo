namespace baseAltura
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Rectangulo...");
            rectangulo miRectangulo = new rectangulo(5, 10);
            miRectangulo.MostrarDatos();

            Console.WriteLine("\nCuadrado...");
            cuadrado miCuadrado = new cuadrado(5);
            miCuadrado.MostrarDatos();

            Console.ReadKey();
        }
    }
}
