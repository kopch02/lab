package figurs;

import Ex.*;
import Ex.Ex.Exc2D;

public class Triangle implements Shape{
    double A;
    double H;
    double S;
    public Triangle(double a, double h)throws Exc2D{
        Ex e = new Ex();
        if ((a>0)&&(h>0)){
            this.A=a;
            this.H=h;
        }
        else{
            throw e.new Exc2D("Rectangle creation fail");
        }
    }
    public void area(){
        S=0.5*A*H;
    }
    public double ret(){
        area();
        return S;
    }
    public void show(){
        area();
        System.out.printf("sqare of triangle= %s\n",S);
    }
}
