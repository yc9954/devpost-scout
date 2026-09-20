---
slug: "uipath-testing_framework"
url: "https://devpost.com/software/uipath-testing_framework"
title: "UiPath Testing Framework"
hackathon: "Power Up Automation"
organization: "UiPath"
winner: true
words: 991
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# UiPath Testing Framework

> Tired of testing workflows manually? Framework for running unit tests will help ease the development and save time.

[Devpost](https://devpost.com/software/uipath-testing_framework) · hackathon [[Power Up Automation]]

## Facets

  <sub>weak: deterministic_policy</sub>
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** c#, uipath

## How they structured the write-up

- inspiration
- what it does
- quick guide
- how i built it
- challenges i ran into
- what's next for uipath-testing_framework

## Body

Framework state machine Custom activity and methods Output window Test logs text file Unit test Unit test Arrange stage Unit test Act stage Unit test Assert stage Custom Exception Inspiration Unit testing is a core software development practice and for a good reasons: Helps to find problems early in the development cycle Saves time in the long run: When refactoring code When changing code due to change requests Helps developer write better code My main inspiration was to help myself and other developers save time and effort that manual testing regularily takes, and which can be solved by automation (after all, we are automating processes, so why not a part of the development also?). A big reason too, was to bring UiPath development practices closer to the software development standards. What it does There are three main parts to this project: Framework used for automated running of unit tests and logging. Custom activity package that plays essential part in running of Framework and Unit Tests both. Unit Test Template used to easily make a Framework ready unit tests. Framework Framework automatically runs all unit tests present in the Test_Repository folder. For each test run, the Framework outputs test logs that can be used for debugging in case of a failed test or errors. It is made to be plug and play. No configuring is required. It can be seamlessly integrated into any project or framework. It automatically detects unit tests that hadn't implemented Assert Unit Test activity. Custom Activity Package Custom activity package Custom.Activities.VariableComparer.x.x.x.nupkg contains custom code and activities used in both Framework and Unit Tests (for source code please check Custom Activity Repository ). Custom activity package contains: Custom Assert class that contains various static methods used for evaluating outputs of the tested code: Assert.AreEqual(expected,actual) checks if two variables are equal. Assert.AreNotEqual(expected,actual) checks if two variables are not equal. Assert.AreSame(expected,actual) checks if two variables point to the same reference. Assert.AreNotSame(expected,actual) checks if two variables do not point to the same reference. Assert.Contains(expected,actual) checks if first variable is contained inside of second variable. Assert.NotContains(expected,actual) checks if first variable is not contained inside of second variable. Assert.IsNull(actual) checks variable is null. Assert.IsNotNull(actual) checks variable is not null. Custom Exceptions that are thrown by Assert methods and used by a Framework for logging: AssertException is main exception thrown by Assert methods. AssertNullException is exception thrown when Assert.IsNull or Assert.IsNotNull method returns false. CustomAssertException is generic exception that is thrown when random boolean expression that returns false is passed to Assert Unit Test activity. Custom Assert Unit Test activity used as container for writing Assert methods (used when making unit tests) and also by a Framework as a soft test validation (Framework checks if .xaml file in Tests_Repository folder is a real test or not by looking if it had implemented this activity). Unit Test Template From the developers standpoint, main effort needs to be put into the writing of the unit tests. Luckily, a master template for Unit Tests is supplied with the Framework to make this process quicker and easier. Along with the master template, a few examples are also supplied, and can be used as a start point for the developers not yet familiar with the unit tests. Unit Test Template is not mandatory to be used. Developers can make tests in their own way as long as Framework requirements are satisfied, meaning: Every test has to have implemented Assert Unit Test activity. In case these arguments are not present Framework is programmed to ignore the test and log it as an error . Quick Guide Install custom activity package ( Custom.Activities.VariableComparer.x.x.x.nupkg ) that comes with the Framework and can be found in the root of the directory. Installation is performed by placing .nupkg package into the %localappdata%\UiPath\app-xx.x.x\Packages folder and installing it using Package Manager from inside of UiPath. Using Unit Test template ( Tests_Repository\UnitTestTemplate\MethodName_StateUnderTest_ExpectedBehavior.xaml ) make Unit Tests. Unit tests must implement Assert Unit Test custom activity to be eligible for running in Framework (is implemented by default in the template file). Place Unit Tests into the Tests_Repository folder. When RunAllTests.xaml is started it will run all tests that are found in the Tests_Repository folder. To integrate TestingFramework into another project copy whole folder to the target project root directory. ( Optional ) When integrating TestingFramework into another project, delete project.json file from TestingFramework folder (if present). (This is more of a quality of life improvement. For people that open .xaml from the directory itself. If you have integrated framework into another project, and you open RunAllTests.xaml directly from directory (while project.json is present in framework root) it will count TestingFramework as a standalone project and you will not be able to see parent project files inside of UiPath "Project" sidebar). How I built it Framework was built using the UiPath Studio Custom activity package was built using Microsoft Visual Studio IDE and NuGet Package Explorer Challenges I ran into There were problems when integrating Framework into the other projects (by copying Framework folder into another projects root directory and deleting the project.json from the Framework root directory). Framework got broken because of project directory into which framework was integrated to was now considered as a root of the project. Because of this relative paths were not working no more. Easy solution was to force users to have project.json in Framework directory also. But that was not a satisfing solution. This led me to write code that makes Framework selfconfigure itself on startup. Now Framework can be put into any folder or sub-folder of a parent project and it will still run, even without project.json in its directory. What's next for UiPath-Testing_Framework What's next in the near future is adding, and refining Assert methods code to include even more situations. Idea for the far future is to develop custom activity which would, when Framework is run, popup a GUI from where a developer can filter which tests to run. <div