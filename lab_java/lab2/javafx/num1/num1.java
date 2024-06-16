import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;
import javafx.geometry.Pos;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import java.io.InputStream;
import javafx.scene.image.Image;

public class num1 extends Application {
    public static void main(String[] args) {
        launch(args);
    }
    public void start(Stage primarystage) {
        primarystage.setTitle("num1");
        primarystage.centerOnScreen();
        primarystage.setWidth(500);
        primarystage.setHeight(500);

        InputStream iconStream = getClass().getResourceAsStream("/kekw.png");
        Image image = new Image(iconStream);
        primarystage.getIcons().add(image);

        Button btn = new Button("->");
        TextField t1 = new TextField();
        TextField t2 = new TextField();
        t1.setMaxSize(150, 30);
        t2.setMaxSize(150, 30);

        HBox root = new HBox(20, t1,btn,t2);
        root.setAlignment(Pos.CENTER);

        Scene primaryScene = new Scene(root, 250, 250);
        primarystage.setScene(primaryScene);
        
        btn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent) {
                if (btn.getText() == "->") {
                    t2.setText(t1.getText());
                    t1.setText("");
                    btn.setText("<-");
                } else {
                    t1.setText(t2.getText());
                    t2.setText("");
                    btn.setText("->");
                }

            }

        });

        primarystage.show();
    }
}