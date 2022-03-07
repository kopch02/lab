package figurs;

public class Square extends Rectangle{
    public Square(double as){
        if (as>0){
            this.A=as;
            this.B=as;
        }
        else{
            throw new IllegalArgumentException("error Sqare");
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
