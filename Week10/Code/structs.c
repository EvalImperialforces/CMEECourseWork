#include <stdio.h>
#include <stdlib.h>

/*float x_points[] = {0.73, 0.44, 0.32, 0.43}; // Way in which to store 2D points
float y_points[] = {1.52, 2.34, 3.87, 3.13};*/


struct point_s {
    float x;
    float y;

};

/*union input_datum { // Not common or very safe to use.
    long int as_int;
    float as_flt;
    double as_double;
    char as_char;
}*/

int main (void)
{

    struct point_s pt1;
    struct point_s pt2;

    pt1.x = x_points[0];
    pt1.y = y_points[0];

    return 0;
}