---
template: prompt-log
purpose: "Running log of meaningful AI prompts and outputs used in a project — supports reproducibility and AI-use disclosure"
audience: student
fields_required: [date, goal, prompt, tool, output_location, notes]
naming_convention: "prompt-log.md (one per project, lives in deliverables/)"
courses: [BUS-313, BUS-314, BUS-620, BUS-629, FIN-321, BUS-122B]
started: 2026-08-30
---

# Prompt Log

| Date | Goal | Exact Prompt | Tool (LLM/Sheet/Code) | Output Link/Location | Notes |
| ------ | ------ | -------------- | ------------------------ | ---------------------- | ------- |
| 2026-08-30 | Create professional biography | "Look at this bio template and create a bio for me." | Microsoft Copilot | BIO.md | Generated initial draft from resume and background information. |
| 2026-08-30 | Create Markdown resume | "Look at this resume template and use my uploaded resume to create a resume.md file." | Microsoft Copilot | RESUME.md | Converted resume into repository Markdown format. |
| 2026-08-31 | Review engagement brief hypothesis | "Review this brief by using the info in this site: The Problem: I want to make a recommendation on a planting plan..." | Microsoft Copilot | docs/briefs/perfect-competition-brief.md | Reviewed whether the hypothesis was specific, falsifiable, and supported by an economic mechanism. Used feedback to strengthen the rationale behind the predicted planting mix. |
| 2026-08-31 | Validate hypothesis against Stage 1 instructions | "Ok, check this site and tell me if you still stick with your original recommendation" | Microsoft Copilot | docs/briefs/perfect-competition-brief.md | Compared hypothesis against Stage 1 guidance. Confirmed that the brief should contain a specific prediction and explain the mechanism believed to drive the outcome. |
| 2026-08-31 | Validate new hypothesis against Stage 1 comments from instructor | "Check my brief I just uploaded" | Microsoft Copilot | docs/briefs/perfect-competition-brief.md | Analyzed hypothesis. Costs alone do not determine profitability. Suggest a stronger hypothesis and revised problem statements. |
| 2026-09-02 | Update my hypothesis against Stage 1 comments from instructor | "Look at my brief I just uploaded and compare it against the instructor comments" | Microsoft Copilot | docs/briefs/perfect-competition-brief.md | Analyzed hypothesis. Numbers need to be added. Reasoning updated. |
| 2026-09-07 | Update my hypothesis against Stage 1 comments from instructor | "Look at my brief I just uploaded and compare it against the instructor comments" | Microsoft Copilot | docs/briefs/perfect-competition-brief.md | Analyzed and updated Hypothesis. Falsifiability section updated. |
| 2026-09-07 | Analyze my draft spec using the prompt from instructor | "Here is my model specification below. Do not rewrite it, and do not fill in anything that is missing." | Microsoft Copilot | capabilities/marginal-analysis/spec.md | Analyzed spec and provided recommendations. |
| 2026-09-07 | Run the build | "I need an Excel workbook built from this specification. Before generating anything follow the below steps." | Microsoft Copilot | capabilities/marginal-analysis/model.xlsx | Executed spec and produced xlsx file. |
| 2026-09-07 | Run the audit | "Analyze the Do-Audit section of the attached URL and walk me through the audit steps." | Microsoft Copilot | Output in Copilot interface | Analyzed URL and produced audit steps. |
| 2026-09-10 | Analyze draft brief | "Look at my brief I just uploaded and provide feedback" | Microsoft Copilot | Output in Copilot interface | Analyzed URL and produced feedback on brief. |
| 2026-09-10 | Analyze draft spec using the instructor instructions | "Look at my incomplete spec I just uploaded and provide feedback based on the included URL from the instructor" | Microsoft Copilot | Output in Copilot interface | Analyzed URL and produced feedback on spec. |
| 2026-09-10 | Create a draft paper based on my unfinished spec and completed brief | "Take my draft spec and completed brief and generate a draft paper" | Microsoft Copilot | Output in Copilot interface | Analyzed the spec and brief and generated a Markdown file. |
| 2026-09-10 | Update my marginal-analysis spec.md based on instructor feedback | "Take my spec.md and update it based on instructor feedback" | Microsoft Copilot | Output in Copilot interface | Analyzed marginal-analysis spec and recommended updates. |
| 2026-09-13 | Interpreting tomato MC vs price | "Take my 3 graphs and tell me what the tomato marginal cost and price are doing" | Microsoft Copilot | Output in Copilot interface | Analyzed MC vs price graphs and provided analysis. |
| 2026-09-13 | Understanding binding constraints/shadow prices | "What are the binding constraints and shadow prices of my project" | Microsoft Copilot | Output in Copilot interface | Analyzed the model outputs and explained why the carrot and mesclun constraints were binding, how shadow prices should be interpreted, and which expansion opportunity created greater value. |
| 2026-09-13 | Reviewing the analysis | "Take my perfect-competition-analysis.md and provide feedback" | Microsoft Copilot | Output in Copilot interface | Analyzed perfect-competition-analysis.md and recommended updates. |
| 2026-09-13 | Reviewing the memo | "Take my perfect-competition-memo.md and provide feedback" | Microsoft Copilot | Output in Copilot interface | Analyzed perfect-competition-memo.md and recommended updates. |
| 2026-09-16 | Reviewing the feedback for stage 3 | "Review the instructor's feedback" | Microsoft Copilot | Output in Copilot interface | Identified missing quantitative evidence for shadow prices and average variable cost, corrected the tomato marginal-cost dip location, connected the second carrot and mesclun crossings to the 720-hour labor threshold, and recommended adding a specific verification example to the reflection. |

## Perfect Competition Reflection

AI was most helpful in helping me interpret the optimizer outputs and connect the workbook results to economic concepts such as marginal cost, shadow prices, binding constraints, and profit maximization. The explanations helped me understand why tomato production stopped at approximately 10 beds and why the carrot and mesclun constraints remained binding.

I did not rely on AI outputs without verification. For example, Copilot correctly identified both intersections between marginal cost and market price for carrots and mesclun, and I verified those bed numbers against the workbook schedules. However, the initial AI-assisted analysis treated the second intersections as isolated observations and did not connect them to the tomato marginal-cost dip. The instructor's feedback identified the missing connection: each event occurs when production exhausts the farmer's 720 available field hours and shifts to lower-cost temporary labor. I returned to the workbook and confirmed that carrots cross the labor threshold between beds 16 and 17 and mesclun between beds 13 and 14. I then revised the analysis to explain all three marginal-cost changes through the same underlying labor-cost mechanism.

AI was most useful for translating spreadsheet outputs into economic explanations and identifying areas for further investigation. However, the workbook remained the authoritative source for all calculations, figures, and final recommendations. This project reinforced that an AI-generated interpretation can be numerically correct but analytically incomplete. Validating both the calculations and the causal explanation against primary data and instructor feedback improved the final analysis.
