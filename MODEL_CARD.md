---
license: apache-2.0
library_name: runesmith
tags:
- agent
- code-generation
- self-improvement
- software-engineering
- ai-agents
- program-repair
- autonomous-agents
- llm
- open-source
---

# Runesmith 1.0

Runesmith is a non-traditional model. It has no weights. It is a fixed policy plus persistent, evidence-bearing state that turns whatever inference you give it (a free-tier endpoint, a paid API, a model on your own computer) into verified changes to software. It plans milestones, has your model write the code and the acceptance checks, checks every change before it is applied, and keeps a hash-chained record of what it did. It can also rewrite its own repair step, and a new version of that step becomes active only after it wins a trial on your own work, or when you choose it and the ledger records your choice.

This card is written from the paper, *Beyond the Model* (see "How to cite"), and from the release's audited numbers. Where the paper limits a result, the limit is stated next to the result here.

**What is and is not shown, in short.**

- Runesmith changes its own code only on evidence, and it has passed a sealed test of doing so. It improved on its own previous generation under a sealed, preregistered test: a generation of its repair step that its own Kaizen loop produced repaired 57 of 162 sessions against its predecessor's 35 of 162, with the same cheap repair model, on 54 fresh tasks from two repositories that supplied no task to the organ's development (exact p = 0.000845; within the larger repository alone p = 0.0020), in about half the time per success. The predecessor, an earlier generation from the same loop, had not beaten the shipped one, and the new generation was then compared with the shipped one in two later sealed studies: in a smaller one on small public repositories (U1) it led both the shipped generation and its predecessor in direction, without a significant difference, and in LOC1 (below), on three large public repositories, it repaired more than the shipped one.
- LOC1 (sealed 2026-10-06), the sealed test of that new generation (C7) against the shipped one (g0): on 56 fresh tasks in three large public repositories (pygments, sqlglot and astroid), with one free repair model (gpt-oss-20b) and one envelope for every arm, C7 repaired 42 of 168 sessions and g0 17 of 168 (exact one-sided p = 5835/2097152 = 0.00278, below its Bonferroni level of 0.0083 over its three tests; verdict PASS). A hand-written, trace-aware rule, HEUR, written by the study's designer after C7 existed, repaired 65 of 168, more than C7 (mirrored p = 101/131072 = 0.00077; verdict HEUR_BETTER): a gain that the loop found by itself, a careful designer can also write. A replication on a second model (gemini-3.5-flash) completed one task and could detect no difference (NO_DIFFERENCE_DETECTABLE). The protocol was sealed at 2026-10-06T10:41:04Z and the wording of the result at 11:34:30Z, both before any outcome, and their fingerprints were anchored in Bitcoin blocks 970170 and 970174 (OpenTimestamps) hours before the analysis (16:36:53Z). With SR7 this is a sealed two-step record, and SR7's p-value survives Bonferroni correction across all 23 sealed or registered comparisons the program has run.
- A second self-improvement (faster memory retrieval, authored by a free model) was replicated on a fresh cohort; a frozen generation repaired its own test configuration; the predecessor kernel promoted target-hidden corrections on revisions of a production service and supervised that service's operations across restarts, continuing without observer intervention after its start.
- Free-tier models were the last author of every applied change to Runesmith Motion, whose engine (`motion.mjs`, at 52 milestones) computed the graphics of every frame of the launch film, and which ran unattended by the project lead's definition on two occasions; in the acceptance test, run by an AI in a newcomer's seat, one free Google key took a project to a checked, working feature in 16 minutes. On the build just before 1.0.0, with free models as both repair model and improver, Runesmith's scheduled repair rounds repaired 69 of 89 single-line regressions injected one at a time into a project with a real test suite, each accepted by a held-out judge (one project, observational, no comparison arm).
- Six of the seven sealed tests in the study series (the paper's "SR" studies, SR1 to SR7, each a preregistered test of a change to Runesmith's own machinery) did not show their effect; they shaped the loop that then passed (its held-out validation, and the affordance audit in its author's packet, came from them).
- After that series, three sealed studies, U1 (2026-10-05), U2 and U2b (to 2026-10-06), compared the improved generation with SR6-W's fixed scaffold, which U1's protocol calls "the strongest fixed scaffold the record has defined", driving the same model in the same kernel (formally, "the same model with a simple fixed script in place of Runesmith's repair organ"), on fresh tasks from two public repositories. Across the six model-by-study comparisons, the improved generation was ahead in direction in three (2.6B model: 3 of 17 against 0 of 17; 20B: 33 against 23 of 60; 120B: 34 against 28 of 63), level in two (120B: 10 of 17 each; 2.6B: 9 of 51 each) and behind in one (U1, 20B: 20 against 26 of 51 sessions; per task 5 better, 6 worse, 6 tied, in a study the remaining credit cut to a size with 80% power only for an advantage of about 36 points). None is significant in either direction; this is a descriptive tally, not a registered analysis, and the six are not pooled. U1's replication attempt of SR7 (20 of 51 against the predecessor's 15 of 51) went in SR7's direction and was not significant either.
- Starved of every model in a sealed study (SI, 2026-10-05: 104 opportunities across 13 states, with no model configured or with every model failing), no request reached a model, no change was unauthorized and every ledger chain stayed intact. The sealed harness counted 18 failures (17.3%, upper bound 24.6%): 15 effects recorded without a ledger event of their own (a check-autopilot failure counter, and own-log lines for the owner's one-more-try request and restart decision), and 3 made by a defect in the harness's own detector.
- Not yet measured: whether Runesmith makes a given model better than that model is on its own (no study compares a model working alone with the same model inside Runesmith); whether its competence survives a named change of model; learning across users (release 1 does not do it).

## Model details

| | |
|---|---|
| Name | Runesmith (the Core, which is the runtime, and the Studio, which is its browser interface) |
| Version | Runesmith 1.0 (1.0.0 at release). Builds made before the release carry version 0.1.0, the number of the Core's first release on 2026-09-24. |
| Developed by | AI ThinkLab. Paper author: Lars O. Horpestad. |
| Release date | 2026-10-06 |
| License | Apache-2.0 for the code (copyright AI ThinkLab; `LICENSE` and `NOTICE` ship with the code). The paper, *Beyond the Model*, is CC BY 4.0. |
| Model type | A non-traditional model: a fixed policy plus persistent, evidence-bearing project state. No weights, nothing trained. |
| Runs on | Python 3.11 or newer with the standard library only, and a web browser for the Studio. An earlier Core snapshot passed 88/88 tests on Windows 11 with Python 3.13, and 84 tests with 4 platform skips on Linux; macOS is not yet verified. |
| Paper | *Beyond the Model: Runesmith, an Open Runtime That Improves Software and Itself, and the Instrument–Substrate Hypothesis*, 6 October 2026. Preprint; not peer reviewed. |
| Links | Website: [aithinklab.com](https://aithinklab.com). Code: [repository](https://github.com/Veristria/runesmith). Paper: [PDF](https://aithinklab.com/paper/beyond-the-model.pdf), DOI [10.5281/zenodo.23196763](https://doi.org/10.5281/zenodo.23196763). Technical report: [PDF](https://aithinklab.com/paper/beyond-the-model-technical-report.pdf). Guide: [guide](https://aithinklab.com/guide/). Evidence and data: [aithinklab/runesmith-evidence](https://huggingface.co/datasets/aithinklab/runesmith-evidence) (session tables, recompute scripts, seal records). Film: [YouTube](https://youtu.be/cmb_zbqrKvA). Book: [Build with Runesmith](https://www.amazon.com/dp/B0HM7WKGC9). |

## What kind of model this is

The paper's definition (§2): Runesmith is a model in the sense of *a fixed policy plus persistent, evidence-bearing state that maps a goal, an environment and any available inference to verified changes.* One step is

```
(changes, new state) = F_G(goal, environment, state, available inference)
```

where `G` is the active generation, `state` is the persistent state of one project home, and the available inference may be empty. Each change passed the checks the state requires before it was applied, and the new state extends the old one by appended ledger events, maps, memory of attempts and experience records.

- **No weights.** The "parameters" are readable code and declared configuration: the organs (self-modifiable code such as the repair organ), the contracts that bound them, the acceptance contracts of a project, and policies such as routing order and schedules. The models you connect are inputs to the system, not parameters of it.
- **The policy is fixed within a generation.** A generation binds the organ files, a kernel snapshot and a fixed configuration. It is identified by digests and is immutable once frozen. A change produces a new generation; the previous one stays available for rollback.
- **Learning happens only through evidence gates, or through a recorded owner choice.** In the Core a new generation arises only through the Kaizen loop: Runesmith diagnoses its own telemetry, selects a target by a declared rule, asks a model for an organ change with a prediction and a falsifier, qualifies the candidate on held-out replays, and freezes it. A frozen candidate is not switched on. It becomes active only by winning an online trial on fresh work (seeded assignment, one-sided Fisher exact looks with Bonferroni-spent alpha, compare-and-swap activation, never a default promotion) or by the owner's explicit choice, which the ledger records.
- **What the word does not carry.** Calling this a model does not claim that it generalizes beyond the envelopes under "Evidence", or that a generation transfers to other models. Its behaviour depends on the environment and on the models it is given, not on the policy alone.

## Intended use

- Planning and building software in a project folder: milestones with a "done when" statement, acceptance checks you read and approve, drafts written by the models you connect, checked on a throwaway copy of the project, and applied only when you apply them (or in folders you name, if you switch on automatic apply for checked builds).
- Repairing failing tests in existing Python projects. A repair is made on a private copy and reaches you only after a held-out judge accepts it.
- Keeping a map of your environment and of Runesmith itself, and an activity ledger you can verify.
- Using cheap, free-tier or local models for real work with a record of what was done and checked. Results depend on the model. The project's guidance is that larger models plan and write better and small models work better on small checked steps; no minimum model size is promised.
- Research on evidence-gated self-modification, including replicating the studies in the paper.

The owner stays in the loop: you approve the checks, apply the drafts and decide how much freedom Runesmith has.

## Out of scope

- Operation without an operator. No result in the record shows it. In the longest case study the operator stepped in repeatedly, and the three measured stretches without intervention ended in a silent two-day stall, a 47-hour hold for a recovery review, and a 43-minute stretch with no milestone completed.
- A claim that Runesmith makes any model better than it is alone. No study measures this.
- General recursive self-improvement, improvement of its own improvement policy, or compounding improvement across generations. None is shown.
- Running code or generations you do not trust. Checking a build runs the project's own code on a throwaway copy of the folder, and the copy is not a security boundary. Imported generations should come from trusted sources or run under an operating-system sandbox.
- Repair of natural (non-synthetic) bugs, repair of non-Python objects, other languages, social, commercial or business outcomes, general DevOps, and safety-critical use. None was tested.
- Learning across users. Release 1 does not do it.

## Inputs and outputs

**Inputs.** Your goals and brief; the project folder (files and tests); acceptance checks you approve; settings that decide how much freedom Runesmith has (scheduled work, self-improvement, the check autopilot, full-speed scheduling and file application are all off until you turn them on); the models you connect and the roles you give them (Worker, Planner, Checker, Improver); and API keys for providers that need one.

**Outputs.** Plans and milestones; acceptance checks proposed for your approval; drafts of files (proposals only: nothing is written to your files until you apply them); fixes for failing tests; the maps (environment and self); a hash-chained activity ledger; `RUNESMITH.md`, a one-line-per-event log of what Runesmith did in the folder; frozen generations and the records of their trials.

**Data flow.** With a hosted model, your goals and the file content in each request go to the provider you chose. With a model on your own computer, nothing leaves it. A project's state, evidence and history stay in local files. The Studio listens on `127.0.0.1` only, through a private link.

## Inference sources

Runesmith runs on any OpenAI-compatible chat endpoint. The Studio has presets for the providers below; "free" means a free tier that exists today and has rate limits, not metered cost. A free route is a route label: free capacity varied by the hour in the record and caused stalls.

| Source | Providers |
|---|---|
| Free tiers (where a provider offers one) | Google AI Studio (Gemini), NVIDIA, Groq, OpenRouter, Mistral |
| Paid | OpenAI, Anthropic (through its OpenAI-compatible layer), DeepSeek, Together AI, and paid models on OpenRouter |
| On your own computer | Ollama, LM Studio, llama.cpp server |
| Any OpenAI-compatible endpoint | Hugging Face's inference router, vLLM, a company gateway, and similar. Enter it as a custom endpoint; no Hugging Face preset ships at the time of writing. |
| No key | A chat window: Runesmith shows each request, you paste it into any chat model and paste the reply back. Every call waits for you. |

**What the record exercised, and what it did not.** The studies and case studies in the paper used these routes: Google Gemini 3.1 Flash Lite and Gemini 3.5 Flash; NVIDIA Nemotron 3 Super and Ultra and Kimi K3; `gpt-oss-20b` and `gpt-oss-120b` through Groq and other routes; Liquid LFM 2.5 (2.6B); and Claude Opus 4.5 through OpenRouter, a paid route. Mistral, OpenAI, DeepSeek, Together AI and the Hugging Face router are supported by the connection code but were not exercised in the paper's record. Local servers were tested only against stand-ins that follow the servers' documentation (in one out-of-the-box test), not against real Ollama, LM Studio or llama.cpp servers: they are supported, not proven. No result in the paper licenses a claim that a particular model, local or hosted, will reproduce the reported effects.

## How it adapts

**Within a project.** State accumulates: the ledger, the environment and self maps, memory of what was tried, experience records, and the approved acceptance checks that judge every later build. In the paper's terms this is adaptation ("any history-dependent change in behavior"). It is not learning in the paper's stricter sense, which requires a versioned state change that improves a predeclared future outcome against a matched fixed-state baseline.

**Its own repair step.** The starting generation of the repair organ is g0 (the repair step as shipped). C7 (the improved repair step that the sealed test SR7, described under "Evidence", compared with its predecessor B, an earlier improved generation) ships in a library with a caveat shown to you. The evidence: C7 was shown better than B in SR7 and better than g0 in LOC1 (in which a hand-written trace-aware rule did better than C7), on synthetic single-line bugs with one model (`gpt-oss-20b`); which of its steps carried the gain was not tested, and its module-path step recognises only the package names of the two repositories used in development and does not fire on yours. On your work it must win an online trial before it becomes active, or you may activate it by explicit choice, which ends any open trial and is recorded.

**Across users.** Release 1 does not learn across users. No mechanism sends experience or organ changes between installations. The only path is a generation archive that one person exports and another imports by hand; an imported generation is frozen and inactive, confined like a local one, and becomes active only if it wins an online trial on the receiver's own work or the receiver explicitly chooses it.

## Evidence

All figures are from the paper and its technical report, which together report every sealed result. The p-values are nominal and one-sided under each study's declared design. No result has been rerun by a distinct investigator: the "recomputations" are second scripts written inside the project from the same raw receipts. The SR5 to SR7 studies (sealed, preregistered tests around Runesmith's own repair step) ran on the open-source Core; the object-improvement result, S1 (one self-correction of a generation's own configuration) and M1 (a model-authored memory-retrieval improvement, tested for speed) ran on the earlier kernel and subject machinery, which is a different code base. All were run by AI ThinkLab with AI collaborators in named roles.

### The one sealed positive for the system's own change: SR7

A frozen successor generation of the repair organ (C7), written inside Runesmith's Kaizen loop for a target chosen by a declared rule from the system's own telemetry, was compared with its frozen predecessor (B) on fresh tasks. Sealed 2026-09-25T02:15:52Z.

| | B (predecessor) | C7 (successor) |
|---|---|---|
| Strict successes (54 tasks × 3 rounds = 162 sessions per arm) | 35 / 162 (21.6%) | 57 / 162 (35.2%) |
| Organ errors | 0 | 0 |
| False promotions | 2 | 2 |
| Seconds per strict success | 1,023.6 | 541.8 |

- One-sided sign-flip test over the 54 task components: p = 0.000854 (Monte Carlo, 1,000,000 seeded flips); the exact value is p = 443/524288 = 0.000845, which anyone can recompute from the released session table and script. At task level: 18 better, 3 worse, 33 tied; C7 solved 32 of the 54 tasks at least once, B 20. Within the larger repository alone (50 tasks): 48 against 28, exact p = 0.0020. The result stays below 0.025/m for any family of up to 29 tests, so it survives Bonferroni correction over every sealed comparison in the record.
- Difference +13.6 percentage points; a descriptive, post-hoc 95% cluster-bootstrap interval is +6.2 to +21.6 points, so smaller true effects are not excluded.
- 324 of 324 sessions completed, none censored. The author was Claude Opus 4.5, a paid model reached through a commercial router, which scores below today's free-tier Gemini 3.5 to 3.8 Flash models on SWE-bench Verified (Vals.ai, 2026-09-01: 76.4% against 78.8% to 80.8%); the repair model in both arms was `gpt-oss-20b`; the kernel envelope was identical (at most 5 model calls, 8,192 tokens, 45 signal runs, 64,000 request bytes and 1,800 seconds per session). Cost of the whole study: $5.39.
- Task family: synthetic single-line regressions injected into test-covered functions of two real Python repositories. Development used only two other repositories, so the confirmation tests the organ on code bases it was not developed on.

Boundaries, all stated in the paper:

1. SR7's comparator is B, not g0 and not a conventional scaffold. In an earlier study (SR5), B's point estimate was below g0's (36/180 against 50/180), so SR7 alone does not show C7 beating g0; LOC1 (next section) later compared C7 with g0 directly, and U1, U2 and U2b compared it with a fixed scaffold (no significant difference in any of six comparisons).
2. The author was a paid model (though below today's free-tier Gemini Flash models on a public coding benchmark). Free-class authors produced no transferring change in SR5 or SR6.
3. One of the five accepted tiers (the module-path tier) was inert in the study, and no ablation shows which tiers carried the effect.
4. Errors and false promotions were equal between the arms, not lower. The time figure is per strict success, not per repair.
5. SR7 itself had no replication, no second improving generation, no natural bugs and no hand-written localization comparator (LOC1, next section, is a later study, and in it a hand-written trace-aware rule repaired more than C7). Fifty of the 54 tasks come from one repository (within it alone, p = 0.0020).
6. The target was chosen by a declared rule, but the Kaizen machinery was built by a consultant who knew earlier results (the paper calls this a hybrid lineage).
7. The improvement is of the repair organ. The Kaizen loop, the target rule and the trial machinery did not change, so this is not an improvement of the improver. The paper calls it "a nudge towards recursive self-improvement": the system's own loop rewrote part of the system, a sealed test confirmed the new version better than the one it replaced, and the loop itself did not change.

The paper's earned name for this result: a bounded subject-improving adaptive runtime within the SR7 envelope.

### The second sealed test: C7 against the shipped organ (LOC1)

SR7 compared C7 with its predecessor B, not with the organ Runesmith shipped with (g0), and the October studies (U1, U2, U2b) used repositories small enough that C7's file-ranking steps could not act. LOC1 was sealed on 2026-10-06 to close both gaps: fresh synthetic single-line regressions in three large public Python repositories (pygments, sqlglot, astroid), where the navigation index exceeds its 12,000-byte cap, one free repair model (gpt-oss-20b), three rounds per task and one envelope for every arm. Three arms ran: g0, C7 and HEUR, a hand-written trace-aware localization rule written by the study's designer after C7 existed.

| | g0 (shipped) | C7 (self-improved) | HEUR (hand-written) |
|---|---|---|---|
| Strict successes (56 tasks × 3 rounds = 168 sessions per arm) | 17 of 168 | 42 of 168 | 65 of 168 |
| Sessions with the faulty file in the model's edit view | 27 | 86 | 99 |

- Primary test, C7 against g0: exact one-sided sign-flip p = 5835/2097152 = 0.00278 (mirrored 0.9988), below its Bonferroni level of 0.0083; at task level 15 better, 6 worse, 35 tied; verdict PASS. By repository, C7 against g0: 27 against 13 (pygments), 4 against 3 (astroid) and 11 against 1 (sqlglot), descriptive.
- Secondary test, C7 against HEUR: p = 0.9998 (mirrored 101/131072 = 0.00077); at task level 2 better, 16 worse, 38 tied; verdict HEUR_BETTER. The hand-written rule repaired more than the self-improved organ, so LOC1 does not show C7 above a careful hand-written rule.
- C7 took about half of g0's time per strict success (1,520 against 2,806 seconds).
- Replication on gemini-3.5-flash (free tier): one task completed by the stop time, 3 of 3 sessions each; verdict NO_DIFFERENCE_DETECTABLE. It replicates nothing.
- Sealed in two steps: the protocol at 2026-10-06T10:41:04Z, the wording of the result at 11:34:30Z, the first session at 12:05:45Z, the analysis at 16:36:53Z. The fingerprints were submitted to OpenTimestamps and anchored in Bitcoin block 970170 (12:12:09Z) and block 970174 (12:48:21Z). The evidence dataset ships the session table, the recomputation and the seal records.
- Deviation: at 12:22Z, before any outcome was read, the gateway's concurrency cap for the study's calls was raised from 8 to 16 to raise throughput; the sealed protocol had said it would not change. The paper reports it.

What it licenses: on fresh synthetic single-line regressions in three large public Python repositories, with one free model and an identical envelope, C7 repaired more than the shipped organ g0. With SR7 this is a sealed two-step record: the loop produced a generation that beat its predecessor, and that generation also beat the shipped organ on fresh public repositories. It does not license any claim that C7 beats the hand-written rule, a scaffold or a model working alone, any claim about natural bugs, other task families or other models, or recursive self-improvement beyond "a nudge towards". HEUR was written after C7 existed and developed on SR7's analysed pool; one model carried the test; three repositories.

### All sealed or registered confirmatory comparisons (technical report, Table 1)

Eleven comparisons: three passed (SR7, M1 confirmation 02 and M1 replication 03, which test the same frozen candidate on two cohorts), one failed a preregistered guard, seven did not show their effect or were null. Within the seven SR tests, one passed. U1's two tests and LOC1's three, run after the record's cut, are listed at the foot and are not in that count. The second column says what each row compared.

| Study (2026 date) | Comparison | Result | Verdict |
|---|---|---|---|
| S1-MECHANICS-1 (09-10) | learned vs fresh policy, sealed offline fixture | 73 vs 65 verified outcomes; SCG 0.0333, interval ≈ [−0.0335, 0.1001] | inconclusive |
| O1-Q (09-10) | source-complete workflow vs deployed object, 60 tasks | 54/60 vs 53/60; McNemar p = 0.5 | not confirmed |
| H18 v7 (09-13) | registered scripted challenge, successor vs predecessor, 8 opportunities | 3 successor-only, 0 predecessor-only, 5 ties; p = 0.125 | NOT_PASS |
| M1 confirmation 01 (09-20) | memory-retrieval candidate 15 vs the frozen predecessor, 16 blocks | 13/16; median 0.694862; family 1.279762 > 1.10 | FAIL (guard) |
| M1 confirmation 02 (09-23) | candidate 19 vs the frozen predecessor, 16 blocks | 13/16; median 0.758123; p = 0.0106354 | PASS (candidate 19 was written after confirmation 01's failure; the same applies to replication 03) |
| M1 replication 03 (09-23) | same, fresh seeds | 15/16; median 0.668941; p = 0.0002594 | PASS |
| SR1-MIN (09-23) | model-authored selector vs predecessor, 19 components | 0.210526 vs 0.210526; p = 0.623047 | not shown |
| SR3 (09-23) | experience-derived tool (B) vs Runesmith v1 (C), 20 components | 0.425 vs 0.350; 3/0/17; p = 0.125 | not shown |
| SR4 (09-24) | sharpened tool vs C, repair-cycle time, 30 analyzable components | slower on 30/30; p = 1.0 | not shown |
| SR5 main (09-24) | Kaizen generation B vs g0, 60 tasks × 3 rounds | 36/180 vs 50/180; p = 0.979 | not shown |
| SR5b (09-24) | same, 46 medium-repository tasks × 3 rounds | 58/138 vs 60/138; p = 0.685 | not shown |
| SR6-W (09-24/25) | shipped organ g0 vs a strong fixed scaffold, one 2.6B model, 68 tasks | 5/68 vs 12/68; p = 0.994; mirrored p = 0.0327 | NULL |
| SR7 (09-24/25) | C7 vs B, 54 tasks × 3 rounds | 57/162 vs 35/162; p = 0.000854 (exact 0.000845) | PASS |
| U1 primary (10-05) | C7 vs SR6-W's fixed scaffold, same model and kernel, 17 public-repository tasks × 3 rounds | 20/51 vs 26/51; p = 0.873; mirrored p = 0.2095 | NULL |
| U1 secondary (10-05) | C7 vs B, same tasks | 20/51 vs 15/51; p = 0.1875 | NULL |
| LOC1 primary (10-06) | C7 vs the shipped organ g0, gpt-oss-20b, 56 tasks in three large public repositories × 3 rounds | 42 of 168 vs 17 of 168; p = 5835/2097152 = 0.00278; mirrored p = 0.9988 | PASS (Bonferroni level 0.0083) |
| LOC1 secondary (10-06) | C7 vs HEUR, a hand-written trace-aware rule, same tasks | 42 of 168 vs 65 of 168; p = 0.9998; mirrored p = 101/131072 = 0.00077 | HEUR_BETTER |
| LOC1 replication (10-06) | C7 vs g0, gemini-3.5-flash, 1 task completed | 3 of 3 vs 3 of 3 sessions; p = 1 | NO_DIFFERENCE_DETECTABLE |

Notes on the nulls. SR4 also showed that a keep-best loop scored on tasks whose answers its author sees memorizes them: the tool passed 29/32 development tasks and 1/46 fresh ones; Kaizen now scores only on held-out validation. SR6-W is the one preregistered weak-model test: with a 2.6B model the shipped organ did worse in direction than a strong fixed scaffold, and the mirrored p-value (0.0327) did not meet the declared 0.025, so the verdict is NULL, not a demonstrated harm. The paper does not test why; a plausible reading, not tested, is that model-led navigation spends part of a five-call budget that a weak model needs for edits. SR6-KAIZEN2 (a second free-class generation) closed before confirmation and is not a confirmatory test.

### Other positive results, each bounded

- **Object improvement (the v3 sequence).** Across two owner-specified technical contracts on successive historical revisions of an existing production project, nine terminal episodes produced two strict promotions: the hidden target assertion failed twice on the incumbent and passed twice on the candidate, and all 899 regression tests were preserved. Six of the nine episodes failed, and one more was a correct refutation that was stored as a failure. The successful authors were NVIDIA Nemotron-3-Ultra-550B-A55B (a free route) and `gpt-oss-20b` through Groq. The owner specified both contracts in advance and the controller was changed between episodes, so this is not repeated open-ended discovery and not operation without an operator.
- **Self-correction (S1).** A frozen generation turned a supplied failing-suite receipt into a repair of its own test configuration, with no operator-named target or repair; the repaired generation passed 410/410 tests. One episode (n = 1), and a known flag already made the suite pass in a reference run.
- **Memory-retrieval improvement (M1).** A free-model-authored change to Runesmith's memory retrieval used less search CPU in 13/16 and 15/16 blocks on two fresh cohorts (median reductions 24.2% and 33.1%), after a first candidate failed a preregistered guard. The target was chosen by the operator, the workloads are synthetic, the cohorts ran on one Windows host, and a post-hoc conventional index was not beaten on total CPU (B won 9 blocks, C won 7).

### Out-of-the-box journeys and the Runesmith Motion case study (observational)

Thirteen out-of-the-box journeys (test runs of the Studio as a new owner would meet it): a reference run and twelve more, each operated by one AI (Claude Opus 5.5) acting as the owner and with full knowledge of Runesmith's internals; eleven began from a clean start. They are not a user study and not preregistered. The findings inventory holds 219 findings (49 bugs, 53 gaps, 117 frictions), as a lower bound: 127 fixed and verified live, 69 fixed in test only, 17 open, 4 open with a fix in test, 2 will not be fixed (counts as of 2026-09-29). The check autopilot's approvals were audited by the same AI operator: 8 of 49 were judged wrong at the paper's cut, a self-audit and not a measured error rate.

Runesmith Motion is a browser animation and video composer built through Runesmith in one of those journeys; its engine, at 52 milestones, computed the graphics of every frame of the release's launch film. Figures at the paper's release read of 2026-10-05T11:20Z (they move while the project runs):

- Every one of the 54 applied changes was last written by a free-tier model route (Gemini 3.1 Flash Lite 48, Nemotron 3 Super 120B-A12B 6) and was checked against approved acceptance checks and applied through the guarded path; no applied file was written by the operator, although some literal values in those files were dictated by the operator's milestone texts.
- Of 137 plan items, 54 were done, 76 open and 7 dropped; 116 items were added by the operator and 21 came from Runesmith (its first plan, breakdowns the owner adopted, and smaller steps its stuck policy split off by itself). "Done" means that the approved checks passed and the draft was applied, not that the feature works: the video recorder counted as done was done in name only. The project lead judged one gallery of its output not yet capable of what the launch showcase needs.
- 1,141 model-call records (771 answered, 370 not); the recorded cost estimate is 0.0 on 1,052 and absent on 89, and no call has a positive figure. The operator's own model usage is not metered.
- Unattended by the project lead's definition ("seeing it go at least from one milestone through to the next without interfering") on two occasions: on 2026-09-29 the schedule applied five milestones by itself in 1 h 43 min, and on 2026-10-05 Runesmith applied two milestones in a row that its own stuck policy had split off, with checks approved by its autopilot. Both stretches then waited for the owner (on 2026-09-29 silently). Outside them an AI operator directed the project, and 193 of 281 drafts needed revision.

Supervised field construction of two new projects produced 16 applied changes: 10 by Claude Opus 4.5 (a paid model), 4 by Kimi K3 and 2 by Gemini 3.1 Flash Lite on free routes. Neither project was finished, and a trainer wrote the acceptance checks.

### Test evidence, as logged

The release's operator logged a full suite of 1,609 tests passed with 202 of 202 browser loops for the release of 2026-10-04, and a later run on the merged tree of 1,648 passed and 4 failed, the failures fixed in the next commit. On the release code (commit `05fa549`; the release commit `c94f01f` changes only the README) the full suite passed on 2026-10-06: 1,924 tests passed, 2 skipped and none failed, and every browser use-loop passed. The earlier counts are logged runs, not reruns for this card. The earlier Core snapshot passed 88/88 tests on Windows 11 with Python 3.13 and 84 passed with 4 platform skips on Linux.

## What is not yet measured

- **Uplift.** No study runs a model working alone against the same model inside Runesmith. SR7 and LOC1 run every arm inside Runesmith; SR6-W compares the shipped organ with a strong fixed scaffold, and the scaffold did better in direction; U1, U2 and U2b compared the SR7 generation with that scaffold driving the same model inside the same kernel, with no significant difference in any of six comparisons (the tally is under "What is and is not shown"); the other comparisons are between Runesmith components. Any statement that Runesmith makes a given model better than it is alone is unsupported by a measurement. A preregistered uplift study at equal budget (fresh sealed tasks, at least two named models, a minimal harness and a strong conventional scaffold as comparators) is designed and not yet registered.
- **Named-model substitution.** Whether competence kept as state survives the removal or replacement of the model that produced it has not been tested. The one substitution-like comparison (SR1-MIN, a model-authored selector against its predecessor) returned equal success in both arms.
- **State carryover.** The one measurement (73 vs 65, interval crossing zero) was inconclusive.
- **Weak-model amplification.** Tested once (SR6-W) and null, with the direction favouring the scaffold.
- **Replication of SR7 and LOC1** on other models (LOC1's replication on gemini-3.5-flash completed one task and could detect no difference), a free-class author reproducing SR7, an ablation of C7's five steps, a second improving generation, and natural bugs.
- **Real local servers** (Ollama, LM Studio, llama.cpp), and **first-time, non-technical users**: no journey measured either.

## Limitations

- Every result sits inside a stated envelope (the repair organ of the open-source Core, a rule-selected target, a paid author, one cheap repair model, synthetic single-line regressions). None licenses "general intelligence", "safe system", "recursive self-improver" or "commercial moat".
- Evidence independence is limited. The collaborators who built the studies' machinery, operated the journeys and edited the record are AI collaborators in named roles, and the same model family (Claude Opus) authored SR7's change, built the studies' machinery and operated the journeys. There has been no external peer review.
- The technical report lists 41 threats to validity. Those most relevant here: evaluators and baselines that omit what a conventional workflow already does; development scores on seen tasks that do not transfer; free capacity that varies by the hour; text checks that cannot see rendered output; and the same AI acting as operator and owner, so that every owner audit in the journeys is self-review.
- Several SR task pools come from the laboratory's private repositories, and one evaluator is not hermetic; the paper states what a reader can and cannot reproduce.
- Results depend on the model. Free tiers have rate limits and a round may wait or move to the next model you listed.
- "Done" means that approved checks passed, not that a feature works. A second model that cross-checks the checks can approve wrong ones. Whole-file drafts fail once one file grows past what a model can be shown or can return (targeted edits are planned).

## Safety

- **Checks before change.** Every draft is checked on a throwaway copy of the project against the project's own tests and against acceptance checks written in plain sentences that you read and approve. Nothing is written to your files until you apply it, unless you switch on automatic apply for checked builds in folders you name. Applying a draft is conflict-checked against the files as they are, backed up and undoable; the delegated-build path also requires unchanged source, a root-bound build grant and passing acceptance.
- **Owner control.** Scheduled work, Kaizen, the check autopilot, full-speed scheduling and file application are off by default. A new generation becomes active only by winning an online trial or by your recorded choice, and the previous generation stays available. When a milestone is stuck, the Studio shows a card that says so and lets you choose.
- **The ledger.** A hash-chained, tamper-evident activity ledger, verifiable in the Studio.
- **Keys.** API keys are saved in a file in the project's `.runesmith` folder, referenced by name from the configuration, not written into the configuration or into `RUNESMITH.md`, never shown again after saving, and sent only to the provider they belong to. The file is not encrypted: it relies on your account's file permissions, and the `.runesmith` folder ignores itself for version control.
- **`RUNESMITH.md`.** Runesmith's own one-line-per-event log of what it did in a folder: milestones done, builds applied, checks approved or withdrawn, your decisions, and which model wrote the code. It holds names and counts only, never a prompt, an answer, file contents or a key, and anything that looks like a secret is replaced before it is written.
- **Confinement is engineering, not a security boundary.** Self-modifiable organs run in an isolated interpreter with a secret-free environment and an audit hook; unit tests show reads outside the organ's directory, writes, sockets, subprocesses and environment secrets are refused. The paper states that these hooks are not a hardened boundary. There has been no external security audit.
- **Known failure modes.** Wrong approvals by the check autopilot (8 of 49 at the paper's cut, by self-audit); checks that read text but cannot see what is drawn; stalls that the operator had to notice; free routes that return malformed or repeated output.

## What comes next

Release 1 moves generations between installations only by hand. The design the authors intend to build lets an owner opt in to publishing a generation that has won an online trial on their own work, and lets other installations fetch it, freeze it inactive and activate it only if it wins a trial on their own work. The paper states the open problems: trials on small installations are slow and every look spends real work on a possibly worse generation; privacy of provenance and trial records; poisoning by an adversarial generation; contribution accounting; and gaming. None of this is built. Other planned work: targeted edits for large files, more confined organs each with its own trial, an ablation and replication of SR7, a second improving generation, a named-model substitution study, and the uplift study above.

## How to cite

```bibtex
@misc{horpestad2026beyond,
  author = {Horpestad, Lars O.},
  title  = {Beyond the Model: Runesmith, an Open Runtime That Improves Software and Itself, and the Instrument--Substrate Hypothesis},
  year   = {2026},
  month  = oct,
  note   = {AI ThinkLab. Preprint, 2026-10-06. Not peer reviewed.}
}
```

Model card authors: AI ThinkLab.
