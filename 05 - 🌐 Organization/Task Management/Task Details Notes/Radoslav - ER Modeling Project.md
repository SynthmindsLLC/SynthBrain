---
title: ER Potential Project
status: Todo / In Progress / Done
priority: Low / Medium / High
due_date: YYYY-MM-DD
tags:
  - UrosPesic
  - "#JamesGriffing"
created:
---

# Task Overview

## Description

Dear James and Uros,

I would like to extend my gratitude for the insightful discussion we had regarding my project on dynamic JSON instance generation and ER diagramming.  Your expertise in AI and prompt engineering is invaluable to the progression of this project.

Based on our conversation, I have compiled a detailed specification document outlining the key features, priorities, and desired enhancements for the project.  The main objective is to create a system capable of dynamically updating JSON instances based on predefined JSON schema and ER diagrams through the analysis of conversational inputs during live sessions.  This system should leverage AI and NLP technologies to accurately parse and understand these inputs using NER (Name entity recognition and their relationships)

I believe your experience, particularly in prompt engineering and AI integration, will be crucial in achieving these goals. I am hopeful that we can collaborate effectively to realize this vision.

Below, you will find the detailed specification document. I am eager to hear your thoughts on this and discuss the potential scope, feasibility, and, importantly, the alignment with my budget constraints.

Thank you once again for your time and insights during our meeting. I look forward to the possibility of working together on this exciting venture.

Best regards,

Radoslav Radivojevic

You can find my current POC and thought process when using pure json manipulation in python.

Project Overview:

The primary goal is to develop a system capable of dynamically generating and updating JSON instances based on conversations during live sessions with solution architects, business analysts, or other stakeholders. This system should parse spoken or written input, identify essential elements related to entity-relationship (ER) modeling, and reflect these changes in both a visual ER diagram and a corresponding JSON instance that adheres to a predefined JSON Schema.

Key Features and Priorities:

Dynamic JSON Instance Generation:

Real-time generation and updating of JSON instances based on conversation analysis. Ensure generated JSON instances (see jsonModel as an example of such instance below and entities Product.json,  Category.json) comply with a predefined JSON Schema for entities (EntitySchema.json) , capturing entity definitions, properties, and relationships. Desired json schema for entity can be visualized as Schema ER diagram which can visually aid users in modeling session to know what they can change in target json instance (which they can observe in target json instance ER diagram like this one Target json instance ER diagram):  Below is some useful information about Pythantic model, Instructor Pydantic (Python data validation library) model for this schema: Pydantic model is how I encapsulated json schema in a strongly typed class.  See videos for more info:   
Pydantic is all you need: Jason Liu,   
LlamaIndex Webinar: From Prompt to Schema Engineering with Pydantic (with @jxnlco) - pay attention to the video at this timestamp: Using flatter structure and not deeply nested structure and also notice James (the author of Instructor library) mentioned to use Chain of thoughts prompting to enhance structured response with well parsed output (This is what openai recommends, because this worked better in practice than prompting without chain of thoughts.) Part I - PydanticOutputParser and LLMChain.ipynb Village_Diagram that represents schema for pydantic model in this Python notebook Pydantic V2 - Full Course - Learn the BEST Library for Data Validation and Parsing Pydantic - Nested Models, JSON Schema and Auto-Generating Models with datamodel-code-generator

ER Diagram Visualization: (Not in scope, but a basic visualization can already be achieve) I believe James is right that this diagram can drive parts of prompting and it would be usesfull to have it interractively display current model.

Dynamic updating of ER diagrams to reflect changes in the JSON instance. Visual aids to guide the generation of prompts for AI integration.

AI and NLP Integration:

Use AI and NLP technologies for parsing conversational inputs. Extract relevant information from dialogues to generate and update JSON instances and ER diagrams.

Schema Node Management:

Feature to freeze/unfreeze specific parts of the JSON schema and ER diagram to prevent or allow alterations. Support granular control over elements within the JSON instance and ER diagram.

Advanced Modeling Features:

Support for both high-level (overall structure) and detailed (specific attributes and relationships) modeling. Incorporation of modern modeling paradigms and techniques beneficial for architects and designers.

Major Processing code should run on the server side to hide intellectual property:

Desired Features and Enhancements:

