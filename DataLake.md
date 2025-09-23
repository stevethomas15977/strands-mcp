High-Level Problem & Opportunity

JPMorgan Chase (JPMC) sees its data not just as isolated by business unit, but as an enterprise asset that can deliver much more value when shared and combined (for analytics, machine learning, reports, etc.). 
Amazon Web Services, Inc.

However, sharing data broadly brings risk (security, compliance, data quality). So there is a tension: more sharing = more value, but also more risk. JPMC wanted a way to unlock value while controlling risk. 
Amazon Web Services, Inc.

Strategic Approach

JPMC adopted a two-part strategy to address this:

Data Product Model

Break down data into “products” owned by particular teams who know the data well (its usage, legal constraints, quality, etc.). 
Amazon Web Services, Inc.

Each data product is a coherent grouping of related data: owned, curated, understood. 
Amazon Web Services, Inc.

Data Mesh Architecture

A distributed architecture in which each data product has its own “data lake” (storage) under its domain owner. 
Amazon Web Services, Inc.

Consumers don’t get their own separate copies of data; instead, they access data in place (in the product lake) via secure, governed access. 
Amazon Web Services, Inc.

Key Benefits (Why It Matters Financially)

Reduced Redundancy & Cost Savings
By eliminating unnecessary copies of data, storage costs go down and the maintenance/overhead of keeping multiple versions of data in sync is reduced. 
Amazon Web Services, Inc.

Faster Access & Better Decision Making
Because every data product is well cataloged and discoverable, business units can find and use data more quickly, rather than reinventing pipelines or waiting for someone else to produce it. 
Amazon Web Services, Inc.

Improved Data Accuracy & Consistency
Since data isn’t duplicated, it reduces the risk of different versions of “truth” being used in different reports, which strengthens confidence in analyses and reduces risks in decision-making. 
Amazon Web Services, Inc.

Better Risk Management & Governance
Clear ownership per data product means strong accountability. Also, sharing “in place” allows stricter control on what data (columns, records, etc.) is visible to whom, which helps maintain compliance, privacy, security. 
Amazon Web Services, Inc.

Transparency of Data Flows
JPMC invested in tools/catalogs that let them see which data is flowing where, which team is using what data, so there is auditability and governance. That matters for regulatory oversight, audit, risk. 
Amazon Web Services, Inc.

What This Looks Like in Practice (Simplified Example)

Each group (e.g. a business line) maintains its data “product lake” — imagine that as a repository of all its relevant data, well-organized, owned, and curated.

There’s a shared catalog that shows what data exists (who owns it, what it contains, any limits) so others in the company can find what they need.

When someone needs data for reporting, instead of making copies or asking for extracts, they access it where it sits, under controlled access.

If certain data is sensitive, the owner can mask or limit exposure appropriately.

The company can see “who is using which data, and where it came from” — increasing trust, auditability, and reducing surprises.

Key Risks or Trade-Offs (Worth Watching)

Access control must be very precise. Mistakes in “who can see what” can lead to leaks, etc.

Cultural change required: teams must take responsibility for owning data, maintaining it, managing risk.

Upfront investment in tooling/cataloging and governance. Some costs that may not have immediate ROI, but pay off over time.

Need for ongoing maintenance of the catalog/data product definitions, ensuring people keep their data in shape.

Bottom Line (for an Executive)

JPMC’s approach allows it to get more value from its data — more useful analytics, faster insights, more consistent reporting — without giving up control of sensitive data or creating chaos. The architecture (data mesh + data product model) gives structure & ownership, and reduces duplication and risk, while enabling agility and scale. Over time, this can lead to cost savings, better decision-making, stronger compliance, and ability to scale up things like AI/ML.