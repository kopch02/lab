package Ex;

public class Ex {
    public class Exc2D extends Exception {
        private String msg;

        public Exc2D(String msg) {
            this.msg = msg;
        }

        public void show() {
            System.out.println(msg);
        }
    }
    public class Exc3D extends Exception {
        private String msg;

        public Exc3D( String msg) {
            this.msg = msg;
        }

        public void Out() {
            System.out.println(msg);
            
            
        }
    }
}
