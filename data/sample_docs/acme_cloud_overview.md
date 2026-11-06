# Acme Cloud Integration - Product Knowledge Base

## 1. Overview
Acme Cloud is an enterprise SaaS platform designed to automate multi-cloud data synchronization, workflow triggers, and webhook management across AWS, Azure, and Google Cloud Platform.

## 2. Authentication & API Keys
All API requests to Acme Cloud must be authenticated using an API Bearer token in the request header:
`Authorization: Bearer <YOUR_API_TOKEN>`

Tokens can be generated from the **Acme Cloud Developer Portal -> Settings -> API Keys**.
* Standard tokens expire after 90 days.
* Service account tokens are persistent until manually revoked.

## 3. Webhook Delivery & Retry Policy
When an event occurs in Acme Cloud, the system sends an HTTP POST payload to the configured endpoint URL.
* **Timeout:** The endpoint must respond with an HTTP `200 OK` within 5 seconds.
* **Retry Strategy:** If delivery fails, Acme Cloud applies an exponential backoff retry mechanism (retrying at 1 min, 5 mins, 30 mins, and 2 hours).
* **Failure Alerts:** After 4 failed attempts, an email alert is triggered to the administrator.

## 4. Rate Limiting
To ensure high availability, Acme Cloud enforces standard rate limits:
* **Standard Tier:** 1,000 requests per minute per IP address.
* **Enterprise Tier:** 10,000 requests per minute per IP address.
* When rate limits are exceeded, the API returns HTTP status `429 Too Many Requests`.

## 5. Frequently Asked Questions (FAQ)

### Q: How do I rotate an API token without causing service downtime?
A: You can generate a secondary token in the Developer Portal, update your client application to use the secondary token, verify successful requests, and then delete the old primary token.

### Q: What is the maximum payload size for webhook ingestion?
A: The maximum JSON payload accepted by Acme Cloud webhooks is 10 MB per single request.
