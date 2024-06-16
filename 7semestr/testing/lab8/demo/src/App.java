import lib.CoreTestCase;
import lib.ui.SearchPageObject;


public class App extends CoreTestCase {
    @Override
    protected void setUp() throws Exception {
        super.setUp();
    }

    public void test() {
        SearchPageObject searchPageObject = new SearchPageObject(driver);

        searchPageObject.initSearchInput(); // Нажатие на поле ввода
        searchPageObject.typeSearchLine("Хоббит, или Туда и обратно"); // Ввод в поле ввода
        searchPageObject.waitForSearchResult("Хоббит, или Туда и обратно"); // Нажатие на статью
        searchPageObject.clickPageSaveAndAddToList("Хоббит"); // Сохранение статьи в список для чтения
        searchPageObject.viewListAndDeleteHim(); // Просмотр списка и его удаление
    }
}