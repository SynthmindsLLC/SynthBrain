---
description: 
created date: '[[2024-06-19]]'
type: 
excalidraw-plugin: parsed
tags:
  - excalidraw
excalidraw-open-md: true
relationships:
file folder: _📭 Inbox
---
# [[SynthGen Agents]]

# Purpose
The multi-agent framework is designed to streamline the execution of complex tasks by distributing responsibilities across specialized agents, ensuring high efficiency, quality, and accuracy.

### Workflow

1. **Task Initiation**: The user inputs a complex task.
    - The **Orchestrator Agent** (Chief of Staff) takes the lead, breaking down the task into subtasks, sequencing them, and delegating them to appropriate agents. It also manages the user's calendar and to-do list, ensuring all tasks are tracked and scheduled.
      
2. **Task Delegation**: Subtasks are assigned to specialized agents based on their expertise.
    - For example, data analysis is handled by the **Data Scientist Agent**, creative content generation by the **Creative Content Agent**, social media management by the **Marketing Specialist Agent**, etc.
      
3. **Subtask Execution**: Each specialized agent performs its assigned subtask using its unique set of tools.
    - The **Data Scientist Agent** might run statistical analyses, the **Creative Content Agent** could be writing or editing content, and the **Marketing Specialist Agent** may create and schedule social media posts.
      
4. **Quality Assurance**: Before finalizing, the **Critic Agent** evaluates the outputs from each specialized agent.
    - The Critic Agent assesses the quality, accuracy, completeness, and relevance of the outputs, providing feedback and requiring improvements if necessary. This ensures that only high-quality work is delivered.
      
5. **Task Completion**: Once all subtasks are approved, the **Orchestrator Agent** compiles the final outputs into a comprehensive report or deliverable.
    - The Orchestrator Agent ensures that all pieces fit together seamlessly, presenting a cohesive final product to the user.

### Benefits

- **Efficiency**: Tasks are handled by agents best suited for them, allowing for parallel processing and faster completion times.
- **Quality**: The Critic Agent ensures that all outputs meet high standards before they are finalized.
- **Flexibility**: The framework can handle a wide range of tasks, from data analysis and content creation to IT support and financial management, making it suitable for both personal and professional use.
- **Scalability**: New agents with specialized tools can be added as needed, allowing the framework to grow and adapt to new challenges.
# Components

## Orchestrator Agent (Chief of Staff)
**Role**: Manages overall coordination of tasks, sequences subtasks, delegates to other agents, manages the user's calendar and to-do list, and compiles the final deliverable(s).

**Specialized Tools**:
 - **TaskSequencer**: Breaks down complex tasks into subtasks and sequences them.
 - **DelegationManager**: Delegates tasks to appropriate agents.
 - **ProgressTracker**: Tracks the progress of all assigned tasks.
 - **CalendarManager**: Manages the user's calendar and schedules events.
 - **ToDoListManager**: Manages the user's to-do list and assigns tasks to agents or the user.

### TaskSequencer
```json
{
    "task": "string",
    "subtasks": [
        {
            "subtask": "string",
            "sequence": "integer"
        }
        // Additional subtasks as needed
    ]
}
```

### DelegationManager
```json
{
    "task": "string",
    "assigned_agent": "string",
    "parameters": {
        "param1": "value1",
        "param2": "value2"
        // Additional parameters as needed
    }
}
```

### ProgressTracker
```json
{
    "tasks": [
        {
            "task_id": "string",
            "status": "pending | in_progress | completed"
        }
        // Additional tasks as needed
    ]
}
```

### CalendarManager
```json
{
    "action": "create | update | delete",
    "event": {
        "title": "string",
        "date": "YYYY-MM-DD",
        "time": "HH:MM",
        "location": "string",
        "description": "string"
    }
}
```

### ToDoListManager
```json
{
    "action": "add | update | delete",
    "task": {
        "title": "string",
        "due_date": "YYYY-MM-DD",
        "priority": "low | medium | high",
        "description": "string"
    }
}
```

## Data Scientist Agent
**Role**: Performs data analysis, statistical modeling, and data-driven decision-making.

**Specialized Tools**:
 - **DataAnalyzer**: Executes Python scripts for data analysis.
 - **StatisticalTool**: Performs statistical analysis and modeling.
 - **VisualizationTool**: Creates data visualizations.


### DataAnalyzer
```json
{
    "script": "string",
    "inputs": {
        "input1": "value1",
        "input2": "value2"
        // Additional inputs as needed
    }
}
```

### StatisticalTool
```json
{
    "data": "string",
    "analysis_type": "regression | classification | clustering"
}
```

