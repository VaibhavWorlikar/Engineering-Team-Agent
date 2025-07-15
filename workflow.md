graph TD
    A[👤 User Input] --> B[🎯 Engineering Lead Agent]
    
    B --> C[🔄 Sequential Multi-Agent Chain]
    
    C --> D[⚛️ Frontend Agent]
    C --> E[🔧 Backend Agent]
    C --> F[🧪 Tester Agent]
    
    D --> D1[📱 Generates Gradio Code]
    E --> E1[🔌 Builds API/Server]
    F --> F1[✅ Runs Tests]
    
    D1 --> G[🐳 Docker Environment]
    E1 --> G
    F1 --> G
    
    G --> H[🚀 Executed App]
    
    H --> I[📊 Gradio UI]
    
    %% Styling
    classDef userInput fill:#e1f5fe,stroke:#0277bd,stroke-width:2px
    classDef leadAgent fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef agentChain fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    classDef agents fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    classDef outputs fill:#fff8e1,stroke:#f57f17,stroke-width:2px
    classDef environment fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    classDef finalOutput fill:#fce4ec,stroke:#c2185b,stroke-width:2px
    
    class A userInput
    class B leadAgent
    class C agentChain
    class D,E,F agents
    class D1,E1,F1 outputs
    class G environment
    class H environment
    class I finalOutput