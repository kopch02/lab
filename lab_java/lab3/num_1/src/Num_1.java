public class Num_1
{
    public static void main(String[] args)
    {
        print pr= new print();

        Potoc potoc_1 = new Potoc(pr);
        Potoc potoc_2 = new Potoc(pr);

        potoc_1.setName("поток 1");
        potoc_2.setName("поток 2");

        potoc_1.start();
        potoc_2.start();
    }
}
class Potoc extends Thread
{
    print pr;
    Potoc(print pr){
        this.pr=pr;
    }
    public void run(){
        while (true) {
            pr.print_1();
        }
    }
}
class print{
    public synchronized void print_1(){
        notify();

        System.out.println(Thread.currentThread().getName());
        try {
            Thread.sleep(1000);
        }
        catch (InterruptedException e){
        }
        try {
            wait();
        }
        catch (InterruptedException e) {
        }
    }
}

