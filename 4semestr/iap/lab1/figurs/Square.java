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
    public void show(){

    }
}
