import java.util.Scanner;

public class BFSOnly {

    static int MAX = 10;
    static int[][] graph = new int[MAX][MAX];
    static int nodeCount;

    static void bfs(int start) {
        boolean[] visited = new boolean[nodeCount];
        int[] queue = new int[nodeCount];

        int front = 0, rear = 0;

        visited[start] = true;
        queue[rear++] = start;

        while (front < rear) {
            int node = queue[front++];
            System.out.print(node + " ");

            for (int i = 0; i < nodeCount; i++) {
                if (graph[node][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    queue[rear++] = i;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of nodes: ");
        nodeCount = sc.nextInt();

        System.out.println("Enter adjacency matrix:");
        for (int i = 0; i < nodeCount; i++) {
            for (int j = 0; j < nodeCount; j++) {
                graph[i][j] = sc.nextInt();
            }
        }

        System.out.print("Enter starting node (0-based index): ");
        int start = sc.nextInt();

        System.out.print("BFS Traversal: ");
        bfs(start);

        sc.close();
    }
}
