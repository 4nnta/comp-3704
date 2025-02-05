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

int toInt(string s) {
	int exp = 1, ans = 0;
	for (int i = s.size()-1; i >= 0; --i) {
		ans += (s[i] - '0') *  exp;
		exp *= 10;
	}

	return ans;
}

int main (int argc, char **argv) {
	string num = argv[1];
	int n = toInt(num);
	srand(time(NULL));
	vector <Segment*> segments;

	// freopen("test_0.in", "w+", stdout);
	
	cout << n << "\n";

	for (int i = 0; i < n; ++i) {
		int x1 = rand() % 4000 - 2000, y1 = rand() % 4000 - 2000;
		int x2 = rand() % 4000 - 2000, y2 = rand() % 4000 - 2000;
		Point p1 = Point(x1, y1);
		Point p2 = Point(x2, y2);
		Segment *seg = new Segment(p1, p2);

		while (true) {
			bool noIntersect = true;
			for (int j = 0; j < segments.size(); ++j)
				if (segments[j]->isIntersecting(seg))
					noIntersect = false;

			if (noIntersect)
				break ;

			int replace = rand() % 4;
			if (replace == 0)
				seg->pLeft.x = rand() % 4000 - 2000;
			else if (replace == 1)
				seg->pLeft.y = rand() % 4000 - 2000;
			else if (replace == 2)
				seg->pRight.x = rand() % 4000 - 2000;
			else
				seg->pRight.y = rand() % 4000 - 2000;
		}

		segments.push_back(seg);

		cout << x1 << " " << y1 << " " << x2 << " " << y2 << "\n";
	}

	TrapezoidalMap tMap = TrapezoidalMap();
	tMap.buildMap(segments);
}