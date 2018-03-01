# AIC

```
aic(y, y_pred, p)
```

| Input | Output |
|----------------|-----------------|
| Different length of `y` and `y_pred` | Error, should be in same length |
| `typeof(p) == int`| Error if it is not `int` |
| `typeof(y) == vector`, `typeof(y_pred) == vector` | Error if not vector |
| `p > 0` | Error if `p` is negative |
| `length(y) > 1`, `length(y_pred) > 1` | Error if it is 1 |

# BIC

```
bic(y, y_pred, p)
```

| Input | Output |
|----------------|-----------------|
| Different length of `y` and `y_pred` | Error, should be in same length |
| `typeof(p) == int`| Error if it is not `int` |
| `typeof(y) == vector`, `typeof(y_pred) == vector` | Error if not vector |
| `p > 0` | Error if `p` is negative |
| `length(y) > 1`, `length(y_pred) > 1` | Error if it is 1 |

# Mallow's Cp

```
mallow(y, y_pred, p, k)
```

| Input | Output |
|----------------|-----------------|
| Different length of `y` and `y_pred` | Error, should be in same length |
| `typeof(p) == int`, `typeof(k) == int`| Error if not `int` |
| `typeof(y) == vector`, `typeof(y_pred) == vector` | Error if not vector |
| `p > 0`, `k > 0` | Error if negative |
| `length(y) > 1`, `length(y_pred) > 1` | Error if it is 1 |
| `k <= p` | Error if `k > p` |
