# 309pollution

**Subject :**

The ambient air quality monitoring in France is ensured by independent associations, members of the
ATMO federation, and, on behalf of the State and public authorities, are responsible for implementing means of monitoring.

Why not you? The Lozère market seems easily open for the taking. . .
So, you decide to start a project based on collaborative initiatives like CitoyensCapteurs in order to acquire data.
All that’s left to do is to create a little software for viewing the data. . .
You receive the data in triplets (x, y, p) where x and y are the coordinates (presumably integers so it’s simpler) on a normal grid and p the pollution level (in percentage).
We will consider that the pollution is nonexistent on the grid’s other points.
Your program will use Bézier surfaces to smooth out the data and display the value of the pollution level in a point inside the observed area.

*CSV*

```
cat file.csv
0;0;20
0;1;12
1;0;50
1;1;30
1;2;50
2;2;80
```

*USAGE*

```
./309pollution 3 file.csv 0.6 2
28.20
```
