import java.sql.ResultSet;
import java.sql.SQLException;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;

public class DepartmentDAO {

    public static Department searchDepartment(String deptId) throws SQLException, ClassNotFoundException {
        String select = "select * from department where id = " + deptId;

        try {
            ResultSet rsDept = DBUtil.dbExecuteQuery(select);
            Department department = getDepartmentFromRs(rsDept);
            return department;
        } catch (SQLException e) {
            System.out.println(e.getMessage());
            throw e;
        }

    }

    public static Department getDepartmentFromRs(ResultSet rs) throws SQLException {
        Department dept = null;
        if (rs.next()) {
            dept = new Department();
            dept.setDeptId(rs.getInt("id"));
            dept.setDeptName(rs.getString("name"));
        }
        return dept;
    }

    public static ObservableList<Department> searchDepartments() throws SQLException, ClassNotFoundException {
        String select = "select * from department";

        try {
            ResultSet rsDepts = DBUtil.dbExecuteQuery(select);
            // A list that allows listeners to track changes when they occur.
            ObservableList<Department> deptList = getDepartmentsList(rsDepts);
            return deptList;
        } catch (SQLException e) {
            System.out.println(e.getMessage());
            throw e;
        }
    }

    public static ObservableList<Department> filterDepartments(String selectData)
            throws SQLException, ClassNotFoundException {

        String select = "select * from department where " + selectData;  
        try {
            ResultSet rsDepts = DBUtil.dbExecuteQuery(select);
            ObservableList<Department> deptlist = getDepartmentsList(rsDepts);
            return deptlist;
        } catch (SQLException e) {
            System.out.println(e.getMessage());
            throw e;
        }

    }

    public static ObservableList<Department> getDepartmentsList(ResultSet rs)
            throws SQLException, ClassNotFoundException {
        // A list that allows listeners to track changes when they occur.
        ObservableList<Department> deptList = FXCollections.observableArrayList();

        while (rs.next()) {
            Department dept = new Department();
            dept.setDeptId(rs.getInt("id"));
            dept.setDeptName(rs.getString("name"));
            deptList.add(dept);
        }
        return deptList;
    }

    public static void updateDeptName(String deptId, String deptNewName) throws SQLException, ClassNotFoundException {
        String update = "update department\n set name ='"
                + deptNewName + "' \n where id = "
                + deptId;
        try {
            DBUtil.dbExecuteUpdate(update);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
            throw e;
        }
    }

    public static void deleteDeptWithId(String deptId) throws SQLException, ClassNotFoundException {
        String update = "delete from department\n where id = " + deptId;

        try {
            DBUtil.dbExecuteUpdate(update);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
            throw e;
        }
    }

    public static void insertDept(String id, String name) throws SQLException, ClassNotFoundException {
        String update = "insert into department\n values (" + id + ", '" + name + "')";

        try {
            DBUtil.dbExecuteUpdate(update);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
            throw e;
        }
    }
}