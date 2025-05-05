public class Printer {
    private PrintStrategy strategy;

    public Printer(PrintStrategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(PrintStrategy strategy) {
        this.strategy = strategy;
    }

    public void print(String document) {
        strategy.print(document);
    }
}