AI Model Training: Specialize AI models in enterprise-level ER modeling and JSON schema generation. Minimal DSL Development: Create a domain-specific language for intuitive and efficient command inputs. Integration with Existing Tools: Compatibility with tools like [ABP.IO](http://abp.io/) for CRUD operations and code generation. Knowledge Base Creation: Develop a repository of predefined models and schemas to augment AI capabilities. Collaborative Modeling: Enable multiple teams to work on the same model simultaneously, with real-time synchronization.

Advanced Modeling Tool Features for Designers and Architects:

Interactive ER Diagrams: Intuitive interfaces for manipulating ER diagrams, including drag-and-drop functionality. Model Versioning and History Tracking: Keep track of changes over time, allowing rollback to previous versions. Customizable View Layers: Different views (logical, physical, conceptual) tailored to various user roles (DBA, developer, business analyst). Automated Consistency Checks: Ensure model integrity and compliance with best practices and predefined standards. Model-to-Code Generation: Ability to generate database scripts, backend code, or API definitions directly from the model.

This specification aims to capture the essence of the project while also considering the practical needs of modeling designers and architects. The focus on dynamic, AI-driven model generation and updates, along with advanced tooling features, positions this system as a cutting-edge solution in the realm of ER modeling and JSON schema generation.

jsonModel = "  
{  
    "model": "[Booking.Management](http://booking.management/)",  
    "entities": [{  
            "Id": "4e027f4d-e23a-4072-9cbd-5ed37e069d6e",  
            "Name": "Product",  
            "Properties": [{  
                    "Id": "1219ec25-d77e-4032-a2d8-247ed8bc4ced",  
                    "Name": "Name",  
                    "Type": "string"  
                }  
            ],  
            "NavigationProperties": [{  
                    "EntityNameWithDuplicationNumber": "Media",  
                    "EntitySetNameWithDuplicationNumber": "Medias",  
                    "ReferencePropertyName": "FeaturedMedia",  
                    "UiPickType": "Modal",  
                    "IsRequired": false,  
                    "Name": "FeaturedMediaId"  
                }  
            ],  
            "PhysicalFileName": "Product.json"  
        }, {  
            "Id": "2b0f4dc8-5cef-4e99-9ec5-547cb2a72cc6",  
            "Name": "Category",  
            "Properties": [{  
                    "Id": "5109555f-5969-4582-afb8-cf4d624071e0",  
                    "Name": "Name",  
                    "Type": "string"  
                }, {  
                    "Id": "7cd702ca-cadc-4d14-8c24-4fea549106a5",  
                    "Name": "Slug",  
                    "Type": "string"  
                }  
            ],  
            "NavigationProperties": [],  
            "NavigationConnections": [],  
            "PhysicalFileName": "Category.json"  
        }  
    ]  
}  
"

I used this AI tool that allows designing various diagrams. I am only interested in ER, UML, Class diagrams that can visualize the model I am designing. [https://diagrammingai.com/](https://diagrammingai.com/) (You can see the image with me doing iterative modeling). You also have a normal chat dialog where you can ask general questions) So this UI is quite inspirative for my project.

This might be another idea to use Graph DB like Neo4j to store entity data models and export it to json. Build an Advanced RAG Chatbot with Neo4j Knowledge Graph

This point in video go over an example of extraction of what music to find and what actions to do (play, stop, next, previous) so this one reminds me of using "manipulation json" for incrementally updating target json instance. It doesn't use Instructor like above, but LangChain output parsing  LangChain Output Parsing and Extraction Webinar  
LangChain v0.1.0 Launch: Output Parsing (OpenAIFunctions, JSON, XML, CSV, Pydantic, YAML)

You can ignore this link as this is how we could extract voices for each user in the modeling session and convert to text. Multi Speaker Transcription with Speaker IDs with Local Whisper

I highlighted in yellow in Project Overview above what is in the project scope.

2. ER Diagram Visualization: this one can be achieved by using 2 functions: buildGoJsNodeDataArrayWithAutoLayoutEntities and  
buildGoJsLinkDataArray which, when given jsonModel as argument will create GoJS structures for displaying diagrams. You can see my re-implementation of [https://gojs.net/latest/samples/entityRelationship.html](https://gojs.net/latest/samples/entityRelationship.html) sample: [https://github.com/radrad/GoJS/blob/master/samples/entityRelationshipBookingManagement.html](https://github.com/radrad/GoJS/blob/master/samples/entityRelationshipBookingManagement.html)

## Subtasks

- [ ] Subtask 1
- [ ] Subtask 2
- [ ] Subtask 3

## Resources

- Link to relevant files, documents, or external resources.

## Notes

- Additional notes or comments related to the task.

## Attachments

- Links to any attachments or images related to the task.

---

*