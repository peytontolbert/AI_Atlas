# Audit Corpus

This file defines the source corpus for bounded completeness and sentence-level source auditing.

## Included Source Classes

1. Primary papers, specifications, and standards.
2. Official technical reports from recognized institutions.
3. High-quality surveys and textbooks.
4. Reproducible implementation documentation.
5. Vendor documentation only for vendor-specific behavior.

## Excluded Source Classes

- Marketing pages used as support for technical claims.
- Unsourced blog posts used as sole support for core concepts.
- Forum comments used as sole support for core concepts.
- Generated summaries used as evidence.
- Product release notes unless the node or claim is explicitly product-specific.

## Update Date

Current audit boundary: 2026-06-25.

## Corpus Ledger


| Layer | Corpus searched | Reviewer | Review date | Status |
|---|---|---|---|---|
| foundation | `ref_aima`, `ref_chinchilla`, `ref_formalml`, `ref_scaling`; `23` nodes, `178` sentence-ledger rows, `41` edge-ledger rows | codex | 2026-06-25 | Complete for bounded atlas coverage |
| representation | `ref_aima`, `ref_ddia`, `ref_dlbook`, `ref_domainrand`, `ref_formalml`, `ref_gnn`, `ref_koller`, `ref_moe`, plus 9 more layer sources; `19` nodes, `167` sentence-ledger rows, `57` edge-ledger rows | codex | 2026-06-25 | Complete for bounded atlas coverage |
| paradigm | `ref_aima`, `ref_diffusion`, `ref_domainrand`, `ref_dpo`, `ref_flow`, `ref_gan`, `ref_jepa`, `ref_nas`, plus 6 more layer sources; `23` nodes, `208` sentence-ledger rows, `84` edge-ledger rows | codex | 2026-06-25 | Complete for bounded atlas coverage |
| objective | `ref_aima`, `ref_diffusion`, `ref_dpo`, `ref_flow`, `ref_formalml`, `ref_gan`, `ref_pml`, `ref_rlbook`, plus 3 more layer sources; `22` nodes, `195` sentence-ledger rows, `73` edge-ledger rows | codex | 2026-06-25 | Complete for bounded atlas coverage |
| mechanism | `ref_aima`, `ref_dlbook`, `ref_flow`, `ref_mamba`, `ref_mod`, `ref_pml`, `ref_structured`; `37` nodes, `321` sentence-ledger rows, `111` edge-ledger rows | codex | 2026-06-25 | Complete for bounded atlas coverage |
| model | `ref_aima`, `ref_bert`, `ref_diffusion`, `ref_diffusion_lm`, `ref_dlbook`, `ref_dreamer`, `ref_flow`, `ref_fno`, plus 22 more layer sources; `52` nodes, `465` sentence-ledger rows, `192` edge-ledger rows | codex | 2026-06-25 | Complete for bounded atlas coverage |
| training | `ref_aima`, `ref_chinchilla`, `ref_diffusion`, `ref_dlbook`, `ref_domainrand`, `ref_dpo`, `ref_flow`, `ref_gan`, plus 13 more layer sources; `27` nodes, `247` sentence-ledger rows, `101` edge-ledger rows | codex | 2026-06-25 | Complete for bounded atlas coverage |
| memory | `ref_aima`, `ref_ann`, `ref_dlbook`, `ref_nist`, `ref_pml`, `ref_rag`, `ref_transformer`; `17` nodes, `148` sentence-ledger rows, `54` edge-ledger rows | codex | 2026-06-25 | Complete for bounded atlas coverage |
| reasoning | `ref_aima`, `ref_dlbook`, `ref_dreamer`, `ref_got`, `ref_pml`, `ref_react`, `ref_rlbook`, `ref_rlvr`, plus 4 more layer sources; `26` nodes, `232` sentence-ledger rows, `86` edge-ledger rows | codex | 2026-06-25 | Complete for bounded atlas coverage |
| alignment | `ref_aima`, `ref_c2pa`, `ref_ddia`, `ref_dlbook`, `ref_dpo`, `ref_formalml`, `ref_llmjudge`, `ref_nist`, plus 6 more layer sources; `20` nodes, `180` sentence-ledger rows, `66` edge-ledger rows | codex | 2026-06-25 | Complete for bounded atlas coverage |
| infrastructure | `ref_aima`, `ref_ann`, `ref_c2pa`, `ref_cuda_guide`, `ref_ddia`, `ref_digital_twin_ai`, `ref_dlbook`, `ref_gptq`, plus 13 more layer sources; `22` nodes, `207` sentence-ledger rows, `87` edge-ledger rows | codex | 2026-06-25 | Complete for bounded atlas coverage |
| system | `ref_aima`, `ref_bert`, `ref_c2pa`, `ref_chinchilla`, `ref_ddia`, `ref_diffusion`, `ref_digital_twin_ai`, `ref_dlbook`, plus 32 more layer sources; `32` nodes, `477` sentence-ledger rows, `273` edge-ledger rows | codex | 2026-06-25 | Complete for bounded atlas coverage |
