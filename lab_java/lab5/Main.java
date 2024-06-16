import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.stage.WindowEvent;
import java.io.InputStream;
import javafx.scene.image.Image;

import java.io.IOException;

public class Main extends Application{
    public static void main(String[] args) {
        launch();
    }
    private static Scene scene;

    @Override
    public void start(Stage stage) throws IOException {
        scene = new Scene(loadFXML(), 654, 516);
        stage.setTitle("lab5_bd");
        InputStream iconStream = getClass().getResourceAsStream("/kekw.png");
        Image image = new Image(iconStream);
        stage.getIcons().add(image);
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
        FXMLLoader fxmlLoader = new FXMLLoader(Main.class.getResource("/view.fxml"));
        return fxmlLoader.load();
    }

}