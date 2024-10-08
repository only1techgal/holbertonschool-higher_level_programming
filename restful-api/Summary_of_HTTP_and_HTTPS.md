To start off, HTTP ( Hypertext Transfer Protocal) and HTTPS ( Hypertext Transfer Protocal Secure) serve as fundimental protocals between the client and the server.

That is HTTP and HTTPS?

The HTTP is a protocal or prescribed syntax for presenting information and is also used for transfering data over a network.
The HTTPS uses TLS or SSL to encrypt HTTP requests and responses.

The difference between HTTP and HTTPS:

```mermaid
graph TD;
    A[HTTP] --> B[Data transmitted in plaintext]
    A --> C[No encryption]
    A --> D[Vulnerable to attacks]
    
    F[HTTPS] --> G[Data transmitted in encrypted form]
    F --> H[Uses SSL/TLS for encryption]
    F --> I[More secure against attacks]
    
    A -->|Differs from| F
    B ---|Compared to| G
    C ---|Compared to| H
    D ---|Compared to| I
```