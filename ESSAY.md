# Essay

A few years ago Dev where adding features, QA checking quality, Ops running them on Prem independently from each other.

Dev want to push features as often as possible, Ops want not, they want stable (and secure) production.

DevSecOps brought Continuous integration and Continuous Delivery. They aims to removed silos between Dev QA and Ops to deploy more often.
Avoiding deploying patch Friday evening. Or new big release once a year.
It allow a faster Time to Market and quicker feedback from client.

Now one feature is added in a Pull Request is running, service is built, deployed and tests are running. Only once all steps went fine code is merge in main branch.
Dev, QA, Ops are reviewing PR code and better interact.
This allow to increase quality but is also consuming more resources (Each PR are tested).
Agility required tools such as Jenkins/Gitlab and method such as GitFlow but increased complexity of the overall workflow.

From Ops side DevOps added GitOps principal, so that everything done in server side (provisioning, deployment, monitoring, etc...) is now on git. So no more manual intervention.
We know what and when changes occurs. There is more transparency, reproductibility.
This also required new tools, Chef,Puppet,Ansible,Terraform and now Kubernetes.
It also help Dev QA and Ops to have same environment, to reproduce issues, tests features in a more production like environment.

Service are now running on containers, they are isolated from each other and k8s help to scale and rollback.
On Cloud, adding a service is faster, no need to order a bare metal server and wait for month to be delivered. It is easier to scale up and down. You pay for what you use (FinOps).
If a service crash, it is automatically restarted.

For Dev using container helps to reproduce issues but also push them to split monolithic products into smaller and decoupled services (if not micro services or micro fronted), they are pushed to add more tests. For Ops this allow to add security first principal, immutable environment and better control resources usages, but more services to monitor.

Deploying more often help to find out changes impact.

New deployment way also bring new issues.

Cloud provider are public more subject to attack.
They have their own way (normalization). Will you be tied to one cloud provider forever?
Having on premise and cloud services working together can be challenging.
Splitting application to many smaller services is adding complexity. Testing a standalone service is good, but how do you test that all your services are working together?
We deploy also more open source.
CI/CD is getting more complex and depend one more services (internal or external) so more subject to disruption (SLA). Pipeline build time increase as you add more tests.
Pipeline should not become the bottleneck (and fail) and deployment knowledge unknown as everything has been automated.

All the tools and processes brought by DevOps require code. If done internal is is adding technical debt and like application code must be maintained.

They must as products follow best practices, be tested and deploy using the same principal.

PS : And secured, My CI/CD have been attack 3 weeks ago by https://us-cert.cisa.gov/ncas/current-activity/2021/10/22/malware-discovered-popular-npm-package-ua-parser-js ;-)
