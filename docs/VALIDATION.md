# Validation - 2026-10-06

Windows / Python 3.12 / Node 22 / pnpm 11.19.0. TypeScript checks and production builds passed locally.
All examples use synthetic data. Local tests do not imply successful hosted CI or quality on real customer data.

7 tests passed for server-side price calculation, stock, SKU and quantity checks, duplicate rejection, disabled model and concurrent-call rejection. An actual gpt-6.1-sol Codex invocation selected 2 Oak desks and 2 Form chairs; server total was 87,600 RUB. The invocation was repeated after disabling shell/unified_exec/web search. This narrow test does not prove general model reliability or prompt-injection resistance.

Docker image built and started locally as a non-root user. Static UI and health endpoint returned successfully. Container catalogue has 6 synthetic products; desk + chair quote was 43,800 RUB. Model access stayed disabled in the container.

## Selected interface verification

Final TypeScript/Vite build passed. Browser review at measured 1454 × 818 desktop and 443 px mobile width found no horizontal page overflow. Escape closes project dialogs. `preview.png` is an actual local application screenshot, not a design mockup.
Browser quote for one Line desk and one Form chair: 43,800 RUB. One actual authenticated gpt-6.1-sol Codex request selected these two SKUs and returned the same server-validated quote. Search submission was checked after fixing input focus.
