# RaffleMania

### Objective
Create an application that generates ‘Objects’ upon a set of predefined rules. The ‘Objects’ can be from any domain, being creative.

To simplify, I have to create an application takes data from two different services and generates an ‘Object’. I have complete freedom in the application I decide to create.

### Contents
* [Constraints](#contraints)
* [What I plan to create](#what-i-plan-to-create)
* [User Stories, Acceptance Criteria and Story Points](#user-stories-acceptance-criteria-and-story-points)
* [CI Pipeline](#ci-pipeline)
* [Project Management](#project-management)
* [Risk Assessment](#risk-assessment)
* [Frontend](#frontend)
* [Testing](#testing)
* [Jenkins](#jenkins)
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
The app I plan to create will be split into 4 services. The frontend will be service 1. This is what the user will see and where the ‘Objects’ are displayed. Service 2 will be a list of letters, just like in a raffle where entrants are given a number for a prize draw. Service 3 will be a list of random prizes. Random numbers and prizes from services 2 & 3 will generate the ‘Object’ shown on the frontend, e.g., letter A wins an iPad. And finally service 4 will also create an ‘Object’ using predefines rules based on the results of service 2 + 3.

| Services | Applied on |
| --- | --- |
| 1 |  Frontend (Where ‘Objects’ will be displayed) |
| 2 |  Half of an object (List of letters) |
| 3 |  Other half of the object (List of prizes) | 
| 4 |  ‘Object’ created from results of service 2 + 3 |

### User Stories, Acceptance Criteria and Story Points

To create a vision as to what the application would look like, I used user stories. Being the sole user, the user stories were from my point of view. To understand what a feature requires, an acceptance criterion is attached to the user stories. Story points are a means of calculating how much work it will take to complete a task. PlanningPoker.com is used to decide the story point assigned to a user story. Each user story was given a number depending on complexity using the Fibonacci sequence to calculate the story point.

### CI Pipeline
| CI Pipeline | What was done in this project |
| --- | --- |
|  |  |
|  |  |
|  |  | 
|  |  |

### Project Management
###### Trello and MVP



The Trello board contains three colours, these represent:

Red – Must Have (MVP – Minimum Viable Product)
Orange – Should Have
Yellow - Could Have

This is due to the tasks included only contains tasks that were a necessary part of the project and those that would improve the project in a major way. There is no tasks that represent Won't Have, as the project was completed with tasks that were always to be included. The could have tasks were only left out due to time constraints.

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
| Constantly adding/removing images/containers | Takes a lot of time | High | Low | Mahammed Kassam | Using up arrow, so no need to type enitre code | Using up arrow, so no need to type enitre code | Ensure all code is correct, which will reduce the amount of times needed to add/removes images/containers | 09/05/22 |
| Old PC being used | PC will run really slow | High | High | PC | Only use programs/softwares that are needed | Using a PC with a bigger RAM and a better processor | Keep calm | 09/05/22 |
| File already existing | Jenkins test failing | High | Low | Mahammed Kassam | Rename file | Create a new file | Rename current file | 11/05/22 |
| Unsure how to proceed with a task | Time to complete project will be reduced | High | Low | Mahammed Kassam | Start with documentation to give a layout on how to proceed | Same as current control measures - Start with documentation to give a layout on how to proceed | Ask trainer on what they would recommend | 11/05/22 |

### Frontend
The frontend consists of just one page, consisting of the navigation bar that has just the home page on it. The rest of the page consists of the title, statement with objects from services and a refresh button.

Below are screenshots of the frontend, along with different possible outcomes:

1. If service 2 is either 'A, E, I, O, U' or service 3 starts with an 'A'. Service 4 should return 'Airpods'
    * Service 2 is either 'A, E, I, O, U' and service 3 starts with an 'A'.

    * Service 2 is either 'A, E, I, O, U' and service 3 DOES NOT start with an 'A'.

    * Service 2 IS NOT either 'A, E, I, O, U' and service 3 starts with an 'A'.

2. If service 2 is NOT either 'A, E, I, O, U' or service 3 DOES NOT start with an 'A'. Service 4 should return 'QA CloudAcademy free demo'

### Testing

### Jenkins

### Improvements

Story Points - 
A use story has more influence when the users aren't myself. The best/most usual way to use story points is is a collaborative project, because the chosen story points promote discussion, and multiple perspectives may lead to a consensus.

Frontend - 
The Navigation bar is useless as there is only one webpage for the frontend, it just makes the frontend look presentable. Making the page look presentable without the navbar would have been ideal.

### Authors

Mahammed Kassam

### Acknowledgements

Many thanks go to the trainer, Victoria Sacre, for the help, guidance, and patience. The cohort of 22MarEnable1 deserve to be acknowledged for their support and friendly demeanour. Not forgetting Luke Benson, Harry Volker and Adam Gray for being available to answer question and also Earl Gray for the recodings during week 1 through to 5.

Thanks go to getbootstrap for their navbar.
