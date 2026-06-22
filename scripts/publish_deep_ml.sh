#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

intent="${1:-Preserve Deep-ML practice progress}"
body="${2:-Updates Deep-ML notes, warmups, or solved problem files in the study repository.}"
branch="$(git rev-parse --abbrev-ref HEAD)"

git add AGENTS.md README.md ai/deep-ml scripts/publish_deep_ml.sh

if git diff --cached --quiet; then
  echo "No Deep-ML changes to publish."
  exit 0
fi

git commit \
  -m "$intent" \
  -m "$body" \
  -m "Constraint: Deep-ML solutions should be saved under ai/deep-ml/problems and mirrored to this remote repository
Confidence: high
Scope-risk: narrow
Directive: Do not add final answers before the user has solved the problem
Tested: git diff --cached reviewed before commit
Not-tested: Deep-ML judge unless the problem solution was run separately
Co-authored-by: OmX <omx@oh-my-codex.dev>"

git push -u origin "$branch"
