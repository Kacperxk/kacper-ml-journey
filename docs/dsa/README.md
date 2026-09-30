# Data Structures & Algorithms — Parallel Track

A slow, structured side track running alongside every phase from Phase 1 on. Not a priority over the current phase, but tracked and reviewed like everything else — not background LeetCode.

**Pace:** one reading + 2–3 problems per week (~2–3 hours). At that rate the full path takes roughly 14 months — finishing around when interview prep starts (`docs/ROADMAP.md`, month 15–16).

---

## Resources

| Resource | Use | Access |
|---|---|---|
| *Problem Solving with Algorithms and Data Structures using Python*, 3rd ed. — Miller & Ranum | Theory spine: a first university DSA course, in Python | Free, runestone.academy (pythonds3) |
| NeetCode 150 (neetcode.io) | Practice spine: 150 problems grouped by pattern, easy → hard within each group | Free |
| NeetCode's per-problem explanation videos | Where the book is thin: two pointers, sliding window, backtracking, DP, greedy, intervals | Free |

## Path

Each block: read the chapter first, then that block's NeetCode 150 problems in order.

| # | Block | Reading (pythonds3) | Problems |
|---|---|---|---|
| 0 | Big-O and the real cost of Python's `list`/`dict`/`set`; `collections` (`deque`, `Counter`, `defaultdict`), `heapq`, `bisect` | ch. 2 | — |
| 1 | Arrays & Hashing | 5.5 | 9 |
| 2 | Two Pointers, Sliding Window | NeetCode videos | 11 |
| 3 | Stack | 3.2–3.9 | 7 |
| 4 | Binary Search (+ recursion basics) | 5.2–5.4, 4.1–4.7 | 7 |
| 5 | Linked List | 3.19–3.23 | 11 |
| 6 | Trees, Tries | 6.1–6.8, 6.12–6.15 | 18 |
| 7 | Heap / Priority Queue | 6.9–6.11 | 7 |
| 8 | Backtracking | 4.9–4.11 | 9 |
| 9 | Graphs (BFS, DFS, topological sort, Dijkstra) | ch. 7 | 19 |
| 10 | Dynamic Programming (1-D, 2-D) | 4.12 + NeetCode videos | 23 |
| 11 | Greedy, Intervals | NeetCode videos | 14 |
| 12 | Math & Geometry, Bit Manipulation | 8.3 (optional) | 15 |

Block 9's topological sort is the same algorithm as `microtensor`'s `Value.backward()`.

## Method

- **Try it alone first** — at least 25 minutes before looking anything up. If stuck, watch the explanation, close it, and write your own version later (same day or next).
- **One file per problem:** `dsa/<NN>-<block>/<problem_slug>.py` — problem link, the approach in 1–3 lines, time and space complexity, and `assert`-based tests.
- **Spaced repetition:** at the start of each new block, redo the hardest problem from the previous block without notes.
- **Git:** commit scope `dsa/<block>` (e.g. `feat(dsa/arrays-hashing): two sum`); tag each finished block `dsa-<NN>-<block>`.

## How Claude tracks it

- Solutions get the same line-by-line code review as phase work, including a check of the stated complexity.
- Pace check folded into regular phase pacing: roughly one block per 3–6 weeks.
- Every audit records DSA progress (blocks done, problems done vs. expected pace).

## Progress

- [ ] 0 — Big-O & Python data structures
- [ ] 1 — Arrays & Hashing
- [ ] 2 — Two Pointers, Sliding Window
- [ ] 3 — Stack
- [ ] 4 — Binary Search
- [ ] 5 — Linked List
- [ ] 6 — Trees, Tries
- [ ] 7 — Heap / Priority Queue
- [ ] 8 — Backtracking
- [ ] 9 — Graphs
- [ ] 10 — Dynamic Programming
- [ ] 11 — Greedy, Intervals
- [ ] 12 — Math & Geometry, Bit Manipulation

Started: 2026-09-28.

---

*Last updated: 2026-09-30*
