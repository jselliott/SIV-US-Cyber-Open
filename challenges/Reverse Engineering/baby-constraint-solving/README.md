# Baby Constraint Solving

## Description

Come get some free points on this easy constraint solving crackme, I'll even start your angr script for you:

```python
import angr
p = angr.Project('./virtualized_structures_very_very_easy')
state = p.factory.full_init_state()
simgr = p.factory.simgr(state)
simgr.explore()
```

free hint: When your computer runs out of memory, you might need to swap to Z3

author: caffix

## Files

* [virtualized_structures_very_very_easy](files/virtualized_structures_very_very_easy)

