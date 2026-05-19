# 🦀 Rust Standards
*Focus areas: Low-Level Transport, Log Servers, High-Throughput IO*

## 1. Custom TCP Framing (`SafeSocket`)
Rust implements bespoke wrappers over standard `tokio::net::TcpStream`. The `SafeSocket` pattern enforces strict binary rules over the wire:
- **Length-Prefixed Framing**: Every message is prefixed with a Big-Endian `u32` length.
- **Heartbeats**: 0-length frames are treated as keep-alive heartbeats, automatically swallowed by the reader loop to prevent payload contamination.
- **OOM Protection**: Strict `MAX_MESSAGE_SIZE` bounds (e.g., 10MB) to prevent memory exhaustion attacks.

## 2. Async I/O (Tokio)
Extensive use of the Tokio runtime (`AsyncReadExt`, `AsyncWriteExt`). SafeSockets are explicitly split into independent `OwnedReadHalf` and `OwnedWriteHalf` structures for concurrent, non-blocking bidirectional communication.

## 3. Visual Dividers
Rust files adhere to the fleet-wide visual separator standard to maintain visual parity with Python and Go codebases:
`//-----------------------------------------------------------------------------------------------`

## 4. Cargo / Build Scripts
Build environments often rely on `build.rs` to generate or link external protocols (such as Cap'n Proto).
