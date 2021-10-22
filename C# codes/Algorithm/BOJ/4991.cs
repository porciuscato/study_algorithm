using System;
using System.IO;
using System.Text;
using System.Collections.Generic;

namespace BOJ
{
    class BOJ4491
    {
        static int W, H, ans, dust_count;
        static char[,] room;
        static Coordinate Robot = new Coordinate();
        static List<Coordinate> Dusts;
        static int[] RobotToDusts;
        static int[,] DustsToDusts;
        static int[,] Delta = { { 0, -1 }, { -1, 0 }, { 0, 1 }, { 1, 0 } };

        static StringBuilder sb = new StringBuilder();
        static StreamReader sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
        static StreamWriter sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));

        public static void Start()
        {
            string[] inputs = sr.ReadLine().Split();
            W = int.Parse(inputs[0]);
            H = int.Parse(inputs[1]);

            while (!(W == 0 && H == 0))
            {
                Set();
                CalcRobotToDusts();

                bool flag = true;
                foreach (int i in RobotToDusts)
                {
                    if (i == -1)
                    {
                        sb.Append("-1\n");
                        flag = false;
                        break;
                    }
                }

                if (flag)
                {
                    DustsToDusts = new int[dust_count, dust_count];
                    for (int i = 0; i < dust_count; i++)
                    {
                        CalcDustsToDusts(i);
                    }
                    DFS(0, 0, 0, 0);
                    sb.AppendFormat("{0}\n", ans);
                }

                // 마지막
                inputs = sr.ReadLine().Split();
                W = int.Parse(inputs[0]);
                H = int.Parse(inputs[1]);
            }

            sw.WriteLine(sb.ToString());
            sb.Clear();
            sw.Flush();
        }

        static void DFS(int chosen, int subsum, int visit, int last)
        {
            if (chosen == dust_count)
            {
                ans = Math.Min(ans, subsum);
                return;
            }
            if (subsum >= ans) return;

            for (int i = 0; i < dust_count; i++)
            {
                if ((visit & (1 << i)) == 0)
                {
                    if (chosen == 0) DFS(chosen + 1, subsum + RobotToDusts[i], visit | (1 << i), i);
                    else DFS(chosen + 1, subsum + DustsToDusts[last, i], visit | (1 << i), i);
                }
            }
        }

        static void CalcDustsToDusts(int start)
        {
            Coordinate Start = Dusts[start];
            bool[,] visited = new bool[H, W];
            visited[Start.row, Start.col] = true;

            Queue<Coordinate> que = new Queue<Coordinate>();
            que.Enqueue(new Coordinate { row = Start.row, col = Start.col, distance = 0 });

            while (que.Count > 0)
            {
                Coordinate now = que.Dequeue();

                int nextRow, nextCol, nextDis;
                for (int i = 0; i < 4; i++)
                {
                    nextRow = now.row + Delta[i, 0];
                    nextCol = now.col + Delta[i, 1];
                    nextDis = now.distance + 1;

                    if (nextRow >= 0 && nextRow < H && nextCol >= 0 && nextCol < W && !visited[nextRow, nextCol] && (room[nextRow, nextCol] == '.' || room[nextRow, nextCol] == '*'))
                    {
                        visited[nextRow, nextCol] = true;
                        que.Enqueue(new Coordinate { row = nextRow, col = nextCol, distance = nextDis });

                        if (room[nextRow, nextCol] == '*')
                        {
                            for (int k = 0; k < dust_count; k++)
                            {
                                if (Dusts[k].row == nextRow && Dusts[k].col == nextCol)
                                {
                                    DustsToDusts[start, k] = nextDis;
                                    break;
                                }
                            }
                        }
                    }
                }
            }
        }

        static void CalcRobotToDusts()
        {
            RobotToDusts = new int[dust_count];
            for (int i = 0; i < dust_count; i++)
                RobotToDusts[i] = -1;

            bool[,] visited = new bool[H, W];
            visited[Robot.row, Robot.col] = true;

            Queue<Coordinate> que = new Queue<Coordinate>();
            que.Enqueue(new Coordinate { row = Robot.row, col = Robot.col, distance = 0 });

            while (que.Count > 0)
            {
                Coordinate now = que.Dequeue();

                int nextRow, nextCol, nextDis;
                for (int i = 0; i < 4; i++)
                {
                    nextRow = now.row + Delta[i, 0];
                    nextCol = now.col + Delta[i, 1];
                    nextDis = now.distance + 1;

                    if (nextRow >= 0 && nextRow < H && nextCol >= 0 && nextCol < W && !visited[nextRow, nextCol] && (room[nextRow, nextCol] == '.' || room[nextRow, nextCol] == '*'))
                    {
                        visited[nextRow, nextCol] = true;
                        que.Enqueue(new Coordinate { row = nextRow, col = nextCol, distance = nextDis });

                        if (room[nextRow, nextCol] == '*')
                        {
                            for (int k = 0; k < dust_count; k++)
                            {
                                if (Dusts[k].row == nextRow && Dusts[k].col == nextCol)
                                {
                                    RobotToDusts[k] = nextDis;
                                    break;
                                }
                            }
                        }
                    }
                }
            }
        }

        static void Set()
        {
            room = new char[H, W];
            Dusts = new List<Coordinate> { };
            ans = int.MaxValue;
            dust_count = 0;

            for (int i = 0; i < H; i++)
            {
                string input = sr.ReadLine();

                for (int j = 0; j < W; j++)
                {
                    if (input[j] == 'o')
                    {
                        Robot.row = i; Robot.col = j;
                        room[i, j] = '.';
                        continue;
                    }

                    if (input[j] == '*')
                    {
                        Dusts.Add(new Coordinate { row = i, col = j });
                        dust_count++;
                    }
                    room[i, j] = input[j];
                }
            }
        }
    }

    public struct Coordinate
    {
        public int row { get; set; }
        public int col { get; set; }
        public int distance { get; set; }
    }

    //class Program
    //{
    //    static void Main()
    //    {
    //        BOJ4491.Start();
    //    }
    //}
}
