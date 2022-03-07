package figurs;

public class Eleps implements Shape{
    public double A;
    public double B;
    public double S;
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
