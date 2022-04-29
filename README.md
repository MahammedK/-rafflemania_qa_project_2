# RaffleMania

### Objective
Create an application that generates ‘Objects’ upon a set of predefined rules. The ‘Objects’ can be from any domain, being creative.

To simplify, I have to create an application takes data from two different services and generates an ‘Object’. I have complete freedom in the application I decide to create.

### Contents
* [Constraints](#contraints)
* [What I plan to create](#what-i-plan-to-create)
* [User Stories, Acceptance Criteria and Story Points](#user-stories-acceptance-criteria-and-story-points)
* [ERD](#erd)
* [Project Management - Trello and MVP](#project-management-trello-and-mvp)
* [Risk Assessment](#risk-assessment)
* [Frontend](#frontend)
* [Testing and Issues](#testing-and-issues)
* [Improvements](#improvements)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

### Constraints
The constraints in this project are the technologies that need to be used. The following constraints have been set for this project:
* Trello for project management (Kanban Board)
*	Version Control: Git
*	CI Server: Jenkins
*	Configuration Management: Ansible
*	Using GCP as Cloud Provider
*	Containerisation: Docker
*	Orchestration Tool: Docker Swarm
*	Reverse Proxy: NGINX

### What I plan to create
The app I plan to create will be split into 4 services. The frontend will be service 1. This is what the user will see and where the ‘Objects’ are displayed. Service 2 will be a list of numbers, just like in a raffle where entrants are given a number for a prize draw. Service 3 will be a list of random prizes. Random numbers and prizes from services 2 & 3 will generate the ‘Object’ shown on the frontend, e.g., number 5 wins an iPad. And finally service 4 will also create an ‘Object’ using predefines rules based on the results of service 2 + 3.

| Services | Applied on |
| --- | --- |
| 1 |  Frontend (Where ‘Objects’ will be displayed) |
| 2 |  Half of an object (List of numbers) |
| 3 |  Other half of the object (List of prizes) | 
| 4 |  ‘Object’ created from results of service 2 + 3 |

### User Stories, Acceptance Criteria &amp; Story Points

### ERD

### Project Management – Trello &amp; MVP

### Risk Assessment

Risk Assessments are used to ensure a project&#39;s success by evaluating scenarios that may impact the project in a negative way. Making note of potential risks informs an individual ensuring they are aware of what may occur prior to undergoing a particular task. By evaluating risks, I am able to mitigate the damage that may be caused to the project and may design the project such that theses risks are less likely to occur.

| Description | Evaluation | Likelihood | Impact Level | Responsibility | Current Control Measures | Proposed Control Measures | Response | Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GCP going down | Data will not be able to be accessed | Low | High | Google Cloud Platform | None | Backup files saved on computer | Wait till GCP is back up and running | 28/04/22 |
| Code looking messy | Hard to understand data | High | Med | Mahammed Kassam | Try and understand the code myself | Get a colleague to look over the code and see if they understand it | Make data look presentable | 28/04/22 |
| Application freezing | Unsaved worked will get lost | Med | High | Mahammed Kassam | Constantly pushing to GitHub | Having backups saved | Clone down latest push to GitHub | 28/04/22 |
| Using VMs private IP | Private IP will become public knowledge | High | High | Mahammed Kassam | Ensuring public IP is copied | Constantly checking the public IP is being used | Create an entirely new VM | 28/04/22 |
| Not installing all requirements | Application will not work | High | Low | Mahammed Kassam | When error is thrown up , install all requirements | Have a requirements file, that lists all requirements | Install all requirements from the requirements file | 28/04/22 |
| No relevant firewall rules | There will be no accessing the application | Low | High | Mahammed Kassam | Ensure all firewall rules are in place | Before creating application, know what firewall rules are needed | Add correct firewall rules to VM | 29/04/22 |

### App – Frontend

### Testing and Issues

### Improvements

### Authors

Mahammed Kassam

### Acknowledgements
