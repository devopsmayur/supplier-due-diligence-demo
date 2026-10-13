# Supplier Due-Diligence Workflow API

Python 3.10+ backend, with no external dependencies. This fictional workflow
illustrates engineering controls supporting supplier due diligence. It is not
an applicability calculator or legal compliance certification.

## Run
```bash
python3 -m unittest discover -s tests -v
python3 -m backend.api
```

## Try
```bash
curl -s http://127.0.0.1:8000/health
curl -s -X POST http://127.0.0.1:8000/suppliers/evaluate \
  -H 'Content-Type: application/json' \
  -d '{"assessment_status":"pending","risks":{"labour":0}}'
curl -s -X POST http://127.0.0.1:8000/suppliers/evaluate \
  -H 'Content-Type: application/json' \
  -d '{"assessment_status":"completed","risks":{"labour":95,"environment":5,"safety":5}}'
curl -s -X POST http://127.0.0.1:8000/records/deletion-eligibility \
  -H 'Content-Type: application/json' \
  -d '{"created_at":"2025-10-13","legal_hold":false}'
```

The first two supplier requests must return approved=false. Retention eligibility
depends on the server date; use the deterministic tests for fixed-date evidence.
This local API binds to loopback, uses synthetic data, has no persistence and
returns deletion eligibility without deleting anything.

## Review context
.coderabbit.yaml loads docs/German-LkSG-EU-CSDDD.md as background and
 docs/DEMO-POLICY.md as specific customer requirements for backend/**/*.py.
