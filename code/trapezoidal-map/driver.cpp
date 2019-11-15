#include <bits/stdc++.h>
#include "trapezoidal-map.h"
using namespace std;

void traverse(Node *node) {
	cout << node->name();

	cout << "left(";
	if (node->left != NULL)
		traverse(node->left);
	cout << ")";


	cout << "right(";
	if (node->right != NULL)
		traverse(node->right);
	cout << ")";
}

int main (void) {
	int n; cin >> n;
	vector <Segment*> segments;
	for (int i = 0; i < n; ++i) {
		double x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		Point p1 = Point(x1, y1);
		Point p2 = Point(x2, y2);
		Segment* seg = new Segment(p1, p2);
		segments.push_back(seg);
	}

	TrapezoidalMap tMap = TrapezoidalMap();
	tMap.buildMap(segments);

	
}