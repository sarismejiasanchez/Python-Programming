# TYPES OF TESTING

# Categories of testing:
# 1. Unit Testing
#    In unit or component testing, the program tests specific individual components by isolating them. 
#    The components are low level which means that they are closer to the actual written code. 
#    They often involve use of automation for continuous integration given their small sizes. 
#    So you usually write these tests while writing the code. 
#    For example, if the code is in python, unit tests can be written with packages such as pytest.
#
# 2. Integration Testing
#    Integration testing, combines the unit tests and test the flow of data from one component to another. 
#    The key word here is an interface. 
#    This means that you test if the data is correctly fetched from a database within the python code, 
#    and if you have sent it to the web page. 
#    There are different approaches to it such as:
#    - Top-down appreach
#    - Bottom-up approach 
#    - Sandwich approaches.
#    Your approach depends on what code level interfaces you attempt first. 
#    It builds on the unit testing and a tester deals with it. 

# 3. System Testing
#    Next is system testing, which tests all the software 
#    you tested against the set requirements and expectations to ensure completeness. 
#    This includes measurements of the location of deployed components such as:
#    - Reliability
#    - Performance
#    - Security
#    - Load balancing. 
#    - Operability in the working environment such as the platform.
#    - Operating system. 
#    This is the most important stage handled by team of testers. 
#    It's also the most critical stage as the shipping of software 
#    to the stakeholders and end user happened after this phase.

# 4. Acceptance Testing
#    When the product arrives at this stage, it's generally considered to be ready for deployment. 
#    It's expected to be bug free and meet the set standards. 
#    The stakeholders and the select few end users are involved in acceptance testing.
#    It normally involves alpha, beta and regression testing. 
#    One way of approaching this is to give pre-written scenarios to the users. 
#    You use the results for improvements and try to find bugs that were missed earlier.

# All the different testing levels are designed to optimize software at different stages. 
# The key to testing is testing early and testing frequently. While each of the testing phases is important, 
# early detection saves time, effort and money.
# As the code gets increasingly complex mistakes become harder to fix. 
# It doesn't necessarily mean that unit testing will happen only at the beginning and acceptance at a later stage. 
# There are many testing cycles where these levels are approached iteratively. 
# A typical example is the agile model, here you release different versions of the product 
# iteratively and you perform acceptance testing every few weeks.

# There are different ways in which you can categorize the different test types.
# There are white box and black box tests. 
# White box testing is whether tester has knowledge of the code design and functionalities. 
# Black box tests function with no such information and the tester has no idea about the internal implementation. 
# 
# There are also other ways to categorize different tests:
# 1. Functional
# 2. Non functional
# 3. Maintenance tests. 

# 1. Functional tests are based on the business requirements stated. 
#    They determine if the features and functionalities are in line with the expectations. 
# 2. Non functional tests are more complex to define and involve metrics such as overall performance 
#    and quality of the product. 
# 3. Maintenance tests occur when the system and its operational environment is corrected, changed or extended. 

# But there are also manual and automated testing methods that are dependent on the scale of the software. 
