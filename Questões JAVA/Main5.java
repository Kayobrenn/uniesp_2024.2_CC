import java.util.Scanner;

public class Main5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("====== Folha de Pagamento ======");

        System.out.print("Digite sua matrícula: ");
        int matricula = sc.nextInt();

        sc.nextLine();

        System.out.print("Digite seu nome completo: ");
        String nome = sc.nextLine();

        System.out.print("Digite seu salário bruto: ");
        double salariobruto = sc.nextDouble();


        double descontoinss = salariobruto * 0.15;
        double salarioliquido = salariobruto - descontoinss;


        System.out.println("\n======> Dados do Funcionário <======");
        System.out.println("Matrícula: " + matricula);
        System.out.println("Nome do Funcionário: " + nome);
        System.out.printf("Salário Bruto: R$ %.2f\n", salariobruto);
        System.out.printf("Desconto INSS: R$ %.2f\n", descontoinss);
        System.out.printf("Salário Líquido: R$ %.2f\n", salarioliquido);
        System.out.println("====== FIM =======");

        sc.close();
    }
}

