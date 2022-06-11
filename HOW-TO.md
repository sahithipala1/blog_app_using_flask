# How to use this repo

This is a template repository for easing the development and deployment of Lambda applications.
It heavily uses AWS Lambda Powertools and it shows best practices on how to:
- Implement code to interact with several AWS resources used across the platform
- Interact with 3rd party APIs (Coming soon!!!)
- Implement Lambda logging and monitoring best practices

## Steps to use this template

1. Submit a PR to: https://github.com/goodyear/dataplatform-github/tree/main/terraform/repos/applications/gmc


2. Begin to use this template as backbone for developing and deploying new lambdas, once you have received an email with the address to your newly created repo in GitHub


3. Clone the newly created repo and open it with your favorite IDE


4. Create a new feature branch following the name convention DP-XXXX_feature_name. This should be equivalent to the name of your ticket in Jira


5. Checkout your new branch and get ready to develop


6. Create a new dedicated virtual environment (VE) with Virtualenv. Each project should have a dedicated virtual environment.
   ![img.png](docs/ve.png)


7. Install dependencies in your newly created VE with:
   ```
   #Update pip and install poetry and pre-commit
   pip install --upgrade pip poetry pre-commit

   #Activate pre-commit hooks
   pre-commit install

   #Install dependencies in poetry.lock
   poetry install
   ```
   Optionally, run `make setup` which will execute the Makefile and `poetry install` afterwards.
   Dependencies for local development are managed by poetry in pyproject.toml file and peotry.lock.
   To keep the same version across the platform, poetry will install dependencies in poetry.lock
   Dependencies used in dev, test and prd environments should be specified in the files inside
   src/mc_template_lambda/requirements/


8. Rename mc_git_template_lambda and mc_template_lambda to your_lambda_name everywhere including folder names


9. Happy coding!!!
    - The folder src/code_templates contains lambda handler templates for:
      1. SQS batch processing -  sqs_batch_processor_handler.py
      2. Event source utilities - sns_event_source_handler.py, sqs_event_source_handler.py and kinesis_stream_event_source_handler.py
      3. 3rd party API calls - Coming soon!!!
      4. Interact with AWS infrastructure - S3, DynamoDB, Kinesis, SQS, SNS.
    - Configuration info should be in src/mc_template_lambda/config.py


10. Update your Terraform and Jenkins files by filling in info everywhere there is a TO DO mark and remove these marks accordingly

    - Terraform files to edit in terraform/lambda/
      1. Check everything inside terraform/lambda/*
      2. Copy iam.tf from terraform/aws to terraform/lambda. Fill in info to attach security policies and roles
      3. Copy and rename resource.tf in terraform/aws for any additional resource used in your lambda (e.g., cloud watch event, S3)
    - Jenkins files to edit:
      1. Jenkinsfile
      2. jenkins/deploy.jenkinsfile


11. To test your code run: `pytest -m test_handler.py`.

    - Beware we use coverage for unit testing, therefore you might need to add --no-cov as addition argument to the run configuration when debugging your code to be able to stop in breakpoints
        ![no_cov.png](docs/no_cov.png)

    - You might need to disable AWS X-RAY Tracer when running unit testing locally setting [POWERTOOLS_TRACE_DISABLED](https://github.com/awslabs/aws-lambda-powertools-python) environment variable
        ```
        POWERTOOLS_TRACE_DISABLED=1 AWS_XRAY_SDK_ENABLED=false python -m pytest
        ```
        ![img.png](docs/disable_tracer.png)

      Optionally run `make test` or `make coverage-html` which will execute the test or coverage-html sections on Makefile
    - Configuration files for unit testing in src/mc_template_lambda/tests/config_test.py
    - Raw data for testing in src/mc_template_lambda/tests/data/XXXX.json


12. Complete the Readme.md file by replacing the text in *italic* and providing the information related to this repo


13. Fill in info in section [tool.poetry] in pyproject.toml file


14. Apply the pre-commit hooks:`pre-commit run --all-files` before committing your code


15. Commit and push XXXX_feature_name branch


16. Have a look at our [Code Review Checklist](https://wiki.goodyear.eu/display/DP/Code+Review+Checklist) before submitting code to code review


17. Once you are ready submit a PR and add at least 2 reviewers


18. Merge XXXX_feature_name branch to dev once 2 reviewers have approved you PR. By merging to dev, your changes with be deployed to the data platform dev account.


19. Follow our [deployment workflow](https://wiki.goodyear.eu/display/DP/Development+Branch+and+Deployment+Workflow) to deploy to test and prod accounts.

    [ATTENTION!!!] Synchronize with the responsible teams before deploying to the data platform test and prod accounts. QA and release teams are usually involved depending on the complexity of your task.
