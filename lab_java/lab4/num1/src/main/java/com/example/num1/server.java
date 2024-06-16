package com.example.num1;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

import com.example.num1.Calculator;

public class server {
    Calculator calc=new Calculator();

    public static void main(String[] args) {
        try {
            ss = new ServerSocket(1111);
            while (true) {
                System.out.println("Waiting connection...");

                Socket clientSocket = ss.accept();

                new MyThread(clientSocket).start();

            }

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    static ServerSocket ss = null;

}

class MyThread extends Thread {
    private Socket clientSocket;

    public MyThread(Socket clientSocket) {
        this.clientSocket = clientSocket;
    }

    @Override
    public void run() {
        try {
            Socket localSocket = clientSocket;
            System.out.println("Local port: " + localSocket.getLocalPort());
            System.out.println("Remote port: " + localSocket.getPort());
            DataInputStream in = new DataInputStream(localSocket.getInputStream());
            DataOutputStream out = new DataOutputStream(localSocket.getOutputStream());

            while (true) {

                String firstN = in.readUTF();
                String what = in.readUTF();
                String secondN = in.readUTF();

                String res=in.readUTF();

                System.out.println("READ from client 1 :" + firstN);
                System.out.println("READ from client 2 :" + what);
                System.out.println("READ from client 3 :" + secondN);

                Double firstNumber = Double.valueOf(firstN);
                Double secondNumber = Double.valueOf(secondN);
                double result = 1;
                if (what.equals("+")) {
                    result = firstNumber + secondNumber;
                } else if (what.equals("-")) {
                    result = firstNumber - secondNumber;
                } else if (what.equals("*")) {
                    result = firstNumber * secondNumber;
                } else if (what.equals("/")) {
                    result = firstNumber / secondNumber;
                }

                out.writeUTF("" + result);
                out.flush();

            }



        } catch (Exception e) {
            System.out.println("Connection reset");
        }
    }
}