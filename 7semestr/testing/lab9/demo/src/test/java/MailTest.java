

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

import java.time.Duration;

public class MailTest {
    @Test
    public void test() {
        String chromeDriverPath = "C:\\ycheba\\lab\\7semestr\\testing\\lab9\\demo\\driver\\chromedriver.exe";
        String chromeBinaryPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";

        ChromeOptions chromeOptions = new ChromeOptions();
        chromeOptions.setBinary(chromeBinaryPath); // Установка пути до браузера
        chromeOptions.addArguments("--start-maximized"); //Установка полноэкранного режима для корректного выполнения теста

        System.setProperty("webdriver.chrome.driver",chromeDriverPath); // Установка пути до драйвера
        WebDriver driver = new ChromeDriver(chromeOptions);// Установка заданных опций в WebDriver и его создание

        driver.get("https://account.mail.ru/login"); // Переход на сайт входа в почту mail.ru
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10)); // Задержка
        Assertions.assertEquals(driver.findElement(By.xpath("//input[@name='username']")), driver.switchTo().activeElement()); // Проверка на то, находится ли поле в фокусе страницы
        driver.findElement(By.xpath("//input[@name='username']")).sendKeys("testich201"); // Ввод в поле "Имя аккаунта"
        driver.findElement(By.xpath("//*[@class='inner-0-2-89 innerTextWrapper-0-2-90']")).click(); // Клик на кнопку "Ввести пароль"
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10)); // Задержка
        driver.findElement(By.xpath("//input[@name='password']")).sendKeys("toptester123"); // Ввод в поле "Пароль"
        driver.findElement(By.xpath("//*[@class='inner-0-2-89 innerTextWrapper-0-2-90']")).click(); // Клик на кнопку "Войти"
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10)); // Задержка
        driver.findElement(By.xpath("//*[@class='ph-project ph-project__account svelte-1osmzf1']")).click(); // Клик на иконку почты
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(20)); // Задержка
        WebElement name = driver.findElement(By.xpath("//*[@aria-label='Test Testich']"));
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(20)); // Задержка
        String meganame = name.getText();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(20)); // Задержка
        Assertions.assertEquals("Test Testich", meganame); // Сверка даты
        driver.findElement(By.xpath("//*[@data-click-counter='75068944']")).click(); // Клик на кнопку "Выйти"
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10)); // Задержка

        driver.quit();
    }
}