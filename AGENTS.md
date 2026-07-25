# AGENTS.md

## Project Overview

This repository contains the **ANS Complaints Insights** project, a Data Storytelling analysis about complaints related to Brazilian health insurance operators using ANS (Agência Nacional de Saúde Suplementar) data from 2015 to 2024.

The project combines data engineering practices, data analysis and storytelling to transform raw data into reliable insights.

The objective is not only to create visualizations, but to demonstrate a complete analytical process:

- understanding the data source;
- validating data quality;
- transforming and preparing datasets;
- analyzing indicators;
- extracting business insights;
- communicating findings clearly.

---

# Project Purpose

This project is part of a professional portfolio focused on Data Engineering and Analytics opportunities.

The main goal is to demonstrate:

- technical ability;
- analytical reasoning;
- data quality awareness;
- engineering best practices;
- ability to transform data into meaningful business insights.

Suggestions and improvements should always consider the project as a professional portfolio piece.

---

# Analytical Principles

This project values **analytical thinking over simply producing dashboards**.

Before accepting any metric, indicator or conclusion, consider:

- Is the data source reliable?
- Is the calculation methodology correct?
- Does the indicator represent the real-world scenario?
- Are there possible statistical distortions?
- Does the result make business sense?

The project intentionally prioritizes critical analysis instead of blindly trusting existing metrics.

---

# Important Analytical Decision

One of the main contributions of this project was identifying a methodological limitation in the IGR (Índice Geral de Reclamações) analysis.

A simple average of the available IGR values could generate a distorted interpretation because operators have different beneficiary portfolio sizes.

The project therefore investigates and recalculates the indicator using a methodology that better represents the impact according to the beneficiary portfolio.

Preserve this analytical reasoning in any suggested improvements.

Do not simplify or remove this approach just to make the implementation easier.

---

# Technical Context

Expected technologies and practices may include:

- Python
- Pandas
- Data processing pipelines
- Data visualization
- Streamlit or dashboard technologies
- SQL (when applicable)
- Data analysis workflows

The repository should remain reproducible and understandable.

---

# Coding Standards

When reviewing or suggesting code improvements:

Follow these principles:

- Write clean and readable code.
- Follow Python best practices (PEP8).
- Prefer meaningful variable and function names.
- Avoid unnecessary complexity.
- Avoid duplicated logic.
- Keep functions focused on a single responsibility.
- Add type hints when they improve readability.
- Add documentation where useful.
- Prefer maintainable solutions over clever solutions.

---

# Data Engineering Guidelines

Prioritize improvements related to:

- data quality;
- validation;
- reproducibility;
- pipeline organization;
- performance;
- maintainability;
- error handling;
- logging;
- configuration management.

When suggesting pipeline improvements, explain:

- why the change is needed;
- what problem it solves;
- expected benefits;
- possible trade-offs.

---

# Architecture Review Guidelines

When analyzing the project architecture, evaluate:

- folder organization;
- separation of responsibilities;
- scalability;
- maintainability;
- dependency management;
- project structure.

Do not recommend large architectural changes unless there is a clear benefit.

Prefer incremental improvements.

---

# Documentation Guidelines

The documentation should communicate:

- the business problem;
- the data source;
- the analytical methodology;
- important decisions;
- project results;
- how to reproduce the analysis.

The storytelling aspect is important.

Do not transform the project into only a technical implementation without explaining the insights.

---

# Review Expectations

Act as a Senior Data Engineer and Analytics Engineer reviewing this repository.

Provide an objective and constructive review.

Analyze:

- code quality;
- architecture;
- data processing;
- performance;
- documentation;
- reproducibility;
- portfolio impact.

For every recommendation explain:

1. What should change?
2. Why does it matter?
3. What benefit does it bring?
4. What is the implementation approach?

---

# Prioritization

Organize suggestions into:

## Critical Issues
Problems that affect correctness, reliability or execution.

## Important Improvements
Changes that significantly improve quality or professionalism.

## Optional Improvements
Nice-to-have enhancements.

## Strengths
Things that are already well implemented and should be preserved.

---

# Portfolio Perspective

Evaluate the project as if reviewing it for a Junior Data Engineer candidate.

Consider:

- Does this demonstrate engineering maturity?
- Does it demonstrate analytical thinking?
- Does it show understanding beyond visualization?
- What questions could a technical interviewer ask?
- What improvements would make the project stronger?

---

# Preserve Project Philosophy

This project values:

- correctness over complexity;
- understanding over automation;
- quality over quantity;
- meaningful insights over unnecessary features.

Do not suggest adding technologies, frameworks or patterns only to make the project appear more advanced.

Every improvement should have a clear purpose.

---

# Expected Behavior

Before proposing modifications:

1. Understand the complete project context.
2. Analyze existing decisions.
3. Identify what is already working well.
4. Suggest improvements only when they add real value.

Do not automatically modify files.

First provide analysis and recommendations.
