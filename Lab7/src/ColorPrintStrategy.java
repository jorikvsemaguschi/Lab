// Цветная печать
public class ColorPrintStrategy implements PrintStrategy {
    @Override
    public void print(String document) {
        System.out.println("Печатаем цветной документ: " + document);
    }
}
