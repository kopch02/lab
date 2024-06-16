package col;

import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.scene.*;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

import java.util.ArrayList;
import javafx.scene.shape.*;

public class Collision extends Application {

  private ArrayList<Shape> nodes;

  public static void main(String[] args) { launch(args); }

  @Override public void start(Stage primaryStage) {
    primaryStage.setTitle("Drag circles around to see collisions");
    Group root = new Group();
    Scene scene = new Scene(root, 400, 400);

    nodes = new ArrayList<>();                  //массив со всеми фигурами которые нужно проверять
    nodes.add(new Circle(15, 15, 30));          
    nodes.add(new Circle(90, 60, 30));
    nodes.add(new Circle(40, 200, 30));
    for (Shape block : nodes) {                 //перемещение фигур с сомощью мыши
      setDragListeners(block);
    }
    root.getChildren().addAll(nodes);           //добавление массива с фигурами хз куда                
    checkShapeIntersection(nodes.get(nodes.size() - 1));   //проверка 

    primaryStage.setScene(scene);
    primaryStage.show();
  }

  //функция которая перетаскивает круги мышкой
  public void setDragListeners(final Shape block) {
    final Delta dragDelta = new Delta();

    block.setOnMousePressed(new EventHandler<MouseEvent>() {
      @Override public void handle(MouseEvent mouseEvent) {
        // record a delta distance for the drag and drop operation.
        dragDelta.x = block.getLayoutX() - mouseEvent.getSceneX();
        dragDelta.y = block.getLayoutY() - mouseEvent.getSceneY();
        block.setCursor(Cursor.NONE);
      }
    });
    block.setOnMouseReleased(new EventHandler<MouseEvent>() {
      @Override public void handle(MouseEvent mouseEvent) {
        block.setCursor(Cursor.HAND);
      }
    });
    block.setOnMouseDragged(new EventHandler<MouseEvent>() {
      @Override public void handle(MouseEvent mouseEvent) {
        block.setLayoutX(mouseEvent.getSceneX() + dragDelta.x);
        block.setLayoutY(mouseEvent.getSceneY() + dragDelta.y);
        checkShapeIntersection(block);
      }
    });
  }

  private void checkShapeIntersection(Shape block) {
    boolean collisionDetected = false;
    for (Shape static_bloc : nodes) {   //цикл в котором перебирают все фигуры
                                        //static_bloc - это те, которые не двигаются в данный момент
      if (static_bloc != block) {       
        static_bloc.setFill(Color.GREEN);      //закрашивает не выбранные фигуры зелёным
                                                //выбранная это block - поступает в функцию

        Shape intersect = Shape.intersect(block, static_bloc);  //создание переменной пересечения между выбранной фигурой и остальными
        if (intersect.getBoundsInLocal().getWidth() != -1) {  //получение локальных грониц
                                                                //получение ширины можду этими границами 
                                                                //если эта ширина 
          collisionDetected = true;
        }
      }
    }

    if (collisionDetected) {        //что делать на основе проверки
      block.setFill(Color.BLUE);
    } else {
      block.setFill(Color.GREEN);
    }
  }

  class Delta { double x, y; }
}