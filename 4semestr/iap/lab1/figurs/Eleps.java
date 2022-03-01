package figurs;

public class Eleps implements Shape{
    public double A;
    public double B;
    public Eleps(){}
    public Eleps(double ae, double be){
        if ((ae>0) && (be>0)){
            this.A=ae;
            this.B=be;
        }
        else{
            throw new IllegalArgumentException("error Eleps");
        }
    }
    public double area(){
        return(A*B*PI);
    }
    public void show(){

    }
}
