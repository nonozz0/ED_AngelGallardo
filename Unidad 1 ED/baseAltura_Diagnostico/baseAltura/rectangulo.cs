using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace baseAltura
{
    internal class rectangulo
    {
        //Atributos
        private double _dblbaseR;
        private double _dblaltura;

        public double baseR
        {
            get { return _dblbaseR; }
            set { _dblbaseR = value; }
        }

        public double altura
        {
            get { return _dblaltura; }
            set { _dblaltura = value; }
        }
        //Constructor
        public rectangulo(double baseR, double altura)
        {
            this.baseR = baseR;
            this.altura = altura;
        }

        //Metodos
        public double Area()
        {
            return baseR * altura;
        }

        public double Perimetro()
        {
            return 2 * (baseR + altura);
        }

        public void MostrarDatos()
        {
            Console.WriteLine("Area: " + Area());
            Console.WriteLine("Perimetro: " + Perimetro());
        }
    }
}
