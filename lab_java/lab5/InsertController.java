import java.sql.SQLException;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class InsertController {
    @FXML
    Button OK;

    @FXML
    TextField deptID;
    @FXML
    TextField deptName;

    @FXML
    void insert(ActionEvent actionEvent) {
        try {
            DepartmentDAO.insertDept(deptID.getText(), deptName.getText());
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        Stage stage = (Stage) OK.getScene().getWindow();
        stage.close();
        try {
            Controller.refresh();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}