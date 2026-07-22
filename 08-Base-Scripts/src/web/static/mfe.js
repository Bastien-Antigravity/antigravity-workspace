class BaseScriptsMFE extends HTMLElement {
    constructor() {
        super();
        this.baseUrl = '';
        this.statusData = { healthy: false, status: 'Offline', version: 'N/A', timestamp: 0 };
        this.activeMode = { mode: '4', name: 'Direct-Action', description: '' };
        this.commands = [];
        this.eventSource = null;
        this.chatEventSource = null;
    }

    async connectedCallback() {
        this.baseUrl = this.getAttribute('base-url') || window.location.origin;
        if (this.baseUrl.endsWith('/')) {
            this.baseUrl = this.baseUrl.slice(0, -1);
        }
        
        this.renderSkeleton();
        await this.loadAll();
        this.setupEventListeners();
        
        // Start streaming collaborative chat
        this.loadChatHistory();
        this.startChatStream();
    }

    disconnectedCallback() {
        if (this.eventSource) {
            this.eventSource.close();
        }
        if (this.chatEventSource) {
            this.chatEventSource.close();
        }
    }

    async loadAll() {
        await Promise.all([
            this.loadStatus(),
            this.loadActiveMode(),
            this.loadCommands()
        ]);
        this.updateUI();
    }

    async loadStatus() {
        try {
            const resp = await fetch(`${this.baseUrl}/api/v1/status`);
            if (resp.ok) {
                this.statusData = await resp.json();
            } else {
                this.statusData.healthy = false;
                this.statusData.status = 'Degraded';
            }
        } catch (e) {
            this.statusData.healthy = false;
            this.statusData.status = 'Offline';
        }
    }

    async loadActiveMode() {
        try {
            const resp = await fetch(`${this.baseUrl}/api/v1/squad/active-mode`);
            if (resp.ok) {
                const data = await resp.json();
                if (data.success) {
                    this.activeMode = {
                        mode: data.mode,
                        name: data.name,
                        description: data.description
                    };
                }
            }
        } catch (e) {
            console.error('Failed to load active mode:', e);
        }
    }

    async loadCommands() {
        try {
            const resp = await fetch(`${this.baseUrl}/api/v1/squad/commands`);
            if (resp.ok) {
                const data = await resp.json();
                if (data.success) {
                    this.commands = data.commands;
                }
            }
        } catch (e) {
            console.error('Failed to load commands:', e);
        }
    }

    renderSkeleton() {
        this.innerHTML = `
            <style>
                .squad-container {
                    font-family: var(--font-sans, 'Outfit', 'Inter', system-ui, sans-serif);
                    color: var(--color-text-primary, #eaeaea);
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 24px;
                }
                .squad-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 24px;
                    border-bottom: 1px solid var(--color-border-subtle, #333);
                    padding-bottom: 16px;
                }
                .squad-title h1 {
                    font-size: var(--font-size-2xl, 1.8rem);
                    font-weight: 700;
                    margin: 0 0 4px 0;
                    background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }
                .squad-title p {
                    color: var(--color-text-muted, #888);
                    margin: 0;
                    font-size: var(--font-size-sm, 0.9rem);
                }
                
                .squad-status-badge {
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                    padding: 6px 12px;
                    border-radius: 20px;
                    font-weight: 600;
                    font-size: var(--font-size-xs, 0.8rem);
                    background-color: var(--color-bg-secondary, #222);
                    border: 1px solid var(--color-border-subtle, #333);
                }
                .squad-dot {
                    width: 8px;
                    height: 8px;
                    border-radius: 50%;
                }
                .squad-dot.healthy {
                    background-color: var(--color-accent-success, #4CAF50);
                    box-shadow: 0 0 8px var(--color-accent-success, #4CAF50);
                }
                .squad-dot.offline {
                    background-color: var(--color-accent-danger, #F44336);
                    box-shadow: 0 0 8px var(--color-accent-danger, #F44336);
                }

                /* Tab Styles */
                .squad-tabs {
                    display: flex;
                    gap: 8px;
                    margin-bottom: 24px;
                }
                .squad-tab-btn {
                    background: transparent;
                    border: 1px solid transparent;
                    color: var(--color-text-muted, #888);
                    font-size: var(--font-size-sm, 0.95rem);
                    font-weight: 600;
                    padding: 8px 20px;
                    cursor: pointer;
                    border-radius: 6px;
                    transition: all 0.2s ease;
                }
                .squad-tab-btn:hover {
                    color: #fff;
                    background-color: var(--color-bg-secondary, #222);
                }
                .squad-tab-btn.active {
                    color: #fff;
                    background: linear-gradient(135deg, rgba(255, 65, 108, 0.15) 0%, rgba(255, 75, 43, 0.15) 100%);
                    border-color: var(--color-accent-primary, #ff4b2b);
                }

                .tab-content {
                    display: none;
                }
                .tab-content.active {
                    display: block;
                }

                /* Grid Layouts */
                .squad-grid {
                    display: grid;
                    grid-template-columns: 1fr;
                    gap: 24px;
                    margin-bottom: 24px;
                }
                @media(min-width: 768px) {
                    .squad-grid {
                        grid-template-columns: 1fr 2fr;
                    }
                }

                .squad-card {
                    background: var(--color-bg-surface, #1e1e1e);
                    border: 1px solid var(--color-border-subtle, #2d2d2d);
                    border-radius: 12px;
                    padding: 20px;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
                }
                .squad-card-title {
                    font-size: var(--font-size-sm, 0.9rem);
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    color: var(--color-text-muted, #777);
                    font-weight: 700;
                    margin-bottom: 16px;
                    border-bottom: 1px solid var(--color-border-subtle, #2a2a2a);
                    padding-bottom: 8px;
                }

                /* Mode Switcher */
                .mode-selector {
                    display: flex;
                    flex-direction: column;
                    gap: 12px;
                }
                .mode-item {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 12px 16px;
                    border-radius: 8px;
                    background-color: var(--color-bg-primary, #121212);
                    border: 1px solid var(--color-border-subtle, #2a2a2a);
                    cursor: pointer;
                    transition: all 0.2s ease;
                }
                .mode-item:hover {
                    border-color: var(--color-accent-primary, #ff4b2b);
                    transform: translateX(4px);
                }
                .mode-item.active {
                    background: linear-gradient(135deg, rgba(255, 65, 108, 0.1) 0%, rgba(255, 75, 43, 0.1) 100%);
                    border-color: var(--color-accent-primary, #ff4b2b);
                }
                .mode-name {
                    font-weight: 600;
                    font-size: var(--font-size-sm, 0.95rem);
                }
                .mode-desc {
                    font-size: var(--font-size-xs, 0.75rem);
                    color: var(--color-text-muted, #777);
                    margin-top: 2px;
                }
                
                /* Subcommands Runner */
                .cmd-list {
                    display: flex;
                    flex-direction: column;
                    gap: 12px;
                    max-height: 400px;
                    overflow-y: auto;
                    padding-right: 4px;
                }
                .cmd-item {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 12px 16px;
                    border-radius: 8px;
                    background-color: var(--color-bg-primary, #121212);
                    border: 1px solid var(--color-border-subtle, #2a2a2a);
                }
                .cmd-info {
                    flex: 1;
                }
                .cmd-name {
                    font-weight: 600;
                    font-family: var(--font-mono, monospace);
                    font-size: var(--font-size-sm, 0.9rem);
                    color: var(--color-accent-primary, #ff4b2b);
                }
                .cmd-desc {
                    font-size: var(--font-size-xs, 0.75rem);
                    color: var(--color-text-muted, #888);
                    margin-top: 4px;
                }
                .cmd-run-btn {
                    background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
                    border: none;
                    color: white;
                    padding: 8px 16px;
                    border-radius: 6px;
                    font-size: var(--font-size-xs, 0.8rem);
                    font-weight: 600;
                    cursor: pointer;
                    transition: opacity 0.2s, transform 0.1s;
                }
                .cmd-run-btn:hover {
                    opacity: 0.9;
                }
                .cmd-run-btn:active {
                    transform: scale(0.97);
                }

                /* Terminal Card */
                .terminal-card {
                    background: #0d0d0d;
                    border: 1px solid #1f1f1f;
                    border-radius: 12px;
                    box-shadow: inset 0 0 10px rgba(0,0,0,0.8);
                    overflow: hidden;
                    display: flex;
                    flex-direction: column;
                    height: 380px;
                }
                .terminal-header {
                    background: #141414;
                    padding: 10px 16px;
                    border-bottom: 1px solid #1f1f1f;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }
                .terminal-title {
                    font-family: var(--font-mono, monospace);
                    font-size: var(--font-size-xs, 0.8rem);
                    color: #888;
                }
                .terminal-controls {
                    display: flex;
                    gap: 8px;
                }
                .terminal-btn {
                    background: #222;
                    border: 1px solid #333;
                    color: #bbb;
                    padding: 4px 10px;
                    border-radius: 4px;
                    font-size: 11px;
                    cursor: pointer;
                    font-family: var(--font-mono, monospace);
                }
                .terminal-btn:hover {
                    background: #333;
                    color: #fff;
                }
                .terminal-body {
                    flex: 1;
                    padding: 16px;
                    overflow-y: auto;
                    font-family: var(--font-mono, 'Courier New', Courier, monospace);
                    font-size: 12px;
                    line-height: 1.5;
                    color: #39FF14;
                    background-color: #050505;
                }
                .terminal-line {
                    white-space: pre-wrap;
                    margin-bottom: 4px;
                }
                .terminal-line.start { color: #00e5ff; font-weight: bold; }
                .terminal-line.complete { color: #39FF14; font-weight: bold; }
                .terminal-line.failed { color: #ff3d00; font-weight: bold; }
                .terminal-line.error { color: #ff3d00; font-weight: bold; }

                /* Chat Styles */
                .chat-layout {
                    display: flex;
                    flex-direction: column;
                    height: 600px;
                    background: var(--color-bg-surface, #1e1e1e);
                    border: 1px solid var(--color-border-subtle, #2d2d2d);
                    border-radius: 12px;
                    overflow: hidden;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
                }
                .chat-messages {
                    flex: 1;
                    padding: 20px;
                    overflow-y: auto;
                    display: flex;
                    flex-direction: column;
                    gap: 16px;
                }
                .chat-bubble {
                    display: flex;
                    gap: 12px;
                    padding: 12px 16px;
                    border-radius: 8px;
                    background-color: var(--color-bg-primary, #121212);
                    border: 1px solid var(--color-border-subtle, #2a2a2a);
                    max-width: 85%;
                    align-self: flex-start;
                }
                .chat-bubble.user {
                    align-self: flex-end;
                    background-color: rgba(255, 75, 43, 0.08);
                    border-color: rgba(255, 75, 43, 0.25);
                }
                .chat-bubble.orchestrator {
                    border-left: 3px solid #ff4b2b;
                }
                .chat-bubble.developer {
                    border-left: 3px solid #00e5ff;
                }
                .chat-bubble.qa {
                    border-left: 3px solid #4CAF50;
                }
                .chat-bubble.architect {
                    border-left: 3px solid #E040FB;
                }
                .chat-avatar {
                    font-size: 1.3rem;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background-color: #252525;
                    width: 36px;
                    height: 36px;
                    border-radius: 50%;
                }
                .chat-content {
                    flex: 1;
                }
                .chat-sender {
                    font-size: 0.75rem;
                    font-weight: 700;
                    color: var(--color-text-muted, #888);
                    text-transform: uppercase;
                    letter-spacing: 0.5px;
                    margin-bottom: 4px;
                }
                .chat-text {
                    font-size: 0.9rem;
                    line-height: 1.5;
                    white-space: pre-wrap;
                }
                .chat-input-area {
                    display: flex;
                    gap: 12px;
                    padding: 16px;
                    border-top: 1px solid var(--color-border-subtle, #2a2a2a);
                    background: #141414;
                }
                .chat-input-box {
                    flex: 1;
                    background-color: #0d0d0d;
                    border: 1px solid #2a2a2a;
                    border-radius: 6px;
                    color: #fff;
                    padding: 12px;
                    font-size: 0.9rem;
                    outline: none;
                }
                .chat-input-box:focus {
                    border-color: var(--color-accent-primary, #ff4b2b);
                }
                .chat-send-btn {
                    background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
                    border: none;
                    color: white;
                    padding: 0 24px;
                    border-radius: 6px;
                    font-size: 0.9rem;
                    font-weight: 600;
                    cursor: pointer;
                    transition: opacity 0.2s;
                }
                .chat-send-btn:hover {
                    opacity: 0.9;
                }

                .chat-tools {
                    margin-top: 10px;
                    font-size: 0.8rem;
                    border: 1px solid #333;
                    border-radius: 4px;
                    overflow: hidden;
                    background-color: #0d0d0d;
                }
                .chat-tool-header {
                    background-color: #222;
                    color: #aaa;
                    padding: 6px 12px;
                    font-family: var(--font-mono, monospace);
                    cursor: pointer;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }
                .chat-tool-header:hover {
                    background-color: #2a2a2a;
                    color: #fff;
                }
                .chat-tool-body {
                    background-color: #050505;
                    color: #39FF14;
                    padding: 10px;
                    font-family: var(--font-mono, monospace);
                    white-space: pre-wrap;
                    max-height: 250px;
                    overflow-y: auto;
                    border-top: 1px solid #222;
                }
            </style>
            
            <div class="squad-container">
                <div class="squad-header">
                    <div class="squad-title">
                        <h1>🚀 Squad Control Centre</h1>
                        <p>Independent agent executor interface and collaborative runtime</p>
                    </div>
                    <div id="status-badge" class="squad-status-badge">
                        <span class="squad-dot offline"></span>
                        <span id="status-text">Connecting...</span>
                    </div>
                </div>

                <div class="squad-tabs">
                    <button class="squad-tab-btn active" data-tab="runner">🎛️ Command Control</button>
                    <button class="squad-tab-btn" data-tab="chat">💬 Squad Chat</button>
                </div>

                <!-- Runner View -->
                <div id="tab-runner" class="tab-content active">
                    <div class="squad-grid">
                        <div class="squad-card">
                            <div class="squad-card-title">🕹️ Active Squad Mode</div>
                            <div id="mode-selector" class="mode-selector">
                                <div class="mode-item" data-mode="1">
                                    <div>
                                        <div class="mode-name">🛡️ Spec-First</div>
                                        <div class="mode-desc">High safety, BDD mandatory.</div>
                                    </div>
                                </div>
                                <div class="mode-item" data-mode="2">
                                    <div>
                                        <div class="mode-name">🧪 Free-Labs</div>
                                        <div class="mode-desc">High speed, experimentations.</div>
                                    </div>
                                </div>
                                <div class="mode-item" data-mode="3">
                                    <div>
                                        <div class="mode-name">🛰️ Fleet-Commander</div>
                                        <div class="mode-desc">Global sync, multi-repo.</div>
                                    </div>
                                </div>
                                <div class="mode-item" data-mode="4">
                                    <div>
                                        <div class="mode-name">🥷 Direct-Action</div>
                                        <div class="mode-desc">Bypass mode logic.</div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="squad-card">
                            <div class="squad-card-title">⚙️ Subcommand Execution</div>
                            <div id="commands-list" class="cmd-list">
                                <div style="color: #777; font-size: var(--font-size-xs);">Loading command manifest...</div>
                            </div>
                        </div>
                    </div>

                    <div class="terminal-card">
                        <div class="terminal-header">
                            <div class="terminal-title">📟 live_execution_feed.log</div>
                            <div class="terminal-controls">
                                <button id="btn-clear-term" class="terminal-btn">Clear Log</button>
                            </div>
                        </div>
                        <div id="terminal-body" class="terminal-body">
                            <div class="terminal-line">[SYSTEM] Ready for command dispatch. Select a command above to execute.</div>
                        </div>
                    </div>
                </div>

                <!-- Chat View -->
                <div id="tab-chat" class="tab-content">
                    <div class="chat-layout">
                        <div id="chat-messages" class="chat-messages">
                            <div class="chat-bubble system">
                                <span class="chat-avatar">🤖</span>
                                <div class="chat-content">
                                    <div class="chat-sender">System</div>
                                    <div class="chat-text">Welcome to the AI Squad Chat room. Type a goal below to begin collaborative execution.</div>
                                </div>
                            </div>
                        </div>
                        <div class="chat-input-area">
                            <input type="text" id="chat-input-box" class="chat-input-box" placeholder="Ask the squad to implement, test, or review code..." />
                            <button id="chat-send-btn" class="chat-send-btn">Send</button>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    setupEventListeners() {
        // Tab switching
        const tabBtns = this.querySelectorAll('.squad-tab-btn');
        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                tabBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                
                const tab = btn.dataset.tab;
                this.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
                this.querySelector(`#tab-${tab}`).classList.add('active');
            });
        });

        // Clear terminal button
        const clearBtn = this.querySelector('#btn-clear-term');
        if (clearBtn) {
            clearBtn.addEventListener('click', () => {
                const body = this.querySelector('#terminal-body');
                if (body) {
                    body.innerHTML = '<div class="terminal-line">[SYSTEM] Terminal logs cleared.</div>';
                }
            });
        }

        // Mode selectors
        const modeItems = this.querySelectorAll('.mode-item');
        modeItems.forEach(item => {
            item.addEventListener('click', async () => {
                const mode = item.dataset.mode;
                await this.switchMode(mode);
            });
        });

        // Chat send interaction
        const chatSendBtn = this.querySelector('#chat-send-btn');
        const chatInputBox = this.querySelector('#chat-input-box');
        if (chatSendBtn && chatInputBox) {
            const sendMsg = async () => {
                const text = chatInputBox.value.trim();
                if (!text) return;
                chatInputBox.value = '';
                await this.postChatMessage(text);
            };
            chatSendBtn.addEventListener('click', sendMsg);
            chatInputBox.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') sendMsg();
            });
        }
    }

    async switchMode(mode) {
        try {
            const resp = await fetch(`${this.baseUrl}/api/v1/squad/active-mode`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ mode })
            });
            if (resp.ok) {
                const data = await resp.json();
                if (data.success) {
                    this.printTerminalLine(`[SYSTEM] Mode switched: ${data.message}`, 'start');
                    await this.loadActiveMode();
                    this.updateUI();
                } else {
                    this.printTerminalLine(`[SYSTEM] Mode switch failed: ${data.message}`, 'error');
                }
            }
        } catch (e) {
            this.printTerminalLine(`[SYSTEM] Connection error switching mode: ${e}`, 'error');
        }
    }

    runCommand(cmdName) {
        if (this.eventSource) {
            this.eventSource.close();
        }

        const terminalBody = this.querySelector('#terminal-body');
        if (terminalBody) {
            terminalBody.innerHTML = '';
        }

        this.printTerminalLine(`[SYSTEM] Connecting to stream for subcommand "${cmdName}"...`, 'start');

        this.eventSource = new EventSource(`${this.baseUrl}/api/v1/squad/run/${cmdName}`);

        this.eventSource.onmessage = (event) => {
            const data = event.data;
            let type = '';
            if (data.startsWith('[START]')) type = 'start';
            else if (data.startsWith('[COMPLETE]')) type = 'complete';
            else if (data.startsWith('[FAILED]')) type = 'failed';
            else if (data.startsWith('[ERROR]')) type = 'error';

            this.printTerminalLine(data, type);
        };

        this.eventSource.onerror = (err) => {
            this.printTerminalLine('[SYSTEM] EventSource stream closed.', 'error');
            this.eventSource.close();
        };
    }

    printTerminalLine(text, type = '') {
        const body = this.querySelector('#terminal-body');
        if (!body) return;

        const line = document.createElement('div');
        line.className = 'terminal-line';
        if (type) {
            line.classList.add(type);
        }
        line.textContent = text;
        body.appendChild(line);
        body.scrollTop = body.scrollHeight;
    }

    async loadChatHistory() {
        try {
            const resp = await fetch(`${this.baseUrl}/api/v1/squad/chat/squad_sync_session`);
            if (resp.ok) {
                const data = await resp.json();
                if (data.success && data.history) {
                    const chatMessages = this.querySelector('#chat-messages');
                    if (chatMessages) {
                        chatMessages.innerHTML = `
                            <div class="chat-bubble system">
                                <span class="chat-avatar">🤖</span>
                                <div class="chat-content">
                                    <div class="chat-sender">System</div>
                                    <div class="chat-text">Welcome to the AI Squad Chat room. Type a goal below to begin collaborative execution.</div>
                                </div>
                            </div>
                        `;
                        data.history.forEach(msg => this.appendChatMessage(msg));
                    }
                }
            }
        } catch (e) {
            console.error("Failed to load chat history:", e);
        }
    }

    startChatStream() {
        if (this.chatEventSource) {
            this.chatEventSource.close();
        }
        
        this.chatEventSource = new EventSource(`${this.baseUrl}/api/v1/squad/chat/stream/squad_sync_session`);
        this.chatEventSource.onmessage = (event) => {
            try {
                const msg = JSON.parse(event.data);
                this.appendChatMessage(msg);
            } catch (e) {
                console.error("Failed to parse SSE chat message:", e);
            }
        };
    }

    async postChatMessage(message) {
        try {
            const resp = await fetch(`${this.baseUrl}/api/v1/squad/chat/squad_sync_session`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message })
            });
            if (!resp.ok) {
                console.error("Failed to post chat message");
            }
        } catch (e) {
            console.error("Connection error posting chat message:", e);
        }
    }

    appendChatMessage(msg) {
        const chatMessages = this.querySelector('#chat-messages');
        if (!chatMessages) return;
        
        // Map avatars
        const avatars = {
            'user': '👤',
            'orchestrator': '🤖',
            'developer': '💻',
            'qa': '🧪',
            'architect': '📐'
        };
        const avatar = avatars[msg.sender] || '🤖';
        
        const bubble = document.createElement('div');
        bubble.className = `chat-bubble ${msg.sender}`;
        
        let toolCallsHtml = '';
        if (msg.tool_calls && msg.tool_calls.length > 0) {
            msg.tool_calls.forEach((tool, index) => {
                const toolArgs = JSON.stringify(tool.args || {});
                toolCallsHtml += `
                    <div class="chat-tools">
                        <div class="chat-tool-header" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'none' ? 'block' : 'none'">
                            <span>🛠️ Tool: ${tool.name}</span>
                            <span style="font-size: 10px;">[Toggle Output]</span>
                        </div>
                        <div class="chat-tool-body" style="display: none;">
                            <strong>Arguments:</strong> ${toolArgs}
                            <hr style="border-color: #333; margin: 8px 0;" />
                            <strong>Result:</strong><br />${tool.result}
                        </div>
                    </div>
                `;
            });
        }
        
        bubble.innerHTML = `
            <span class="chat-avatar">${avatar}</span>
            <div class="chat-content">
                <div class="chat-sender">${msg.sender}</div>
                <div class="chat-text">${msg.content}</div>
                ${toolCallsHtml}
            </div>
        `;
        
        chatMessages.appendChild(bubble);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    updateUI() {
        const badge = this.querySelector('#status-badge');
        const statusText = this.querySelector('#status-text');
        const dot = this.querySelector('.squad-dot');
        
        if (badge && statusText && dot) {
            dot.className = 'squad-dot ' + (this.statusData.healthy ? 'healthy' : 'offline');
            statusText.textContent = this.statusData.healthy ? 'Healthy (v' + this.statusData.version + ')' : this.statusData.status;
        }

        const modeItems = this.querySelectorAll('.mode-item');
        modeItems.forEach(item => {
            if (item.dataset.mode === String(this.activeMode.mode)) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });

        const list = this.querySelector('#commands-list');
        if (list && this.commands.length > 0) {
            list.innerHTML = '';
            this.commands.forEach(cmd => {
                if (cmd.name === 'start-squad') return;

                const item = document.createElement('div');
                item.className = 'cmd-item';
                item.innerHTML = `
                    <div class="cmd-info">
                        <div class="cmd-name">${cmd.name}</div>
                        <div class="cmd-desc">${cmd.description}</div>
                    </div>
                    <button class="cmd-run-btn" data-cmd="${cmd.name}">Execute</button>
                `;
                list.appendChild(item);
            });

            const runBtns = list.querySelectorAll('.cmd-run-btn');
            runBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    const cmd = btn.dataset.cmd;
                    this.runCommand(cmd);
                });
            });
        }
    }
}

customElements.define('base-scripts-mfe', BaseScriptsMFE);
