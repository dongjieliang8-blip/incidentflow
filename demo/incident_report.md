# Incident Report: Payment Service Outage

## Severity: P1
## Duration: 2024-01-15 14:00 - 16:30 (2.5 hours)

## Summary
Payment service became unresponsive, preventing all user transactions.

## Timeline
- 14:00 - Payment service started returning 503 errors
- 14:05 - Monitoring alert triggered
- 14:15 - On-call engineer paged
- 14:30 - Root cause identified: database connection pool exhaustion
- 15:00 - Connection pool size increased as temporary fix
- 15:30 - Service restored, monitoring for stability
- 16:30 - Incident closed

## Impact
- 15,000 users affected
- $45,000 in failed transactions
- Customer support received 500+ complaints

## Root Cause
A new feature released at 13:50 introduced a database query without proper connection handling, causing connections to leak and exhaust the connection pool.

## Actions Taken
- Increased connection pool size
- Restarted affected instances
- Rolled back the problematic feature release
