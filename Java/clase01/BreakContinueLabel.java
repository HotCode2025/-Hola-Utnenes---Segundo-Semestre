public class BreakContinueLabel {
    public static void main(String[] args) {
        // break con etiqueta: sale de ambos bucles
        outer:
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (i == 2 && j == 2) {
                    System.out.println("break outer en i=2, j=2");
                    break outer;
                }
                System.out.println("i=" + i + ", j=" + j);
            }
        }

        System.out.println("---");

        // continue con etiqueta: salta a la siguiente iteración de i
        outer2:
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (j == 2) {
                    System.out.println("continue outer2 en j=2 (salta a siguiente i)");
                    continue outer2;
                }
                System.out.println("outer2 i=" + i + ", j=" + j);
            }
        }
    }
}

