# German LkSG and EU CSDDD

**Current-status brief | Checked: 13 October 2026**  
**Audience:** Solutions engineering, procurement, compliance and engineering leaders.

## 1. What they mean

**LkSG** is Germany’s *Lieferkettensorgfaltspflichtengesetz*, commonly called the Supply Chain Due Diligence Act. It concerns human rights and specified environmental risks in business supply chains. **CSDDD**, also called **CS3D**, is the EU Corporate Sustainability Due Diligence Directive. It establishes corporate duties concerning adverse human rights and environmental impacts. [1][4]

Neither is a software vulnerability standard. In a CodeRabbit discussion, distinguish supplier due diligence from technical controls supporting software used to perform that due diligence.

## 2. Comparison

| Topic | German LkSG | EU CSDDD, as amended in 2026 |
|---|---|---|
| Legal form | German national law, already applicable | EU directive requiring national implementation |
| Main scope test | Relevant German establishment and normally at least 1,000 employees in Germany; statutory counting rules apply | Main EU-company test: more than 5,000 employees **and** more than €1.5 billion worldwide net turnover |
| Foreign companies | Qualifying German branches can be covered | Main non-EU-company test: more than €1.5 billion net turnover in the EU; no equivalent employee test |
| Supplier reach | Own business and direct suppliers; additional indirect-supplier duties arise on substantiated knowledge | Own operations, subsidiaries and the legally defined chain of activities; risk-based assessment |
| Authority | BAFA | Authorities designated by EU Member States |
| Timing | In force since 2023; employee threshold reduced in 2024 | National transposition by 26 July 2028; application from 26 July 2029 |

Sources: [1][4][5]. These are headline tests: group/consolidation rules, qualifying periods, exemptions and special franchising/licensing provisions require entity-specific assessment. CSDDD’s “chain of activities” is a defined legal term, not every downstream use of every product.

## 3. German LkSG: duties and current reporting position

The published statute requires proportionate risk management, assigned responsibility, risk analysis, a policy statement, prevention, remedial measures, a complaints procedure and documentation. Protected interests include labour rights; environmental provisions address specific treaty-linked risks. [1]

Risk analysis is annual and also triggered by material changes in risk. Documentation must be kept for at least seven years. [7][8]

**Reporting status needs careful wording.** BAFA says it has stopped reviewing annual reports and its submission channel is unavailable. The government’s amendment initiative proposes retroactive removal of the reporting duty and changes to sanctions. However, the official statute retrieved for this brief still contains the reporting provisions. Administrative non-enforcement must therefore be distinguished from an enacted repeal. [1][2][3]

Do not infer that risk analysis, prevention, remediation or documentation have disappeared because annual report processing has stopped. Confirm any subsequent enacted amendment before relying on this brief for a filing or enforcement decision.

## 4. EU CSDDD: the 2026 changes

Directive (EU) 2026/470 amended the original Directive (EU) 2024/1760. The amendment was published on 26 February 2026 and entered into force on 18 March 2026. [4][6]

The revised framework raises scope thresholds, permits assessment focused on likely/severe impacts using reasonably available information, removes CSDDD’s mandatory climate transition plan and removes the harmonised EU civil-liability regime. National liability can still apply. The pecuniary penalty cap is 3% of net worldwide turnover. [5]

Due diligence still involves identifying and addressing impacts, stakeholder engagement, complaints, monitoring and communication. Smaller suppliers can face customer expectations without becoming directly regulated merely because they supply a covered company. [4]

| Milestone | Current date |
|---|---|
| National transposition | 26 July 2028 |
| Application to covered companies | 26 July 2029 |
| Article 16 reporting measures | Financial years starting on or after 1 January 2030 |

Source: [4]. Earlier 2027/2028 phased application dates and the former general 1,000-employee/€450-million CSDDD threshold should not be used as the current position. CSRD, the sustainability **reporting** directive, is a separate instrument with its own scope and rules.

## 5. Relevance to CodeRabbit and enterprise engineering

