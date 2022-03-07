package Cilinder;

import figurs.*;

public class Cylinder{
    double S;
    double H;
    public Cylinder(Shape a,double h){
        if (h>0){
            this.S=a.ret();
            this.H=h;
        }
        else{
            throw new IllegalArgumentException("error Cylinder");
        }
    }
    public double volume(){
        return(S*H);
    }
}