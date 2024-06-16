package figurs;

import Ex.*;
import Ex.Ex.Exc2D;

public class Circle extends Eleps{
    public Circle(double r)throws Exc2D{
        Ex e = new Ex();
        if(r>0){
            this.A=r;
            this.B=r;
        }
        else{
            throw e.new Exc2D("Circle creation fail");
        }
    }
    public double ret(){
        area();
        return S;
    }
    public void show(){
        area();
        System.out.printf("sqare of circle= %s\n",S);
    }
}
