# Source-Driven Development

## Use When

Use this overlay when implementation correctness depends on current framework, library, SDK, protocol, cloud, browser, database, or platform behavior.

Common triggers: React/Next/Vue/Svelte, OpenAI APIs, auth providers, payment APIs, ORMs, migrations, cloud services, browser APIs, CI/CD config, or any fast-moving dependency.

## Process

1. Detect stack and exact versions from project files.
2. Fetch official documentation for the specific pattern being used.
3. Prefer official docs, official examples, changelogs, migration guides, standards docs, and runtime compatibility tables.
4. Implement according to verified current patterns.
5. Cite sources in the final answer and, when useful, in short code comments near non-obvious choices.
6. If official docs conflict with existing project style, surface the tradeoff before choosing.

## Source Hierarchy

1. Official product/framework docs.
2. Official blog, changelog, migration guide, RFC, release notes.
3. Standards bodies and platform references.
4. Compatibility databases maintained for the platform.

Avoid using random blog posts, Q&A sites, or memory as primary authority for version-sensitive decisions.

## Integration

- Combine with SDD for new systems whose stack choices matter.
- Combine with TDD when API behavior can be tested deterministically.
- Combine with EDD when LLM SDK, tool-calling, tracing, or eval APIs are involved.
- Use `openai-docs` as the official-source path when building with OpenAI products or APIs.
- Use `vercel-composition-patterns` when current React component architecture or React 19 API guidance matters.
- Combine with review mode to catch stale APIs in diffs.

## Output Contract

State:

- Detected versions.
- Official sources used.
- Patterns adopted.
- Any unverified or conflicting areas.
- Commands run or recommended.
