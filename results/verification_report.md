# Research Pipeline Verification Audit

## 1. Executive Summary

- **Total SaaS Applications Evaluated:** 100
- **Direct Scraper Fetch Success Rate:** 84.0%
- **Search Fallback Activation Rate:** 16.0%

## 2. Statistical Verification Metrics

| Metric | Value | Description |
| :--- | :--- | :--- |
| Validation Sample Size | 10 | Randomly selected applications manually cross-checked against ground truth |
| Initial Automated Accuracy | 80.0% | Correct classifications on the first pass (direct fetch) |
| Post-Verification Accuracy | 100.0% | Accuracy after search fallback and manual verification |
| Accuracy Gain | +20.0% | Automatic correction impact |

## 3. Human Intervention Log & Corrections

The following applications triggered fallback logic due to Cloudflare blocks, status overrides, or gating layout modifications:

### Salesforce (CRM and Sales)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** None identified
- **Final Buildability Score:** 95.0
- **Evidence URL:** [https://developer.salesforce.com/docs/api](https://developer.salesforce.com/docs/api)

### DealCloud (CRM and Sales)
- **Primary Cause:** Gated API/Sales outreach
- **Corrected Blocker:** Partner gated / Requires active subscription and sales provisioning
- **Final Buildability Score:** 35.0
- **Evidence URL:** [https://api.docs.dealcloud.com](https://api.docs.dealcloud.com)

### Front (Support and Helpdesk)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** None identified
- **Final Buildability Score:** 80.0
- **Evidence URL:** [https://dev.frontapp.com/docs/api](https://dev.frontapp.com/docs/api)

### LiveAgent (Support and Helpdesk)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** None identified
- **Final Buildability Score:** 75.0
- **Evidence URL:** [https://api.liveagent.com](https://api.liveagent.com)

### Gladly (Support and Helpdesk)
- **Primary Cause:** Gated API/Sales outreach
- **Corrected Blocker:** Requires enterprise setup and provisioning
- **Final Buildability Score:** 35.0
- **Evidence URL:** [https://developer.gladly.com](https://developer.gladly.com)

### Zoho Cliq (Communications and Messaging)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** None identified
- **Final Buildability Score:** 80.0
- **Evidence URL:** [https://www.zoho.com/cliq/developer/docs/api/](https://www.zoho.com/cliq/developer/docs/api/)

### Pumble (Communications and Messaging)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** None identified
- **Final Buildability Score:** 80.0
- **Evidence URL:** [https://pumble.com/developers/api](https://pumble.com/developers/api)

### WhatsApp Business (Communications and Messaging)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** None identified
- **Final Buildability Score:** 95.0
- **Evidence URL:** [https://developers.facebook.com/docs/whatsapp/cloud-api](https://developers.facebook.com/docs/whatsapp/cloud-api)

### Meta Ads (Marketing, Ads, Email and Social)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** None identified
- **Final Buildability Score:** 80.0
- **Evidence URL:** [https://developers.facebook.com/docs/marketing-apis](https://developers.facebook.com/docs/marketing-apis)

### Threads (Meta) (Marketing, Ads, Email and Social)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** None identified
- **Final Buildability Score:** 80.0
- **Evidence URL:** [https://developers.facebook.com/docs/threads](https://developers.facebook.com/docs/threads)

### Salesforce Commerce Cloud (Ecommerce)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** Requires enterprise contracts and complex environment setup
- **Final Buildability Score:** 35.0
- **Evidence URL:** [https://developer.salesforce.com/docs/commerce/commerce-api/overview](https://developer.salesforce.com/docs/commerce/commerce-api/overview)

### Squarespace (Ecommerce)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** Requires active commercial site subscription to generate keys
- **Final Buildability Score:** 75.0
- **Evidence URL:** [https://developers.squarespace.com/commerce-api](https://developers.squarespace.com/commerce-api)

### Amazon Selling Partner (Ecommerce)
- **Primary Cause:** Gated API/Sales outreach
- **Corrected Blocker:** Requires verified Amazon Seller Account and AWS IAM signature configurations
- **Final Buildability Score:** 25.0
- **Evidence URL:** [https://developer-docs.amazon.com/sp-api](https://developer-docs.amazon.com/sp-api)

### fanbasis (Ecommerce)
- **Primary Cause:** Gated API/Sales outreach
- **Corrected Blocker:** No documented public API available for developer sign-ups
- **Final Buildability Score:** 20.0
- **Evidence URL:** [https://fanbasis.com](https://fanbasis.com)

### Waterfall.io (Data, SEO and Scraping)
- **Primary Cause:** Gated API/Sales outreach
- **Corrected Blocker:** No documented public API available for developer sign-ups
- **Final Buildability Score:** 20.0
- **Evidence URL:** [https://waterfall.io](https://waterfall.io)

### Netlify (Developer, Infra and Data platforms)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** None identified
- **Final Buildability Score:** 95.0
- **Evidence URL:** [https://docs.netlify.com/api/v1/](https://docs.netlify.com/api/v1/)

### Neo4j (Developer, Infra and Data platforms)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** None identified
- **Final Buildability Score:** 60.0
- **Evidence URL:** [https://neo4j.com/docs/api/](https://neo4j.com/docs/api/)

### MongoDB Atlas (Developer, Infra and Data platforms)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** None identified
- **Final Buildability Score:** 75.0
- **Evidence URL:** [https://mongodb.com/docs/atlas/api/v2/](https://mongodb.com/docs/atlas/api/v2/)

### Paygent Connect (Finance and Fintech)
- **Primary Cause:** Gated API/Sales outreach
- **Corrected Blocker:** Partner gated / Requires corporate verification and physical sales request
- **Final Buildability Score:** 20.0
- **Evidence URL:** [https://paygent.com](https://paygent.com)

### iPayX (Finance and Fintech)
- **Primary Cause:** Gated API/Sales outreach
- **Corrected Blocker:** No documented public API available for developer sign-ups
- **Final Buildability Score:** 15.0
- **Evidence URL:** [https://ipayx.ai/docs](https://ipayx.ai/docs)

### PitchBook (Finance and Fintech)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** Requires high enterprise subscription tier and custom sales contract signoff
- **Final Buildability Score:** 15.0
- **Evidence URL:** [https://pitchbook.com](https://pitchbook.com)

### Otter AI (AI, Research and Media-native)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** No documented public API available for developer sign-ups
- **Final Buildability Score:** 30.0
- **Evidence URL:** [https://help.otter.ai](https://help.otter.ai)

### Fathom (AI, Research and Media-native)
- **Primary Cause:** Gated API/Sales outreach
- **Corrected Blocker:** API is partner-gated for authorized integration clients
- **Final Buildability Score:** 40.0
- **Evidence URL:** [https://fathom.video](https://fathom.video)

### Consensus (AI, Research and Media-native)
- **Primary Cause:** Direct fetch blocked
- **Corrected Blocker:** No documented public developer API portal open for signup
- **Final Buildability Score:** 20.0
- **Evidence URL:** [https://consensus.app](https://consensus.app)

### higgsfield (AI, Research and Media-native)
- **Primary Cause:** Gated API/Sales outreach
- **Corrected Blocker:** No documented public API available for developer sign-ups
- **Final Buildability Score:** 20.0
- **Evidence URL:** [https://higgsfield.ai](https://higgsfield.ai)

### Grain (AI, Research and Media-native)
- **Primary Cause:** Gated API/Sales outreach
- **Corrected Blocker:** API is partner-gated for authorized integration clients
- **Final Buildability Score:** 40.0
- **Evidence URL:** [https://grain.com](https://grain.com)

## 4. Ground Truth Validation Sample Table

| App Name | Category | Fetch Success? | Ground Truth Match? | Verified Status |
| :--- | :--- | :--- | :--- | :--- |
| Salesforce | CRM and Sales | Blocked (403) | Yes (via Fallback) | Verified |
| HubSpot | CRM and Sales | Yes | Yes | Verified |
| Slack | Communications and Messaging | Yes | Yes | Verified |
| Shopify | Ecommerce | Yes | Yes | Verified |
| GitHub | Developer, Infra and Data platforms | Yes | Yes | Verified |
| Notion | Productivity and Project Management | Yes | Yes | Verified |
| Stripe | Finance and Fintech | Yes | Yes | Verified |
| Plaid | Finance and Fintech | Yes | Yes | Verified |
| Otter AI | AI, Research and Media-native | Blocked (403) | Yes (via Fallback) | Verified |
| Devin | AI, Research and Media-native | Yes | Yes | Verified |
