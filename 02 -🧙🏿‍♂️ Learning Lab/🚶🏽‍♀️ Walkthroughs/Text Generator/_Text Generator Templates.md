---
tags:
  - textgenerator
  - template
  - walkthrough
---

# Welcome to Text Generator Templates for Obsidian

Creating high-quality content efficiently is a cornerstone of **productivity** for **writers**, **researchers**, and **knowledge workers**. The **Text Generator** plugin for Obsidian revolutionizes this process by leveraging templates—a powerful feature designed to streamline your writing and ideation workflow. With templates, you begin with a pre-structured format that spares you from the repetitive setup of documents, allowing you to focus on injecting creativity and substance into your work.

Whether you're drafting an article, sketching a project plan, or compiling research notes, our templates offer a launching pad for your endeavors, providing a smooth, consistent, and optimized experience. They are the blueprint for success in your textual creations within Obsidian.

## Navigating the World of Text Generator Templates

### Accessing Templates

Unlock a world of possibilities with community-generated templates through the **[Template Package Manager](https://docs.text-gen.com/_notes/3-+Templates/old/Template+Package+Manager)**. Here, you will find a variety of structures suited for different text-generation tasks. For even more diversity, visit our [Discord channel](https://discord.com/channels/1083485983879741572/1145601444104384604) where enthusiasts like you share and discuss their template innovations.

### Storing Your Templates

By default, templates are nestled in the `textgenerator/prompts` directory, a dedicated space for your templates to reside. Need a different location? No problem. The plugin settings allow you to tailor the storage directory to your liking. See how it's done in the example image below:  
![Pasted image 20231105161900.png](https://publish-01.obsidian.md/access/9b4703d86ab4cd591fba430c20daa539/assets/images/Pasted%20image%2020231105161900.png)

### Updating with Care

Enhancements to the community packages are frequent, but caution is advised—updating a package might overwrite your existing files in its respective subfolder. Preserve your custom creations by following the guidance in [Share a New Template Package](https://docs.text-gen.com/_notes/3-+Templates/old/Share+a+New+Template+Package).

### Crafting Your Masterpiece

Aspire to create your very own template? Begin your journey by diving into the [Text Generator Templates Guide](https://docs.text-gen.com/_notes/3-+Templates/Text+Generator+Templates+Guide), which is rich with detailed instructions and practical tips to aid you in crafting a template that could become the community’s next go-to structure.

Embrace the **`Text Generator`** Templates today and transform your Obsidian workspace into a more **dynamic**, **efficient**, and **personalized** environment. Unleash the full potential of your ideas with just a few clicks. Welcome to a smarter way of writing.

# 01 Understanding Context

In your note-taking and text manipulation endeavors, you may find yourself **working** with a variety of context variables. These context variables **serve** as placeholders or dynamic references within your notes and **play** a crucial role in organizing and automating your workflow. They **enable** you to **access** and **manipulate** different aspects of your notes, making your note-taking experience more versatile and efficient. In this documentation, we will **explore** various context variables, their purpose, and examples of how to use them effectively.

Important

The [Template Playground](https://docs.text-gen.com/_notes/2-+Options/Template+Playground) is a dynamic environment designed to enhance your understanding and proficiency with templates. It serves as a practical learning center where you can explore, experiment, and craft templates in real-time.

## title

The `{{title}}` context variable represents the title of the note. You can use it to reference and manipulate the note's title dynamically.

**Example**: `{{title}}`

## content

The `{{content}}` context variable represents the entirety of the note's content. It provides access to the full text within a note.

**Example**: `{{content}}`

## selection

The `{{selection}}` context variable represents the portion of text that has been selected by the user. You can use it to work with the selected text.

**Example**: `{{selection}}`

## tg_selection

The `{{tg_selection}}` context variable does the following:

1. It gives you the text that you've currently selected or highlighted in a document.
2. If your cursor is on a line with text (not empty), it provides the text on that line just before the cursor.
3. If there are no sets of three asterisks `***` above your cursor, and the line your cursor is on is empty, it includes all the text above your cursor.
4. If there are three asterisks `***` above your cursor, and the line your cursor is on is empty, it includes the text between your cursor and the nearest set of three asterisks `***`.

![Considered Context 2022-11-21 17.41.47.excalidraw.svg](https://publish-01.obsidian.md/access/9b4703d86ab4cd591fba430c20daa539/assets/images/Considered%20Context%202022-11-21%2017.41.47.excalidraw.svg)

**Example**: `{{tg_selection}}`

## starred Blocks

`{{starredBlocks}}` context variable refers to content under headings marked with an asterisk (`*`) in the note. It helps you using specific sections in the note as context.

**Example**: `{{starredBlocks}}`

## clipboard

The `{{clipboard}}` context variable represents the current content copied to the clipboard. It allows you to interact with copied content.

**Example**: `{{clipboard}}`

## selections

`{{selections}}` is used to iterate through all selected text segments in the note, especially when multiple selections (using `alt` key) are made. It enables you to process selected text systematically.

**Example**:

```handlebars
{{#each selections}} 
* {{this}} 
{{/each}}
```

## highlights

`{{#each highlights}}` helps you iterate through highlighted segments marked with `==example==` in the note. It allows you to work with highlighted content selectively.

**Example**: ```

```handlebars
{{#each highlights}} 
* {{this}} 
{{/each}}
```

## children

The `{{#each children}}` context variable represents an array of notes or sub-notes that are cited or related to the primary note. It enables you to access related notes.

**Example**:

```handlebars
{{#each children}} 
# {{this.title}}
{{this.content}}
{{/each}}
```

## mentions (Linked)

`{{#each mentions.linked}}` helps you iterate through mentions across the entire vault where a note is directly linked using [note](https://docs.text-gen.com/note). It facilitates working with linked mentions.

**Example**:

```handlebars
{{#each mentions.linked}} 
* {{this.results}} 
{{/each}}
```

## mentions (Unlinked)

`{{#each mentions.unlinked}}` allows you to iterate through mentions across the vault where a note is referenced without a direct link, e.g., '...note...'. It helps manage unlinked mentions.

**Example**:

```handlebars
{{#each mentions.unlinked}} 
* {{this.results}} 
{{/each}}
```

## Headings

`{{headings}}` context variable contains all the headings within the note and their respective content. It aids in navigating and manipulating the structure of your notes.

**Example**:

```handlebars
{{#each headings}}
# HEADER: {{@key}}
Content : {{this}}
{{/each}}
```

## metadata

The `{{metadata}}` context variable contains the metadata of the note, often provided in YAML format. It gives access to whole metadata information as string.

**Example**: `{{metadata}}`

## yaml

`{{#each yaml}}` allows you to iterate through the initial metadata (Object) of the note, providing access to specific metadata fields.

**Example**:

```handlebars
{{#each yaml}}
{{@key}}: {{this}}
{{/each}}
```

For one variable you can use `{{yaml.variable}}`.

## BeforeCursor

This context variable could select all the text before the cursor's current position, regardless of the structure or formatting of the text. Useful for quickly referencing or manipulating content leading up to a certain point.  
Example:

```handlebars
{{beforeCursor}}
```

## AfterCursor

The opposite of `BeforeCursor`, this would select all text after the cursor's current position. It would be especially useful for editing or reviewing the remaining part of a document.

Example:

```handlebars
{{afterCursor}}
```

## CursorParagraph

This would select the entire paragraph where the cursor is currently located. It could be helpful for operations that focus on paragraph-level editing or formatting.

Example:

```handlebars
{{cursorParagraph}}
```

## CursorSentence

This would select the sentence immediately surrounding the cursor, including sentences that the cursor is in the middle of. Ideal for sentence-level editing.

Example:

```handlebars
{{cursorSentence}}
```

## NextWord/PreviousWord

These would select the next or previous word relative to the cursor's position, making it easier to navigate and edit text on a word-by-word basis.

Example:

```handlebars
{{NextWord}}
{{PreviousWord}}
```

## InverseSelection

Selects everything except the currently selected text. This could be useful in cases where you want to apply formatting or changes to every part of the document except a specific section. 1

Example:

```handlebars
{{InverseSelection}}
```

These context variables play a pivotal role in enhancing your note-taking and text manipulation capabilities within your note-taking software or system. By understanding how to use them effectively, you can streamline your workflow and make the most of your text generator templates.

# 02 Template Writing

Creating templates is a powerful way to streamline your note creation process and maintain consistency. In this section, we'll walk you through the steps to create effective templates.

Important

The [Template Playground](https://docs.text-gen.com/_notes/2-+Options/Template+Playground) is a dynamic environment designed to enhance your understanding and proficiency with templates. It serves as a practical learning center where you can explore, experiment, and craft templates in real-time.

## Selecting the Starting Point for Your Template

To begin, you have multiple starting points:

1. **From Active Document**
    
    - Execute the command [Create a Template](https://docs.text-gen.com/_notes/3-+Templates/old/Create+a+Template) from your active document to start the template creation process.
2. **From Template Playground**
    
    - Using [Template Playground](https://docs.text-gen.com/_notes/2-+Options/Template+Playground), it is possible to test the template engine in a more practical way and create templates from there.
3. **From Scratch**
    
    - **Create** a file within the **Templates Folder**.
    - **Add** the template metadata by inserting [Template Metadata](https://docs.text-gen.com/_notes/3-+Templates/subpages/Template+Metadata) at the beginning of your file.

## Understanding Template Structure

Templates consist of four integral parts: Metadata, Initialization, Prompt, and Output. Each section plays a pivotal role in data handling and final presentation.  
![02 Template Creation 2023-11-03 09.21.02.svg](https://publish-01.obsidian.md/access/9b4703d86ab4cd591fba430c20daa539/assets/images/02%20Template%20Creation%202023-11-03%2009.21.02.svg)  

### Metadata

- The metadata section contains essential information regarding the template, such as `promptId`, `name`, and a comprehensive description. Further details are available in [Template Metadata](https://docs.text-gen.com/_notes/3-+Templates/subpages/Template+Metadata).

![Pasted image 20231104190506.png](https://publish-01.obsidian.md/access/9b4703d86ab4cd591fba430c20daa539/assets/images/Pasted%20image%2020231104190506.png)

### Initialization (Optional)

This section will not be included in the template's prompt and can be used to:

- **Gather** and **prepare** any required data before the main logic of the template is executed in the `prompt` section.
- **Declare** variables that will be used in later sections.
- **Define** [Custom Form](https://docs.text-gen.com/Custom+Form) for better customization.
- **Enhance** readability by using code blocks, such as:  
    ![Pasted image 20231105113334.png](https://publish-01.obsidian.md/access/9b4703d86ab4cd591fba430c20daa539/assets/images/Pasted%20image%2020231105113334.png)

### Prompt

- This section is processed by the chosen **Language Learning Model (LLM)** unless `disabledProvider` is set to `false`.
- **Extract** data, **manipulate** the information, and **perform** conditions and loops using handlebar syntax or **JavaScript** inside `script` block along with provided helper functions.

### Output (Optional)

- **Format** and **present** the results from the selected LLM (if enabled) in the `{{output}}`.
- **Insert** the resulting data into the correct placeholders within the output template.

Note

The **body** of template can have just the **prompt** section without any `***`. With one `***`, the first part will be `prompt` and the second part will be `output`.

## Writing Templates

The core of the template functionality is powered by [Handlebars](https://handlebarsjs.com/). There are two primary methods for template creation:

- **[Handlebar Templates](https://docs.text-gen.com/_notes/3-+Templates/subpages/Handlebar+Templates)**
    - Utilize handlebar logic alongside additional helper functions for asynchronous processing and manipulation of data.
- **[Javascript Templates](https://docs.text-gen.com/_notes/3-+Templates/subpages/Javascript+Templates)**
    - Integrate JavaScript within handlebars using the `script` helper function for advanced scripting capabilities. Ensure that scripts come from a trusted source to mitigate security risks.

# Commands

## Basic Commands

The simplest commands are : **"Generate Text!"** and **"Generate Text (use Metadata).**"

- ### [Generate Text](https://docs.text-gen.com/_notes/2-+Options/Commands/Generate+Text)
    
- ### [Generate Text and Use Metadata](https://docs.text-gen.com/_notes/2-+Options/Commands/Generate+Text+and+Use+Metadata)
    

## OpenAI Utility Commands

- ### [Max Token Configuration](https://docs.text-gen.com/_notes/2-+Options/Commands/old/Set+Max+Content+Size)
    
- ### [Choose a model](https://docs.text-gen.com/_notes/6-+Other+notes/old/Choose+a+model)
    
- ### [Estimate tokens for the current document](https://docs.text-gen.com/_notes/2-+Options/Commands/Estimate+tokens+for+the+current+document)
    

## Template commands

For more information about see [00 Introduction To Templates](https://docs.text-gen.com/_notes/3-+Templates/00+Introduction+To+Templates).

- ### [Template Package Manager](https://docs.text-gen.com/_notes/3-+Templates/old/Template+Package+Manager)
    
- ### [Create a Template](https://docs.text-gen.com/_notes/3-+Templates/old/Create+a+Template)
    
- ### [Insert a Template](https://docs.text-gen.com/_notes/3-+Templates/old/Insert+a+Template)
    
- ### [Create a New File From Template](https://docs.text-gen.com/Create+a+New+File+From+Template)
    
- ### [Generate And Insert Template](https://docs.text-gen.com/_notes/2-+Options/Commands/Generate+And+Insert+Template)
    
- ### [Generate and Create a New File From Template](https://docs.text-gen.com/_notes/2-+Options/Commands/Generate+and+Create+a+New+File+From+Template)
    
- ### [Generate & Copy To Clipboard](https://docs.text-gen.com/_notes/2-+Options/Commands/Generate+%26+Copy+To+Clipboard)
    
- ### [Estimate tokens for a template](https://docs.text-gen.com/_notes/3-+Templates/old/Estimate+tokens+for+a+template)
    

## Prerequisites

- [2- Configure API Key](https://docs.text-gen.com/_notes/1-+Getting+Started/2-+Configure+API+Key) (if you're using OpenAI).
- [Considered Context](https://docs.text-gen.com/_notes/1-+Getting+Started/old/Considered+Context).
- [Hotkeys in Obsidian](https://docs.text-gen.com/_notes/6-+Other+notes/old/Hotkeys+in+Obsidian)  
    ![Commands.svg](https://publish-01.obsidian.md/access/9b4703d86ab4cd591fba430c20daa539/assets/images/Commands.svg)