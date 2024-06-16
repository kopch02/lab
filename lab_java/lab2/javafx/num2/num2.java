import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
//import javafx.scene.Group;
//import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.stage.Stage;
import javafx.geometry.Pos;
//import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import java.io.InputStream;
import java.io.FileInputStream; 
import java.io.FileNotFoundException;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;

public class num2 extends Application {
    public static void main(String[] args) {
        launch(args);
    }
    public void start(Stage primarystage) throws FileNotFoundException{
        primarystage.setTitle("num2");
        primarystage.centerOnScreen();
        primarystage.setWidth(500);
        primarystage.setHeight(500);

        InputStream iconStream = getClass().getResourceAsStream("/kekw.png");
        Image image = new Image(iconStream);
        primarystage.getIcons().add(image);

        CheckBox check1 = new CheckBox("");
        CheckBox check2 = new CheckBox("");
        CheckBox check3 = new CheckBox("");

        Image image_apchi = new Image(new FileInputStream("4semestr/iap/lab2/javafx/num2/images/apchi.gif"));
        Image image_chupa = new Image(new FileInputStream("4semestr/iap/lab2/javafx/num2/images/chupa.gif"));
        Image image_nezuko = new Image(new FileInputStream("4semestr/iap/lab2/javafx/num2/images/nezuko.gif"));

        ImageView view_apchi = new ImageView(image_apchi);
        view_apchi.setFitHeight(100); 
        view_apchi.setFitWidth(100);    
        view_apchi.setPreserveRatio(true);
        HBox box_check1 = new HBox(20, view_apchi,check1);
        box_check1.setAlignment(Pos.CENTER);

        ImageView view_chupa = new ImageView(image_chupa);
        view_chupa.setFitHeight(100); 
        view_chupa.setFitWidth(100);    
        view_chupa.setPreserveRatio(true);
        HBox box_check2 = new HBox(20, view_chupa,check2);
        box_check2.setAlignment(Pos.CENTER);

        ImageView view_nezuko = new ImageView(image_nezuko);
        view_nezuko.setFitHeight(100); 
        view_nezuko.setFitWidth(100);    
        view_nezuko.setPreserveRatio(true);
        HBox box_check3 = new HBox(20, view_nezuko,check3);
        box_check3.setAlignment(Pos.CENTER);    

        HBox box = new HBox(20, box_check1,box_check2,box_check3);

        Scene groupScene = new Scene( box, 250,250);
        
        //Scene boxScene = new Scene(box_check1, 250,250);

        primarystage.setScene(groupScene);

        check1.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent1) {
                if (check1.isSelected()) {
                    view_apchi.setOpacity(100);
                } else {
                    view_apchi.setOpacity(0);
                }

            }
        });
        check2.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent1) {
                if (check2.isSelected()) {
                    view_chupa.setOpacity(100);
                } else {
                    view_chupa.setOpacity(0);
                }

            }
        });
        check3.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent1) {
                if (check3.isSelected()) {
                    view_nezuko.setOpacity(100);
                } else {
                    view_nezuko.setOpacity(0);
                }

            }
        });
        view_apchi.setOpacity(0);
        view_chupa.setOpacity(0);
        view_nezuko.setOpacity(0);

        primarystage.show();
        
    }
}