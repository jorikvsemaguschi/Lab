public class Main {
    public static void main(String[] args) {
        Printer printer = new Printer(new BlackAndWhitePrintStrategy());
        printer.print("Документ 1"); // Печатает черно-белым

        printer.setStrategy(new ColorPrintStrategy());
        printer.print("Документ 2"); // Печатает цветным

        printer.setStrategy(new LaserPrintStrategy());
        printer.print("Документ 3"); // Печатает лазерным
    }
}

