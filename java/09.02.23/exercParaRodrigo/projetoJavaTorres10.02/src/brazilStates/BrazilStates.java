package brazilStates;

import java.util.Arrays;
import java.util.Scanner;

public class BrazilStates {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        String[] state_name = {"Acre", "Alagoas", "amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernanbuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"};
        String[] state_code = {"AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"};
        int[] state_population = {111};

        System.out.println("Write the name of the state you want to know about: ");
        String state_user = scanner.next();

        int state_index = Arrays.asList(state_name).indexOf(state_user);

        System.out.println("State: " + state_name[state_index]);
        System.out.println("Code: " + state_code[state_index]);
        System.out.println("State Population: " + state_population[state_index]);

    }
}
