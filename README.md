# Task C Documentation

## Pipeline Architecture
Our CI/CD pipeline leverages **GitHub Actions** to implement a proactive "Shift-Left" approach to security. Integrating security scans into the pull request process ensures that we stop bad code before it merges into the main branch, which is a highly cost-effective strategy for identifying and fixing vulnerabilities early in the development lifecycle.

To optimize the pipeline's performance, we utilize **Parallel jobs**, adhering to the "Fail Fast" methodology (as discussed in Week 5). By running jobs concurrently, we significantly speed up execution time. For example, running our primary security scanners like Bandit and Semgrep at the same time reduces the overall wait time for developers, providing quicker feedback.

Our pipeline specifically incorporates three primary scanners, each serving a unique purpose:
* **Bandit**: Chosen for fast Python Static Application Security Testing (SAST). It effectively targets Python-specific vulnerabilities and coding errors.
* **Semgrep**: Selected for fast OWASP Web SAST. It is highly effective at identifying common web vulnerabilities and enforcing secure coding standards rapidly.
* **SonarCloud**: Integrated for deep historical analysis. It tracks overall code quality, technical debt, and provides comprehensive long-term security metrics.

## Evidence
*Pipeline running*
![Pipeline Running](placeholder_pipeline_run.png)

*Failing on the SQLi*
![SQLi Failure](placeholder_sqli_failure.png)

*Blocked Pull Request (Branch Protection)*
![Blocked PR](placeholder_blocked_pr.png)

## Triage & Limitations
While Static Application Security Testing (SAST) is essential, it has fundamental limitations. Specifically, SAST tools rely on pattern matching and lack deep understanding of business logic, leading to false positives. In DevSecOps theory, generating too many false positives creates **Alert Fatigue** and **Developer Friction**, potentially causing developers to ignore alerts or abandon the security pipeline altogether. Proper triage is critical to maintaining trust in the tooling.

"Automated SAST tools evaluate Abstract Syntax Trees (AST) but lack business logic and runtime context. The scanner flagged a hardcoded string as a severe vulnerability, but contextually, this was a dummy variable in a localized test function, not a production credential. This represents the 'False Positive Avalanche' typical of context-blind static analysis. To prevent alert fatigue and pipeline abandonment by developers, I triaged this by applying an 'as-code' risk acceptance via inline suppression."