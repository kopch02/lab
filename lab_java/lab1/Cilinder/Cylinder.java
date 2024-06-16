package Cilinder;

import figurs.*;
import Ex.*;
import Ex.Ex.Exc3D;

public class Cylinder{
    double H;
    Shape f;
    public Cylinder(Shape a,double h)throws Exc3D{
        Ex e = new Ex();
        if (h>0){
            this.H=h;
            this.f=a;
        }
        else{
            throw e.new Exc3D( "Error creating cylinder");
        }
    }
    public double volume(){
        return(f.ret()*H);
    }
}