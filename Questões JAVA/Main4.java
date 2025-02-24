import java.util.Scanner;

public class Main4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite o valor bruto do seu sálario:");
        double salario = sc.nextDouble();

        if (salario <= 900) {
            System.out.println("Isento de Imposto de Renda");
        } else if (salario <= 1500) {
            System.out.println("Desconto de 5% do seu salario bruto para o IRPF");
        } else if (salario <= 2500) {
            System.out.println("Desconto de 10% do seu salario bruto para o IRPF");
        } else if (salario > 2500) {
            System.out.println("Desconto de 20% do seu salario bruto para o IRPF");

        }
    }
}
