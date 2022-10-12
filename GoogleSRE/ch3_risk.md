chapter 3 risk

SREs strive to make a service reliable enough, but no more reliable than it needs to be.

This is done to find a perfect balance between cost and reliability of the system. 
* Cost is comprised of machine resources and opportunity resources - when engineering resources are spent on building systems instead of visible features.
* Reliability is managed by managing risk

System's risk tolerance is usually measured by unplanned downtime.
Unplanned downtime is captured by the desired level of serice availability.

Time-base availability
availability = uptime / uptime + downtime

Aggregate-availability (request success rate)
availability = successful requests / total requests
* Used when is always partially available

In Google, risk tolerance is set by the service owners and the business goals they have for the service.

consumer services
* target level of availability: depends on function it provides and popularity
* types of failures: a constant low rate of failures, or an occasional full-site outage
* cost: how many "nines" are appropriate
* other: e.g. service latency

infrastructure services:
* target level of availability: might vary significantly for different clients, there is no single formula for it
* types of failures: same as above
* cost: to solve above problems, multiple clusters with different configurations must be built, this saves 10-50% of cost.
