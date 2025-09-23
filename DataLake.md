Here’s a version of the summary of the JPMC “Data Mesh” blog, **framed for a financial executive** who is thinking about how data needs to be shaped so that *agentic AI systems* (i.e. AI agents) using something like the **Model Context Protocol (MCP)** can make use of it well.

---

## What JPMC did: The Data Mesh Approach (Low-Tech Recap)

To start, here’s what JPMorgan Chase built:

* They treat data as *products* owned by specific domain teams. Each “data product” is a coherent group of related data (for example, credit risk, trading, etc.). ([Amazon Web Services, Inc.][1])
* Each data product has its own data lake: physically separated storage, cloud-based, catalogued, schema-managed. ([Amazon Web Services, Inc.][1])
* They built a **data mesh**: domains with data product lakes, and consuming applications are separate, but there’s infrastructure so data can be discovered and accessed securely in place (rather than many copies floating around). ([Amazon Web Services, Inc.][1])
* Key features: visibility of where data flows; strong access controls (down to columns, records, even masked/tokenized values when needed); governance and ownership; tools for cataloging (Glue, LakeFormation in AWS). ([Amazon Web Services, Inc.][1])

---

## What “Agentic AI” + MCP Brings / Implies

Agentic AI here means AI agents that operate semi-autonomously: they observe, plan, and act. MCP (Model Context Protocol, from recent literature) is a way for agents to connect to external data sources/tools via a standardized, secure, governed interface. This enables agents to fetch or query data, call tools, etc., in real time, subject to rules. ([Medium][2])

To serve such agents well, the data environment must satisfy additional or stronger properties than what’s needed for human analysts or BI tools. Here are what those are, and how the JPMC data mesh maps to them (or, what gaps might need further work).

---

## Key Requirements for MCP-Ready Data Mesh

| Requirement                                   | Why It Matters for Agents + MCP                                                                                                                                                                                                                             | How JPMC’s Mesh Helps / What Else Is Needed                                                                                                                                                                                                                 |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Discoverability**                           | Agents need to know *what data exists*, *what domains/products have what data*, *metadata* such as structure, semantics, quality, lineage. They need to do this automatically (without manual catalog lookup).                                              | JPMC has an enterprise-wide data catalog, with schema, ownership, etc. That helps agents locate data products. ([Amazon Web Services, Inc.][1])                                                                                                             |
| **Stable, well-defined schemas & semantics**  | Agents need consistency: predictable field names/types, clear definitions, business logic built in (e.g. what “customer ID” means, how “exposure” is computed, etc.) so agents don’t misinterpret or break when upstream data changes.                      | JPMC data products are schematized and curated; domain teams are responsible for understanding “uses & limitations.” ([Amazon Web Services, Inc.][1])                                                                                                       |
| **Low latency / freshness**                   | Agents often make decisions in near-real time; stale data degrades performance or risk.                                                                                                                                                                     | JPMC shares data in-place and avoids multiple stale copies; the mesh reduces divergence. But depending on the use case, further pipeline speed (ingestion lag, streaming) might be needed. ([Amazon Web Services, Inc.][1])                                 |
| **Access control & governance**               | Agents must only see what they are permitted to see. That could be masked data; or only certain columns/rows; must support fine-grained permissions. Also auditability: every agent’s data usage must be logged.                                            | JPMC’s mesh allows masking, tokenization; fine-grained access to columns/records; visibility via the mesh catalog of where data is going. ([Amazon Web Services, Inc.][1])                                                                                  |
| **APIs / interfaces for programmatic access** | Agents using MCP need standardized, machine-friendly access: query interfaces (SQL, search), possibly streaming, standard protocols, schemas, maybe graph or other enriched context.                                                                        | JPMC uses query services like Athena; data catalog services; LakeFormation. These help. But for agentic AI & MCP, more might be needed in terms of live endpoints, possibly embedding context (e.g. knowledge graphs) or real-time APIs.                    |
| **Context & metadata**                        | Agentic systems benefit from rich metadata: lineage (where data came from), freshness, reliability, ownership, constraints, semantics. MCP presumes tools/resources are described in metadata so agents can decide which interfaces to call.                | JPMC has catalog, schema, ownership, and audit via the mesh catalog. But might need expansion: richer metadata (confidence levels, quality metrics, drift, update frequency, etc.), so that agents can make decisions (e.g. choose product X vs product Y). |
| **Security, privacy, compliance built-in**    | Agents increase risk vectors: automated pipelines can amplify mistakes. Thus security must be strong: authentication, authorization, encryption, masking, differential privacy, logging, encryption in transit/at rest. MCP servers must comply with these. | JPMC has strong controls, masking, tokenization, access control, physical separation of data lakes, etc. Good foundation. But agentic usage may require additional guardrails: real-time monitoring, anomaly detection, tools to detect misuse.             |

---

## What Data Must be Transformed or Prepared (if You’re Building toward Agentic AI / MCP)

From the perspective of preparing data so that agents can use it well (and safely), here are what I would expect an executive to ensure in an organization, drawing from JPMC’s path and extending for MCP:

