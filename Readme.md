# ReAct Agent with Python and Groq

## Overview

This project demonstrates the creation of a ReAct (Reasoning and Action) agent using Python and Groq without relying on any LLM frameworks. The ReAct agent integrates reasoning capabilities with actionable steps, enabling more sophisticated interactions and problem-solving.

### What is an Agent?

An agent is essentially a loop that interacts with a language model (LLM) based on a user query. It inspects the responses formulated by the LLM iteratively until the desired result is obtained.

### What is a ReAct Agent?

The ReAct agent, short for Reasoning and Action agent, is a framework that combines the reasoning abilities of LLMs with actionable steps. This integration allows the agent to perform more complex tasks by alternating between generating thoughts and executing task-specific actions in an iterative process. The ReAct agent was introduced in the paper "ReAct: Synergizing Reasoning and Acting in Language Models" and has been designed to enhance the versatility, capability, and interpretability of LLMs.

### Technology Stack

- **Python**: A high-level, interpreted, object-oriented programming language.
- **Groq**: An advanced AI solutions company known for its innovative hardware and software platforms that optimize the performance of LLMs and other AI applications.

## Workflow

The ReAct agent operates on a thought-action-observation loop, where it reasons about previous observations to decide on the next actions. The loop continues until the agent reaches the final answer or completes the maximum number of iterations.

### Agent Workflow:

1. **Thought**: The agent considers the query and determines the necessary action.
2. **Action**: The agent executes the determined action, such as performing a calculation or retrieving information from Wikipedia.
3. **Observation**: The agent observes the result of the action and uses it to inform the next steps.
4. **Answer**: Once the agent has enough information, it formulates and outputs the final answer.

### Example Use Cases

1. **Calculate Age**: The agent calculates the current age of a person and multiplies it by 2.
2. **Mass of Earth**: The agent retrieves the mass of Earth from Wikipedia, performs a calculation, and returns the result.
3. **Longest River**: The agent identifies the longest river in the world and retrieves its length.

## Installation

To set up the ReAct agent, you need to install the required libraries, set up the Groq API key, and instantiate the LLM with Groq. Detailed installation steps are provided in the code implementation.

## Usage

You can use the ReAct agent by initiating a query. The agent will process the query through the thought-action-observation loop and return the answer. Example queries include calculating the age of a person, determining the mass of the Earth, and finding the longest river in the world.

## Conclusion

This project showcases a simple yet effective implementation of a ReAct agent using Python and Groq. By leveraging the reasoning and action capabilities of LLMs, the agent can perform sophisticated tasks and provide accurate answers to complex queries.