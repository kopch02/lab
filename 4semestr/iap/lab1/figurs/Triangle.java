package figurs;

public class Triangle implements Shape{
    double A;
    double H;
    public Triangle(double a, double h){
        if ((a>0)&&(h>0)){
            this.A=a;
            this.H=h;
        }
        else{
            throw new IllegalArgumentException("error Triangle");
        }
    }
    public double area(){
        return(0.5*A*H);
    }
    public void show(){

    }
}
