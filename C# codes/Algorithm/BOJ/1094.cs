using System;

namespace BOJ
{
    class BOJ1094
    {
        static int ans = 0, aim = 0;
        const int MAX = 64;

        public static void start()
        {
            aim = Convert.ToInt32(Console.ReadLine());
            DivideExec(MAX);
            Console.WriteLine(ans);
        }

        static void DivideExec(int now)
        {
            if (aim == 0) return;
            
            if (now > aim)
            {
                DivideExec(now / 2);
            }
            else
            {
                ans += 1;
                aim -= now;
                DivideExec(now / 2);
            }
        }
    }
    //class Program
    //{
    //    static void Main()
    //    {
    //        BOJ1094.start();
    //    }
    //}
}
