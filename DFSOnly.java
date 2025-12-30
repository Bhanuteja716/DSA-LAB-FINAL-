import java.util.Scanner;

public class DFSOnly {

    static int MAX = 10;
    static int[][] graph = new int[MAX][MAX];
    static boolean[] visited;
    static int nodeCount;

    static void dfs(int node) {
        visited[node] = true;
        System.out.print(node + " ");

        for (int i = 0; i < nodeCount; i++) {
            if (graph[node][i] == 1 && !visited[i]) {
                dfs(i);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of nodes: ");
        nodeCount = sc.nextInt();

        graph = new int[nodeCount][nodeCount];
        visited = new boolean[nodeCount];

        System.out.println("Enter adjacency matrix:");
        for (int i = 0; i < nodeCount; i++) {
            for (int j = 0; j < nodeCount; j++) {
                graph[i][j] = sc.nextInt();
            }
        }

        System.out.print("Enter starting node (0-based index): ");
        int start = sc.nextInt();

        System.out.print("DFS Traversal: ");
        dfs(start);

        sc.close();
    }
}
