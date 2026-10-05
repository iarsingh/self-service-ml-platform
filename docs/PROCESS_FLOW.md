# Self-Service ML Platform: process flows

## Domain request

Endpoint: `POST /check`. Stages summarize [src/ssml/gate.py](../src/ssml/gate.py). This is in-process Python, not a hosted model or production apply.

```mermaid
flowchart TD
  A["POST /check"] --> B{"Valid input?"}
  B -->|"No"| E["HTTP 422"]
  B -->|"Yes: JSON object body"| C["Domain function in gate.py"]
  C --> O["catalog fields present; applied false"]
  O --> X["No production side effect"]
```

See [INTERVIEW_QA.md](../INTERVIEW_QA.md) for fixture walkthroughs and [PROJECT_ARCHITECTURE.md](../PROJECT_ARCHITECTURE.md) for the component map.
