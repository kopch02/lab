package com.example.num_2;

import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.scene.control.Label;

public class HelloController {
    @FXML
    Label welcomeText=new Label();
    @FXML
    Label potoc_text=new Label();
    @FXML
    Label potoc_text_2=new Label();

    @FXML
    protected void onHelloButtonClick() {
        while (true) {
            welcomeText.setText("0");
        }
    }
    @FXML
    protected void potoc_1() {
        Potoc potoc_1 = new Potoc();
        potoc_1.start();
    }
    @FXML
    protected void potoc_2(){
        Potoc_2 potoc_2=new Potoc_2();
    }
    class Potoc extends Thread{
        int x =0;
        public void run(){
            while (true) {
                try {
                    Thread.sleep(20);
                }
                catch (InterruptedException e){
                }
                Platform.runLater(new Runnable() {
                    @Override
                    public void run() {
                        x++;
                        potoc_text.setText(""+x);
                    }
                });
            }
        }
    }

    class Potoc_2 implements Runnable{
        Thread thread;
        int x=0;
        Potoc_2(){
            thread=new Thread(this,"potoc_2");
            thread.start();
        }
        @Override
        public void run() {
            while (true) {
                try {
                    Thread.sleep(20);
                } catch (InterruptedException e) {
                }
                Platform.runLater(new Runnable() {
                    @Override
                    public void run() {
                        x++;
                        potoc_text_2.setText("" + x);
                    }
                });
            }
        }
    }
}
