module com.example.num1 {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.num1 to javafx.fxml;
    exports com.example.num1;
}