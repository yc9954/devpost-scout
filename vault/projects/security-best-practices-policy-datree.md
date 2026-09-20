---
slug: "security-best-practices-policy-datree"
url: "https://devpost.com/software/security-best-practices-policy-datree"
title: "Cluster Security"
hackathon: "Cloud Native Hackathon"
organization: "WeMakeDevs"
winner: true
words: 672
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
---

# Cluster Security

> Make your Kubernetes cluster more secure effortlessly

[Devpost](https://devpost.com/software/security-best-practices-policy-datree) · hackathon [[Cloud Native Hackathon]]

## Facets

**domain** [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** datree, kubernetes, yaml

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cluster security

## Body

Inspiration The inspiration for this policy comes from this article . After reading this article and a number of other blogs, I was able to ascertain the need for a policy which encompasses the best practices for container security while being unopinionated in its configuration. After going through a variety of sources I built this policy containing 7 rules which enable Kubernetes engineers to ensure the security of their clusters and the containers. What it does This policy checks and validates a number of security configurations for Kubernetes clusters like privileged , runAsUser and runAsGroup . All the rules in the policy are listed below: CUSTOM_SECURITY_USER_CHECK : This rule checks the presence of runAsUser field in the securityContext section. It also validates whether the value provided is in the correct range or not. CUSTOM_SECURITY_GROUPS_CHECK : This rule checks the presence of runAsGroup field in the securityContext section. It also validates whether the value provided is in the correct range or not. CUSTOM_SECURITY_PRIVILEGE_CHECK : This rule checks the presence of allowPrivilegeEscalation field in the securityContext section. It also validates whether the value supplied is a boolean or not. CUSTOM_SECURITY_FILESYSTEM_ACCESSIBILITY : This rule checks the presence of readOnlyRootFilesystem field in the securityContext section. It also validates whether the value supplied is a boolean or not. CUSTOM_SECURITY_DEPRECATED_CHECK : This rule checks whether the configuration uses PodSecurityPolicy, which is a deprecated resource and can break security configurations. CUSTOM_SECURITY_PRIVILEGED_CHECK : This rules checks the presence of privileged key in the securityContext field. It also makes sure the value supplied is of type boolean. CUSTOM_SECURITY_IMAGE_PULL : This rule ensures that there is a field imagePullPolicy and it is set to Always , as a best practice and a security configuration. CUSTOM_SECURITY_FLEX_VOLUME_CHECK : This rule checks the presence of flexVolumes in the volumes section, if allowFlexVolumes key was present in the spec field. This rule prevents misconfigurations pertaining to the flex volumes which may lead to vulnerabilities if not handled properly. CUSTOM_SECURITY_PROC_MOUNT_CHECK : To test the above rules and the policy itself, please go to the GitHub repository and using the datree CLI, verify the working by testing with pass.yaml and fail.yaml files. How we built it We built it using yaml. Yaml is a pseudo language similar to json and toml. Using yaml, I was able to build out the logic of my policy and the rules within it. The logic was declared using json schema, which is used by datree's CLI in order to test the configurations and publish them. Finally, datree played a big role in this policy, mainly because the policy was built to run on datree but also because datree was critical in order for me to test the policy and publish it. Challenges we ran into One major challenge we ran into was during the logic for the if conditions. After trying multiple times, we got it to work, which consumed a good chunk of our time. After that we did not face many issues, but we still worked on improving our policy and adding multiple rules to the policy. Accomplishments that we're proud of I am proud of building this entire policy having no prior knowledge of datree and frankly, Kubernetes. After doing this project I am confident in Kubernetes and Datree's CLI. I am also proud of having learnt datree and a lot about Kubernetes in just one weekend. What we learned I learnt about datree and it's purpose along with it's usage. I will certainly use datree in my next Kubernetes projects since it looks promising and it's use case is very inviting. Along with learning about datree, I also learnt a lot about json schema and the way logic is written using json schema. Finally, I learnt about Kubernetes and resources like DaemonSet and StatefulSet, plus I learnt about securityContext configuration in Kubernetes. What's next for Cluster Security In the future, we would definitely add more rules to improve the main idea of the policy and possibly create more policies around the idea of "best practices" in Kubernetes. <div