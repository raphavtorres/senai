import java.util.Scanner;

public class Cliente {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Escolha uma opção:\n[0]Sou Cliente\n[1]Não Sou Cliente");
        int cliente_or_not = scanner.nextInt();

        switch (cliente_or_not) {
            case 0:
                System.out.println("Em qual perfil você se encaixa?:\n[S]ilver\n[G]old\n[P]remium");
                String perfil = scanner.next().toUpperCase();

                System.out.println("Qual o valor da sua compra?: ");
                float valor_compra = scanner.nextFloat();

                float desconto = 0;

                switch (perfil){
                    case "S":
                        desconto += valor_compra * 0.95;
                        System.out.println("Você é um cliente Silver! Seu desconto é de 5%"); // 5%
                        break;
                    case "G":
                        desconto = (float) (valor_compra * 0.85);
                        System.out.println("Você é um cliente Gold! Seu desconto é de 15%"); // 15%
                        break;
                    case "P":
                        desconto = (float) (valor_compra * 0.75);
                        System.out.println("Você é um cliente Premium! Seu desconto é de 25%"); //25%
                        break;
                }

                System.out.printf("O valor a ser pago é R$ %.2f %n", desconto);

            case 1:
                System.out.println("Apenas clientes recebem promoção! ");
        }
    }
}
