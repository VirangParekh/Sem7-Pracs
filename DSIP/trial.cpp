#include "pbPlots.hpp"
#include "supportLib.hpp"
#include <bits/stdc++.h>
using namespace std;
int main()
{

    RGBABitmapImageReference *imageRef = CreateRGBABitmapImageReference();

    vector<double> x{-2.0, -2.0, 0.0, 1.0, 2.0};
    vector<double> y{-2.0, -2.0, 0.0, 1.0, 2.0};

    DrawScatterPlot(imageRef, 600, 400, &x, &y);

    vector<double> *pngData = ConvertToPNG(imageRef->image);
    WriteToFile(pngData, "plot.png");
    DeleteImage(imageRef->image);
    return 0;
}