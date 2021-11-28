package java;
// import java.io.*;
import java.util.*;
// import java.text.*;
// import java.math.*;
// import java.util.regex.*;


class Shape {
    int x,y;
    public Shape(int l,int b){
        x = l;
        y = b;
    }
    public void area() {
        System.out.println(x+" "+y);
    }
}

class Rectangle extends Shape {
    public Rectangle(int l, int b) {
        super(l, b);
    }
    public void area() {
        System.out.println(x*y);
    }
}

public class Solution {
    public static void main(String args[] ) throws Exception {
        try (Scanner sc = new Scanner(System.in)) {
            int l = sc.nextInt();
            int b = sc.nextInt();

            Shape shape = new Shape(l,b);
            shape.area();

            Shape rectangle = new Rectangle(l,b);
            rectangle.area();
        }
    }
}