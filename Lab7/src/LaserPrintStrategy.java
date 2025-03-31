// Лазерная печать
public class LaserPrintStrategy implements PrintStrategy {
    @Override
    public void print(String document) {
        System.out.println("Печатаем лазерным принтером: " + document);
    }
}
