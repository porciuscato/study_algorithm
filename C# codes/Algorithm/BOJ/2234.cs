using System;
using System.IO;
using System.Text;
using System.Collections.Generic;

namespace BOJ
{
    class BOJ2234
    {
        static int ROW, COL;
        static int[,] Delta = new int[4, 2] { { 0, -1 }, { -1, 0 }, { 0, 1 }, { 1, 0 } };
        static Node[,] Castle;

        static int maxRoomSize = 0, roomCount = 0, maxWallSize = 0;

        static StringBuilder sb = new StringBuilder();
        static StreamReader sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
        static StreamWriter sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));

        public static void Start()
        {
            string[] inputs = sr.ReadLine().Split();
            COL = int.Parse(inputs[0]);
            ROW = int.Parse(inputs[1]);
            Castle = new Node[ROW, COL];

            for (int i = 0; i < ROW; i++)
            {
                inputs = sr.ReadLine().Split();
                for (int j = 0; j < COL; j++)
                {
                    int val = int.Parse(inputs[j]);

                    Castle[i, j] = new Node(i, j);
                    for (int k = 0; k < 4; k++)
                    {
                        if (val == (val | 1 << k)) continue;

                        Castle[i, j].adjcents.Add(new adjNode(i + Delta[k, 0], j + Delta[k, 1]));
                    }
                }
            }

            Grouping();
            GetMaxCombi();

            sw.WriteLine(sb.ToString());
            sb.Clear();
            sw.Flush();
        }

        public static void Grouping()
        {
            bool[,] visited = new bool[ROW, COL];

            for (int i = 0; i < ROW; i++)
            {
                for (int j = 0; j < COL; j++)
                {
                    if (!visited[i, j])
                    {
                        int roomSize = 0;

                        roomCount++;
                        Castle[i, j].roomNum = roomCount;

                        List<adjNode> list = new List<adjNode> { };
                        int front = -1, tail = 0;

                        list.Add(new adjNode(i, j));
                        visited[i, j] = true;

                        while (front != tail)
                        {
                            front++;
                            roomSize++;
                            int r = list[front].row;
                            int c = list[front].col;

                            foreach (adjNode node in Castle[r, c].adjcents)
                            {
                                if (!visited[node.row, node.col])
                                {
                                    tail++;
                                    list.Add(new adjNode(node.row, node.col));
                                    visited[node.row, node.col] = true;
                                    Castle[node.row, node.col].roomNum = roomCount;
                                }
                            }
                        }

                        foreach (adjNode node in list)
                        {
                            Castle[node.row, node.col].roomSize = roomSize;
                        }
                        maxRoomSize = Math.Max(maxRoomSize, roomSize);
                    }
                }
            }

            sb.Append(roomCount.ToString() + "\n");
            sb.Append(maxRoomSize.ToString() + "\n");
        }

        public static void GetMaxCombi()
        {
            for (int i = 0; i < ROW; i++)
            {
                for (int j = 0; j < COL; j++)
                {
                    for (int k = 0; k < 4; k++)
                    {
                        int r = i + Delta[k, 0];
                        int c = j + Delta[k, 1];
                        if (r >= 0 && r < ROW && c >= 0 && c < COL)
                        {
                            if (Castle[i, j].roomNum != Castle[r, c].roomNum)
                            {
                                maxWallSize = Math.Max(maxWallSize, Castle[i, j].roomSize + Castle[r, c].roomSize);
                            }
                        }
                    }
                }
            }

            sb.Append(maxWallSize.ToString());
        }

        public class adjNode
        {
            public int row { get; set; }
            public int col { get; set; }

            public adjNode(int r, int c)
            {
                this.row = r;
                this.col = c;
            }
        }

        public class Node
        {
            public int row { get; set; }
            public int col { get; set; }
            public int roomNum { get; set; }
            public int roomSize { get; set; }
            public List<adjNode> adjcents;

            public Node(int r, int c)
            {
                this.row = r;
                this.col = c;
                adjcents = new List<adjNode> { };
            }
        }
    }
    class Program
    {
        static void Main()
        {
            BOJ2234.Start();
        }
    }
}
