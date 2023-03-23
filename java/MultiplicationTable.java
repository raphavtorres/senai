public class MultiplicationTable {
    public static void main(String[] args){

        int[][] table = new int[11][11];

        for(int row = 0; row < 11; row++){
            for(int column = 0; column < 11; column++){
                table[row][column] = column * row;
                System.out.print(table[row][column] + "\t");
            }
            System.out.println();
        }
    }
}
