package com.example.num1;

import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.stage.WindowEvent;

import java.io.IOException;

public class Calculator extends Application{
    public static void main(String[] args) {
        launch();
    }
    private static Scene scene;

    @Override
    public void start(Stage stage) throws IOException {
        scene = new Scene(loadFXML(), 387, 588);
        stage.setScene(scene);
        stage.show();
        stage.setOnCloseRequest(new EventHandler<WindowEvent>() {
            public void handle(WindowEvent e) {
                System.out.println("Shutting down");
                System.exit(0);
            }
        });
    }

    static void setRoot(String fxml) throws IOException {
        scene.setRoot(loadFXML());
    }

    private static Parent loadFXML() throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(Calculator.class.getResource("/view.fxml"));
        return fxmlLoader.load();
    }

    private String buffer = "", operator, operand1, operand2;
    private boolean isOperator = false;

    public String addNumber(String value) {
        buffer += value;
        if (!isOperator) {
            operand1 = buffer;
        } else {
            operand2 = buffer;
        }
        return buffer;
    }

    public void addOperator(String value) {
        operator = value;
        buffer = "";
        isOperator = true;
    }

    public String[] getResult()  {
        isOperator = false;
        buffer = "";
        int check;

        check = Integer.parseInt(operand1);
        check = Integer.parseInt(operand2);

        return new String[]{operand1, operand2, operator};
    }

}