1. **Standardized Data Products with Clear API or Query Interfaces**
   Data products must publish stable interfaces: documented endpoints, query contracts, schemas etc. If an agent asks for “customer exposure data”, you need a clear, consistent product.

2. **Metadata Richness (Beyond Basic Schema)**

   * Data freshness/timestamps
   * Versioning (when schema or definitions change)
   * Data lineage
   * Business metadata: definitions of metrics, how computed, business uses, caveats
   * Quality metrics (e.g. error rates, missing values)

3. **Semantic Harmonization / Ontology / Common Definitions**
   Agents often act across domains. So shared vocabulary is important: e.g. what is “customer”, “account”, “exposure”, “risk rating”, etc. Ensures cross-product consistency.

4. **Access / Masking / Privacy Layers Integrated into the Mesh**
   Agents should not have free range; data must be masked or redacted as needed. Permissions must be enforceable programmatically (not manual) so that agents cannot inadvertently pull in disallowed data.

5. **Real-Time or Near Real-Time Data Where Needed**
   Some agentic workloads require up-to-date data; so pipelines must support streaming or frequent refreshes. For slower use cases (monthly reporting) batch may suffice.

6. **Endpoint / Protocol Layer for MCP or Equivalent**

   * A “MCP server” or equivalent that can expose data products/resources to agent clients via a standardized, secure protocol.
   * Tools/Services that agents can call as resources: for example, “get latest transaction summary”, “query portfolio exposure by counterparty”, etc.
   * This may require wrapping existing query engines or data lakes with such services.

7. **Governance, Auditing & Monitoring**
   Agents increase automation and the risk that errors cascade. You need logs, monitoring, and feedback loops. For example: which agent requested what resource, how often, what data was returned, was masking applied, etc.

---

## How JPMC’s Data Mesh Aligns with These, and Where They Might Need to Adapt to Fully Support MCP-Agentic Use Cases

JPMC has many of the building blocks already:

* Domains/data product lakes, schema, ownership, cataloging, access control. These provide much of what MCP needs in terms of structured data, governance, discoverability. ([Amazon Web Services, Inc.][1])
* In-place consumption avoids stale copied data; masking and tokenization are supported. ([Amazon Web Services, Inc.][1])
* Visibility via catalogs tracks flows, which helps audit and oversight. ([JPMorgan Chase][3])

But to fully enable agents via MCP, possible additional work includes:

* Implementing standardized machine-friendly endpoints/resources for each data product, so agents can query/call them via MCP servers.
* Enhancing metadata: not just schema, owner, but also quality scores, data freshness, usage statistics.
* Ensuring latency / streaming capabilities for data products where agents need near real-time decision support.
* Stronger monitoring of agent interactions: detect misuse, anomalies, drift.
* Ensuring versioning of data product APIs so that agents are not broken by schema changes.

---

## Strategic Implications and Financial Considerations

As a financial executive, here’s what these transformations mean in terms of risks, investments, and potential returns:

* **Upfront investment** will be higher: building out richer metadata, governance, MCP-capable endpoints, streaming pipelines, monitoring etc. Possibly new tooling, personnel with skills in AI systems and protocol security.

* **Risk reduction**: better control over data flows means less chance of data misuse, regulatory exposure, inconsistent decision-making. That is especially important as agentic systems make decisions or recommendations.

* **Efficiency and ROI**: once agents are able to access, trust, and use data reliably, they can automate many repetitive decisions, generate faster insights, exposure/risk monitoring, etc. Reducing manual analytic labor, faster reaction to market or operational changes.

* **Competitive advantage**: organizations that can deploy safe, effective agents (via MCP or similar) will likely outpace others in speed, adaptability, risk control.

* **Ongoing maintenance costs**: must budget for maintaining catalogs, schemas, data product definitions, monitoring, versioning, updates for compliance.

---

## Bottom-Line Summary

If you view this with the lens of *agentic AI + MCP*, JPMC’s data mesh provides a strong foundation: domain ownership, discoverability, governance, in-place sharing, masking. To unlock full value for agents, there needs to be work to transform data products into MCP-compatible resources: standardized APIs, richer metadata, low latency where needed, robust oversight.

If done well, the payoff is substantial: faster, more trustworthy decisioning; automation that scales; better control of risk; potential cost savings. If not, there is risk of agents misusing data or breaking when underlying data shifts, which could expose regulatory, financial, or reputational risk.

---

If you like, I can sketch a roadmap of steps (with cost estimates) to move from a standard data mesh to a fully MCP-ready agentic architecture in a financial organization.

[1]: https://aws.amazon.com/blogs/big-data/how-jpmorgan-chase-built-a-data-mesh-architecture-to-drive-significant-value-to-enhance-their-enterprise-data-platform/?utm_source=chatgpt.com "How JPMorgan Chase built a data mesh architecture to ..."
[2]: https://medium.com/%40balarampanda.ai/ai-and-model-context-protocol-in-banking-transforming-financial-services-through-intelligent-agent-71ae00c1bfea?utm_source=chatgpt.com "AI and Model Context Protocol in Banking"
[3]: https://www.jpmorganchase.com/about/technology/blog/evolution-of-data-mesh-architecture?utm_source=chatgpt.com "Evolution of data mesh architecture can drive significant ..."