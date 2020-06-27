//g++ -std=gnu++11 templ.cpp
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <stack>
#include <unordered_set>
#include <unordered_map>
#include <math.h>
#include <set>
#include <map>
#include <list>
#include <random>
#include <time.h>
#include <deque>
#include <queue>
#include <climits>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

bool find(TreeNode* root, int idx) {
    if (idx <= 0) return false;

    int i, j;
    for(j = idx, i = 0; j != 0; ++i, j >>= 1); 
    //cout << i << endl;
    for(i -= 2; i >= 0; --i) {
        if (root == NULL) return false;
	if (idx & (1<<i)) root = root->right;
	else root = root->left;
    }
    return (root != NULL);
}

int main(int argc, char* argv[]) {
    srand(time(NULL));
    TreeNode* root = NULL;
    cout << find(root, 5) << endl;
    root = new TreeNode(1);
    root->left = new TreeNode(1);
    cout << find(root, 2) << endl;
    return 0;
}

