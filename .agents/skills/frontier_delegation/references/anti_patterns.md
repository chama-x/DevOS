# Anti-Patterns Registry

Known failure modes discovered during frontier delegation workflows.
Each entry documents what went wrong, why, and the rule that prevents recurrence.

This registry is append-only. New entries are added via the governed evolution loop.

---

## AP-001: The Async Core

**Session:** Gami-Life initial infrastructure wiring
**What happened:** The IDE agent implemented `applyPatch` as an async function backed by IndexedDB (Dexie). The anchor code's interface defined it as synchronous: `(patch: CorePatch) => { applied: boolean; conflictRev?: number }`.
**Why it's dangerous:** The SyncOrchestrator called `applyPatch` and immediately used its return value to decide whether to delete outbox jobs. An async implementation returned a fake `{ applied: true }` synchronously while the real DB operation ran in the background. If the DB operation failed (rev conflict), the outbox job was already deleted — data loss.
**The rule:** Never make a function async if the anchor code's interface returns synchronously. If the constraint surface says `() => T`, your implementation MUST be `() => T`.
**The fix pattern:** Use a Write-Through Cache. The Zustand store (in-memory) is the synchronous source of truth. IndexedDB mirrors it asynchronously as a side effect.

---

## AP-002: Type Pollution

**Session:** Gami-Life initial infrastructure wiring
**What happened:** The IDE agent added `rev: number` and `captureId: string` directly to the `Move` objects stored in the Zustand state array, then cast with `(m as any).rev` to retrieve them.
**Why it's dangerous:** TypeScript can no longer verify the state shape. The `Move` type is the Architect's domain object — polluting it with infrastructure concerns breaks the separation of concerns and makes the constraint surface unreliable.
**The rule:** Never modify anchor code types. Use separate Maps for infrastructure metadata (`moveRevs: Map<MoveId, number>`).

---

## AP-003: Bridge Bypass

**Session:** Gami-Life initial infrastructure wiring
**What happened:** The IDE agent reimplemented the `captureVoice` flow manually in `useStore.ts` — calling `heuristicParse`, then `applyPatch`, then manually enqueueing a reconciliation job — instead of calling the provided `captureVoice()` function from `neuro-symbolic-bridge.ts`.
**Why it's dangerous:** The `captureVoice` function embeds critical invariants: the 4-second abort timeout, the `sanitize()` gate on LLM output, the `logRepairs` audit trail. Reimplementing it loses all of these.
**The rule:** Always use the anchor code's exported functions before writing your own. If the Architect provided a function for a workflow, call it.

---

## AP-004: Prop Guessing

**Session:** Gami-Life app shell wiring
**What happened:** The IDE agent passed `moves={store.rankedMoves}` to `KineticQueue`, but the actual prop name was `ranked`. The agent also passed `move` and `isTop` to `KineticMoveCard`, but the actual props were `ranked` and `isTopSlot`.
**Why it's dangerous:** Wasted build cycles on preventable type errors.
**The rule:** Always `grep_search` for the exact interface definition before wiring component props. Never guess prop names from memory.

---

## AP-005: Telemetry Event Shape Mismatch

**Session:** Gami-Life app shell wiring
**What happened:** The IDE agent constructed a `DWELL_BEFORE_ACT` telemetry event with `{ move, actualMinutes, slot }` fields, but the anchor code's discriminated union defined it as `{ moveId, dwellMs, at }`.
**Why it's dangerous:** Runtime shape mismatch. The friction reducer's `switch` statement would hit the `default` branch, silently dropping the telemetry signal.
**The rule:** When constructing discriminated union values, always read the exact type definition first. Each variant has a unique shape — don't assume they share fields.
