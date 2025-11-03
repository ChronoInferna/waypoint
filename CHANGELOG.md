## 0.2.0 (2025-11-02)

### Feat

- integrate frontend
- **path.py**: validation of path objects (#28)
- add a* algorithm (#6)
- **preprocessing.py**: added map from id to name (#5)

### Fix

- **main.py**: small import fix (#22)
- fixed type of parameter for graph in algorithms (#20)
- absolute imports rather than relative (#8)
- skip node if empty data
- path dataclass fix

### Refactor

- **path.py**: force use of factory methods (#37)
- delete bfs.py (#31)
- more path invariants (#30)
- import shenanigans (#29)
- remove raising errors and just return empty path (#27)
- **path.py**: rename distance to time (#26)