### VisualizationTool
```json
{
    "data": "string",
    "chart_type": "bar | line | pie"
}
```

## Creative Content Agent
**Role**: Supports creative content generation, including writing, video, and podcast production.

**Specialized Tools**:
 - **WritingAssistant**: Helps with writing articles, scripts, and other written content.
 - **VideoEditor**: Assists in editing video content.
 - **AudioEditor**: Assists in editing podcast and audio content.
 - **IdeaGenerator**: Generates ideas for creative projects.

### WritingAssistant
```json
{
    "title": "string",
    "content": "string",
    "tags": ["string"]
}
```

### VideoEditor
```json
{
    "video_file": "string",
    "edit_operations": [
        {
            "operation": "cut | trim | merge | add_effect",
            "parameters": {
                "start_time": "HH:MM:SS",
                "end_time": "HH:MM:SS"
                // Additional parameters as needed
            }
        }
        // Additional edit operations as needed
    ]
}
```

### AudioEditor
```json
{
    "audio_file": "string",
    "edit_operations": [
        {
            "operation": "cut | trim | merge | add_effect",
            "parameters": {
                "start_time": "HH:MM:SS",
                "end_time": "HH:MM:SS"
                // Additional parameters as needed
            }
        }
        // Additional edit operations as needed
    ]
}
```

### IdeaGenerator
```json
{
    "topic": "string",
    "keywords": ["string"]
}
```

## Marketing Specialist Agent
**Role**: Manages social media, creates social media posts, and schedules them.

**Specialized Tools**:
 - **PostCreator**: Designs and creates social media posts.
 - **CampaignManager**: Schedules and manages social media campaigns.
 - **AnalyticsTool**: Analyzes social media performance and engagement.


### PostCreator
```json
{
    "content": "string",
    "image_url": "string",
    "hashtags": ["string"],
    "platform": "twitter | facebook | instagram | linkedin"
}
```

### CampaignManager
```json
{
    "campaign_name": "string",
    "posts": [
        {
            "content": "string",
            "image_url": "string",
            "scheduled_time": "YYYY-MM-DDTHH:MM:SS"
            // Additional parameters as needed
        }
        // Additional posts as needed
    ]
}
```

### AnalyticsTool
```json
{
    "platform": "twitter | facebook | instagram | linkedin",
    "metrics": ["engagement", "reach", "likes", "shares", "comments"]
}
```

## Operations Manager Agent
**Role**: Oversees operational tasks, workflow optimizations, and logistics.

**Specialized Tools**:
 - **WorkflowOptimizer**: Analyzes and optimizes workflows.
 - **AutomationEngineer**: Creates automations to support the user.
 - **ResourceAllocator**: Allocates resources efficiently.


### WorkflowOptimizer
```json
{
    "workflow": "string",
    "optimization_criteria": "efficiency | cost | time"
}
```

### LogisticsManager
```json
{
    "logistics_task": "string",
    "parameters": {
        "origin": "string",
        "destination": "string",
        "items": ["string"]
    }
}
```

### ResourceAllocator
```json
{
    "resource": "string",
    "quantity": "number",
    "allocation_strategy": "priority | round_robin"
}
```

## Relationship Manager Agent
**Role**: Manages interactions with various contacts, including customers, colleagues, and personal contacts.

**Specialized Tools**:
 - **ContactManager**: Manages contact information and interactions.
 - **CommunicationTool**: Sends emails or texts.
 - **FeedbackAnalyzer**: Collects and analyzes feedback from interactions.
\
### ContactManager
```json
{
    "action": "add | update | delete",
    "contact": {
        "first_name": "string",
        "last_name": "string",
        "email": "string",
        "phone": "string",
        "notes": "string"
    }
}
```

### CommunicationTool
```json
{
    "method": "email | text",
    "recipient": {
        "name": "string",
        "email": "string", // If method is email
        "phone": "string" // If method is text
    },
    "message": "string",
    "subject": "string" // Optional, for emails only
}
```

### FeedbackAnalyzer
```json
{
    "feedback_data": "string",
    "analysis_type": "sentiment | trend"
}
```

## Finance Manager Agent
**Role**: Handles financial planning, budgeting, and financial analysis.

**Specialized Tools**:
 - **BudgetPlanner**: Plans and tracks budgets.
 - **FinancialAnalyzer**: Analyzes financial data and generates reports.
 - **ExpenseTracker**: Tracks and manages expenses.


### BudgetPlanner
```json
{
    "budget_period": "string",
    "allocations": [
        {
            "category": "string",
            "amount": "number"
        }
        // Additional allocations as needed
    ]
}
```

