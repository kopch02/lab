package TestMain;

import java.util.Scanner;
import Cilinder.*;
import figurs.*;
import Ex.Ex.Exc2D;
import Ex.Ex.Exc3D;


class One{
    public static void main(String[] args)throws Exception {
        try{
            Scanner in = new Scanner(System.in);
            double V;

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

            Shape e= new figurs.Eleps(ae,be);
            Shape c= new figurs.Circle(r);
            Shape rec= new figurs.Rectangle(a,b);
            Shape s= new figurs.Square(as);
            Shape t= new figurs.Triangle(at,h);

            Cylinder ce = new Cilinder.Cylinder(e,he);
            Cylinder cc = new Cilinder.Cylinder(c,hc);
            Cylinder cr = new Cilinder.Cylinder(rec,hr);
            Cylinder cs = new Cilinder.Cylinder(s,hs);
            Cylinder ct = new Cilinder.Cylinder(t,ht);

            e.show();
            V=ce.volume();
            System.out.printf("volume of eleps= %s\n\n",V);

            c.show();
            V=cc.volume();
            System.out.printf("volume of circle= %s\n\n",V);

            rec.show();
            V=cr.volume();
            System.out.printf("volume of rectangle= %s\n\n",V);

            s.show();
            V=cs.volume();
            System.out.printf("volume of square= %s\n\n",V);

            t.show();
            V=ct.volume();
            System.out.printf("volume of triangle= %s\n\n",V);

            in.close();
        }catch (Exc2D exc2d) {
            exc2d.show();
        } catch (Exc3D exc3d) {
            exc3d.Out();
        }
    }
}
