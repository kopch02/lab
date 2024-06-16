module col {
    requires javafx.controls;
    requires javafx.fxml;

    opens col to javafx.fxml;
    exports col;
}
