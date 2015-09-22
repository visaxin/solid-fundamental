package algorithm;
import java.util.Scanner;
/**
 * Created by jason03.zhang on 2015/9/22.
 */
public class MaxtrixUDG {
    private int mEdgNum;
    private char[] mVexs;
    private int[][] mMatrix;
    private static final int INF = Integer.MAX_VALUE;

    //USING given vexs and matrix to init graph
    public MaxtrixUDG(char[] vexs, int[][] matrix){
        //init vex numbers
        int vlen = vexs.length;
        //init vex
        mVexs = new char[vlen];
        for(int i=0;i < mVexs.length;i++)
            mVexs[i] = vexs[i];

        mMatrix = new int[vlen][vlen];
        for(int i=0;i<vlen;i++){
            for(int j=0;j<vlen;j++){
                mMatrix[i][j] = matrix[i][j];
            }
        }


        mEdgNum = 0;
        for(int i=0;i<vlen;i++)
            for(int j=i+1;j<vlen;j++)
                if(mMatrix[i][j] !=INF)
                    mEdgNum++;


    }
    //get v's closet neighborhood.
    public int firstVertex(int v){
        if(v<0 || v>(mMatrix.length-1)){
            return -1;
        }

        for(int i=0;i<mMatrix.length;i++)
            if(mMatrix[v][i]!=0 && mMatrix[v][i]!=INF)
                return i;
        return -1;
    }

    public void print(){
        System.out.println("Print Maxtrix Graph");
        for(int i=0;i<mVexs.length;i++){
            for (int j=0;j<mVexs.length;j++){
                System.out.printf("%10d", mMatrix[i][j]);
            }
            System.out.println("");
        }
    }

    /**
     *
     * @param vs start vertex
     * @param prev record vertexes that in path to target vertex
     * @param dist record the sum of weight
     */
    public void dijkstra(int vs, int[] prev,int[] dist){
        //flag means point vs to point i has been get shortest path
        boolean[] flag = new boolean[mVexs.length];
        //vs to i(i is all other poin) init
        //dist is weight between vs and i
        for(int i=0;i<mVexs.length;i++){
            flag[i] = false;
            prev[i] = 0;
            dist[i] = mMatrix[vs][i];
        }


        flag[vs] = true;
        dist[vs] = 0;
        //traversal mVexs.length-1 times to find shortest path
        int k=0;

        for(int i=0;i<mVexs.length;i++) {
            int min = INF;
            for (int j = 0; j < mVexs.length; j++) {
                if (flag[j] == false && dist[j] < min) { //when dist[j] is shortest, update min
                    min = dist[j];
                    k = j;
                }
            }
            //update prev and dist
            flag[k] = true;
            for (int j = 0; j < mVexs.length; j++) {
                //System.out.println(mMatrix[k][j]);
                int tmp = (mMatrix[i][j] == INF ? INF : (min + mMatrix[k][j]));
                //int tmp = (mMatrix[i][j] == INF?INF:(mMatrix[k][j]));
                if (flag[j] == false && (tmp < dist[j])) {
                    dist[j] = tmp;
                    prev[j] = k;
                }
            }
        }

        System.out.printf("dijkstra(%c): \n",mVexs[vs]);
        for(int i=0;i<mVexs.length;i++)
            System.out.printf(" shortest(%c,%c) = %d\n",mVexs[vs],mVexs[i],dist[i]);


    }


    public static void main(String[] args){
        char [] vexs = {'A', 'B', 'C', 'D', 'E', 'F', 'G'};
        int matrix[][] = {
                 /*A*//*B*//*C*//*D*//*E*//*F*//*G*/
          /*A*/ {   0,  12, INF, INF, INF,  16,  14},
          /*B*/ {  12,   0,  10, INF, INF,   7, INF},
          /*C*/ { INF,  10,   0,   3,   5,   6, INF},
          /*D*/ { INF, INF,   3,   0,   4, INF, INF},
          /*E*/ { INF, INF,   5,   4,   0,   2,   8},
          /*F*/ {  16,   7,   6, INF,   2,   0,   9},
          /*G*/ {  14, INF, INF, INF,   8,   9,   0}};

        MaxtrixUDG m = new MaxtrixUDG(vexs,matrix);
        m.print();
        //System.out.println(m.firstVertex(1));
        int[] prev = new int[m.mVexs.length];
        int[] dist = new int[m.mVexs.length];
        m.dijkstra(0,prev,dist);
    }
}
