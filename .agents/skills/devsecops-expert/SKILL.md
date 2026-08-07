---
name: devsecops-expert
description: Configuration profile for CI/CD pipelines. Enforces a strict sequence of security scans and checks.
---

# DevSecOps Pipeline Configuration

This is a configuration profile, not a textbook. You already know how CI/CD tools work. When generating or auditing pipelines, enforce this exact structural sequence:

## Mandatory Pipeline Sequence
1. **Pre-Flight / Secret Scan:** (Trivy, TruffleHog, or Gitleaks). Must block the pipeline BEFORE any dependencies are downloaded or code is built.
2. **Static Analysis & Linting:** (Checkov, tfsec for IaC; Semgrep or equivalent for code).
3. **Build & Unit Tests.**
4. **Artifact / Container Scanning:** (Trivy). Scan the final built image, not just the source.
5. **Provenance:** Generate SLSA provenance and use Sigstore/Cosign for artifact signing.

## Hard Constraints
- **Fail-Fast:** Any High or Critical vulnerability must exit with code > 0 and fail the pipeline immediately.
- **Least Privilege:** CI/CD runners must use OIDC (OpenID Connect) to authenticate to cloud providers (AWS, GCP, Azure). Long-lived static credentials are forbidden.
- **Pinned Actions:** GitHub Actions or GitLab includes MUST be pinned to a specific commit SHA, not `@v2` or `@main`.
