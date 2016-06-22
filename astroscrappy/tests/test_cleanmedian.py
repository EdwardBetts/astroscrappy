# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import numpy as np
from ..astroscrappy import detect_cosmics
imdata = np.array([ 2369, 2404, 2387, 2406, 2448, 2470, 2454, 2460,
                    2494, 2491, 2448, 2411, 2413, 2393, 2408, 2378,
                    2364, 2365, 2331, 2304, 2362, 2353, 2381, 2405,
                    2458, 2437, 2426, 2442, 2484, 2418, 2444, 2444,
                    2398, 2388, 2395, 2373, 2352, 2332, 2322, 2310,
                    2338, 2353, 2370, 2396, 2367, 2432, 2419, 2433,
                    2420, 2432, 2413, 2398, 2405, 2356, 2376, 2383,
                    2338, 2331, 2290, 2284, 2302, 2337, 2329, 2364,
                    2391, 2375, 2441, 2386, 2421, 2398, 2370, 2414,
                    2407, 2349, 2391, 2360, 2326, 2335, 2336, 2290,
                    2334, 2333, 2320, 2324, 2372, 2365, 2392, 2398,
                    2361, 2367, 2348, 2357, 2361, 2345, 2335, 2310,
                    2337, 2310, 2307, 2323, 2304, 2324, 2327, 2338,
                    2365, 2338, 2336, 2319, 2357, 2378, 2391, 2345,
                    2342, 2342, 2325, 2304, 2292, 2336, 2329, 2307,
                    2309, 2287, 2309, 2283, 2344, 2318, 2312, 2334,
                    2330, 2336, 2328, 2304, 2334, 2339, 2298, 2291,
                    2321, 2315, 2306, 2320, 2308, 2293, 2317, 2333,
                    2326, 2313, 2356, 2327, 2298, 2337, 2328, 2320,
                    2316, 2297, 2313, 2332, 2310, 2307, 2319, 2302,
                    2333, 2338, 2322, 2303, 2316, 2279, 2324, 2318,
                    2290, 2322, 2325, 2342, 2336, 2292, 2301, 2299,
                    2287, 2315, 2301, 2318, 2301, 2306, 2313, 2325,
                    2313, 2313, 2294, 2302, 2309, 2306, 2333, 2327,
                    2310, 2257, 2304, 2315, 2303, 2309, 2314, 2315,
                    2331, 2321, 2310, 2307, 2317, 2299, 2324, 2315,
                    2323, 2336, 2295, 2316, 2330, 2309, 2306, 2314,
                    2272, 2347, 2319, 2310, 2301, 2320, 2321, 2408,
                    2703, 2649, 2295, 2329, 2321, 2307, 2321, 2320,
                    2312, 2298, 2312, 2311, 2298, 2301, 2296, 2317,
                    2306, 2332, 2307, 2334, 2310, 2339, 2658, 2658,
                    2643, 2660, 2523, 2322, 2284, 2322, 2322, 2338,
                    2302, 2287, 2309, 2307, 2305, 2317, 2316, 2310,
                    2306, 2306, 2344, 2310, 2285, 2308, 2421, 2679,
                    2675, 2701, 2657, 2421, 2303, 2331, 2307, 2307,
                    2317, 2297, 2304, 2319, 2327, 2300, 2331, 2338,
                    2302, 2323, 2303, 2305, 2308, 2313, 2322, 2554,
                    2654, 2670, 2678, 2638, 2316, 2302, 2322, 2299,
                    2339, 2305, 2321, 2291, 2280, 2304, 2324, 2318,
                    2282, 2281, 2301, 2306, 2295, 2284, 2288, 2313,
                    2294, 2301, 2324, 2344, 2330, 2304, 2312, 2317,
                    2326, 2306, 2326, 2318, 2329, 2318, 2300, 2287,
                    2268, 2294, 2293, 2319, 2279, 2322, 2298, 2298,
                    2330, 2296, 2326, 2331, 2310, 2303, 2314, 2329,
                    2315, 2322, 2296, 2307, 2272, 2309, 2310, 2315,
                    2325, 2314, 2264, 2293, 2312, 2305, 2308, 2318,
                    2287, 2267, 2314, 2302, 2310, 2277, 2310, 2307,
                    2304, 2315, 2314, 2313, 2318, 2309, 2315, 2305,
                    2312, 2289, 2268, 2310, 2315, 2294, 2314, 2312,
                    2286, 2311, 2305, 2320, 2299, 2293, 2283, 2302]).reshape(20,20)

imdata = imdata.astype('f4')

def test_medclean():
    mask1, _clean = detect_cosmics(imdata, fsmode='median',
                                    cleantype='median', niter = 1)

    mask2, _clean = detect_cosmics(imdata, fsmode='median', cleantype='median', niter = 2)
    
    assert (mask1.sum() < mask2.sum())

