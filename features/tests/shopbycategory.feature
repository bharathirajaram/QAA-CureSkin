# Created by bharathirajaram at 7/15/23
Feature: Test Scenarios for Shop by Category

Scenario: Verify That Category Body product is being shown up
  Given Open CureSkin Shopping page
  When Click Shop by Category Menu
  When Click Body Menu item
  Then Verify that Body text is exists in URL
