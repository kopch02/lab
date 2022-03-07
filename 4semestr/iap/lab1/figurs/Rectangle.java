package figurs;

import Ex.*;
import Ex.Ex.Exc2D;

public class Rectangle implements Shape{
    double A;
    double B;
    double S;
    public Rectangle(){}
    public Rectangle(double a, double b)throws Exc2D{
        Ex e = new Ex();
        if ((a>0)&&(b>0)){
            this.A=a;
            this.B=b;
        }
        else{
            throw e.new Exc2D("Rectangle creation fail");
        }
    }
    public double ret(){
        area();
        return S;
    }
    public void area(){
        S=A*B;
    }
    public void show(){
        area();
        System.out.printf("sqare of rectangle= %s\n",S);
    }
}