The following is an **illustrative engineering interpretation**, not a statutory requirement or a verified promise that CodeRabbit detects every issue.

A customer may build supplier onboarding, risk assessment, grievance handling or remediation software. Reviewing changes in those systems can help identify defects that undermine its chosen processes.

| Customer workflow | Example code defect to investigate | Review evidence to retain |
|---|---|---|
| Supplier risk assessment | A scoring change silently downgrades a severe risk | Approved scoring specification, test results and reviewer decision |
| Supplier onboarding | Approval proceeds before a required assessment is complete | Requirement-to-test mapping and approval records |
| Complaints handling | Identity details appear in broadly accessible logs | Access-control tests and logging policy |
| Remediation tracking | An unresolved corrective action is marked complete | Workflow tests and evidence of authorised closure |
| Documentation retention | A deletion job removes records earlier than policy permits | Applicable retention policy and deletion tests |
| Management reporting | Missing records are counted as “no risk” | Data-quality tests and reconciliation results |

**Suggested customer wording:** “Where your due-diligence processes rely on software, we can evaluate whether AI-assisted code review helps identify defects in the workflows and data controls that support those processes.”

A PR review cannot establish labour conditions at a supplier, verify an environmental impact, determine legal applicability or certify LkSG/CSDDD compliance. Avoid claims such as “CodeRabbit makes you LkSG compliant” or “CSDDD requires AI code review.” Self-hosting alone also does not establish compliance with either instrument.

## 6. Practical discovery questions

1. Which legal entity and supplier relationships does your compliance team consider in scope?
2. Which systems support risk analysis, complaints and corrective actions?
3. Which workflow failures would materially affect those processes?
4. Which policies and business rules can engineering use as approved review context?
5. Which evidence must stay in the compliance system, and which belongs in the development workflow?
6. Who validates a finding’s business impact and accepts the fix?

For an evaluation, agree on a small set of realistic defects, supply the relevant business specifications, and measure validated detections, false positives and remediation effort. Retain the customer’s adjudication; do not equate a review comment with proof of compliance.

## 7. Action checklist

- Ask legal/compliance to confirm entity scope and the current German amendment position.
- Separate statutory obligations from procurement requests and internal policies.
- Map relevant processes to system owners and approved specifications.
- Test workflow controls independently of AI-generated findings.
- Recheck official sources before quoting dates, thresholds or penalties externally.

## 8. Official sources

All sources checked on 13 October 2026. Where BAFA pages were not directly retrievable, their current indexed official statements were used for the limited administrative-status summary.

1. [German LkSG — official statute](https://www.gesetze-im-internet.de/lksg/BJNR295910021.html), especially §§ 1–3, 9–10 and 19.
2. [BAFA — reporting status](https://www.bafa.de/DE/Lieferketten/Berichtspflicht/berichtspflicht_node.html).
3. [German Ministry for Economic Affairs — BAFA enforcement instruction, 26 September 2025](https://www.bundeswirtschaftsministerium.de/Redaktion/DE/Pressemitteilungen/2025/09/20250926-bmwe-bafa-zurueckhaltung-lieferkettengesetz.html).
4. [European Commission — current CSDDD overview](https://commission.europa.eu/topics/business-and-industry/company-law-and-corporate-governance/corporate-sustainability-due-diligence_en).
5. [Council of the EU — final approval of simplification, 24 February 2026](https://www.consilium.europa.eu/en/press/press-releases/2026/02/24/council-signs-off-simplification-of-sustainability-reporting-and-due-diligence-requirements-to-boost-eu-competitiveness/).
6. [Directive (EU) 2026/470 — Official Journal record](https://eur-lex.europa.eu/eli/dir/2026/470/oj/eng).
7. [LkSG § 5 — risk analysis](https://www.gesetze-im-internet.de/lksg/__5.html).
8. [LkSG § 10 — documentation and reporting](https://www.gesetze-im-internet.de/lksg/__10.html).

*This brief supports preparation and customer conversations. An entity’s legal applicability and obligations require assessment against the applicable enacted national law.*
