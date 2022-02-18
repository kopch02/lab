import java.util.Scanner;

class One {
    public static void main(String[] args) {
        Create r=new Create();
        r.run();
    }
}  
class Create{
    public void run(){
        try{
            Scanner in = new Scanner(System.in);
            double S,V;

            System.out.print("endter a and b for eleps a->");
            double ae=in.nextDouble();
            System.out.print("b->");
            double be=in.nextDouble();
            System.out.print("hight for eleps->");
            double he=in.nextDouble();

            System.out.print("enter radius for circle(r)->");
            double r=in.nextDouble();
            System.out.print("hight for circle->");
            double hc=in.nextDouble();

            System.out.print("enter a and b sides of the rectangle a->");
            double a=in.nextDouble();
            System.out.print("b->");
            double b=in.nextDouble();
            System.out.print("hight for rectangle->");
            double hr=in.nextDouble();

            System.out.print("enter a sides of the square a->");
            double as=in.nextDouble();
            System.out.print("hight for square->");
            double hs=in.nextDouble();

            System.out.print("endter base of triangle(base)->");
            double at=in.nextDouble();
            System.out.print("enter height for triangle(h)->");
            double h=in.nextDouble();
            System.out.print("hight for triangle->");
            double ht=in.nextDouble();

            Shape e= new Eleps(ae,be);
            Shape c= new Circle(r);
            Shape rec= new Rectangle(a,b);
            Shape s= new Square(as);
            Shape t= new Triangle(at,h);

            Cylinder ce = new Cylinder(e,he);
            Cylinder cc = new Cylinder(c,hc);
            Cylinder cr = new Cylinder(rec,hr);
            Cylinder cs = new Cylinder(s,hs);
            Cylinder ct = new Cylinder(t,ht);


            S=e.area();
            System.out.printf("площадь эллипса= %s\n",S);
            V=ce.volume();
            System.out.printf("обьём эллипса= %s\n\n",V);

            S=c.area();
            System.out.printf("площадь круга= %s\n",S);
            V=cc.volume();
            System.out.printf("обьём круга= %s\n\n",V);

            S=rec.area();
            System.out.printf("площадь прямоугольника= %s\n",S);
            V=cr.volume();
            System.out.printf("обьём прямоугольника= %s\n\n",V);

            S=s.area();
            System.out.printf("площадь квадрата= %s\n",S);
            V=cs.volume();
            System.out.printf("обьём квадрата= %s\n\n",V);

            S=t.area();
            System.out.printf("площадь треугольника= %s\n",S);
            V=ct.volume();
            System.out.printf("обьём треугольника= %s\n\n",V);

            in.close();
        }catch(IllegalArgumentException exc)
        {
            System.out.println(exc.getMessage());
        }
    }
}
interface Shape{
    final double PI=3.14159265359;
    double area();
    void show();
}

class Cylinder{
    double S;
    double H;
    Cylinder(Shape a,double h){
        if (h>0){
            this.S=a.area();
            this.H=h;
        }
        else{
            throw new IllegalArgumentException("error Cylinder");
        }
    }
    double volume(){
        return(S*H);
    }
}

class Eleps implements Shape{
    protected double A;
    protected double B;
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
class Circle extends Eleps{
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
class Triangle implements Shape{
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
class Rectangle implements Shape{
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
class Square extends Rectangle{
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