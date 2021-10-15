using System;
using System.IO;
using System.Text;
using System.Collections;

namespace BOJ
{
    class BOJ11723
    {
        const int SIZE = 21;
        static StringBuilder sb = new StringBuilder();
        static StreamReader sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
        static StreamWriter sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));

        public static void start()
        {
            BitArray barr = new BitArray(SIZE);
            int N = int.Parse(sr.ReadLine());

            string cmd = "";
            int num = 0;

            for (int i = 0; i < N; i++)
            {
                String[] input = sr.ReadLine().Split();
                cmd = input[0];
                if (input.Length > 1) num = int.Parse(input[1]);

                switch (cmd)
                {
                    case "add":
                        barr.Set(num, true);
                        break;
                    case "remove":
                        barr.Set(num, false);
                        break;
                    case "check":
                        sb.Append(barr.Get(num) ? "1\n" : "0\n");
                        break;
                    case "toggle":
                        if (barr.Get(num)) barr.Set(num, false);
                        else barr.Set(num, true);
                        break;
                    case "all":
                        barr.SetAll(true);
                        break;
                    case "empty":
                        barr.SetAll(false);
                        break;
                }
            }
            sw.WriteLine(sb.ToString());
            sw.Close();
        }
    }

    //class Program
    //{
    //    static void Main()
    //    {
    //        BOJ11723.start();
    //    }
    //}
}
