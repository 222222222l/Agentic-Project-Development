# Source Map

This suite is a rewritten integration layer, not a verbatim bundle. It preserves the practical roles of installed and researched skills while reorganizing them under a single project-development architecture.

## Installed Skills Integrated

| Skill | Integrated role |
| --- | --- |
| `clarify-project-requirements` | Alignment gate and low-cost path discipline |
| `karpathy-guidelines` | Non-trivial coding discipline: surface assumptions, keep changes simple, edit surgically, and define verifiable success criteria |
| `grill-with-docs` | Deep project questioning plus domain/ADR capture |
| `grilling` | One-question-at-a-time design interrogation |
| `domain-modeling` | Shared project vocabulary and domain docs |
| `codebase-design` | Deep-module design vocabulary and seam reasoning |
| `setup-matt-pocock-skills` | Per-repo issue tracker, triage labels, and domain doc setup |
| `to-prd` | Conversation/spec to PRD synthesis |
| `to-issues` | Vertical tracer-bullet issue decomposition |
| `tdd` | Deterministic red-green implementation at agreed seams |
| `improve-codebase-architecture` | Architecture review and deepening opportunities |
| `code-review` | Standards and spec review |
| `diagnosing-bugs` | Reproduce-minimize-hypothesize-instrument-fix loop |
| `vercel-composition-patterns` | React component API and composition overlay for scalable UI architecture |
| `openai-docs` | Official OpenAI documentation overlay for SDK/API/model-sensitive implementation |
| `product-design:get-context` | Product/UI brief gate before design, prototype, or image-to-code work |
| `product-design:audit` | Evidence-based UX, flow, and accessibility review from captured screens |
| `product-design:ideate` | Image-based visual exploration for product UI directions |
| `product-design:image-to-code` | Responsive frontend implementation from selected visual references |
| `browser:control-in-app-browser` | Local browser verification, screenshots, and interaction checks for web work |
| `chrome:control-chrome` | Logged-in or extension-dependent browser verification when existing Chrome state matters |

## Installed Skills Reviewed but Kept Outside the Core Router

These skills remain useful, but they are domain, artifact, discovery, or meta-skill specialists rather than general project-development modes:

| Skill | Reason |
| --- | --- |
| `find-skills` | Discovery support for finding more skills; not a development lifecycle mode |
| `search` | Source retrieval support; source-driven development already defines when to use official sources |
| `skill-creator`, `skill-installer`, `plugin-creator` | Meta-skills for building or installing skills/plugins |
| `documents`, `pdf`, `presentations`, `spreadsheets`, `template-creator` | Artifact specialists used only when the project deliverable is that file type |
| `imagegen`, `hatch-pet` | Visual asset or pet-package specialists, optional for projects needing those assets |
| `market-signal-analysis`, `china-policy-risk-analysis` | Domain-analysis skills, not general software project-development skills |

## Researched Skills Rewritten Into This Suite

| Skill | Integrated role |
| --- | --- |
| `addyosmani/agent-skills@spec-driven-development` | SDD assumptions/spec/plan/tasks/implementation gates |
| `addyosmani/agent-skills@source-driven-development` | Official-doc verification overlay |
| `fradser/dotclaude@behavior-driven-development` | BDD discovery, Given/When/Then, executable specifications |
| `robotlearning123/behavior-driven-testing@behavior-driven-testing` | Branch matrix, behavior-first test coverage, real-environment validation |
| `promptfoo/promptfoo@promptfoo-evals` | Promptfoo eval suites, rubrics, datasets, CI eval gates |
| `github/awesome-copilot@eval-driven-dev` | Python LLM app eval pipeline, instrumentation, golden datasets, result analysis |

## Design Difference

The original skills are usable independently. This suite adds:

- A single mode-selection router.
- Explicit tradeoffs between SDD, BDD, TDD, EDD, and source-driven work.
- Progressive disclosure by project risk and output type.
- Repo-level personalization.
- Explainable decision traces.
