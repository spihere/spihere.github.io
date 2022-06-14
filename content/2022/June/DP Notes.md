## DP Problemss I've met

### LC22

Note: BFS-Like Solution
```cpp
class Solution
{
public:
    vector<string> generateParenthesis(int n)
    {
        deque<pair<string, pair<int, int>>> dq;
        vector<string> res;
        dq.push_back({"(", {1, 0}});
        while (!dq.empty())
        {
            auto tt = dq.front();
            string t = tt.first;
            auto l = tt.second.first, r = tt.second.second;
            dq.pop_front();

            if (t.length() == n * 2)
                res.push_back(t);
            else
            {
                if (l < n)
                    dq.push_back({t + "(", {l + 1, r}});

                if (r < l)
                    dq.push_back({t + ")", {l, r + 1}});
            }
        }
        return res;
    }
};
```