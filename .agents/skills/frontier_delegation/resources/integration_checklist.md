# Integration Checklist

Use this checklist after injecting anchor code and before writing infrastructure.
Copy this into a task artifact and check items off as you verify them.

---

## A. Contract Extraction (Phase 3)

For each anchor module, extract:

### Exported Interfaces
```bash
grep -n "export interface" src/core/**/*.ts
```
- [ ] List every exported interface
- [ ] For each interface, identify what concrete implementation it needs
- [ ] Note whether each method returns synchronously (`T`) or asynchronously (`Promise<T>`)

### Exported Types
```bash
grep -n "export type\|export const.*:" src/core/**/*.ts
```
- [ ] List every exported type, especially branded types and discriminated unions
- [ ] Note default values (`DEFAULT_*`, `initial*`) — these are the bootstrap state

### Dependency Injection Points
```bash
grep -n "deps:" src/core/**/*.ts
```
- [ ] List every function that accepts a `deps` parameter
- [ ] For each dep, trace its type definition
- [ ] Classify each dep as sync-required or async-allowed

### Invariant Comments
```bash
grep -niE "(MUST|NEVER|ALWAYS|invariant|guarantee|<[0-9]+ms|NO async|NO I/O)" src/core/**/*.ts
```
- [ ] List every invariant
- [ ] For each invariant, note which infrastructure code it constrains

---

## B. Wiring Plan Verification (Phase 4)

For each interface in the constraint surface:

| Interface | Method | Return Type | My Implementation | Sync Match? |
|---|---|---|---|---|
| `OutboxStore` | `load()` | `Promise<...>` | Dexie query | ✅ async OK |
| `BridgeDeps.applyPatch` | `(patch) => { applied }` | Synchronous | Zustand reducer | ✅ sync |
| ... | ... | ... | ... | ... |

### Sync/Async Alignment
- [ ] Every synchronous interface method is implemented synchronously
- [ ] No `async` wrapper around a synchronous contract
- [ ] No `await` in a function that must return `T` (not `Promise<T>`)

### Type Alignment
- [ ] No `as any` casts on anchor code types
- [ ] Branded types are preserved through the infrastructure layer (not widened to `string`)
- [ ] `ReadonlyArray` is not assigned to `Array` (use spread: `[...readonlyArr]`)
- [ ] `ReadonlyMap` is not assigned to `Map` without explicit conversion

### Domain Type Integrity
- [ ] No infrastructure-specific fields added to anchor code types (use separate Maps)
- [ ] Anchor code's exported functions are called, not reimplemented
- [ ] Anchor code's default values are used for initial state (not custom defaults)

---

## C. Cross-Reference Audit (Phase 5)

### Contract Satisfaction
For each exported interface:
- [ ] A concrete implementation exists in the infrastructure layer
- [ ] The implementation passes `pnpm build` type checking
- [ ] The implementation is wired into the app lifecycle (initialized, cleaned up)

### Invariant Compliance
For each invariant comment:
- [ ] The infrastructure code does not violate it
- [ ] Document HOW the invariant is maintained (one line per invariant)

### Anti-Pattern Scan
- [ ] No `(variable as any).anchorField` — indicates a type mismatch being papered over
- [ ] No anchor code types extended via `interface MyType extends Move { rev: number }` in the store
- [ ] No `setTimeout` or `requestAnimationFrame` wrapping synchronous anchor functions
- [ ] No swallowed errors from anchor code functions (if it throws, let it throw)
- [ ] No manual reimplementation of anchor code logic (captureVoice, sanitize, rankQueue, etc.)

### Build Gate
- [ ] `pnpm build` passes with zero errors
- [ ] No `@ts-ignore` or `@ts-expect-error` comments added to suppress anchor code type errors
