## Zero Trust Architecture Overview

This diagram illustrates the secure microservice flow, identity and policy enforcement, and integrated security tooling used in this lab. It supports RMF documentation by mapping technical controls to NIST SP 800-53 and providing evidence for implementation and monitoring phases.
flowchart TD
    A[External Partner] --> B[API Gateway / Service Mesh]
    B --> C1[Data Ingest Service]
    B --> C2[Data Processing Service]
    B --> C3[Data Access Service]
    C1 --> D[Data Store]
    C2 --> D
    C3 --> D

    subgraph Identity & Policy
        E[Keycloak (IdP)]
        F[OPA (Policy Decision Point)]
    end

    A --> E
    E --> B
    C1 --> F
    C2 --> F
    C3 --> F
    F --> C1
    F --> C2
    F --> C3

    subgraph Security Tooling
        G1[Semgrep (Static)]
        G2[Trivy / Terrascan (Container/IaC)]
        G3[Falco (Runtime)]
        G4[SIEM (Splunk / OpenSearch)]
    end

    C1 --> G3
    C2 --> G3
    C3 --> G3
    G3 --> G4
    G1 --> G4
    G2 --> G4
