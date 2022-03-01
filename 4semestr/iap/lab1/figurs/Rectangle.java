package figurs;

public class Rectangle implements Shape{
    double A;
    double B;
    public Rectangle(){}
    public Rectangle(double a, double b){
        if ((a>0)&&(b>0)){
            this.A=a;
            this.B=b;
        }
        else{
            throw new IllegalArgumentException("error Rectangle");
        }
    }
    public double area(){
        return(A*B);
    }
    public void show(){

    }
}
