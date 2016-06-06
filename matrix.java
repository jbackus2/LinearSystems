
public class Matrix {

    int[][] matrix;
    final int n, m;

    public int[] getRow(int a) {
        int[] row = new int[n];
        row = matrix[a];
        return row;
    }
    //This returns a given row, namely row a.
    public int[] getColm(int b) {
        int[] colm = new int[m];
        for (int i = 0; i <= m; i++) {
            colm[i] = matrix[i][b];
        }
        return colm;
    }
    //This returns a given ccolumn, namely column b.
    public int getNumRow() {
        return n;
    }
    //This returns the number of rows.
    public int netNumCol() {
        return m;
    }
    //This returns the number of columns. 


    public void setRow(int a, int[] rr) {
        try {
            matrix[a] = rr;
        }
        catch (IndexOutOfBoundsException e) {
            System.err.println("Matrix has " + n + " rows, attempted " + a + " on setRow()");
        }
    } 
    public void setColm(int b, int[] rr) {
        try {
            for(int i =0; i<=m; i++) 
                matrix[i][b] = rr[i];
        }
        catch (IndexOutOfBoundsException e) {
            System.err.println("Matrix has " + m + " coluumns, attempted " + b + " on setColm()");
        }
    } 
}