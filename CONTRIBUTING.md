# Contributing

Persons contributing to this project agree to the [code of conduct](./CONDUCT.md) and agree to the potential redistribution of their code under our license.

## Contributor Agreement: 

### Task:
- Ha @hadinh1306 : AIC + Table output
- Simran @simrnsethi : BIC
- Stephanie @rq1995 : Mallow’s Cp

### Communication:
Each group member is responsible to be:

- Responsive on Slack , especially during Friday and Saturday. 
- 10-minute stand-up meeting on Monday during lunch break, to talk about weekly plan.

### Contribute to the project
- For small changes, create Branch is ok. Guidelines below.
- For big changes, please use Folk. Guidelines below.
- Commit frequently with clear and concise commit message.
- Write tests for function changes.
- Once your changes are done, submit a Pull Request.
- Wait for comments from team member. Then make changes from your Branch/Folk repo.
- Only merge after reaching whole team agreement.

## Where to Contribute(Workflow)

#### Using GitHub
1.  We can use GitHub flow (branch) to manage changes:
   - Create a new branch in your desktop copy of this repository for each significant change.
   - Commit the change in that branch.
   - Submit a pull request from that branch to the master repository.
   - If you receive feedback, make changes on your desktop and push to your branch on GitHub: the pull request will update automatically.
   - **If a major change is made by any person, tag other two. If this change is approved by all → accept pull request.

2.   We also use GitHub flow (fork) to manage changes:
   - Fork, then clone this repo
   - Push that branch to your fork of this repository on GitHub.
   - Submit a pull request
   - If you receive feedback, make changes on your desktop and push to your branch on GitHub: the pull request will update automatically.
   - **If a major change is made by any person, tag other two. If this change is approved by all → accept pull request.

## How to Contribute

#### Code comment 
- Functions need to be documented clearly.

#### Commit message
- Big changes:
  
  ```
$ git commit -m "A brief summary of the commit
> 
> A paragraph describing what changed and its impact."
```

-  Small changes:
   - 1-line detailed message including what change you made.

- Frequent commit everytime you make changes.


#### Testing conventions
- Details coming in 1 week.

#### Coding convention
- Python:

      - All code should in `.py` file rather than jupyter notebook file
- R:
      - Avoid using `=` when assign objects. Instead, use `->`
      - Use `%>%` (including in **dplyr** package)
      - All code should be in `.R` file rather than `.Rmd` or R notebook.





