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
import javafx.scene.layout.VBox;
import java.io.InputStream;
import java.io.FileInputStream; 
import java.io.FileNotFoundException;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;

public class num3 extends Application {
    public static void main(String[] args) {
        launch(args);
    }
    public void start(Stage primarystage) throws FileNotFoundException{
        primarystage.setTitle("num3");
        primarystage.centerOnScreen();
        primarystage.setWidth(700);
        primarystage.setHeight(500);

        InputStream iconStream = getClass().getResourceAsStream("/kekw.png");
        Image image = new Image(iconStream);
        primarystage.getIcons().add(image);

        CheckBox check1 = new CheckBox("");
        CheckBox check2 = new CheckBox("");
        CheckBox check3 = new CheckBox("");

        Image image_kompot = new Image(new FileInputStream("4semestr/iap/lab2/javafx/num3/images/kompot.jpg"));
        Image image_makarony = new Image(new FileInputStream("4semestr/iap/lab2/javafx/num3/images/makarony.jpg"));
        Image image_svinina = new Image(new FileInputStream("4semestr/iap/lab2/javafx/num3/images/svinina.jpg"));

        ImageView view_kompot= new ImageView(image_kompot);
        view_kompot.setFitWidth(130);
        view_kompot.setFitHeight(100);
        ImageView view_makarony=new ImageView(image_makarony);
        view_makarony.setFitWidth(130);
        view_makarony.setFitHeight(100);
        ImageView view_svinina=new ImageView(image_svinina);
        view_svinina.setFitWidth(130);
        view_svinina.setFitHeight(100);

        check1.setLayoutX(215);
        check1.setLayoutY(192);

        VBox box1 = new VBox(view_kompot,check1);
        VBox box2 = new VBox(view_makarony,check2);
        VBox box3 = new VBox(view_svinina,check3);

        VBox box = new VBox(box1,box2,box3);

        Scene Scene = new Scene( box, 250,250);

        primarystage.setScene(Scene);

        primarystage.show();
        
    }
}