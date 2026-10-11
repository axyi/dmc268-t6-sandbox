# Security

SQL queries with user values must be parameterized.

## Python

In Python files (`**/*.py`) an expected error is caught by its specific exception type.
Catching `Exception` is allowed only at the outer boundary of a background job.

## TypeScript

In TypeScript files (`**/*.ts`) treat the result of an external JSON API as `unknown`
until its structure is checked.

# Performance

Do not run a separate database query for every item of a list.

# Style

Duplicated test setup is allowed for readability.

# Ignore

Generated code and bundles are not reviewed.

```review-ignore
generated/**
**/*.min.js
```
