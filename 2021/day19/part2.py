scanners = [
    (0,0,0),
    (-1073,-1262,-1084),
    (24,-1203,-1060),
    (-1206,-1134,-3529),
    (-1215,-1176,3631),
    (8,-2369,1232),
    (1259,-25,96),
    (-1222,-2464,34),
    (1185,-1172,2461),
    (-1136,-1251,1226),
    (-1103,-3646,1333),
    (95,-1228,3607),
    (-2264,-1282,1228),
    (42,-1129,1156),
    (131,1177,119),
    (-1229,-1121,-2263),
    (118,-2436,2536),
    (5,-3612,2371),
    (-8,-1141,2420),
    (2468,-2359,2369),
    (1300,-3697,1199),
    (1311,-1135,3694),
    (102,-1253,-2391),
    (1207,-2384,98),
    (34,-1251,105),
    (2376,-2330,3618),
    (-1170,-2479,1245),
    (2422,-2319,1314),
    (1242,-2451,1335)
]

max_dist = 0

for scanner1 in scanners:
    for scanner2 in scanners:
        dist = sum([abs(c1 - c2) for (c1, c2) in zip(scanner1, scanner2)])
        if dist > max_dist:
            max_dist = dist

print(max_dist)
