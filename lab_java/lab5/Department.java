import javafx.beans.property.IntegerProperty;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;

public class Department {
    private IntegerProperty id;
    private StringProperty name;

    public Department() {
        this.id = new SimpleIntegerProperty();
        this.name = new SimpleStringProperty();
    }

    public int getDeptId() {
        return id.get();
    }

    public void setDeptId(int deptId) {
        this.id.set(deptId);
    }

    public IntegerProperty deptIdProperty(){
        return id;
    }

    public String getDeptName() {
        return name.get();
    }

    public void setDeptName(String deptName) {
        this.name.set(deptName);
    }

    public StringProperty deptNameProperty(){
        return name;
    }
}