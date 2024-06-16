

import java.io.IOException;
import java.sql.SQLException;

import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ContextMenu;
import javafx.scene.control.MenuItem;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseButton;
import javafx.scene.input.MouseEvent;
import javafx.stage.Modality;
import javafx.stage.Stage;

public class Controller {
    @FXML
    Button filter;

    @FXML
    TextField filterData;
    
    @FXML
    TableView<Department> deptTable;
    @FXML
    static TableView<Department> deptTableCopy;


    @FXML
    TableColumn<Department, Integer> deptIdCol;

    @FXML
    TableColumn<Department, String> deptNameCol;

    @FXML
    void initialize() {
        deptIdCol.setCellValueFactory(cellData -> cellData.getValue().deptIdProperty().asObject());
        deptNameCol.setCellValueFactory(cellData -> cellData.getValue().deptNameProperty());

        ContextMenu contextMenu = new ContextMenu();

        MenuItem act1 = new MenuItem("Insert");
        contextMenu.getItems().add(act1);

        MenuItem act2 = new MenuItem("Update");
        contextMenu.getItems().add(act2);

        MenuItem act3 = new MenuItem("Delete");
        contextMenu.getItems().add(act3);

        deptTable.addEventHandler(MouseEvent.MOUSE_CLICKED, new EventHandler<MouseEvent>() {

            @Override
            public void handle(MouseEvent click) {
                if (click.getButton() == MouseButton.SECONDARY) {
                    contextMenu.show(deptTableCopy, click.getScreenX(), click.getScreenY());
                }
            }
        });

        act1.setOnAction(event -> {
            try {
                insertDept();
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
        });

        act2.setOnAction(event -> {
            try {
                updateDeptName();
            } catch (IOException e) {
                e.printStackTrace();
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }
        });

        act3.setOnAction(event -> {
            try {
                deleteDept();
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        });
        deptTableCopy = deptTable;
        try {
            refresh();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    @FXML
    static void populateDepartment(ObservableList<Department> deptData) throws ClassNotFoundException {
        deptTableCopy.setItems(deptData);
    }

    @FXML
    public static void refresh() throws ClassNotFoundException, SQLException {
        try {
            ObservableList<Department> deptData = DepartmentDAO.searchDepartments();
            populateDepartment(deptData);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
            throw e;
        }
    }

    @FXML
    void filterDepartments(ActionEvent actionEvent) throws ClassNotFoundException, SQLException {
        try {
            String query = filterData.getText();
            if (query == ""){
                refresh();
                return;
            }
            ObservableList<Department> deptData = DepartmentDAO.filterDepartments(query);
            populateDepartment(deptData);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
            throw e;
        }
    }

    @FXML
    void updateDeptName() throws ClassNotFoundException, IOException {
        try {
            Stage stage = new Stage();
            Parent root = FXMLLoader.load(getClass().getResource("/updateView.fxml"));
            Scene scene = new Scene(root);
            stage.setScene(scene);
            stage.setResizable(false);
            stage.initModality(Modality.WINDOW_MODAL);
            stage.initOwner(deptTable.getScene().getWindow());
            stage.show();
            refresh();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    @FXML
    void insertDept() throws ClassNotFoundException, IOException {
        try {
            Stage stage = new Stage();
            Parent root = FXMLLoader.load(getClass().getResource("/insertView.fxml"));
            Scene scene = new Scene(root);
            stage.setScene(scene);
            stage.setResizable(false);
            stage.initModality(Modality.WINDOW_MODAL);
            stage.initOwner(deptTable.getScene().getWindow());
            stage.show();
        } catch (IOException e) {
            System.out.println(e.getMessage());
            throw e;
        }
    }

    @FXML
    void deleteDept() throws SQLException, ClassNotFoundException {
        try {
            String id = String.valueOf(deptTable.getSelectionModel().getSelectedItem().getDeptId());
            DepartmentDAO.deleteDeptWithId(id);
            refresh();
        } catch (SQLException e) {
            System.out.println(e.getMessage());
            throw e;
        }
    }

}