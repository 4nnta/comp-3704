#include <bits/stdc++.h>
using namespace std;

class Point {
public:
	double x;
	double y;

	Point(double x = 0.0, double y = 0.0): x(x), y(y) {}
};

class Segment {
public:
	Point pLeft;
	Point pRight;

	Segment(Point p, Point q): pLeft(p), pRight(q) {
		// have to make sure pLeft is the point on the left, in case of tie, resolve by lexicographic order
		if (pLeft.x > pRight.x || (pLeft.x == pRight.x && pLeft.y > pRight.y))
			swap(pLeft, pRight);
	}

	// relative position of point target and the segment.
	// 1 for above
	// 0 for on the support line
	// -1 for below
	int isAbove(Point target) {
		double pos = turn(target);
		if (pos > 0)
			return 1;
		else if (pos < 0)
			return -1;
		else
			return 0;
	}
private:
	// return the turn of pLeft, pRight, target
	double turn(Point target) {
		return (pRight.x - pLeft.x) * (target.y - pLeft.y) - (target.x - pLeft.x) * (pRight.y - pLeft.y);
	}
};

class Node;

class Trapezoid {
public:
	string name;

	Trapezoid *upLeft;
	Trapezoid *upRight;
	Trapezoid *lowLeft;
	Trapezoid *lowRight;

	Segment *top;
	Segment *bot;

	Node *node;

	Point left;
	Point right;

	Trapezoid(): upLeft(NULL), upRight(NULL), lowLeft(NULL), lowRight(NULL), node(NULL) {}

	
};

class Node {
public:
	virtual ~Node() {}
	virtual Trapezoid* getTrapezoid() { return NULL; }	// return a trapezoid if the node is a square node, NULL otherwise
	virtual Node* next(Point target) { return NULL; }	// traverse the tree, inherited by classes below
	virtual string name() { return NULL; }				// name of the node

	Node *left;
	Node *right;
	vector <Node*> parent;
};

class XNode: public Node {
public:
	Point p;

	XNode(Point p): p(p) {}

	Node* next(Point target) {
		if (target.x < p.x)
			return left;
		else
			return right;
	}

	string name() { return "X"; }
};

class YNode: public Node {
public:
	Segment *seg;

	YNode(Segment *s): seg(s) {}

	Node* next(Point target) {
		int state = seg->isAbove(target);
		if (state > 0)
			return left;
		else if (state < 0)
			return right;
		else
			return NULL; // this suppose to report the segment, gonna deal with this later
	}

	string name() { return "Y"; }
};

class SquareNode: public Node {
public:
	Trapezoid *trapezoid;

	SquareNode(Trapezoid *trapezoid): trapezoid(trapezoid) {}

	Trapezoid* getTrapezoid() { return trapezoid; }

	string name() { return "Square"; }
};