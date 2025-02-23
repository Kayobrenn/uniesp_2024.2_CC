import java.util.Locale;
import java.util.Scanner;

public class Main3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.useLocale(Locale.US);

        System.out.println("Digite qual é a primeira nota:");
        double nota1 = sc.nextDouble();
        System.out.println("Digite qual a segunda nota:");
        double nota2 = sc.nextDouble();
        System.out.println("Digite qual a terceira nota:");
        double nota3 = sc.nextDouble();

        double resultado = (nota1 + nota2 + nota3) / 3;

        if (resultado >= 7.0) {
            System.out.println("Aluno Aprovado!!!");
        } else if (resultado < 4.0) {
            System.out.println("Aluno Reprovado!!!");
        } else {
            System.out.println("Aluno está na Final!!!");
        }

        sc.close();
    }
}