### FinancialAnalyzer
```json
{
    "financial_data": "string",
    "analysis_type": "profit_loss | balance_sheet | cash_flow"
}
```

### ExpenseTracker
```json
{
    "expenses": [
        {
            "category": "string",
            "amount": "number"
        }
        // Additional expenses as needed
    ]
}
```

## IT Support Agent
**Role**: Helps with computer or technology-related problems or obstacles.

**Specialized Tools**:
 - **Troubleshooter**: Handles troubleshooting and resolving technical issues.
 - **SystemOptimizer**: Optimizes system performance and resolves inefficiencies.
 - **SecurityAdvisor**: Ensures cybersecurity and manages security protocols.

### Troubleshooter
```json
{
    "issue": "string",
    "details": "string"
}
```

### SystemOptimizer
```json
{
    "system_component": "hardware | software",
    "optimization_task": "clean_up | update | tune_up"
}
```

### SecurityAdvisor
```json
{
    "security_task": "scan | update | monitor",
    "parameters": {
        "system": "string"
    }
}
```

## Researcher Agent
**Role**: Conducts research, gathers data, and provides insights on various topics.

**Specialized Tools**:
 - **WebSearch**: Searches for relevant information online.
 - **LiteratureReviewTool**: Reviews and summarizes academic papers and articles.
 - **SurveyTool**: Designs and analyzes surveys to gather data.

### WebSearch
```json
{
    "query": "string"
}
```

### LiteratureReviewTool
```json
{
    "topic": "string",
    "sources": ["string"]
}
```

### SurveyTool
```json
{
    "survey_title": "string",
    "questions": [
        {
            "question_text": "string",
            "question_type": "multiple_choice | open_ended",
            "options": ["string"] // Optional for multiple_choice
        }
        // Additional questions as needed
    ]
}
```

## Critic Agent
**Role**: Evaluates the outputs of other agents, provides feedback, and ensures quality.

**Specialized Tools**:
 - **QualityEvaluator**: Assesses the quality and accuracy of outputs.
 - **FeedbackProvider**: Gives constructive feedback and suggestions for improvement.
 - **RetryManager**: Manages the retry logic and tracks the iterations.

### QualityEvaluator
```json
{
    "task_id": "string",
    "output": "string",
    "criteria": {
        "accuracy": "high | medium | low",
        "completeness": "complete | incomplete",
        "relevance": "high | medium | low"
    },
    "evaluation": "approved | needs_improvement"
}
```

### FeedbackProvider
```json
{
    "task_id": "string",
    "feedback": {
        "comments": "string",
        "suggestions": ["string"]
    }
}
```

### RetryManager
```json
{
    "task_id": "string",
    "retry_count": "integer",
    "max_retries": "integer",
    "status": "pending | retry | failed"
}
```



# Excalidraw Data
## Text Elements
%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebTieGjoghH0EDihmbgBtAF1+CFw4OABlKKhxVFAwSHVUyogiZWkkmoZCBAoAIVxsAGtlUmEOYgBhNnw2Um4IAGIAM0Wl1shs

EUCMgEkK/TKhvoRxyemJWYBGBAuLlYg10g2obdSe/sHhsYmpmahyDmY4XAPG53B5PfQAMUI+HwZRgwRmgg8wPW6UeOz2bAOAHUSOpuHxwKsUVt0T9MQhYfCJIiSMj7qiwQAlYTNDjhLJoM78In0kmpADyAOwahg3DOAAZxdzbsS0alwZwoODcPooaLOdKQQydgqMiVCEZKjwpYSZby5foACpYKAAQSaXAkwXmUDpoNJgLt9zYFEkIWI3A4Qmhmtl

YIAoiNbd7ff6ZoChlRpcxsENoQANMU8ACsABZk6mJvgAJrcABsZbiAGYzgB2Wu5gCc4p4VdzVdr2elRjYBm41Ta9AIQkqZ0JAF9Q+ame82cwOeghkIRjdBiR9YbA8H8NK1x9jv3CZAuhMA6dRo2LxfweCVpBGQhlMHATNZuGACIfj83iATqcPDEDkFKB2D+LcQ1NOBAjMYRmAAcVIdcDUqIMILaeZyDSB8RiYQgOGUQ8akgdJcE0YIz1QH4R25VY

iDgbgqIQGiIA4FVKkY5jhCgIg2QY0gRz/U07AAKwQbBMhKVi4AAWTYYgEEjUjyO4eYCDCcBJzoeYoXCftxxAccgA
```
%%