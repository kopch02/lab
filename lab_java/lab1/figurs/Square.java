package figurs;

import Ex.*;
import Ex.Ex.Exc2D;

public class Square extends Rectangle{
    public Square(double as)throws Exc2D{
        Ex e = new Ex();
        if (as>0){
            this.A=as;
            this.B=as;
        }
        else{
            throw e.new Exc2D("Square creation fail");
        }
    }
    public double ret(){
        area();
        return S;
    }
    public void show(){
        area();
        System.out.printf("sqare of square= %s\n",S);
    }
}
