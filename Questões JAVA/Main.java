import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Pessoa persona = new Pessoa();

        System.out.print("Digite o seu nome: ");
        persona.nome = sc.nextLine();

        System.out.print("Digite a sua idade: ");
        persona.idade = sc.nextInt();

        System.out.print("Digite a sua altura: ");
        persona.altura = sc.nextDouble();

        System.out.println("Idade antes do aniversário: " + persona.idade);
        persona.fazAniversario();
        System.out.println("Idade após o aniversário: " + persona.idade);

        sc.close();
    }
}
