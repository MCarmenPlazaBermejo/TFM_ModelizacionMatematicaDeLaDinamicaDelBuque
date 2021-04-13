cl1=0.1;
//caja

// Puntos de la caja

Point( 1 )={ -1 , -1 , 0.5 , cl1};
Point( 2 )={ -1 , 1 , 0.5, cl1};
Point( 3 )={ -1 , -1 , -0.5 , cl1 };
Point( 4 )={ -1 , 1 , -0.5, cl1 };
Point( 5 )={ +3 , -1 , 0.5 , cl1 };
Point( 6 )={ +3 , 1 , 0.5, cl1 };
Point( 7 )={ +3 , -1 , -0.5 , cl1 };
Point( 8 )={ +3 , 1 , -0.5, cl1 };

//Esfera

//Puntos

Point( 9 )={ 0.25 , 0 , 0 , cl1};
Point( 10 )={0 , 0 , 0, cl1};
Point( 11 )={ 0.5, 0 , 0 , cl1 };
Point( 12 )={ 0.25 , 0.25, 0, cl1 };
Point( 13 )={ 0.25, -0.25 , 0 , cl1 };
Point( 14)={ 0.25 , 0 , 0.25, cl1 };
Point( 15 )={ 0.25 , 0 , -0.25 , cl1 };
//+
Circle(1) = {11, 9, 12};
//+
Circle(2) = {15, 9, 12};
//+
Circle(3) = {14, 9, 12};
//+
Circle(4) = {10, 9, 12};
//+
Circle(5) = {13, 9, 14};
//+
Circle(6) = {11, 9, 13};
//+
Circle(7) = {15, 9, 13};
//+
Circle(8) = {10, 9, 13};
//+
Circle(9) = {11, 9, 14};
//+
Circle(10) = {11, 9, 15};
//+
Circle(11) = {10, 9, 15};
//+
Circle(12) = {10, 9, 14};
//+
Curve Loop(1) = {1, -2, -10};
//+
Surface(1) = {1};
//+
Curve Loop(2) = {3, -1, 9};
//+
Surface(2) = {2};
//+
Curve Loop(3) = {3, -4, 12};
//+
Surface(3) = {3};
//+
Curve Loop(4) = {2, -4, 11};
//+
Surface(4) = {4};
//+
Curve Loop(5) = {7, -8, 11};
//+
Surface(5) = {5};
//+
Curve Loop(6) = {12, -5, -8};
//+
Surface(6) = {6};
//+
Curve Loop(7) = {6, -7, -10};
//+
Surface(7) = {7};
//+
Curve Loop(8) = {5, -9, 6};
//+
Surface(8) = {8};
//+
Surface Loop(1) = {3, 2, 1, 4, 5, 7, 8, 6};
//+
Volume(1) = {1};
//+
Line(13) = {6, 8};
//+
Line(14) = {8, 4};
//+
Line(15) = {4, 2};
//+
Line(16) = {2, 6};
//+
Line(17) = {6, 5};
//+
Line(18) = {5, 7};
//+
Line(19) = {7, 8};
//+
Line(20) = {2, 2};
//+
Line(21) = {2, 1};
//+
Line(22) = {1, 3};
//+
Line(23) = {3, 4};
//+
Line(24) = {3, 7};
//+
Line(25) = {1, 5};
//+
Curve Loop(9) = {15, 21, 22, 23};
//+
Plane Surface(9) = {9};
//+
Curve Loop(10) = {14, 15, 16, 13};
//+
Plane Surface(10) = {10};
//+
Curve Loop(11) = {19, -13, 17, 18};
//+
Plane Surface(11) = {11};
//+
Curve Loop(12) = {24, -18, -25, 22};
//+
Plane Surface(12) = {12};
//+
Curve Loop(13) = {14, -23, 24, 19};
//+
Plane Surface(13) = {13};
//+
Curve Loop(14) = {16, 17, -25, -21};
//+
Plane Surface(14) = {14};
//+
Surface Loop(2) = {14, 10, 13, 9, 12, 11};
//+
Volume(2) = {2};
