using System;
using System.IO;

namespace BOJ
{
    class BOJ14391
    {
        static int[,] paper;
        static int N, M, sum, ans, bitValue;

        static StreamReader sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));

        public static void Start()
        {
            Set();

            for (int bitmask = 0; bitmask < (1 << N * M); bitmask++)
            {
                sum = 0;

                CalcRows(bitmask);
                CalcCols(bitmask);

                ans = Math.Max(ans, sum);
            }

            Console.WriteLine(ans.ToString());
        }

        static void CalcRows(int bitmask)
        {
            for (int i = 0; i < N; i++)
            {
                int now = 0;
                for (int j = 0; j < M; j++)
                {
                    int index = i * M + j;
                    if ((bitmask & (bitValue >> index)) == 0)
                    {
                        now = now * 10 + paper[i, j];
                    }
                    else
                    {
                        sum += now;
                        now = 0;
                    }
                }
                sum += now;
            }
        }

        static void CalcCols(int bitmask)
        {
            for (int j = 0; j < M; j++)
            {
                int now = 0;
                for (int i = 0; i < N; i++)
                {
                    int index = i * M + j;
                    if((bitmask & (bitValue >> index)) != 0)
                    {
                        now = now * 10 + paper[i, j];
                    }
                    else
                    {
                        sum += now;
                        now = 0;
                    }
                }
                sum += now;
            }
        }

        static void Set()
        {
            string[] NM = sr.ReadLine().Split();
            N = int.Parse(NM[0]);
            M = int.Parse(NM[1]);
            paper = new int[N, M];

            for (int i = 0; i < N; i++)
            {
                string line = sr.ReadLine();
                for (int j = 0; j < M; j++)
                {
                    paper[i, j] = int.Parse(char.ToString(line[j]));
                }
            }

            ans = 0;
            bitValue = 1 << (N * M - 1);
        }
    }
    //class Program
    //{
    //    static void Main()
    //    {
    //        BOJ14391.Start();
    //    }
    //}
}
