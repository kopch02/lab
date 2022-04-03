package figurs;
import Ex.*;
import Ex.Ex.Exc2D;

public class Eleps implements Shape{
    public double A;
    public double B;
    public double S;
    public Eleps(){}
    public Eleps(double ae, double be)throws Exc2D{
        Ex e = new Ex();
        if ((ae>0) && (be>0)){
            this.A=ae;
            this.B=be;
        }
        else{
            throw e.new Exc2D("Eleps creation fail");
        }
    }
    public void area(){
        S=A*B*PI;
        
    }
    public double ret(){
        area();
        return S;
    }
    public void show(){
        area();
        System.out.printf("sqare of eleps= %s\n",S);
    }
}
