module LaplaceTop() {
    surface(file = "/home/frank/do/freericks/all-scripts/triangle300x300.dat", center = true, convexity = 2);
}

module LaplaceBase() {
    $fn=1000; 
    minkowski() {
        cube(size = [150,150,30], center=true);
        translate ([0,0,-15])cylinder(h=15, r=150);
    }
}

union() {
    LaplaceTop();
    translate([0,0,-15]) LaplaceBase();
}