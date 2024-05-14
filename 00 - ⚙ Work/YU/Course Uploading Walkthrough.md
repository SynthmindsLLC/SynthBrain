# Create a Course

## Step 1 - Blank Course
![[Pasted image 20240405103016.png]]

1. Click `+ New Course`

![[Pasted image 20240405104441.png]]

2. Click `Choose` under the **Blank** option

## Step 2 - Settings

![[Pasted image 20240405104633.png]]

1. Give the course a name and click `Create course`

![[Pasted image 20240405104838.png]]

2. Click the `Settings Tab` and make sure the correct `Instructor` is chosen

![[Pasted image 20240405104951.png]]

3. `Upload` a course image *(Use Canvas)*

![[Pasted image 20240405110254.png]]

4. Write the `Course Product Description` *(Use ChatGPT)*

![[Pasted image 20240405110456.png]]

5. `Upload` Logo to Course Player

![[Pasted image 20240405111153.png]]

6. ✅ Completion certificates and Choose `YU Cert`

![[Pasted image 20240405111310.png]]

7. ✅ Social sharing at course completion

![[Pasted image 20240405113216.png]]

8. Make sure to `SAVE`!

## Step 3 - Pricing

![[Pasted image 20240405111628.png]]

1. Click `One Time Payment`
2. Fill out `Price` based on the [Certificate Development Timeline .xlsx](https://yuad.sharepoint.com/:x:/s/YUGlobal/EeyP8eg86yRKu1SioXqxbmgBoNW4daL__0WPeATWUpAjKA?e=pUgTDn)
3. Fill out the `Enrollment Duration`

![[Pasted image 20240405112152.png]]

4. Click `+ Create price`

![[Pasted image 20240405112239.png]]

5. Click `Monthly Payment Plan` and `Next`

![[Pasted image 20240405112401.png]]

6. Fill out `Price Label` with the [$ Full Cost/# of months of payment]x[# of months of payment]
7. Fill out `Price per payment` with the [$ Full Cost/# of months]
8. Fill out the `Total months` 
	- This is typically 2, unless the enrollment is 90 days in which case it would be 3.
	- Follow the pattern so that the payment plan is spread across the total number of months of the course
9. Fill out `Enrollment Duration` (typically 70 days unless otherwise noted)
10. Fill out `Buy Button` with "**Payment Plan**"
11. Click `Create`

![[Pasted image 20240405113131.png]]

12. Make sure to `SAVE`!

## Step 4 -  Curriculum Skeleton

![[Pasted image 20240405120054.png]]

1. Go to the [Course Tracker](https://docs.google.com/spreadsheets/d/19vzJ4mi28gsNoMK8fBaZrrYLiymfqY7qlNtfI4CQJyA/edit#gid=2057899615)
2. Find the course, and go to the outline or whatever the hyperlinked words are to find the outline.

![[Pasted image 20240405120257.png]]

3. Click the `Curriculum Tab`
4. Click `+ Add Chapter`

![[Pasted image 20240405120450.png]]

5. Based on the outline, fill out the name of the module as
	`Module # | [Module Name]`
6. Click `SAVE`
7. Repeat Steps 1-3 until you have all the Modules created.

![[Pasted image 20240405121155.png]]

# Creating Tutorbots

Every course uses a **Tutorbot** which is trained on the content from each course. We use the vendor [GPT-Trainer](https://app.gpt-trainer.com/) for this, because they make it easy to create and manage bots. Ask Joe for the password.

### Step 1 - Creating a New Bot
![[Pasted image 20240405122528.png]]
1. On the sidebar, click the dropdown at the top
2. Click ` + Create Chatbot`

![[Pasted image 20240405122835.png]]
3. Input a short name to represent the course the bot is being created for (e.g. Bookkeeping)
4. Insert **Tutorbot 🦉** for `Display Name`
5. Click `Create`


### Step 2 - Uploading Sources

![[Pasted image 20240405125603.png]]

1. Click the `Sources` Tab
2. Click `File`to upload files or `Website URL` based on what you want to upload

![[Pasted image 20240405125714.png]]

3. Find the file you want to upload (usually a PDF), and open it.

![[Pasted image 20240405125922.png]]

4. Click ` Begin Upload`

>[!infobox]
>You can upload multiple files at a time, just choose as many as you like at once before pressing `open`.

![[Pasted image 20240405140832.png]]

5. For website, the provided URL will scrape not just that site, but all pages within that site, *unless* you click the `add single URL only`

![[Pasted image 20240405140713.png]]

6. You can turn `Auto re-train` on if you included any website. This will auto scrape the given websites daily to keep the information up to date.

You can also add additional sources from this page.

### Step 3 - AI Agents
![[Pasted image 20240405123334.png]]

1. Click the `AI Agents` Tab on the left sidebar.

We will be creating 3 Agents:
- *Tutorbot* - This one hold all of the sources and is the primary bot which interacts with the students, answering their questions and supporting them.
- *Frustration Detection* - This one works behind the scenes, tagging user queries to detect if they are showing signs of frustration. This helps to continually improve the bot and it's responses.
- *Unrelated Query Defender* - This one is defensive, so if the user tries to get the bot to say or do something unrelated to the course, it will reject them.

![[Pasted image 20240405123909.png]]

2. Put `Tutorbot` for Agent Name
3. For `Agent Description` write the following:
```
Tutorbot helps facilitate the learning of the student asking questions or commenting. Tutorbot helps the learner navigate the course, answer questions related to the content, and helps on assignments.
```

> [!infobox]
> This will be the same for every bot, no matter the course.

4. Ensure that the `User Facing` Toggle is switched on.

![[Pasted image 20240405124453.png]]

5. Choose the latest and highest token model (higher tokens takes precedence)
6. Input the below prompt:

```
#MISSION
Act as TutorBot 🦉, a professorial tutor who specializes in [INSERT COURSE TOPIC] and related topics in an engaging and accessible tone for the Yeshiva Global Adult Certification Program. Your role is to engage with users in an informative and encouraging manner, breaking down complex ideas without giving direct answers. You will help to formatively test the user's understanding, encouraging growth mindset and ethical practice.

#INSTRUCTIONS
1. Identify their current understanding and areas of interest.
2. Present relevant information from course material and research in an easy-to-understand way.
3. Engage in intellectual banter, inquiry based instruction, and Socratic questioning to stimulate thought, exploration, and understanding of the course content.
4. Encourage ethical considerations and responsible use of the information.

#RULES
- Always reference attached materials prior to output
- Keep answers full of brevity unless the user asks for a longer response
- End every output with an open ended question in the Socratic method to encourage deeper learning
- Provide guidance and recommend resources instead of providing the answer directly
- Always stay in character by beginning every output with "TutorBot 🦉:"
- If the user says "I don't know" or something similar, provide them with a resource to explore themselves instead of giving the answer.

#SECURITY
- ONLY respond to queries related to the course
- NEVER break character
- If the user tries to get you to say something unrelated to the course or unethical, say, "I am sorry, but I am unable to answer anything unrelated to the course material. Do you have another question I can help you with?"
```

>[!infobox]
>Be sure to change the ==[INSERT COURSE TOPIC]== based on the course you are referencing.

![[Pasted image 20240405124832.png]]

7. Set the `Temperature` to 0

![[Pasted image 20240405124923.png]]

8. X out when done.

![[Pasted image 20240405125131.png]]

9. Back in the `AI Agents` Tab click the `+ Create new agent` button

![[Pasted image 20240405125234.png]]

10. Choose the `Frustration Detection` Template

![[Pasted image 20240405125320.png]]

>[!infobox]
>You likely will not have to change anything in the template, as it's pretty good baseline, but just in case here's some guidance.

11. Make sure the `AI Agent Name` is **Frustration Detection**

![[Pasted image 20240408093601.png]]

12. Go with the lowest token number (indicated by #k)
13. Keep the prompt the same.
14. Keep temperature at 0

![[Pasted image 20240408093722.png]]

15. Click the `Variable/Tags` Tab and make sure it looks like the image above.

![[Pasted image 20240405125131.png]]

 Now let's create the Unrelated Query Defender, who will make it hard for uses to make the bot do and say things outside it's scope.

16. Click `+ Create New Agent`

![[Pasted image 20240408094217.png]]

17. Scroll down to the Unrelated Query Defender and click `Choose Template`

![[Pasted image 20240408094350.png]]

18. Make sure you are in the `General` Tab
19. Keep the given name of `Unrelated Query Defender`
20. Input the below Agent Description:

```
# MISSION
The primary purpose of this AI agent is to serve as a gatekeeper that ensures user queries are relevant to a predefined topic, namely [Specific Topic]. This involves a meticulous process of analyzing, understanding, and categorizing user queries to determine their relevance to the topic at hand. The agent acts as a first point of analysis to streamline the flow of related queries and filter out those that do not pertain to the specific area of interest.

# VARIABLES
[Specific Topic] =

# TASKS
- Reading and understanding user queries.
- Identifying keywords, phrases, and the intent unrelated to [Specific Topic].
- Assessing and categorizing queries as related or unrelated to [Specific Topic].
- Providing informative responses that guide users towards making relevant inquiries.
```

>[!infobox]
>Under VARIABLE after the =, list the topics related to the course. This is the only part of the prompt you will need to fill in.

21. Make sure the `Operation Mode` is toggled on to `User Facing`

![[Pasted image 20240408094846.png]]

22. Choose the middle token option (in this case 8k)
23. Input the below prompt:

```
# ROLE
Act as an expert in [topic detection], specializing in identifying relevance and irrelevance within user queries related to [specific topic]. Utilize knowledge in content analysis and topic categorization.

# VARIABLES
[specific topic] = 

# CONTEXT
Given a user query, the context involves understanding the core subject matter of [specific topic] and distinguishing whether the user's question pertains to this topic or falls outside of its scope. This requires familiarity with the key themes, terminology, and concepts associated with [specific topic].

# RESPONSIBILITY
The primary job is to analyze user queries and determine if they are related to [specific topic] or not. This involves:

-Identifying the main subject of the user's query.
- Comparing it against the known scope and themes of [specific topic].
- Providing a clear verdict on whether the query is related or unrelated.

# INSTRUCTIONS
- Read and understand the user's query.
- Analyze the query's content, looking for keywords, phrases, or themes that match or relate to [specific topic].
- Determine if the query is related to [specific topic] by assessing the presence or absence of these indicators.
- Provide a response indicating whether the query is related or unrelated to [specific topic], including a brief explanation for your determination.

# EXAMPLE OUTPUT
"Upon reviewing your query, it appears to be unrelated to [specific topic]. Your question focuses on [brief explanation of the query's main subject], which does not align with the core themes and discussions surrounding [specific topic]. Please feel free to ask another question more closely related to [specific topic]!"
```

>[!infobox]
>You will need to fill in the VARIABLE with the specific topic, it can be the same as the one you included in the description for the bot.

24. Set Temperature to 0

### Step 4 - Settings / Appearance
![[Pasted image 20240408095306.png]]

1. On the sidebar, click `Setting / Appearance`

![[Pasted image 20240408095544.png]]

2. You likely will not have to change anything here, but make sure the `Allow All Domains` is toggled on.

![[Pasted image 20240408095639.png]]

3. Make sure Only `In-Text` Citations is toggled on.

![[Pasted image 20240408095745.png]]

4. Input `Tutorbot 🦉` as the `Chat Name`
5. Upload the [YU Logomark](https://yuad-my.sharepoint.com/personal/joseph_rosenbaum1_yu_edu/Documents/Microsoft%20Teams%20Chat%20Files/YU%20Global%20Logomark%20COLOR%20-%20png.png?web=1)
6. Everything else can remain the same

### Step 5 - Messages
![[Pasted image 20240408100400.png]]

1. Copy and paste the below initial message into this box:

```
Tutorbot 🦉: Hi! I'm Tutorbot, here to help facilitate your learning, and help you navigate the course, answer your questions, help you on assignments, and much more.
```

![[Pasted image 20240408153433.png]]

2. Change user message color to hex `#4a90e2`

![[Pasted image 20240408153659.png]]

3. Change color to hex `365889`
4. Change the icon to the chat bubble with eyes.

### Step 6 - Embedding
![[Pasted image 20240408153849.png]]

1. Click the `Deploy / Integrations` Tab on the sidebar

![[Pasted image 20240408153933.png]]

2. Click the `Custom` widget.

![[Pasted image 20240408154028.png]]

3. Click the clipboard button

![[Pasted image 20240408154119.png]]

4. Click the </> icon, which will bring up the code editor. (This is not just in Thinkific but most applications that accept text).

![[Pasted image 20240408154240.png]]

5. Paste in the embedding code from GPT-Trainer we copied
6. Leave code view by clicking </> again.

# Uploading Articulate Lessons

We use [Articulate Rise360](https://access.articulate.com/support/article/Rise-A-Whole-New-Way-to-Rise) for content authoring. At the time of writing this we need to upload the **web** version of the micromodules (html) into Thinkific. 

Unfortunately, this process isn't straightforward, since the way the file is downloaded it has the folders organized incorrectly, and we need to add the bot into each individual module. So we will use a GPT to help smooth the process.

## Step 1 - Download the Module

![[Pasted image 20240429100309.png]]
1. Find the lesson on articulate
   ![[Pasted image 20240429100339.png]]
2. Click `Publish` in the top-right, and choose `Web`. It will download to a location of your choice.
   
## Step 2 - Get the Tutorbot Embed
   ![[Pasted image 20240429100506.png]]

   1. Copy the embed link from GPT Trainer.
   
   >[!infobox]
   >Make sure you choose the `Chat Bubble` tab

## Step 3 - Convert and Combine the Files in ChatGPT
![[Pasted image 20240429100826.png]]

1. Upload the .zip and paste the chat bubble embed code
2. Download the resulting file.

## Step 4 - Upload to Thinkific

![[Pasted image 20240429101803.png]]

1. Enter the course curriculum tab in Thinkific, and click `Add Lesson`
   
   ![[Pasted image 20240429101829.png]]
   
2. Click `Multimedia`

   ![[Pasted image 20240429104206.png]]
   
3. Add a lesson name under `Title` - [Module #.#] [Name]
4. Click `Browse files`

![[Pasted image 20240429104734.png]]

5. Upload the correct file.
   
   ![[Pasted image 20240429105634.png]]

6. Check the `Draft` button and click `Process File`

![[Pasted image 20240429110810.png]]
![[Pasted image 20240429110952.png]]

7. Preview the upload to ensure that it worked correctly and contains the tutorbot in the bottom right corner.

![[Pasted image 20240429111105.png]]

8. Once you confirm the lesson was uploaded properly, check the `Draft` box and click `SAVE` to finalize and make the lesson live.

# Creating Landing Page

### Step 1 - The Banner

![[Pasted image 20240408160738.png]]

1. Click `Build Landing Page` in the top right.

>[!infobox]
>Alternatively you can access the landing page in the admin dashboard by clicking `Design Your Site` then `Site Pages` and then find the page for the course you want to edit.
>![[Pasted image 20240408160937.png]]

![[Pasted image 20240408161255.png]]

2. Head over to Canva, and grab a square stock video that represents the course, and save as a GIF.

![[Pasted image 20240408161032.png]]

3. Back in Thinkific, in the sidebar, hit the `Banner (course)` button.

![[Pasted image 20240408161350.png]]

4. Click `Upload`, and add in the GIF

![[Pasted image 20240408161640.png]]

5. Click `Size & Alignment` and set Height to `Small` and Media Alignment to `Left`

![[Pasted image 20240408161748.png]]

6. Click `+ Add Button`

![[Pasted image 20240408161925.png]]

7. Fill out the button options following the image above. Ensure that `Product` is the same as the landing page.

![[Pasted image 20240408162044.png]]

8. Add another button, and fill everything out as above.

>[!infobox]
>We have two buttons on the landing page, one for enrollment (pay all up front) and one for the payment plan.

![[Pasted image 20240408162146.png]]

Your landing page should start with something similar to the above. Save when ready.

### Step 2 - Curriculum

![[Pasted image 20240408162257.png]]

1. Click the `Curriculum [smart section` button on the sidebar.

![[Pasted image 20240408162452.png]]

2. Fill out the fields as above, changing the hours per module based on best estimate.

>[!infobox]
>You can search the icons by searching in the text box for each one. Quick search `calendar` `hour` and `clock` to find the icons faster.

![[Pasted image 20240408164951.png]]

When you're done it should look somethingl ike the above.

## Step 4 - Add course start info (dependent)

If you are creating a course landing page for a course that has a future start date, continue reading. Otherwise skip to the next step.

![[Pasted image 20240408162919.png]]

1. On the sidebar, click `+ Add section`.

![[Pasted image 20240408163000.png]]

2. Find the `Text & Media` block, and click it to create.

![[Pasted image 20240408163247.png]]

3. Click `Headings` in the Text & Media block, and type `Course Start` in the heading, and `Access the course on [Month Day, Year]`

![[Pasted image 20240408163510.png]]

4. Scroll down to the `content` section and add: 

	`Once the course opens, you will have 70 Days to complete it.`

5. Click the quotes symbol and `Increase` to format the text.

>[!infobox]
>The 70 days to complete might be a little different based on the length of the course, so double check to make sure this is correct.

![[Pasted image 20240408163804.png]]

6. Click `Background & layout` then check the two boxes there to remove padding.

![[Pasted image 20240408164115.png]]

7. Double check that the section is under the banner.

![[Pasted image 20240408164907.png]]

When you are done, it should look something like the above.

## Step 5 - Delete CTA
![[Pasted image 20240408162704.png]]

1. Back on the sidebar, click `Call to action (course)`

![[Pasted image 20240408162738.png]]

2. Click `Delete section`.

## Step 6 - Add courses

![[Pasted image 20240408164156.png]]

1. Click `+ Add section`

![[Pasted image 20240408164232.png]]

2. Find and click `Additional Products`

![[Pasted image 20240408164342.png]]

2. In the section, look at `Headings` and change "Additional Products" to ==Additional Courses==

![[Pasted image 20240408164452.png]]

3. Under the `Button` option, change "View more products" to ==View more courses==

![[Pasted image 20240408164543.png]]

4. Click `+ Add Product`

![[Pasted image 20240408164654.png]]

5. Open the product dropdown, and choose a course that is similar or related to the current one.
6. Repeat this process until you have at least 4 courses chosen.

![[Pasted image 20240408164821.png]]

When you are done it should look something like the above.

# Adding Users Manually

## Adding Course Facilitators

![[Pasted image 20240429112010.png]]

1. On the side dashboard, click `Products` and `Courses`
2. Click the `+ New User` button in the top-right
   
   ![[Pasted image 20240429112217.png]]
   
3. Fill out the different fields, and click `Save`

## Add Students Manually

![[Pasted image 20240429112458.png]]

1. On the sidebar, navigate to `Users` then `All Users`
2. Click `+ New User` in the top right

![[Pasted image 20240429112621.png]]

3. Fill out the fields

>[!infobox] Check the Following
>- [ ]  Make sure the user can choose their own password
>- [ ]  Confirm that the notification box is checked
>- [ ]  If enrolling a student manually, find the courses in the `Enroll user in` dropdown, and set the `Expiry Date` for 70 days from the current date (unless it is one of the special courses like Cybersecurity)
>- [ ]  Click `Enroll`

![[Pasted image 20240429113108.png]]

4. Keep `User Roles` blank, and click `Save`