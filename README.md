# checkpoint

Here’s the high-level functional test plan for the **Firewall as a Service (FWaaS)** functionality.  

---

### **High-Level Functional Test Plan for Firewall as a Service (FWaaS)**  

| **Test ID** | **Test Scenario** | **Steps to Execute** | **Expected Result** |
|------------|------------------|----------------------|---------------------|
| **1.1** | **Integration with Network Resources** | Configure FWaaS with on-premises and cloud-based resources, initiate traffic flow between them. | FWaaS correctly routes and manages traffic, ensuring seamless communication. |
| **1.2** | **Cross-Platform Compatibility** | Test FWaaS on various OS (Windows, macOS, Linux) and mobile devices. | FWaaS functions properly on all tested platforms. |
| **1.3** | **Identity Provider Integration** | Connect FWaaS with an identity provider (Okta, Azure AD), test user authentication. | Users can authenticate successfully using the identity provider. |
| **2.1** | **Data Flow Visibility** | Access FWaaS logs, monitor real-time traffic flows. | Traffic logs are accurately captured and displayed in the management console. |
| **2.2** | **Network Monitoring** | Simulate different types of network traffic and verify monitoring accuracy. | FWaaS displays detailed insights into network traffic. |
| **3.1** | **Granular Access Control Rules** | Define access rules based on identity, role, and device type. | Traffic adheres to defined policies, blocking unauthorized access. |
| **3.2** | **Layer 3 & Layer 4 Segmentation** | Segment network by IP and protocol, attempt unauthorized access. | Access is restricted per segmentation policies. |
| **4.1** | **User Scalability** | Increase the number of users and monitor system performance. | FWaaS handles scaling without performance degradation. |
| **4.2** | **Policy Update Handling** | Modify an existing policy and validate real-time enforcement. | Policies update immediately and apply to traffic correctly. |
| **5.1** | **Identity-Based Access Policies** | Assign different access levels based on user roles. | Users can access only the permitted resources. |
| **5.2** | **Multi-Factor Authentication (MFA) Enforcement** | Enable MFA for login and attempt access. | Users must verify identity through MFA before gaining access. |
| **6.1** | **Network Segmentation Enforcement** | Segment network and attempt unauthorized resource access. | Segmentation rules successfully isolate traffic. |
| **7.1** | **Global Private Gateway Deployment** | Deploy FWaaS gateways in different regions and test connectivity. | Traffic flows through the nearest gateway, ensuring low latency. |
| **7.2** | **Policy Enforcement Across Gateways** | Configure firewall rules on multiple gateways and test traffic. | Policies are enforced consistently across all gateways. |
| **8.1** | **Mutual TLS Encryption Validation** | Inspect encrypted traffic between endpoints. | FWaaS encrypts data in transit using TLS. |
| **8.2** | **Wi-Fi Security and DNS Filtering** | Connect to public Wi-Fi and test protection features. | FWaaS secures traffic and filters malicious domains. |
| **9.1** | **Policy Management UI Functionality** | Create, update, and delete policies via the dashboard. | Policies are applied correctly and reflected in the UI. |
| **9.2** | **Policy Application to Specific Users/Groups** | Assign policies to users and test enforcement. | Users experience access restrictions based on policy settings. |
| **10.1** | **Audit Logging and Compliance** | Generate logs and review stored records. | Logs meet compliance standards and are accessible for audits. |

---
