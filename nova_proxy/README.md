# 🚀 Amazon Nova API Proxy with AWS secret manager  
*A simple guide for beginners*

## 📘 What Is a “Proxy” in AWS?

A **proxy** is a small service that sits **between a client** (your app, website, or another backend) **and a downstream service** (Nova API), forwarding requests and returning responses.  
Think of it as a middleman:

```
Client  →  Proxy  →  Nova API
```

The proxy itself does not do the main work. Instead, it:

- receives the request  
- optionally validates or logs it  
- forwards it to the actual service  
- returns the response  

returns the response - this pattern works extremely well in protecting your api key and your secrets!

---

## ⭐ Why Use a Proxy?

### 1. Hide Secrets  
Your proxy stores API keys securely in **AWS Secrets Manager** so clients never see them.

### 2. Centralize Authentication & Validation  
Every request passes through the proxy, allowing you to enforce:

- authentication  
- schema validation  
- rate limiting  
- safety checks  

### 3. Standardize Requests  
Your proxy can rewrite or normalize requests:

- add default parameters  
- enforce model versions  
- attach metadata  
- convert formats  

### 4. Safer Rollouts  
You can upgrade your backend, change routes, update model versions, or add safeguards **without modifying client code**.

### 5. Monitoring & Observability  
With it you can add:

- logs  
- metrics  
- alarms and alerts  
- error tracking  

Your upstream system receives clean, normalized traffic.

---

## 🏗️ Architecture Overview

A fully managed AWS proxy looks like this:

```
Client
   |
   v
API Gateway (public HTTPS endpoint)
   |
   v
AWS Lambda (your proxy code)
   |
   v
Nova API
```

API Gateway = HTTPS entrypoint  
Lambda = code execution  
Secrets Manager = secure key storage  
Backend = your actual ChatCompletion API

---

## 🧰 What a Lambda Proxy Typically Does

Inside your proxy Lambda, the flow is:

1. Parse the incoming JSON request  
2. Fetch your API key from Secrets Manager  
3. Initialize the backend SDK with that key  
4. Forward the request to the upstream service  
5. Return the upstream response to the caller  

This gives you full control over the request pipeline.

---

## 🚀 How to Deploy a Proxy to AWS (Simple Steps)

Below is the simplest possible deployment workflow using the AWS Console.

---

### **1. Create the Secret in Secrets Manager**

1. Open **AWS Secrets Manager**  
2. Click **Store a new secret**  
3. Choose **Other type of secret**  
4. Store your *plain text* API key: (You can fetch your api key from nova.amazon.com/dev/api)

---

### **2. Create the Lambda Function**

1. Go to **AWS Lambda → Create function**  
2. Choose **Author from scratch**  
3. Runtime: **Python 3.10+**  
4. Add environment variables to the Lambda configuration:
```
SECRET_MANAGER_SECRET_NAME=backend/NovaApiKey
```

5. Paste your proxy Python code into the editor (the handler should read the request, fetch the secret, call the backend, and respond).

---

### **3. Grant Lambda Permission to Read the Secret**

Open the **execution role** attached to the Lambda and add this IAM policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:REGION:ACCOUNT:secret:backend/NovaApiKey"
    }
  ]
}
```
⚠️ Replace REGION and ACCOUNT with your values.

### **4.Create the HTTPS Endpoint (API Gateway)**
This makes your proxy publicly reachable.
1. Open API Gateway
2. Create an HTTP API
3. Add a route:
```
POST /chat
```
4. Integrate that route with your Lambda 
5. Deploy the API

You will receive a public URL like:
```
https://abc123.execute-api.us-east-1.amazonaws.com/chat
```
This is your new proxy endpoint.

🧪 Example: Calling Your Proxy

```
curl -X POST https://abc123.execute-api.us-east-1.amazonaws.com/chat \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nova-2-lite-v1",
    "messages": [
      { "role": "user", "content": "Hello from client!" }
    ]
  }'
```
Your proxy Lambda will:

1. Receive this request
2. Fetch the secret
3. Forward it to your ChatCompletion backend
4. Return the result

### **5. Integrate proxy with your FE code (You are almost there!)**

Once your Lambda proxy is deployed behind API Gateway, you’ll receive a public HTTPS endpoint like:

```
https://abc123.execute-api.us-east-1.amazonaws.com/chat
```

Your frontend (React, Vue, Next.js, plain JS, etc.) can call this endpoint directly.  
Because the proxy hides the API key, the frontend sends **no secrets**.

### ✅ Example: Using Fetch in JavaScript

```js
async function callChatProxy(userMessage) {
  const response = await fetch("https://abc123.execute-api.us-east-1.amazonaws.com/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      model: "nova-2-lite-v1",
      messages: [
        { role: "user", content: userMessage }
      ]
    })
  });

  const data = await response.json();
  return data;
}

// Usage:
callChatProxy("Hello from the frontend!").then(console.log);
```

### Summary
There you have it! if you followed this tutorial you are able to deploy, run and build you own single turn Chat bot while still upholding the highest security standards!

### What to do next?
1. You can expand the FE code to handle multi turns!
2. You can add a DNS for your proxy endpoint using [Route 53](https://aws.amazon.com/route53/) 
3. You can add logging, authentication, error handling to your lambda
4. You can start supporting streaming and a lot more!