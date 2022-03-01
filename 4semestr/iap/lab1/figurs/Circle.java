package figurs;
public class Circle extends Eleps{
    public Circle(double r){
        if(r>0){
            this.A=r;
            this.B=r;
        }
        else{
            throw new IllegalArgumentException("error Circle");
        }
    }
    public void show(){

    }
}
