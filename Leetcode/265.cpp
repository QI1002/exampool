
#include <vector>
#include <stdio.h>
#include <stdint.h>

using namespace std;

class Solution1 {
public:
    int minCostII(vector<vector<int>>& costs) {
        if (costs.empty() || costs[0].empty()) return 0;
        vector<vector<int>> dp = costs;
        int min1 = -1, min2 = -1;
        for (int i = 0; i < dp.size(); ++i) {
            int last1 = min1, last2 = min2;
            min1 = -1; min2 = -1;
            for (int j = 0; j < dp[i].size(); ++j) {
                if (j != last1) {
                    dp[i][j] += last1 < 0 ? 0 : dp[i - 1][last1];
                } else {
                    dp[i][j] += last2 < 0 ? 0 : dp[i - 1][last2];
                }
                if (min1 < 0 || dp[i][j] < dp[i][min1]) {
                    min2 = min1; min1 = j;
                } else if (min2 < 0 || dp[i][j] < dp[i][min2]) {
                    min2 = j;
                }
            }
        }
        return dp.back()[min1];
    }
};

class Solution2 {
public:
    int minCostII(vector<vector<int>>& costs) {
        if (costs.empty() || costs[0].empty()) return 0;
        int min1 = 0, min2 = 0, idx1 = -1;
        for (int i = 0; i < costs.size(); ++i) {
            int m1 = INT32_MAX, m2 = m1, id1 = -1;
            for (int j = 0; j < costs[i].size(); ++j) {
                int cost = costs[i][j] + (j == idx1 ? min2 : min1);
                if (cost < m1) {
                    m2 = m1; m1 = cost; id1 = j;
                } else if (cost < m2) {
                    m2 = cost;
                }
            }
            min1 = m1; min2 = m2; idx1 = id1;
        }
        return min1;
    }
};

int main()
{
    Solution1 s1;
    Solution2 s2;

    const int cost1[4][4] = { {1,3,2,4},{4,1,2,3},{2,3,1,4},{1,4,2,3} };
    vector< vector<int> > costv1;
    for (int i = 0; i < sizeof(cost1)/sizeof(cost1[0]); i++)
    {	    
        vector<int> v(cost1[i], cost1[i] + sizeof(cost1[i])/sizeof(cost1[i][0]));
	costv1.push_back(v);
    }

    printf("%d:%d\n", s1.minCostII(costv1), s2.minCostII(costv1));

    const int cost2[4][4] = { {1,3,2,4},{1,101,102,103},{2,3,1,4},{1,4,2,3} };
    vector< vector<int> > costv2;
    for (int i = 0; i < sizeof(cost2)/sizeof(cost2[0]); i++)
    {	    
        vector<int> v(cost2[i], cost2[i] + sizeof(cost2[i])/sizeof(cost2[i][0]));
	costv2.push_back(v);
    }

    printf("%d:%d\n", s1.minCostII(costv2), s2.minCostII(costv2));
    
    return 0;
}
