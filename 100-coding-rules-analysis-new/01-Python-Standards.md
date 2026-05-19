# 🐍 Python Standards
*Focus areas: Data Processing, AI, MT5 Gateways, Fundamental Analysis*

## 1. The "Triple-Block" Module Documentation
Python files require a highly structured docstring at the top of the module to outline context for both human maintainers and AI interpretation. This is mandatory for operational services.

```python
"""
ESSENTIAL PROCESS:
[High-level description of what the module does]

DATA FLOW:
1. [Step 1]
2. [Step 2]

KEY PARAMETERS:
- [param]: [description]
"""
```

## 2. File Headers & Encoding
Every Python file must begin strictly with:
```python
#!/usr/bin/env python
# coding:utf-8
```

## 3. Strict Typing & Self-Identification
- **Explicit Typing**: Heavy use of the `typing` module (`typingDict`, `typingList`, `typingAny`, `typingOptional`) and `Pydantic` for strict data validation boundaries.
- **Self-Identification**: Classes explicitly declare a `Name` class attribute (e.g., `Name = "BackTest"`, `Name = "ProfileLoader"`).
- **Log Injection**: This `Name` attribute is injected into all logging statements for strict, searchable traceability: 
  `self.logger.info("{0} : using MTF bundle".format(self.Name))`

## 4. Visual Organization
Methods and classes must be separated by a specific 95-character comment divider to enhance vertical readability:
`# -----------------------------------------------------------------------------------------------`

## 5. Asynchronous Data Handling
- Heavy reliance on `asyncio` and `aiohttp` for non-blocking I/O tasks.
- Proper event loop management is expected when interacting with synchronous legacy components.
