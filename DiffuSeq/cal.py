import numpy as np

a=   [   101,
        10694,
         1012,
         2128,
         2288,
         1000,
         2026,
         1037,
         2006,
         1000,
         2288,
         2275,
         1000,
         2026,
         1037,
         2299,
         2011,
         2600,
         2288,
         2011,
         1012,
         1012,
         3220,
         2006,
         3063,
         2207,
         1012,
         2309,
         1997,
         2006,
         1000,
         2015,
         1010,
         2230,
         1000,
         2013,
         2309,
         1000,
         1012,
         1012,
         2009,
         2001,
         2013,
         2009,
         1998,
         2001,
         1000,
         1996,
         2309,
         2201,
         1999,
         1996,
         2013,
         2038,
         1005,
         1055,
         2309,
         2201,
         1012,
         1012,
         2006,
         1996,
         3092,
         2327,
         2201,
         1000,
         2980,
         2531,
         2584,
         2095,
         2004,
         1996,
         2299,
         1998,
         2257,
         2751,
         1005,
         1055,
         2406,
         4908,
          102,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0]

b=  [   101,  2508,  4097,  2577,  6676,  1000,  2288,  2026,  2568,  2275,
         2006,  2017,  1000,  1006,  2036,  2517,  2004,  1000,  1006,  2288,
         2026,  2568,  1007,  2275,  2006,  2017,  1000,  1007,  2003,  1037,
         2299,  2517,  1998,  3605,  2011, 18254,  5215,  1998,  2761,  2680,
         2011,  2508,  4097,  1999,  3705,  1010,  2104,  1996,  2516,  1000,
         1045,  1005,  2310,  2288,  2026,  2568,  2275,  2006,  2017,  1000,
         1012,  2019,  5493,  2544,  1997,  1996,  2299,  2001,  2207,  2101,
         1999,  1996,  2095,  2004,  1037,  2309,  2006,  1996,  8790,  2614,
         3830,   102,     0,     0,     0,     0,     0,     0,     0,     0,
            0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
            0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
            0,     0,     0,     0,     0,     0,     0]
if __name__ == "__main__":
   print(a)
   print(np.dot(a, b)/np.linalg.norm(a)/np.linalg.norm(b))