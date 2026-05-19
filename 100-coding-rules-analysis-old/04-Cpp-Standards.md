# ⚙️ C/C++ Standards
*Focus areas: Legacy Integrations, CGO Bridges, FFI (Foreign Function Interfaces)*

## 1. RAII Wrappers for CGO
When interfacing with Go-compiled shared libraries (like the `Universal Logger` or `SafeSocket`), C++ code wraps the bare C-handles into strict RAII (Resource Acquisition Is Initialization) classes.

```cpp
class UniLog {
public:
    UniLog(...) {
        handle_ = UniLog_Init(...);
    }
    ~UniLog() {
        if (handle_ != 0) {
            UniLog_Close(handle_);
        }
    }
    // Disable copying to prevent double-close
    UniLog(const UniLog&) = delete;
    UniLog& operator=(const UniLog&) = delete;
}
```

## 2. Automated Metadata Macros
To ensure parity with the Universal Logging standard, C++ relies on preprocessor macros to automatically inject execution metadata (`__FILE__`, `__LINE__`, `__FUNCTION__`) into logging streams.

```cpp
#define UNILOG_INFO(logger, msg) \
    (logger).log(UniLog::INFO, (msg), __FILE__, std::to_string(__LINE__), __FUNCTION__, "cpp-module")
```

## 3. Memory Safety Over FFI Boundaries
C++ bindings explicitly handle memory allocated by Go (`C.CString`). Whenever a Go exported function returns a string pointer, the C++ wrapper copies the value into an `std::string` and immediately calls `free()` on the C-pointer to prevent memory leaks.

## 4. Visual Structure
C/C++ code strictly implements namespacing (e.g., `namespace microservice_toolbox::connectivity`) and utilizes visual block dividers consistent with the rest of the fleet:
`// -----------------------------------------------------------------------------`
