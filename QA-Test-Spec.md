---
microservice: rag-engine
type: qa-test-spec
status: completed
role: qa
tags:
- '#zone/0-orchestration'
- '#service/rag-engine'
- '#type/qa-test-spec'
- '#state/completed'
- '#performance'
---
# BDD Test Specification: Turbo Pipeline Verification

## 1. Context Injection
> **Mandatory Check**: I have read the `Master-Plan.md` and the `Architecture-Blueprint.md` to perfectly align these expectations with the Orchestrator's original idea.

## 2. Gherkin Scenarios

### Scenario 1: High-Throughput Bulk Indexing
- **Given** a workspace containing 1000 dummy files
- **And** the `RAG_WALKER_CONCURRENCY` is set to 64
- **When** the indexing pipeline is executed
- **Then** the total indexing time must be less than 30 seconds
- **And** all 1000 files must be correctly present in the stores.

### Scenario 2: Atomic Batch Persistence
- **Given** a batch of 10 files being processed
- **When** a simulated failure occurs during the storage phase
- **Then** none of the file hashes for that failed batch should be updated in the Parent Store
- **And** a subsequent indexing run must attempt to re-process all files from that failed batch.

### Scenario 3: LLM Enricher Concurrency Guard
- **Given** 64 chunks queued for enrichment
- **And** the `LLMEnricher` concurrency limit is set to 4
- **When** the enrichment process starts
- **Then** the number of active external LLM API calls must never exceed 4.

## 3. Verification Report
- **Test Suite**: `09-RAG-Engine/tests/test_turbo_pipeline.py`
- **Performance Test**: `09-RAG-Engine/tests/perf_test_turbo.py`
- **Results**:
    - `test_llm_enricher_concurrency_guard`: PASSED
    - `test_atomic_batch_persistence`: PASSED (after fixing `task_done()` bug in implementation)
    - `test_multiprocessing_chunk_integrity`: PASSED
    - `Bulk Indexing Performance (1000 files)`: PASSED (7.44s)

## 4. Root Cause Analysis (Resolved Bugs)
1. **Early `task_done()`**: The flusher loop was calling `task_done()` as soon as it pulled an item from the queue, not after the batch was flushed. This caused `await self._queue.join()` to return prematurely. **FIXED**.
2. **Subprocess Pickling**: The test was passing `AsyncMock` objects to the `ProcessPoolExecutor`, which failed. Test updated to use picklable `TextAnalyzer`. **FIXED**.

## 5. Next Step
Implementation verified. Sign-off for deployment.
