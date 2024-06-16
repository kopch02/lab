module com.example.num_2 {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.num_2 to javafx.fxml;
    exports com.example.num_2;
}