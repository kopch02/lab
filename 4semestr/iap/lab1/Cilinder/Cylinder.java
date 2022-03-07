package Cilinder;

import figurs.*;
import Ex.*;
import Ex.Ex.Exc3D;

public class Cylinder{
    double S;
    double H;
    public Cylinder(Shape a,double h)throws Exc3D{
        Ex e = new Ex();
        if (h>0){
            this.S=a.ret();
            this.H=h;
        }
        else{
            throw e.new Exc3D( "Error creating cylinder");
        }
    }
    public double volume(){
        return(S*H);
    }
}