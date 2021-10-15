using System;
using System.IO;

namespace BOJ
{
    class BOJ2961
    {
        static long ans = Int64.MaxValue;
        static int N;
        static bool[] visited;
        static ulong[,] ingredients;

        static StreamReader sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));

        public static void Start()
        {
            N = int.Parse(sr.ReadLine());
            ingredients = new ulong[N, 2];
            visited = new bool[(int)Math.Pow(2, N)];

            for (int i = 0; i < N; i++)
            {
                String[] input = sr.ReadLine().Split();
                ingredients[i, 0] = ulong.Parse(input[0]);
                ingredients[i, 1] = ulong.Parse(input[1]);
            }

            Calculate(0, new ulong[2] { 1, 0 });

            Console.WriteLine(ans.ToString());
        }

        static void Calculate(int visit, ulong[] result)
        {
            int temp_visit;
            ulong S, B;
            long diff;
            for (int i = 0; i < N; i++)
            {
                temp_visit = visit | 1 << i;

                if (visited[temp_visit]) continue;

                visited[temp_visit] = true;
                S = result[0] * ingredients[i, 0];
                B = result[1] + ingredients[i, 1];
                diff = Math.Abs((long)(S - B));

                ans = Math.Min((long)ans, (long)diff);

                Calculate(temp_visit, new ulong[2] { S, B });
            }
        }
    }
    class Program
    {
        static void Main()
        {
            BOJ2961.Start();
        }
    }
}
