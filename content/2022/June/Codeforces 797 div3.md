# Codeforces #797 (Div.3) Simple Solution

Original Problems: [https://codeforces.com/contest/1690](https://codeforces.com/contest/1690)

## A
Try split the problem into three situations: $n \bmod 3 = 0$, $n \bmod 3 = 1$, $n \bmod 3 = 2$. Then it can be solved easily.

Code:
```cpp
void solve()
{
    int n;
    cin >> n;
    if (n % 3 == 0)
        cout << n / 3 << ' ' << n / 3 + 1 << ' ' << n / 3 - 1 << endl;
    else if (n % 3 == 1)
        cout << n / 3 << ' ' << n / 3 + 2 << ' ' << n / 3 - 1 << endl;
    else
        cout << (n + 1) / 3 << ' ' << (n + 1) / 3 + 1 << ' ' << n / 3 - 1 << endl;
}
```

## B
For each pair of pair $a$ and $b$, if b equals to zero. $a$ have to be subtracted at least b times, but have no limit on how high it goes. If $b$ is not zero, $a$ but be greater or equal than $b$, also $a - b$ must be equal to the $a - b$ on other pairs where $b$ is not zero.

Code: 
```cpp
typedef vector<int> vi;
#define yesnosolve cout << (solve() ? "NO" : "YES") << endl

int solve()
{
    int n;
    cin >> n;
    vi a(n), b(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    for (int i = 0; i < n; i++)
        cin >> b[i];

    int m = -1;

    for (int i = 0; i < n; i++)
        m = max(a[i] - b[i], m);

    for (int i = 0; i < n; i++)
    {
        if (b[i] == 0)
        {
            if (a[i] > m)
                return 1;
        }
        else
        {
            if (a[i] < b[i] || a[i] - b[i] < m)
                return 1;
        }
    }

    return 0;
}
```

## C
For the first end time $f_1$, duration is $f_1 - s_1$. For other end time $f_i$, duration is $f_i - max(s_i,f_{i-1})$

Code: 
```cpp
typedef vector<int> vi;

void solve()
{
    int n;
    cin >> n;
    vi s(n), f(n);
    for (int i = 0; i < n; i++)
        cin >> s[i];
    for (int i = 0; i < n; i++)
        cin >> f[i];

    cout << f[0] - s[0] << ' ';
    for (int i = 1; i < n; i++)
    {
        cout << f[i] - max(s[i], f[i - 1]) << ' ';
    }
    cout << endl;
}
```

## D
Use prefix sum algorithm to determine black strips in a certain region. Iterate through the array and find the minimum value of $k - count(key=B, from = i, to = i+m)$

Code:
```cpp
const int INF = 2e9;
typedef vector<int> vi;

void solve()
{
    string s;
    int n, m;
    cin >> n >> m;
    cin >> s;
    s = ' ' + s;
    vi p(n + 10), a(n + 10);
    for (int i = 1; i <= n; i++)
        if (s[i] == 'B')
            p[i]++;

    for (int i = 1; i <= n + 1; i++)
        a[i] = a[i - 1] + p[i];

    int mi = INF;
    for (int i = 1; i + m <= n + 1; i++)
        mi = min(mi, m - a[i + m - 1] + a[i - 1]);
    cout << mi << endl;
}
```

## E
1. Sum the value of each $x / k$ where $/$ is integer division for each goods to a value $ans$.
2. Create a new array using the remainder of the lat step.
3. Sort the array and use binary search to find the minimun solution $x$ where $x  >= k - remainder$.
4. If found, add one to $ans$ and erase both elements. Else, continue to the next element.

Code: 
```cpp
typedef unsigned long long ull;
typedef vector<int> vi;
void solve()
{
    int n, k;
    cin >> n >> k;
    vi g(n);
    for (int i = 0; i < n; i++)
        cin >> g[i];

    multiset<int> st;

    ull ans = 0;
    for (auto& a : g)
        ans += a / k, st.insert(a % k);

    while (!st.empty())
    {
        auto t = *st.begin();
        st.erase(st.begin());

        auto it = st.lower_bound(k - t);
        if (it != st.end())
            ans++, st.erase(it);
    }

    cout << ans << endl;
}
```