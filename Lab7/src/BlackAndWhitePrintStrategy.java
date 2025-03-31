// Черно-белая печать
public class BlackAndWhitePrintStrategy implements PrintStrategy {
    @Override
    public void print(String document) {
        System.out.println("Печатаем черно-белый документ: " + document);
    }
}
