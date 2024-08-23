#include <stdio.h>
#include <math.h>
int min(double *array)
{
    double menor = INFINITY;
    for (int i = 0; i < 5; i++)
    {
        if (array[i] < menor)
        {
            menor = array[i];
        }
    }
    return menor;
}
int max(double *array)
{
    double menor = INFINITY * -1;
    for (int i = 0; i < 5; i++)
    {
        if (array[i] > menor)
        {
            menor = array[i];
        }
    }
    return menor;
}
int main()
{
    double a, b, c, d, e;
    scanf("%lf", &a);
    scanf("%lf", &b);
    scanf("%lf", &c);
    scanf("%lf", &d);
    scanf("%lf", &e);
    double array[5] = {a, b, c, d, e};
    printf("%d ", min(array));
    printf("%d", max(array));
    return 0;
}