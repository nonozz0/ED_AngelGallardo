using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace baseAltura
{
    internal class cuadrado : rectangulo
    {

        //Constructor
        public cuadrado(double lado ) : base(lado, lado)
        {
            this.baseR = lado;
        }
    }
    
    
}
