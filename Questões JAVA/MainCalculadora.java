import java.util.Scanner;

public class MainCalculadora {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Calc c = new Calc();

        System.out.print("Digite o primeiro número:");
        c.n1 = sc.nextInt();

        System.out.print("Digite o segundo número:");
        c.n2 = sc.nextInt();

        System.out.print("Digite o operador (+,*,-,/):");
        char operador = sc.next().charAt(0);


        switch (operador){
            case '+':
                c.somar();
                System.out.println("Resultado: " + c.resultado1);
                break;

            case '-':
                c.subtrair();
                System.out.println("Resultado: " + c.resultado2);
                break;

            case '*':
                c.multiplicar();
                System.out.println("Resultado: " + c.resultado3);
                break;

            case '/':
                c.dividir();
                System.out.println("Resultado: " + c.resultado4);
                break;
            default:
                throw new IllegalStateException("Unexpected value: " + operador);
        }
    }
}

