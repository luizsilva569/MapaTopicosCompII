import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        String texto;

        while (true) {
            System.out.print("Digite uma palavra (ou 'sair' para encerrar): ");
            texto = scan.next();
    
            // Verifica se o usuário digitou sair
            if (texto.equalsIgnoreCase("sair")) {
                System.out.println("Sistema encerrado.");
                break; 
            }
            System.out.println("Você digitou: " + texto);
        }
        scan.close();
    }
}
