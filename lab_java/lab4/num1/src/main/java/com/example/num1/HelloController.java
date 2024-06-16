package com.example.num1;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.layout.Pane;
import javafx.scene.control.TextField;

//import javax.naming.Context;
//import javax.naming.InitialContext;
//import javax.naming.NamingException;
import java.util.Properties;



public class HelloController {
    @FXML
    Button button0=new Button();
    @FXML
    Button button1=new Button();
    @FXML
    Button button2=new Button();
    @FXML
    Button button3=new Button();
    @FXML
    Button button4=new Button();
    @FXML
    Button button5=new Button();
    @FXML
    Button button6=new Button();
    @FXML
    Button button7=new Button();
    @FXML
    Button button8=new Button();
    @FXML
    Button button9=new Button();
    @FXML
    Button button_plus=new Button();
    @FXML
    Button button_minus=new Button();
    @FXML
    Button button_mult=new Button();
    @FXML
    Button button_devision=new Button();
    @FXML
    Button button_sbros=new Button();
    @FXML
    Button button_final=new Button();
    @FXML
    Pane pane=new Pane();
    @FXML
    TextField displayTextField=new TextField();

    Calculator calculator = new Calculator();

    @FXML
    private void initialize() {
        System.out.println("initialize()");
        displayTextField.setText("0");

        button1.setOnAction(event -> displayTextField.setText(calculator.addNumber("1")));
        button2.setOnAction(event -> displayTextField.setText(calculator.addNumber("2")));
        button3.setOnAction(event -> displayTextField.setText(calculator.addNumber("3")));
        button4.setOnAction(event -> displayTextField.setText(calculator.addNumber("4")));
        button5.setOnAction(event -> displayTextField.setText(calculator.addNumber("5")));
        button6.setOnAction(event -> displayTextField.setText(calculator.addNumber("6")));
        button7.setOnAction(event -> displayTextField.setText(calculator.addNumber("7")));
        button8.setOnAction(event -> displayTextField.setText(calculator.addNumber("8")));
        button9.setOnAction(event -> displayTextField.setText(calculator.addNumber("9")));
        button0.setOnAction(event -> displayTextField.setText(calculator.addNumber("0")));
        button_plus.setOnAction(event -> {
            calculator.addOperator("+");
            displayTextField.setText("");
        });
        button_minus.setOnAction(event -> {
            calculator.addOperator("-");
            displayTextField.setText("");
        });
        button_mult.setOnAction(event -> {
            calculator.addOperator("*");
            displayTextField.setText("");
        });
        button_devision.setOnAction(event -> {
            calculator.addOperator("/");
            displayTextField.setText("");
        });
        button_sbros.setOnAction(event -> displayTextField.setText(""));
    }
    /*
    private void doRequest(String[] data) throws NamingException, MyException {
        Properties props = new Properties();
        props.put(Context.INITIAL_CONTEXT_FACTORY, "org.wildfly.naming.client.WildFlyInitialContextFactory");
//        props.put(Context.URL_PKG_PREFIXES, "org.jboss.ejb.client.naming");
//        props.put(Context.PROVIDER_URL, "remote+http://localhost:8080");
        props.put(Context.PROVIDER_URL, "http-remoting://localhost:8080");
//        props.put("jboss.naming.client.ejb.context", "true");
//        props.put(Context.SECURITY_PRINCIPAL, "admin");
//        props.put(Context.SECURITY_CREDENTIALS, "123");
        Context ctx = new InitialContext(props);
        //System.out.println(ctx.getEnvironment());

        CalcRemote calcRemote = (CalcRemote) ctx.lookup("Calc_ear_exploded/ejb/CalcSessionEJB!com.calc.server.CalcRemote");    //java:jboss/exported/Calc_ear_exploded/ejb/CalcSessionEJB!com.calc.server.CalcRemote
        String res = Integer.toString(process(calcRemote, data));
        displayTextField.setText(res);
        System.out.println(res);
    }*/

    private int process(CalcRemote calcRemote, String[] resData) throws MyException {
        int operand1 = Integer.parseInt(resData[0]);
        int operand2 = Integer.parseInt(resData[1]);
        String operator = resData[2];
        switch (operator) {
            case "+":
                return calcRemote.add(operand1, operand2);
            case "-":
                return calcRemote.sub(operand1, operand2);
            case "*":
                return calcRemote.mul(operand1, operand2);
            case "/":
                return calcRemote.div(operand1, operand2);
        }
        return 0;
    }

    @Override
    public void run() {
        displayTextField.setText("WAITING...");
        try {
            doRequest(calculator.getResult());
        } catch (MyException ex) {
            displayTextField.setText(ex.getMessage());
        }
    }

}