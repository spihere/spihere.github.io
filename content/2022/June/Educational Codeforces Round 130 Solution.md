## Educational Codeforces Round 130

Origin Problem set can be fine [here](https://codeforces.com/contest/1697)

### A. Parkway Walk

If the amount of energy is capable of allowing us to travel without a rest, return $0$. Else return the energy needed to be recover.

Code:
```rust
fn slove(sc: &mut Scanner, wr: &mut Writer) {
    let n = sc.nextInt();
    let m = sc.nextInt();
    let mut s = 0;
    for _ in 0..n {
        let tmp = sc.nextInt();
        s += tmp;
    }
    wr.println(max(&(s - m), &0));
}
```

### B. Promo

After getting all of the input, sort the array reversly and calulate prefix sum of it. For each pair of $x$ and $y$, the maximum value of free item would be $prefix[x] - prefix[x-y]$.

Code:
```rust
fn slove(sc: &mut Scanner, wr: &mut Writer) {
    let n = sc.nextUsize();
    let m = sc.nextInt();
    let mut v: Vec<i32> = (0..n).map(|_| sc.nextInt()).collect();
    v.sort_unstable();
    v.reverse();
    let mut s: Vec<u64> = vec![0; n + 1];
    for i in 1..n + 1 {
        s[i] = s[i - 1] + v[i - 1] as u64;
    }
    for _ in 0..m {
        let (x, y) = (sc.nextUsize(), sc.nextUsize());
        wr.println(&(s[x] - s[x-y]));
    }
}
```

### C. awoo's Favorite Problem

First, the count of `a`, `b` and `c` must be the same. A `c` must come after a `a` in order for them to be exchanged. At any position $i$, $s[i] != t[i]$. 

Code:
```rust
fn slove(sc: &mut Scanner, _wr: &mut Writer) -> bool {
    let n = sc.nextUsize();
    let s: Vec<_> = sc.nextLine().chars().collect();
    let t: Vec<_> = sc.nextLine().chars().collect();
    let mut x = vec![];
    let mut y = vec![];
    for i in 0..n {
        if s[i] == 'c' {
            x.push((2, i));
        } else if s[i] == 'a' {
            x.push((0, i));
        }
        if t[i] == 'c' {
            y.push((2, i));
        } else if t[i] == 'a' {
            y.push((0, i));
        }
    }
 
    if x.len() != y.len() {
        return false;
    }
 
    x.iter().zip(y.iter()).all(|(&(t1, p1), &(t2, p2))| {
        if t1 != t2 {
            return false;
        }
        if t1 == 0 {
            return p1 <= p2;
        }
        return p1 >= p2;
    })
})}
```

### D. Guess The String

For character at a index $i$, check $q2(x, i)$ where $0 <= x < y$. If result of q2 equals to the unique letters in the range, the letter at $i$ must equal to the letter on position`$x$. We can then use a binary search to imporve this algorithm to decrease the amount of query for each letter to $O(log(n))$. If there is no such result even when $x = 0$, the letter must be a new letter. Use q1 on it.

Total Number of query2 would be `O(nlog(n))`. 

Unoptimized Code:
```cpp
char q1(int pos)
{
    string s;
    cout << "? 1 " << pos + 1 << endl
         << flush;
    cin >> s;
    return s[0];
}
 
int q2(int pos1, int pos2)
{
    int ans;
    cout << "? 2 " << pos1 + 1 << ' ' << pos2 + 1 << endl
         << flush;
    cin >> ans;
    return ans;
}
 
void solve()
{
    int len;
    cin >> len;
    vector<char> res(len, '?');
 
    res[0] = q1(0);
    for (int i = 1; i < len; i++)
    {
        set<char> st;
        bool f = false;
        for (int j = i - 1; j >= 0; j--)
        {
            st.insert(res[j]);
            if (q2(j, i) == int(st.size()))
            {
                res[i] = res[j];
                f = true;
                break;
            }
        }
 
        if (!f)
            res[i] = q1(i);
 
    }
 
    cout << "! ";
    for (auto &a : res)
        cout << a;
    cout << endl
         << flush;
}
```
